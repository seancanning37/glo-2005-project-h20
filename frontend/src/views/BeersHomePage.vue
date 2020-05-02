<template>
  <v-container>
    <p class="headline text-left mb-0 pl-3">
      Results {{ this.firstBeerId }}-{{ this.lastBeerId }} of
      {{ this.beers.length }}
    </p>
    <beer-list :beerList="shownBeers" />

    <v-container class="pt-0">
      <v-row class="pt-0">
        <v-spacer />
        <v-col class="text-right pr-6 pt-0">
          <a
            :class="
              isCurrentPage(n)
                ? 'current-page black--text font-weight-bold text-center'
                : 'link black--text text-center'
            "
            v-for="n in Math.ceil(this.beers.length / 12)"
            :key="n"
            @click="updateBeers(n)"
          >
            {{ n }}
          </a>
        </v-col>
      </v-row>
    </v-container>
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
    shownBeers: [],
    firstBeerId: 0,
    lastBeerId: 12,
    currentPage: 0,
  }),
  async created() {
    this.beers = await this.getAllBeers();
    this.updateBeers(1);
  },
  methods: {
    getAllBeers: async function() {
      const beers = await getAllBeers();
      return beers.data;
    },
    updateBeers: function(n) {
      this.currentPage = n;
      this.firstBeerId = 12 * (n - 1) + 1;
      this.lastBeerId = this.firstBeerId + 11;

      if (this.lastBeerId > this.beers.length) {
        this.lastBeerId = this.beers.length;
      }
      this.shownBeers = this.beers.slice(this.firstBeerId - 1, this.lastBeerId);
    },
    isCurrentPage: function(n) {
      return n === this.currentPage;
    },
  },
};
</script>

<style scoped>
.current-page {
  text-decoration: underline;
}
</style>
