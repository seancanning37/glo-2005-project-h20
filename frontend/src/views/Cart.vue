<template>
  <v-container>
    <cart-header />
    <cart-item v-for="item in cart" :key="item.beer_id" :cartItem="item" />
    <v-btn v-on:click="proceedToCheckout">
      Proceed to Checkout
    </v-btn>
  </v-container>
</template>

<script>
import { checkout, getCartItems } from "../api/cart";
import CartItem from "../components/cart/CartItem";
import CartHeader from "../components/cart/CartHeader";

export default {
  name: "Cart",
  components: {
    "cart-header": CartHeader,
    "cart-item": CartItem
  },
  data: function() {
    return {
      cart: {},
      customerInfos: {}
    };
  },
  async created() {
    this.cart = await this.getShoppingCartItems();
  },
  methods: {
    getShoppingCartItems: function() {
      return getCartItems();
    },
    proceedToCheckout: function() {
      checkout();
    }
  }
};
</script>

<style scoped></style>
