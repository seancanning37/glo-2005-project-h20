<template>
    <v-card height="275" width="400">
        <v-row>
            <v-col>
                <v-card-title class="mb-0 pb-0">
                    <a :href="'/brands/' + brand.id" class="link black--text ">
                        <p
                                :class="needsSmallerFont() ? 'title' : 'headline' + ' mb-0 mx-6'"
                        >
                            {{ brand.name }}
                        </p>
                    </a>
                    <v-container class="pt-0 my-0">
                        <p class="text-right subtitle-1">
                            {{ brand.address }} • {{ brand.city }}
                            {{ brand.country }} • {{ brand.id }}
                            {{ brand.name }} • {{ brand.phone }}
                        </p>
                    </v-container>
                </v-card-title>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
    export default {
        name: "Brand",
        props: ["brand"],
        methods: {
            needsSmallerFont() {
                return this.brand.name.length > 17;
            }
        }
    };
</script>

<style></style>
