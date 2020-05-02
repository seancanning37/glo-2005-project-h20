<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <v-container class="text-left pt-12">
          <v-list class="pt-12">
            <hr />
            <nested-list
              title="Type"
              :items="types"
              :currentProperty="filterProperty"
              v-on:item-clicked="filterBeers"
            />

            <hr />
            <nested-list
              title="Style"
              :items="styles"
              :currentProperty="filterProperty"
              v-on:item-clicked="filterBeers"
            />

            <hr />
            <v-list-item link @click="filterBeers('See all', '')">
              <v-list-item-title>See all</v-list-item-title>
            </v-list-item>

            <hr />
          </v-list>
        </v-container>
      </v-col>
      <v-col>
        <v-container class="pb-0 my-0">
          <v-row class="pb-0 my-0">
            <v-col class="pb-0">
              <p
                style="position:relative; top: 15%;"
                class="headline text-left mb-0 pl-3"
              >
                Results {{ this.firstBeerId }}-{{ this.lastBeerId }} of
                {{ this.filteredBeers.length }}
              </p>
            </v-col>
            <v-spacer />
            <v-col cols="3" class="pb-0">
              <v-select
                v-model="sortedProperty"
                :items="properties"
                outlined
                v-on:change="sortBeers()"
                dense
              >
              </v-select>
            </v-col>
          </v-row>
        </v-container>

        <beer-list class="pt-0" :beerList="shownBeers" />
      </v-col>

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
              v-for="n in Math.ceil(this.filteredBeers.length / 12)"
              :key="n"
              @click="updateBeers(n)"
            >
              {{ n }}
            </a>
          </v-col>
        </v-row>
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import { getAllBeers } from "../api/beer_api.js";
import BeerList from "../components/beer/BeerList.vue";
import NestedList from "../components/NestedList";

export default {
  name: "BeersHomePage",
  components: {
    BeerList,
    NestedList
  },
  data: () => ({
    beers: [],
    filteredBeers: [],
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
      "Volume"
    ],
    sortedProperty: "Name (A-Z)",
    filterProperty: "",
    styleIdMap: {
      1: "Amber",
      2: "Blonde",
      3: "Brown",
      4: "Cream",
      5: "Dark",
      6: "Pale",
      7: "Strong",
      8: "Wheat",
      9: "Red",
      10: "Lime",
      11: "Pilsner",
      12: "Golden",
      13: "Fruit",
      14: "Honey"
    },
    typeIdMap: {
      1: "Ale",
      2: "Lager",
      3: "Malt",
      4: "Stout"
    },
    types: ["Ale", "Lager", "Malt", "Stout"],
    styles: [
      "Amber",
      "Blonde",
      "Brown",
      "Cream",
      "Dark",
      "Pale",
      "Strong",
      "Wheat",
      "Red",
      "Lime",
      "Pilsner",
      "Golden",
      "Fruit",
      "Honey"
    ]
  }),
  async created() {
    this.beers = await this.getAllBeers();
    this.filteredBeers = this.beers;
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

      if (this.lastBeerId > this.filteredBeers.length) {
        this.lastBeerId = this.filteredBeers.length;
      }
      this.shownBeers = this.filteredBeers.slice(
        this.firstBeerId - 1,
        this.lastBeerId
      );
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
          this.filteredBeers.sort(this.dynamicSort("name"));
          break;
        case "Name (Z-A)":
          this.filteredBeers.sort(this.dynamicSort("-name"));
          break;
        case "Price (low to high)":
          this.filteredBeers.sort(this.dynamicSort("price"));
          break;
        case "Price (high to low)":
          this.filteredBeers.sort(this.dynamicSort("-price"));
          break;
        case "Volume":
          this.filteredBeers.sort(this.dynamicSort("volume"));
          break;
        case "Alcohol %":
          this.filteredBeers.sort(this.dynamicSort("abv"));
          break;
      }

      this.updateBeers(this.currentPage);
    },
    filterBeers: function(property, filterName) {
      this.filterProperty = filterName;
      switch (property) {
        case "Type":
          this.filterType(filterName);
          break;
        case "Style":
          this.filterStyle(filterName);
          break;
        case "See all":
          this.filteredBeers = this.beers;
          break;
      }

      this.updateBeers(this.currentPage);
    },
    filterType: function(filterName) {
      const filteredBeers = [];
      for (const beer of this.beers) {
        if (this.typeIdMap[beer.type_id] === filterName) {
          filteredBeers.push(beer);
        }
      }
      this.filteredBeers = filteredBeers;
    },
    filterStyle: function(filterName) {
      const filteredBeers = [];
      for (const beer of this.beers) {
        if (this.styleIdMap[beer.style_id] === filterName) {
          filteredBeers.push(beer);
        }
      }
      this.filteredBeers = filteredBeers;
    }
  }
};
</script>

<style scoped>
.current-page {
  text-decoration: underline;
}
</style>
