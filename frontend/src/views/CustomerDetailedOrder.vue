<template>
  <DetailedOrder :order="order" :key="order.order_id" />
</template>

<script>
import axios from "axios";
import DetailedOrder from "../components/order/DetailedOrder.vue";
import { getOrder } from "../api/orders";

export default {
  name: "CustomerDetailedOrder",
  components: {
    DetailedOrder
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
      order: {
        order_id: "",
        customer_id: 0,
        order_date: "",
        status: "",
        total_price: 0,
        comment: ""
      },
      isCurrentCustomer: false,
      isLoading: true
    };
  },
  created: async function() {
    await this.getCustomerInfos();
    await this.getOrder();
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
    getOrder: async function() {
      const response = await getOrder(this.$route.params.order_id);
      this.order = response.data;
    }
  }
};
</script>

<style scoped></style>
