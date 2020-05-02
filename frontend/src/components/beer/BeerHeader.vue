<template>
  <v-container class="py-0">
    <v-row class="py-0">
      <v-col cols="4" justify="start">
        <v-container>
          <v-img height="500px" width="300px" :src="beer.pictureURL"></v-img>
        </v-container>
      </v-col>

      <v-col class="my-0" style="background-color: #f7f7f7;">
        <v-container text-left>
          <a class="link black--text" :href="'/brands/' + brand.id">
            <p class="display-1 my-0">{{ brand.name }}</p>
          </a>
          <p class="display-2">{{ beer.name }}</p>
          <p class="title">{{ beer.description }}</p>
        </v-container>

        <v-container text-left>
          <v-row>
            <v-col cols="2">
              <p class="headline">{{ type.name }}</p>
            </v-col>
            <v-col cols="1">
              <p class="headline">|</p>
            </v-col>
            <v-col cols="2">
              <p class="headline">{{ beer.volume }} ml</p>
            </v-col>
            <v-col cols="1">
              <p class="headline">|</p>
            </v-col>
            <v-col>
              <p class="headline">{{ brand.city }}, {{ brand.country }}</p>
            </v-col>
          </v-row>
        </v-container>

        <v-container text-left>
          <p class="display-1">{{ beer.price }}$</p>
        </v-container>

        <hr />

        <v-container>
          <v-row>
            <v-col col="1">
              <v-icon>mdi-check</v-icon>
            </v-col>
            <v-col cols="3">
              <p>{{ beer.disponibility }} avalaible online</p>
            </v-col>
          </v-row>
        </v-container>

        <v-container text-left>
          <v-btn v-on:click="$emit('addBeerToCart')">
            Add to cart
          </v-btn>
        </v-container>
      </v-col>
    </v-row>
    <v-container> </v-container>
  </v-container>
</template>

<script>

export default {
  name: "BeerHeader",
  props: ["beer", "brand", "type"],
};
</script>

<style scoped></style>
