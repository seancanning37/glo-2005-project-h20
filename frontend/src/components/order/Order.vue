<template>
  <v-card height="275">
    <v-row>
      <v-col>
        <v-card-title class="mb-0 pb-0">
          <a
            :href="`/customers/${order.customer_id}/${order.order_id}`"
            class="link black--text"
          >
            <p
              :class="needsSmallerFont() ? 'title' : 'headline' + ' mb-0 mx-6'"
            >
              Order: {{ order.order_id }}
            </p>
          </a>
        </v-card-title>

        <v-card-text class="pt-5">
          <p class="subtitle-2 mx-6 text-left">
            Order Placed: {{ order.order_date }}
          </p>
          <p class="subtitle-2 mx-6 text-left">Status: {{ order.status }}</p>
          <p class="subtitle-2 mx-6 text-left">Comments: {{ order.comment }}</p>
          <p class="subtitle-2 mx-6 text-left font-weight-bold">
            Total: {{ order.total_price }}$
          </p>
        </v-card-text>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: "Order",
  props: ["order"],
  methods: {
    needsSmallerFont() {
      return this.order.customer_id.length > 17;
    }
  }
};
</script>

<style></style>
