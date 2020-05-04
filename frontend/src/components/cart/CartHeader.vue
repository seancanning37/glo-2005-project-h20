<template>
  <v-container>
    <p class="display-2">
      Cart
    </p>
    <p>
      Money earned: {{ money_earned }}
    </p>
  </v-container>
</template>

<script>
  import {getRewards} from "../../api/cart";

  export default {
  name: "CartHeader",
    data: function() {
    return {
      money_earned: 0
    }
    },
    created: async function () {
      await this.getRewards()
    },
    methods: {
    getRewards: async function () {
      const response = await getRewards();
      this.money_earned = response.data['money_earned'];
    }
    }
};
</script>

<style scoped></style>
