<template>
  <v-container class="text-center">
    <v-card class="px-5">
      <v-card-title class="justify-center">
        To continue, log in to The Last Beerbender
      </v-card-title>
      <v-text-field
        class="py-0"
        v-model="email"
        label="Email"
        :error="invalidEmail"
      ></v-text-field>
      <v-text-field
        class="py-0"
        v-model="password"
        type="password"
        label="Password"
        v-bind:error="invalidPassword"
      ></v-text-field>
      <v-container class="text-center py-8">
        <v-btn @click="login">Log in</v-btn>
      </v-container>
      <v-container class="text-center">
        <p class="subtitle-1">Don't have an account ?</p>
        <v-btn href="/signup">
          Sign up for Beerbender
        </v-btn>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import Router from "../router";

export default {
  name: "LoginForm",
  data: function() {
    return {
      email: "",
      password: "",
      invalidEmail: false,
      invalidPassword: false
    };
  },
  methods: {
    login: function() {
      const path = "http://localhost:5000/login";
      if (this.email !== "" && this.password !== "") {
        axios
          .post(path, {
            email: this.email,
            password: this.password
          })
          .then(response => {
            console.log(response.data);
            Router.push("/");
          })
          .catch(error => {
            console.log(error.response.data);
          });
      }
      this.invalidEmail = true;
      this.invalidPassword = true;
    }
  }
};
</script>

<style scoped></style>
