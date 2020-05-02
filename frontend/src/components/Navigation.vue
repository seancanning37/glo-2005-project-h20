<template>
  <v-list dense nav>
    <v-list-item v-for="page in pages" :key="page.text" :to="page.path">
      <v-icon left v-text="page.icon" />
      <v-list-item-content>
        <v-list-item-title
          class="subtitle-1 font-weight-bold"
          v-text="page.text"
        />
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: "Navigation",
  data: function() {
    return {
      pages: [
        { text: "Home", path: "/", icon: "mdi-home" },
        { text: "Beers", path: "/beers", icon: "mdi-home" },
        { text: "Brands", path: "/brands", icon: "mdi-home" },
        { text: "Shopping Cart", path: "/cart", icon: "mdi-cart" }
      ]
    };
  }
};
</script>

<style scoped></style>
