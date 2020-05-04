<template>
  <div>
    <h1>HOME</h1>
    <v-btn v-on:click="randomShit"> console log token </v-btn>
    <v-btn v-on:click="goToSignUp"> Sign up </v-btn>
    <v-btn v-on:click="goToLogin"> Login </v-btn>
    <v-btn v-on:click="goToLogout"> Logout </v-btn>
  </div>
</template>

<script>
import { getToken, logout } from "../api/login";
export default {
  name: "Home",
  methods: {
    randomShit: function() {
      console.log(getToken());
    },
    goToSignUp: function() {
      this.$router.push({ name: "SignUp" });
    },
    goToLogin: function() {
      this.$router.push({ name: "Login" });
    },
    goToLogout: function() {
      const responseStatus = logout();
      console.log(responseStatus);
    }
  }
};
</script>
