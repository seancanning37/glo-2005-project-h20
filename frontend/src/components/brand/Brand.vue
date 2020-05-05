<template>
  <v-card height="215" width="400">
    <v-row>
      <v-col>
        <v-card-title class="mb-0 pb-0">
          <a :href="'/brands/' + brand.id" class="link black--text ">
            <p class="headline">
              {{ brand.name }}
            </p>
          </a>
          <v-container class="pt-0 my-0">
            <p class="text-left subtitle-1">
              {{ brand.address }}
            </p>
            <p class="text-left subtitle-1">
              {{ brand.city }}, {{ brand.country }}
            </p>
            <p class="text-left subtitle-1">{{ brand.phone }}</p>
          </v-container>
        </v-card-title>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: "Brand",
  props: ["brand"],
};
</script>

<style></style>
