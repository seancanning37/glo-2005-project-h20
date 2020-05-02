<template>
  <v-container class="mb-0 pb-0">
    <p class="display-2 mb-0 pb-2">{{ brand.name }}</p>
    <p class="subtitle-1">{{ brand.city }}, {{ brand.country }}</p>
    <v-row>
      <v-col class="mb-0 pb-0">
        <p>{{ brand.address }}</p>
      </v-col>
      <v-col class="mb-0 pb-0">
        <p>{{ brand.phone }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "BrandHeader",
  props: ["brand"]
};
</script>

<style></style>
