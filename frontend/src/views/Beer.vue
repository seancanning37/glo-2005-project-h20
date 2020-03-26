<template>
  <div>
    <h1>
      BEER PAGE
    </h1>
    <p>Beer id: {{ this.beer.id }}</p>
    <p>Beer name: {{ this.beer.name }}</p>
    <p>Brand id: {{ this.beer.brand_id }}</p>
    <p>abv: {{ this.beer.abv }}</p>
    <p>ibu: {{ this.beer.ibu }}</p>
    <p>volume: {{ this.beer.volume }}</p>
    <p>country: {{ this.beer.country }}</p>
    <p>price: {{ this.beer.price }}</p>
    <p>Description: {{ this.beer.description }}</p>
  </div>
</template>

<script>
import axios from "axios";

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
      country: "",
      price: 0.0,
      description: ""
    }
  }),
  created() {
    this.getBeer();
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
    }
  }
};
</script>

<style scoped></style>
