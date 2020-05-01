<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-row>
            <v-col>
              <v-img :src="beer.pictureURL" height="300" width="100"></v-img>
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Beer",
  props: ["beer"],
};
</script>

<style></style>
