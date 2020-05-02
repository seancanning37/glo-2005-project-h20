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
          <router-view />
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import Navigation from "./components/Navigation";

export default {
  name: "app",
  components: {
    "nav-menu": Navigation
  },
  data: function() {
    return {
      drawer: null
    };
  },
  methods: {
    goToCart: function() {
      this.$router.push("/cart");
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
