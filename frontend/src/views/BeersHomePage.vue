<template>
  <div id="container">
    <v-list
      v-for="(beer, index) in beers"
      v-bind:key="beer.id"
      v-bind:index="index"
      @click.native="$router.push(`/beers/${beer.id}`)"
    >
      <v-card>
        <v-row>
          <v-col>
            <v-img width="200" height="200" contain :src="beer.pictureURL" />
          </v-col>
          <v-col>
            <v-list-item two-line>
              <v-list-item-content>
                <v-list-item-title id="collectionName">{{
                  beer.name
                }}</v-list-item-title>
                <v-list-item-subtitle id="collectionYear">{{
                  beer.price
                }}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
      </v-card>
    </v-list>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BeersHomePage",
  data: () => ({
    beers: []
  }),
  created() {
    this.getAllBeers();
  },
  methods: {
    getAllBeers() {
      const path = "http://localhost:5000/beers";
      axios
        .get(path)
        .then(response => {
          console.log(response.data);
          this.beers = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped></style>
