import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home";
import NotFound from "../views/NotFound";
import Beer from "../views/Beer";
import SignUp from "../views/SignUp";
import Login from "../views/Login";
import Customer from "../views/Customer";
import CustomerSettings from "../views/CustomerSettings";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "*",
    name: "NotFound",
    component: NotFound
  },
  {
    path: "/beers/:beer_id",
    name: "BeerPage",
    component: Beer
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignUp
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/customers/:customer_id",
    name: "CustomerPage",
    component: Customer
  },
  {
    path: "/customers/:customer_id/settings",
    name: "CustomerSettings",
    component: CustomerSettings
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
