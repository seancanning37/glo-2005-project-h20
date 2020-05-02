<template>
  <v-card class="mb-5">
    <v-card-title class="justify-center">
      {{ "Beer id: " + cartItem.beer_id }}
    </v-card-title>
    <v-card-subtitle>
      {{ "Quantity: " + cartItem.quantity }}
    </v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: "CartItem",
  props: ["cartItem"]
};
</script>

<style scoped></style>
