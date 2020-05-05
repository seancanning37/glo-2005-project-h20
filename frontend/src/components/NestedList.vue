<template>
  <v-list-group>
    <template v-slot:activator>
      <v-list-item-title>{{ title }}</v-list-item-title>
    </template>

    <v-list-item
      v-for="(item, i) in items"
      :key="i"
      :class="currentProperty === item ? 'color: blue lighten-4' : ''"
      @click="itemClicked(title, item)"
      link
    >
      <v-list-item-content>
        <v-list-item-title>
          {{ item }}
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-list-group>
</template>

<script>
export default {
  name: "NestedList",
  props: ["title", "items", "currentProperty"],
  methods: {
    itemClicked: function(property, name) {
      this.$emit("item-clicked", property, name);
    }
  }
};
</script>

<style></style>
