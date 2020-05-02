<template>
  <v-container>
    <p>{{ brand.name }}</p>
    <p>{{ brand.city }}, {{ brand.country }}</p>
  </v-container>
</template>

<script>
export default {
  name: "BrandHeader",
  props: ["brand"],
};
</script>

<style></style>
