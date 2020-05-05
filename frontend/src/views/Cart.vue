<template>
  <v-container>
    <cart-header v-if="isConnected"/>
    <cart-item v-for="item in cart" :key="item.beer_id" :cartItem="item" v-on:deleteItem="deleteItem" v-on:changeQuantity="changeQuantity" />
    <v-btn v-on:click="proceedToCheckout">
      Proceed to Checkout
    </v-btn>
    <v-snackbar v-model="snackbar" :color="color" :timeout="timeout">
      {{ message }}</v-snackbar
    >
  </v-container>
</template>

<script>
  import {changeQuantity, checkout, getCartItems, removeItem} from "../api/cart";
import CartItem from "../components/cart/CartItem";
import CartHeader from "../components/cart/CartHeader";
import { isConnected } from "../api/login";

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
      message: "",
      isConnected: false
    };
  },
  async created() {
    if (isConnected()) {
      this.cart = await this.getShoppingCartItems();
      this.isConnected = true;
    } else {
      this.$emit("cart-connected");
      this.$router.push({ name: "Login" });
    }
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
        this.$router.push({ name: "Beers" });
      } else {
        console.log("response code: " + response);
        this.color = "info";
        this.message = "Un cas que je ne gere pas";
      }
      this.cart = await this.getShoppingCartItems();
      this.snackbar = true;
    },
    deleteItem: async function(beerId) {
      await removeItem(beerId);
      this.cart = await this.getShoppingCartItems();
    },
    changeQuantity: async function(beerId, quantity) {
      await changeQuantity(beerId, quantity);
      this.cart = await this.getShoppingCartItems();
    }
  }
};
</script>

<style scoped></style>
