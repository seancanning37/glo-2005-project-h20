<template>
  <CustomerHeader v-if="!isLoading" v-bind:customer="customer" />
</template>

<script>
import CustomerHeader from "../components/CustomerHeader";
import axios from "axios";
import { getTokenInfo, isConnected } from "../api/login";

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
    if (isConnected()) {
      this.customer = await this.getCustomerInfos();
    } else {
      this.$router.push({ name: "Login" });
    }
  },
  methods: {
    getCustomerInfos: async function() {
      const tokenInfo = (await getTokenInfo()).data;
      const path =
        "http://localhost:5000/customers/" + this.$route.params.customer_id;
      if (
        tokenInfo["customer_id"].toString() === this.$route.params.customer_id
      ) {
        axios
          .get(path)
          .then(response => {
            this.customer = response.data;
            this.isLoading = !this.isLoading;
          })
          .catch(error => {
            console.log(error);
          });
      } else {
        this.$emit("unauthorized");
        this.$router.push({ name: "Home" });
      }
    }
  }
};
</script>

<style scoped></style>
