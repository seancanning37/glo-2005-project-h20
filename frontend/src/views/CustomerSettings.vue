<template>
  <v-container>
    <v-text-field
      v-model="parameters.name"
      label="Name"
      prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.phone"
            label="Phone"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.email"
            label="Email"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.username"
            label="Username"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.address_line_1"
            label="Address line 1"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.address_line_2"
            label="Address line 2"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.city"
            label="City"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-text-field
            v-model="parameters.country"
            label="Country"
            prepend-icon="mdi-account"
    ></v-text-field>
    <v-btn v-on:click="update">Update</v-btn>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "CustomerSettings",
  data: function() {
    return {
      parameters: {
        name: "",
        phone: "",
        email: "",
        username: "",
        address_line_1: "",
        address_line_2: "",
        city: "",
        country: ""
      }
    };
  },
  methods: {
    update: function() {
      const path =
        "http://localhost:5000/customers/" +
        this.$route.params.customer_id +
        "/modify";

      const modified_parameters = this.getModifiedParameters();

      axios
        .put(path, modified_parameters)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "CustomerPage" });
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    getModifiedParameters: function() {
      let modified_parameters = {};
      for (let key in this.parameters) {
        if (this.parameters[key] !== "") {
          modified_parameters[key] = this.parameters[key];
        }
      }
      return modified_parameters
    }
  }
};
</script>

<style scoped></style>
