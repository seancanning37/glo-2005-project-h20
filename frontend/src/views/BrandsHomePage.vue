<template>
  <v-container>
    <v-row>
      <v-col>
        <v-container class="pb-0 my-0">
          <v-row class="pb-0 my-0">
            <v-col class="pb-0">
              <p
                style="position:relative; top: 15%;"
                class="headline text-left mb-0 pl-3"
              >
                Results {{ this.firstBrandId }}-{{ this.lastBrandId }} of
                {{ this.filteredBrands.length }}
              </p>
            </v-col>
          </v-row>
        </v-container>
        <v-row class="pt-6">
          <v-col v-for="brand in shownBrands" class="pt-0" :key="brand.name">
            <Brand :brand="brand" />
          </v-col>
        </v-row>
      </v-col>

      <v-container class="pt-0" style="position: relative; right: -375px;">
        <a
          :class="
            isCurrentPage(n)
              ? 'current-page black--text font-weight-bold text-center'
              : 'link black--text text-center'
          "
          v-for="n in Math.ceil(this.filteredBrands.length / 12)"
          :key="n"
          @click="updateBrands(n)"
        >
          {{ n }}
        </a>
      </v-container>
    </v-row>
  </v-container>
</template>

<script>
import { getAllBrands } from "../api/brand.js";
import Brand from "../components/brand/Brand";
export default {
  name: "BrandsHomePage",
  components: { Brand },
  data: () => ({
    brands: [],
    filteredBrands: [],
    shownBrands: [],
    firstBrandId: 0,
    lastBrandId: 12,
    itemsPerPage: 12,
    currentPage: 0
  }),
  async created() {
    this.brands = await this.getAllBrands();
    this.filteredBrands = this.brands;
    this.updateBrands(1);
  },
  methods: {
    getAllBrands: async function() {
      const brands = await getAllBrands();
      return brands.data;
    },
    updateBrands: function(n) {
      this.currentPage = n;
      this.firstBrandId = this.itemsPerPage * (n - 1) + 1;
      this.lastBrandId = this.firstBrandId + this.itemsPerPage - 1;
      if (this.lastBrandId > this.filteredBrands.length) {
        this.lastBrandId = this.filteredBrands.length;
      }
      this.shownBrands = this.filteredBrands.slice(
        this.firstBrandId - 1,
        this.lastBrandId
      );
    },
    isCurrentPage: function(n) {
      return n === this.currentPage;
    }
  }
};
</script>

<style scoped></style>
