<template>
  <v-container>
    <v-row>
      <v-col cols="4" class="py-6">
        <p class="display-2">Detailed info</p>
      </v-col>

      <v-col class="py-6" style="background-color: #f7f7f7">
        <v-row>
          <v-col cols="6">
            <p class="my-1">Country</p>
            <p class="font-weight-bold">{{ brand.country }}</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">Brand</p>
            <p class="font-weight-bold">{{ brand.name }}</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">City</p>
            <p class="font-weight-bold">{{ brand.city }}</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">Type</p>
            <p class="font-weight-bold">{{ type.name }}</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">Degree of alcohol</p>
            <p class="font-weight-bold">{{ beer.abv }} %</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">Style</p>
            <p class="font-weight-bold">{{ beerStyle.name }}</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">Size</p>
            <p class="font-weight-bold">{{ beer.volume }} ml</p>
          </v-col>

          <v-col cols="6">
            <p class="my-1">IBU</p>
            <p class="font-weight-bold">{{ beer.ibu }}</p>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "BeerInfo",
  props: ["beer", "brand", "type", "beerStyle"]
};
</script>

<style></style>
