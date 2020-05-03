<template>
  <sign-up-form v-on:success-signup="$emit('success-signup')"/>
</template>

<script>
import SignUpForm from "../components/SignUpForm";
export default {
  name: "SignUp",
  components: {
    SignUpForm
  }
};
</script>

<style scoped></style>
