<template>
  <v-card class="mb-5">
    <v-card-title class="justify-center">
      {{ "Beer id: " + beer_id }}
    </v-card-title>
    <v-card-subtitle>
      {{ "Quantity: " + quantity }}
    </v-card-subtitle>
  </v-card>
</template>

<script>
export default {
  name: "CartItem",
  props: ["quantity", "beer_id"]
};
</script>

<style scoped></style>
