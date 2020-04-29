<template>
  <v-container>
    <v-text-field
      v-model="name"
      label="Name"
      prepend-icon="mdi-account"
    ></v-text-field>
    <v-btn v-on:click="updateName">Update name</v-btn>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "CustomerSettings",
  data: function() {
    return {
      name: ""
    };
  },
  methods: {
    updateName: function() {
      const path =
        "http://localhost:5000/customers/" +
        this.$route.params.customer_id +
        "/name";
      axios
        .put(path, {
          newName: this.name
        })
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "CustomerPage" });
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  }
};
</script>

<style scoped></style>
