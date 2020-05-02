<template>
    <v-card>
        <v-card-title>
        </v-card-title>
    </v-card>
</template>

<script>
    export default {
        name: "CartItem",
        props: ["quantity", "beer_id"],
        created() {
            console.log("beer id: " + this.beer_id);
        }
    }
</script>

<style scoped>

</style>
