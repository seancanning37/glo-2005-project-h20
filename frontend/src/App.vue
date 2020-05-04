<template>
  <div id="app">
    <v-app id="inspire">
      <v-navigation-drawer v-model="drawer" app clipped>
        <nav-menu />
      </v-navigation-drawer>
      <v-app-bar app clipped-left>
        <v-app-bar-nav-icon v-on:click.stop="drawer = !drawer">
        </v-app-bar-nav-icon>
        <v-toolbar-title>
          Beerbender
        </v-toolbar-title>
        <v-spacer />
        <v-btn v-on:click="goToCustomerProfile" class="mr-2">
          <v-icon>
            mdi-account
          </v-icon>
        </v-btn>
        <v-btn v-on:click="goToCart">
          <v-icon>
            mdi-cart
          </v-icon>
        </v-btn>
      </v-app-bar>
      <v-content class="align-content-center">
        <v-container
          class="d-flex justify-center align-baseline fill-height"
          fluid
        >
          <router-view v-on:success-signup="successSignUp" />

        </v-container>
      </v-content>
      <v-snackbar class="text-center" top="top" right="right"  v-model="snackbar" :color="color" :timeout="timeout">
        {{ message }}</v-snackbar
      >
    </v-app>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";
import { getCurrentCustomerId } from "./api/customer";
import {isConnected} from "./api/login";

export default {
  name: "app",
  components: {
    "nav-menu": Navigation
  },
  data: function() {
    return {
      drawer: null,
      timeout: 6000,
      snackbar: false,
      color: "success",
      message: "Account created"
    };
  },
  methods: {
    goToCart: function() {
      this.$router.push("/cart");
    },
    goToCustomerProfile: function() {
      if (isConnected()) {
        const getCurrentCustomerId = this.getCurrentCustomerId();
        this.$router.push("/customers/" + getCurrentCustomerId);
      } else {
        this.$router.push({name: "Login"})
      }
    },
    getCurrentCustomerId: function() {
      return getCurrentCustomerId();
    },
    successSignUp: function() {
      this.snackbar = true;
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}

.link {
  text-decoration: none !important;
}

.link:hover {
  text-decoration: underline !important;
}
</style>
