<template>
  <div>
    <h1>HOME</h1>
    <v-btn v-on:click="randomShit"> console log token </v-btn>
  </div>
</template>

<script>
import { getToken } from "../api/login";
export default {
  name: "Home",
  methods: {
    randomShit: function() {
      console.log(getToken());
    }
  }
};
</script>
