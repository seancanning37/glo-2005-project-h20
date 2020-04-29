<template>
  <v-container>
    <h1>
      CUSTOMER PROFILE
    </h1>
    <h2>Name: {{ customer.name }}</h2>
    <p>Customer id: {{ customer.id }}</p>
    <p>pPhone: {{ customer.phone }}</p>
    <p>Email: {{ customer.email }}</p>
    <p>Username: {{ customer.username }}</p>
    <p>Address: {{ customer.address }}</p>
    <p>City: {{ customer.city }}</p>
    <p>Country: {{ customer.country }}</p>

    <v-btn :to=path>
      update informations
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: "CustomerHeader",
  props: ["customer"],
  data: function() {
    return {
      path: this.$route.params.customer_id + "/settings",
      customerId: this.$route.params.customer_id
    };
  }
};
</script>

<style scoped></style>
