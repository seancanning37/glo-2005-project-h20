<template>
  <v-container>
    <v-btn :to="this.orderHistoryPath" v-text="'Order History'" class="subtitle-1 font-weight-bold">
      <v-icon left v-text="'mdi-cart'" />
    </v-btn>
    <h1>
      CUSTOMER PROFILE
    </h1>
    <h2>Name: {{ customer.name }}</h2>
    <p>Customer id: {{ customer.id }}</p>
    <p>Phone: {{ customer.phone }}</p>
    <p>Email: {{ customer.email }}</p>
    <p>Username: {{ customer.username }}</p>
    <p>Address: {{ customer.address }}</p>
    <p>City: {{ customer.city }}</p>
    <p>Country: {{ customer.country }}</p>

    <v-btn :to="path">
      update informations
    </v-btn>
  </v-container>
</template>

<script>
import {getTokenInfo} from "../api/login";

export default {
  name: "CustomerHeader",
  props: ["customer"],
  data: function() {
    return {
      path: this.$route.params.customer_id + "/settings",
      customerId: this.$route.params.customer_id,
      orderHistoryPath: ""
    };
  },
  created: async function() {
    const response = await getTokenInfo();
    if (response) {
      this.orderHistoryPath = `/customers/${response.data['customer_id']}/order_history`
    }
  }
};
</script>

<style scoped></style>
