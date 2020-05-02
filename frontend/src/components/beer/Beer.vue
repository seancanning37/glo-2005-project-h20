<template>
  <v-card height="350" width="550">
    <v-row>
      <v-col cols="3">
        <v-img
          :src="beer.pictureURL"
          height="300"
          width="100"
          class="ml-10 mt-3"
        ></v-img>
      </v-col>

      <v-col>
        <v-card-title class="mb-0 pb-0">
          <a :href="'/beers/' + beer.id" class="link black--text ">
            <p
              :class="
                needsSmallerFont() ? 'headline' : 'display-1' + ' mb-0 mx-6'
              "
            >
              {{ beer.name }}
            </p>
          </a>
          <v-container class="pt-2 my-0">
            <p class="text-right">{{ beer.volume }} ml • {{ beer.abv }} %</p>
          </v-container>
        </v-card-title>

        <v-card-text>
          <p class="subtitle-1 mx-6 text-left">{{ beer.description }}</p>
        </v-card-text>

        <v-card-actions
          style="position: absolute; right:6px; bottom: 10px;"
          class=" px-6"
        >
          <v-spacer />
          <p class="font-weight-bold px-4 pt-5">{{ beer.price }}$</p>
          <v-btn @click="addToCart()">add to cart</v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: "Beer",
  props: ["beer"],
  methods: {
    addToCart: function() {
      console.log("Add to cart");
    },
    needsSmallerFont() {
      return this.beer.name.length > 18;
    }
  }
};
</script>

<style></style>
