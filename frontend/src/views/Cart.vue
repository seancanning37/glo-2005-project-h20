<template>
  <v-container>
    <cart-header />
    <cart-item v-for="cartItem in Object(cart)" :key="cartItem.key"/>
  </v-container>
</template>

<script>
import { getCartItems } from "../api/cart";
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
    }
  }
};
</script>

<style scoped></style>
