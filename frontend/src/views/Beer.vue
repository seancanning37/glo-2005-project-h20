<template>
  <v-container>
    <v-container>
      <h1>
        BEER PAGE
      </h1>
      <p>Beer id: {{ this.beer.id }}</p>
      <p>Beer name: {{ this.beer.name }}</p>
      <p>Brand id: {{ this.beer.brand_id }}</p>
      <p>abv: {{ this.beer.abv }}</p>
      <p>ibu: {{ this.beer.ibu }}</p>
      <p>volume: {{ this.beer.volume }}</p>
      <p>price: {{ this.beer.price }}</p>
      <p>Description: {{ this.beer.description }}</p>
    </v-container>
    <v-container>
      <v-btn v-on:click="addBeerToCart">
        Add to cart
      </v-btn>
    </v-container>
  </v-container>
</template>

<script>
import Cookies from "js-cookie";
import { getBeer } from "../api/beer_api.js";
import { addBeerToCart } from "../api/cart";

export default {
  name: "Beer",
  data: () => ({
    beer: {
      id: 0,
      name: "",
      brand_id: 0,
      abv: 0.0,
      ibu: 0,
      volume: 0,
      price: 0.0,
      description: ""
    },
    quantity: 0
  }),
  created() {
    this.getAllBeers();
  },
  methods: {
    getBeer: async function() {
      const beer = await getBeer(this.$route.params.beer_id);
      this.beer = beer.data;
    },
    addBeerToCart: async function() {
      await addBeerToCart(this.beer.id, this.quantity);
      console.log(JSON.parse(Cookies.get("beerbender-token")));
    }
  }
};
</script>

<style scoped></style>
