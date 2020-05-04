<template>
  <v-container>
    <cart-header />
    <cart-item v-for="item in cart" :key="item.beer_id" :cartItem="item" />
    <v-btn v-on:click="proceedToCheckout">
      Proceed to Checkout
    </v-btn>
    <v-snackbar v-model="snackbar" :color="color" :timeout="timeout">
      {{ message }}</v-snackbar
    >
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
      customerInfos: {},
      snackbar: false,
      color: "error",
      timeout: 6000,
      message: ""
    };
  },
  async created() {
    this.cart = await this.getShoppingCartItems();
  },
  methods: {
    getShoppingCartItems: function() {
      return getCartItems();
    },
    proceedToCheckout: async function() {
      const response = await checkout();
      if (response === 500) {
        this.color = "error";
        this.message = "Oops something went wrong, please try again";
      } else if (response === 400) {
        this.color = "error";
        this.message = "Cart is empty";
      } else if (response === 201) {
        this.color = "success";
        this.message = "Checkout was successfull";
      } else {
        console.log("response code: " + response);
        this.color = "info";
        this.message = "Un cas que je ne gere pas";
      }
      this.cart = await this.getShoppingCartItems();
      this.snackbar = true;
    }
  }
};
</script>

<style scoped></style>
