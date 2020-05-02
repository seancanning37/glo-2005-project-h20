<template>
  <v-container>
    <cart-header />
    <cart-item v-for="(quantity, beer_id) in cart" :key="beer_id" :quantity="quantity" :beer_id="beer_id"/>
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
