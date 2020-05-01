<template>
  <h1>
    BEER PAGE
  </h1>
</template>

<script>
import axios from "axios";

export default {
  name: "BeersHomePage",
  data: () => ({
    beers: [],
  }),
  created() {
    this.getAllBeers();
  },
  methods: {
    getAllBeers() {
      const path = "http://localhost:5000/beers";
      axios
        .get(path)
        .then((response) => {
          console.log(response.data);
          this.beers = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
