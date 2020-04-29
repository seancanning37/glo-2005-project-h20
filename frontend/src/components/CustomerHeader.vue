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
    <p>Address: {{ customer.address}}</p>
    <p>City: {{ customer.city }}</p>
    <p>Country: {{ customer.country}}</p>
  </v-container>
</template>

<script>
export default {
  name: "CustomerHeader",
  props: ["customer"]
};
</script>

<style scoped></style>
