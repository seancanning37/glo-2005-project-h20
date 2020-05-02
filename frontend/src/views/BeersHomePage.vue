<template>
  <v-container>
    <v-container class="pb-0 my-0">
      <v-row class="pb-0 my-0">
        <v-col class="pb-0">
          <p
            style="position:relative; top: 15%;"
            class="headline text-left mb-0 pl-3"
          >
            Results {{ this.firstBeerId }}-{{ this.lastBeerId }} of
            {{ this.beers.length }}
          </p>
        </v-col>
        <v-spacer />
        <v-col cols="3" class="pb-0">
          <v-select
            v-model="sortedProperty"
            :items="properties"
            outlined
            v-on:change="sortBeers()"
          >
          </v-select>
        </v-col>
      </v-row>
    </v-container>

    <beer-list class="pt-0" :beerList="shownBeers" />

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
    BeerList
  },
  data: () => ({
    beers: [],
    shownBeers: [],
    firstBeerId: 0,
    lastBeerId: 12,
    itemsPerPage: 12,
    currentPage: 0,
    properties: [
      "Name (A-Z)",
      "Name (Z-A)",
      "Price (low to high)",
      "Price (high to low)",
      "Alcohol %",
      "Volume",
    ],
    sortedProperty: "Name (A-Z)",
  }),
  async created() {
    this.beers = await this.getAllBeers();
    this.sortBeers();
    this.updateBeers(1);
  },
  methods: {
    getAllBeers: async function() {
      const beers = await getAllBeers();
      return beers.data;
    },
    updateBeers: function(n) {
      this.currentPage = n;
      this.firstBeerId = this.itemsPerPage * (n - 1) + 1;
      this.lastBeerId = this.firstBeerId + this.itemsPerPage - 1;

      if (this.lastBeerId > this.beers.length) {
        this.lastBeerId = this.beers.length;
      }
      this.shownBeers = this.beers.slice(this.firstBeerId - 1, this.lastBeerId);
    },
    isCurrentPage: function(n) {
      return n === this.currentPage;
    },
    dynamicSort: function(property) {
      var sortOrder = 1;
      if (property[0] === "-") {
        sortOrder = -1;
        property = property.substr(1);
      }
      return function(a, b) {
        var result =
          a[property] < b[property] ? -1 : a[property] > b[property] ? 1 : 0;
        return result * sortOrder;
      };
    },
    sortBeers: function() {
      switch (this.sortedProperty) {
        case "Name (A-Z)":
          this.beers.sort(this.dynamicSort("name"));
          break;
        case "Name (Z-A)":
          this.beers.sort(this.dynamicSort("-name"));
          break;
        case "Price (low to high)":
          this.beers.sort(this.dynamicSort("price"));
          break;
        case "Price (high to low)":
          this.beers.sort(this.dynamicSort("-price"));
          break;
        case "Volume":
          this.beers.sort(this.dynamicSort("volume"));
          break;
        case "Alcohol %":
          this.beers.sort(this.dynamicSort("abv"));
          break;
      }

      this.updateBeers(this.currentPage);
    }
  }
};
</script>

<style scoped>
.current-page {
  text-decoration: underline;
}
</style>
