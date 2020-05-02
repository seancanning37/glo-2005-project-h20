<template>
  <v-container>
    <beer-list :beerList="beers" />
  </v-container>
</template>

<script>
import { getAllBeers } from "../api/beer_api.js";
import BeerList from "../components/beer/BeerList.vue";

export default {
  name: "BeersHomePage",
  components: {
    BeerList,
  },
  data: () => ({
    beers: [],
  }),
  async created() {
    this.beers = await this.getAllBeers();
  },
  methods: {
    getAllBeers: async function() {
      const beers = await getAllBeers();
      return beers.data;
    },
  },
};
</script>

<style scoped></style>
