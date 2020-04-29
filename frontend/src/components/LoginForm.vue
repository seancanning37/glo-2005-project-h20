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
import { login } from "../api/login";

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
      if (this.email !== "" && this.password !== "") {
        login(this.email, this.password);
      }
      this.invalidEmail = true;
      this.invalidPassword = true;
    }
  }
};
</script>

<style scoped></style>
