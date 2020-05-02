<template>
    <v-container>
        <a :href="`/customers/${order.customer_id}/${order.order_id}`">
            {{ order.order_id }}
        </a>
        <v-card-text>
            {{ order.customer_id }} {{ order.order_date }} {{ order.status }} {{ order.total_price }} {{ order.comment }}
        </v-card-text>
    </v-container>
</template>

<script>
    export default {
        name: "Order",
        props: ["order"],
        methods: {
        },
    };
</script>

<style></style>
