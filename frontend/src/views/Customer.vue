<template>
  <CustomerHeader v-if="!isLoading" v-bind:customer="customer" />
</template>

<script>
import CustomerHeader from "../components/CustomerHeader";
import axios from "axios";

export default {
  name: "Customer",
  components: {
    CustomerHeader
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
      isCurrentCustomer: false,
      isLoading: true
    };
  },
  created: async function() {
    this.customer = await this.getCustomerInfos();
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
    }
  }
};
</script>

<style scoped></style>
