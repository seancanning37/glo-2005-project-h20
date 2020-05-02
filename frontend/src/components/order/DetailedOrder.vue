<template>
    <v-container>
        <Order :order="order"/>
        <v-container v-for="item in order_items" :key="item.item_id">
            <v-card-text>
                {{ item.item_id }} {{ item.order_id }} {{ item.beer_id }} {{ item.quantity }}
            </v-card-text>
        </v-container>
    </v-container>
</template>

<script>
    import axios from "axios";
    import Order from "./Order.vue";

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
            getOrderItems: function() {
                if (this.order.order_id === "") {
                    return;
                }
                const path = `http://localhost:5000/orders/${this.order.order_id}/items`;
                axios
                    .get(path)
                    .then(response => {
                        this.order_items = response.data;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        },

    };
</script>

<style></style>
