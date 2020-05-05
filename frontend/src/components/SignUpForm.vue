<template class="mt-5">
  <v-container class="text-center">
    <v-card>
      <v-card-title class="justify-center">
        Sign up
      </v-card-title>
      <v-container>
        <v-text-field
          class="py-0"
          v-model="name"
          placeholder="Name"
          :rules="[rules.required]"
        ></v-text-field>

        <v-text-field
          class="py-0"
          v-model="email"
          placeholder="Email"
          :rules="[rules.required, rules.email]"
        ></v-text-field>

        <v-text-field
          class="py-0"
          v-model="username"
          placeholder="Username"
          :rules="[rules.required]"
        ></v-text-field>

        <v-row class="py-0">
          <v-col class="py-0">
            <v-text-field
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              placeholder="Password"
              @click:append="showPassword = !showPassword"
              :rules="[rules.required]"
            ></v-text-field>
          </v-col>
          <v-col class="py-0">
            <v-text-field
              :append-icon="showConfirmed ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showConfirmed ? 'text' : 'password'"
              v-model="confirmedPassword"
              placeholder="Confirm"
              @click:append="showConfirmed = !showConfirmed"
              :rules="[rules.required, rules.confirmed]"
            >
            </v-text-field>
          </v-col>
        </v-row>

        <v-container>
          <v-btn
            @click="signUpFunction"
            :disabled="!(isEmailValid() && isNameValid() && isPasswordValid())"
          >
            Sign up
          </v-btn>
        </v-container>
      </v-container>

      <v-container class="text-center">
        <p>
          Already have an account ?
          <a class="link" href="/login">Log in</a>
        </p>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import { signup } from "../api/signup";

export default {
  name: "SignUpForm",
  data: function() {
    return {
      name: "",
      email: "",
      username: "",
      password: "",
      confirmedPassword: "",
      invalidName: false,
      invalidEmail: false,
      invalidPassword: false,
      showPassword: false,
      showConfirmed: false,
      emailRegExp: /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
      rules: {
        required: value => !!value || "Required",
        email: value => this.isEmailValid(value) || "Invalid e-mail",
        confirmed: value => value == this.password || "Passwords do not match"
      }
    };
  },
  methods: {
    isNameValid: function() {
      if (this.name === "") {
        this.invalidName = true;
        return false;
      }
      this.invalidName = false;
      return true;
    },
    isPasswordValid: function() {
      if (
        this.password === "" ||
        this.confirmedPassword === "" ||
        this.password !== this.confirmedPassword
      ) {
        this.invalidPassword = true;
        return false;
      }
      this.invalidPassword = false;
      return true;
    },
    isEmailValid: function() {
      if (!this.emailRegExp.test(this.email)) {
        this.invalidEmail = true;
        return false;
      }
      this.invalidEmail = false;
      return true;
    },
    signUpFunction: async function() {
      const response = await signup(
        this.email,
        this.name,
        this.username,
        this.password
      );
      console.log(response);
      if (response === 201) {
        this.$emit("success-signup");
        this.$router.push("/login");
      } else {
        this.$router.push("/signup");
      }
    }
  }
};
</script>

<style scoped>
.main-container {
  max-width: 600px;
}
</style>
