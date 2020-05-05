<template>
  <v-card class="mb-5">
    <v-card-title class="justify-center">
      {{ cartItem.name }}
    </v-card-title>
    <v-card-title class="justify-center">
      ${{ (beer.price * quantity).toFixed(2) }}
    </v-card-title>
    <v-container class="d-flex align-center" style="width: 250px;">
      <v-select
        label="Quantity"
        type="number"
        :items="beerDisponibility"
        v-model="quantity"
        class="mr-5"
        v-on:change="$emit('changeQuantity', cartItem.beer_id, quantity)"
      />
      <v-btn v-on:click="$emit('deleteItem', cartItem.beer_id)" class="mb-2">
        <v-icon>
          mdi-delete
        </v-icon>
      </v-btn>
    </v-container>
  </v-card>
</template>

<script>
import { getBeer } from "../../api/beer_api";

export default {
  name: "CartItem",
  props: ["cartItem"],
  data: function() {
    return {
      quantity: 0,
      beerDisponibility: [],
      beer: {}
    };
  },
  async created() {
    this.quantity = this.cartItem.quantity;
    this.beerDisponibility = this.getQuantities(
      (await getBeer(this.cartItem.beer_id)).data.disponibility
    );
    this.beer = (await getBeer(this.cartItem.beer_id)).data;
  },
  methods: {
    getQuantities: function(disponibility) {
      let numberList = [];
      for (let i = 1; i <= disponibility; i++) {
        numberList.push(i);
      }
      return numberList;
    }
  }
};
</script>

<style scoped></style>
