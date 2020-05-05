<template>
  <v-container>
    <p class="display-2">
      Cart
    </p>
    <p>Cart total = {{ this.cartTotal.toFixed(2) }}</p>
    <v-container style="width: 500px;">
      <p class="headline pb-0 mb-0">Reward status</p>
      <p class="pt-0 mt-0">
        Spend 100 $ to get free shipping on your next order !
      </p>
      <v-progress-linear
        :value="money_earned"
        color="yellow darken-3"
        background-color="blue lighten-3"
        height="35px"
        width="150px"
        striped
        >{{ money_earned }} / 100</v-progress-linear
      >
    </v-container>
  </v-container>
</template>

<script>
import { getRewards } from "../../api/cart";

export default {
  name: "CartHeader",
  data: () => ({
    money_earned: 0
  }),
  props: ["cartTotal"],
  created: async function() {
    await this.getRewards();
  },
  methods: {
    getRewards: async function() {
      const response = await getRewards();
      this.money_earned = response.data["money_earned"] * 100;
    }
  }
};
</script>

<style scoped></style>
