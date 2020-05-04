<template>
  <v-container>
    <v-card-title>
      <p class="black--text" style="font-size: 30px;">
        Your Orders
      </p>
    </v-card-title>
    <v-container v-for="order in orders" :key="order.order_id">
      <Order :order="order" />
    </v-container>
  </v-container>
</template>

<script>
import axios from "axios";
import Order from "../components/order/Order.vue";

export default {
  name: "CustomerOrderHistory",
  components: {
    Order
  },
  data: function() {
    return {
      customer: {
        id: "",
        name: "",
        phone: "",
        email: "",
        username: "",
        address: "",
        city: "",
        country: ""
      },
      orders: [],
      isCurrentCustomer: false,
      isLoading: true
    };
  },
  created: async function() {
    await this.getCustomerInfos();
    await this.getDetailedOrders();
  },
  methods: {
    getCustomerInfos: function() {
      const path =
        "http://localhost:5000/customers/" + this.$route.params.customer_id;
      axios
        .get(path)
        .then(response => {
          this.customer = response.data;
          this.isLoading = !this.isLoading;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getDetailedOrders: function() {
      const path = `http://localhost:5000/orders/customer/${this.$route.params.customer_id}`;
      axios
        .get(path)
        .then(response => {
          this.orders = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped></style>
