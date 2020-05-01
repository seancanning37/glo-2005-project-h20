<template>
  <v-container>
    <beer v-for="beer in beerList" :key="beer.id" :beer="beer" />
  </v-container>
</template>

<script>
import Beer from "./Beer.vue";

export default {
  name: "BeerList",
  props: ["beerList"],
  components: {
    Beer,
  },
};
</script>

<style></style>
