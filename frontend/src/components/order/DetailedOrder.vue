<template>
  <v-container>
    <Order :order="order" />

    <v-card height="275" v-for="item in order_items" :key="item.item_id">
      <v-row v-if="item.beer">
        <v-col cols="3">
          <v-img
                  :src="item.beer.pictureURL"
                  height="200"
                  width="75"
                  class="ml-10 mt-3"
          ></v-img>
        </v-col>

        <v-col>
          <v-card-title class="mb-0 pb-0">
            <a :href="'/beers/' + item.beer_id" class="link black--text ">
              <p
                      :class="'headline' + ' mb-0 mx-6'"
              >
                {{ item.beer.name }}
              </p>
            </a>
          </v-card-title>

          <v-card-text class="pt-5 text-left">
            <p class="subtitle-2 mx-6">Price: {{ item.beer.price }}$</p>
            <p class="subtitle-2 mx-6">Quantity: {{ item.quantity }}</p>
            <p class="subtitle-2 mx-6 font-weight-bold">Total: {{ item.beer.price * item.quantity }}$</p>
          </v-card-text>

        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
import Order from "./Order.vue";
import {getBeer} from "../../api/beer_api";
import {getOrderItems} from "../../api/orders";

export default {
  name: "DetailedOrder",
  props: ["order"],
  components: {
    Order
  },
  data: function() {
    return {
      order_items: []
    };
  },
  created: async function() {
    await this.getOrderItems();
  },
  methods: {
    getOrderItems: async function() {
      if (this.order.order_id === "") {
        return;
      }
      const response = await getOrderItems(this.order.order_id);
      this.order_items = response.data;
      await this.getBeers();
    },
    getBeers: async function() {
      if (this.order.order_id === "") {
        return;
      }

      for (let i=0; i<this.order_items.length; i++) {
        const response = await getBeer(this.order_items[i].beer_id);
        this.order_items[i]['beer'] = response.data;
        this.order_items[i]['item_id'] += 1; //help
        this.order_items[i]['item_id'] -= 1; //help
      }
    }
  }
};
</script>

<style></style>
