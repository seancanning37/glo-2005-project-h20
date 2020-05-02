<template>
    <v-container>
        <v-card-text>
            {{ order.order_id }}
        </v-card-text>
        <v-card-text>
            {{ order.customer_id }}
        </v-card-text>
        <v-card-text>
            {{ order.order_date }}
        </v-card-text>
        <v-card-text>
            {{ order.status }}
        </v-card-text>
        <v-card-text>
            {{ order.total_price }}
        </v-card-text>
        <v-card-text>
            {{ order.comment }}
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
