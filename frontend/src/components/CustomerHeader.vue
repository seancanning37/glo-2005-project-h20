<template>
  <v-container>
    <h1>
      CUSTOMER PROFILE
    </h1>

    <v-container v-if="edit" class="align-center" style="width: 400px;">
      <v-text-field
        class="pb-0 mb-0 pt-8"
        v-model="parameters.name"
        label="Name"
        :append-icon="editName ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editName"
        @click:append="editName = !editName"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.phone"
        label="Phone"
        :append-icon="editPhone ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editPhone"
        @click:append="editPhone = !editPhone"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.email"
        label="Email"
        :append-icon="editEmail ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editEmail"
        @click:append="editEmail = !editEmail"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.username"
        label="Username"
        :append-icon="editUsername ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editUsername"
        @click:append="editUsername = !editUsername"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.address_line_1"
        label="Address line 1"
        :append-icon="editAddress1 ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editAddress1"
        @click:append="editAddress1 = !editAddress1"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.address_line_2"
        label="Address line 2"
        :append-icon="editAddress2 ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editAddress2"
        @click:append="editAddress2 = !editAddress2"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.city"
        label="City"
        :append-icon="editCity ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editCity"
        @click:append="editCity = !editCity"
        dense
      ></v-text-field>

      <v-text-field
        class="py-1 my-0"
        v-model="parameters.country"
        label="Country"
        :append-icon="editCountry ? 'mdi-check' : 'mdi-pencil'"
        :readonly="!editCountry"
        @click:append="editCountry = !editCountry"
        dense
      ></v-text-field>

      <v-btn @click="update">
        update informations
      </v-btn>
    </v-container>

    <v-container v-else class="align-center">
      <p>Name: {{ customer.name }}</p>
      <p>Customer id: {{ customer.id }}</p>
      <p>Phone: {{ customer.phone }}</p>
      <p>Email: {{ customer.email }}</p>
      <p>Username: {{ customer.username }}</p>
      <p>Address line 1: {{ customer.address_line_1 }}</p>
      <p>Address line 2: {{ customer.address_line_2 }}</p>
      <p>City: {{ customer.city }}</p>
      <p>Country: {{ customer.country }}</p>

      <v-container class="d-flex" style="width: 500px;">
        <v-btn class="mx-6" @click="edit = true">Edit informations</v-btn>
        <v-btn :to="this.orderHistoryPath" v-text="'Order History'">
          <v-icon left v-text="'mdi-cart'" />
        </v-btn>
      </v-container>
      <v-container>
        <v-btn v-on:click="logout">
          Logout
        </v-btn>
      </v-container>
    </v-container>
  </v-container>
</template>

<script>
import { getTokenInfo, logout } from "../api/login";
import { requestParametersChanges } from "../api/customer";

export default {
  name: "CustomerHeader",
  props: ["customer"],
  data: function() {
    return {
      path: this.$route.params.customer_id + "/settings",
      customerId: this.$route.params.customer_id,
      orderHistoryPath: "",
      parameters: {
        name: "",
        phone: "",
        email: "",
        username: "",
        address_line_1: "",
        address_line_2: "",
        city: "",
        country: ""
      },
      edit: false,
      editName: false,
      editEmail: false,
      editUsername: false,
      editCountry: false,
      editAddress1: false,
      editAddress2: false,
      editCity: false,
      editPhone: false
    };
  },
  created: async function() {
    const response = await getTokenInfo();
    if (response) {
      this.orderHistoryPath = `/customers/${response.data["customer_id"]}/order_history`;
    }
    this.updateParameters();
  },
  methods: {
    update: async function() {
      const path = "/customers/" + this.$route.params.customer_id + "/modify";
      const modified_parameters = this.getModifiedParameters();
      await requestParametersChanges(path, modified_parameters);
      this.$router.go();
      this.edit = false;
    },
    getModifiedParameters: function() {
      let modified_parameters = {};
      for (let key in this.parameters) {
        if (this.parameters[key] !== "") {
          modified_parameters[key] = this.parameters[key];
        }
      }
      return modified_parameters;
    },
    updateParameters: function() {
      for (let key in this.parameters) {
        this.parameters[key] = this.customer[key];
      }
    },
    logout: async function() {
      await logout();
      this.$router.push({ name: "Login" });
    }
  }
};
</script>

<style scoped></style>
