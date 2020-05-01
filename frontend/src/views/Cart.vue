<template>
  <v-container>
    <v-card v-for="cartKey in Object.keys(cart)" :key="cartKey">
      <v-card-title>
        {{ cartKey + ": " + cart[cartKey] }}
      </v-card-title>
    </v-card>
  </v-container>
</template>

<script>
import { getCartItems } from "../api/cart";

export default {
  name: "Cart",
  data: function() {
    return {
      cart: {}
    };
  },
  async created() {
    this.cart = await this.getShoppingCartItems();

  },
  methods: {
    getShoppingCartItems: function() {
      return getCartItems();
    }
  }
};
</script>

<style scoped></style>
