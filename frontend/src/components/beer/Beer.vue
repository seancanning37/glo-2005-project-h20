<template>
  <v-card height="275" width="400">
    <v-row>
      <v-col cols="3">
        <v-img
          :src="beer.pictureURL"
          height="200"
          width="75"
          class="ml-10 mt-3"
        ></v-img>
      </v-col>

      <v-col>
        <v-card-title class="mb-0 pb-0">
          <a :href="'/beers/' + beer.id" class="link black--text ">
            <p
              :class="needsSmallerFont() ? 'title' : 'headline' + ' mb-0 mx-6'"
            >
              {{ beer.name }}
            </p>
          </a>
          <v-container class="pt-0 my-0">
            <p class="text-right subtitle-1">
              {{ beer.volume }} ml • {{ beer.abv }} %
            </p>
          </v-container>
        </v-card-title>

        <v-card-text>
          <p class="subtitle-2 mx-6 text-left">{{ beer.description }}</p>
        </v-card-text>

        <v-card-actions
          style="position: absolute; right:6px; bottom: 10px;"
          class=" px-6"
        >
          <v-spacer />
          <p class="font-weight-bold px-4 pt-5">{{ beer.price }}$</p>
          <v-btn @click="addToCart()">add to cart</v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import {addBeerToCart} from "../../api/cart";

export default {
  name: "Beer",
  props: ["beer"],
  methods: {
    addToCart: function() {
      addBeerToCart(this.beer.id, 1, this.beer.name)
    },
    needsSmallerFont() {
      return this.beer.name.length > 17;
    }
  }
};
</script>

<style></style>
