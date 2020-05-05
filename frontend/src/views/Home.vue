<template>
  <div>
    <h1>HOME</h1>
    <v-btn v-on:click="randomShit"> Get token info </v-btn>
    <v-btn v-on:click="goToSignUp"> Sign up </v-btn>
    <v-btn v-on:click="goToLogin"> Login </v-btn>
    <v-btn v-on:click="goToLogout"> Logout </v-btn>
    <v-btn v-on:click="getCookie"> Cookie </v-btn>
    <v-btn v-on:click="isConnected"> isConnected </v-btn>
  </div>
</template>

<script>
import { getCookie, getTokenInfo, isConnected, logout } from "../api/login";
export default {
  name: "Home",
  methods: {
    randomShit: async function() {
      const response = await getTokenInfo();
      if (response !== null) {
        console.log(response.data);
      } else {
       this.$router.push({name: "Login"})
      }
    },
    goToSignUp: function() {
      this.$router.push({ name: "SignUp" });
    },
    goToLogin: function() {
      this.$router.push({ name: "Login" });
    },
    goToLogout: async function() {
      const responseStatus = await logout();
      console.log(responseStatus);
    },
    getCookie: function() {
      const response = getCookie();
      console.log(response);
    },
    isConnected: function() {
      if (isConnected()) {
        console.log("Je suis connecté");
      } else {
        console.log("Je ne suis pas connecté");
      }
    }
  }
};
</script>
