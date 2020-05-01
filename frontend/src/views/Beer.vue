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
import axios from "axios";
import Cookie from "js-cookie";

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
    beers: []
  }),
  created() {
    this.getAllBeers();
  },
  methods: {
    getBeer() {
      const path = "http://localhost:5000/beers/1";
      axios
        .get(path)
        .then(response => {
          console.log(response.data);
          this.beer = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addBeerToCart: function() {
      let cookie = Cookie.get("beerbender-token");
      console.log(cookie);
    },
    getAllBeers(){
      const path = "http://localhost:5000/beers";
      axios
        .get(path)
        .then(response => {
          console.log(response.data);
          this.beers = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped></style>
