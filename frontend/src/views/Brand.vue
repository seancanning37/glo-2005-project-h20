<template>
  <v-container>
    <p class="display-2">Brand</p>
    <brand-header />
    <hr />
    <beer-list :beerList="beerList" />
  </v-container>
</template>

<script>
import BrandHeader from "../components/brand/BrandHeader.vue";
import BeerList from "../components/beer/BeerList.vue";
import { getBrandBeers } from "../api/beer_api.js";

export default {
  name: "Brand",
  components: {
    BrandHeader,
    BeerList,
  },
  data: () => ({
    beerList: [],
  }),
  async created() {
    this.beerList = await this.getBrandBeers(this.$route.params.brand_id);
  },
  methods: {
    getBrandBeers: async function(brand_id) {
      const beerList = await getBrandBeers(brand_id);
      return beerList.data;
    },
  },
};
</script>

<style></style>
