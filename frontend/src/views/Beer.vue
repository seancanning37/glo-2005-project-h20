<template class="salut">
  <v-container>
    <beer-header
      :beer="beer"
      :brand="brand"
      :type="type"
      v-on:addBeerToCart="addBeerToCart"
    />

    <hr />

    <beer-info
      :beer="beer"
      :brand="brand"
      :type="type"
      :beerStyle="beerStyle"
    />
  </v-container>
</template>

<script>
import BeerHeader from "../components/beer/BeerHeader.vue";
import BeerInfo from "../components/beer/BeerInfo.vue";
import { getBeer, getBrand, getStyle, getType } from "../api/beer_api.js";
import { addBeerToCart } from "../api/cart";

export default {
  name: "BeerPage",
  components: {
    BeerHeader,
    BeerInfo
  },
  data: () => ({
    beer: {
      id: 0,
      name: "",
      brand_id: 0,
      abv: 0.0,
      ibu: 0,
      volume: 0,
      price: 0.0,
      description: "",
      pictureURL: "",
      disponibility: 0
    },
    brand: {
      name: "brand",
      city: "city",
      country: "country"
    },
    type: {
      name: "type"
    },
    beerStyle: {
      name: "style"
    },
    quantity: 0
  }),
  async created() {
    await this.getBeer();
    await this.getBrand();
    await this.getStyle();
    await this.getType();
  },
  methods: {
    getBeer: async function() {
      const beer = await getBeer(this.$route.params.beer_id);
      this.beer = beer.data;
    },
    getBrand: async function() {
      const brand = await getBrand(this.beer.brand_id);
      this.brand = brand.data;
    },
    getStyle: async function() {
      const beerStyle = await getStyle(this.beer.style_id);
      this.beerStyle = beerStyle.data;
    },
    getType: async function() {
      const type = await getType(this.beer.type_id);
      this.type = type.data;
    },
    addBeerToCart: async function(quantity) {
      await addBeerToCart(this.beer.id, quantity);
    }
  }
};
</script>

<style scoped></style>
