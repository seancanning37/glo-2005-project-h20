<template>
  <v-container>
    <cart-header />
    <cart-item
      v-for="(quantity, beer_id) in cart"
      :key="beer_id"
      :quantity="quantity"
      :beer_id="beer_id"
    />
    <v-btn>
      Continue sho
    </v-btn>
    <v-btn>
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
