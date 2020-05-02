<template>
  <v-container>
    <v-row>
      <v-col v-for="beer in beerList" :key="beer.id">
        <beer :beer="beer" />
      </v-col>
    </v-row>
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
