import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home";
import NotFound from "../views/NotFound";
import BeerPage from "../views/Beer";
import BeersHomePage from "../views/BeersHomePage";
import BrandPage from "../views/Brand";
import SignUp from "../views/SignUp";
import Login from "../views/Login";
import Customer from "../views/Customer";
import CustomerSettings from "../views/CustomerSettings";
import Cart from "../views/Cart";
import CustomerOrderHistory from "../views/CustomerOrderHistory";
import CustomerDetailedOrder from "../views/CustomerDetailedOrder";
>>>>>> master

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
    component: BeerPage
  },
  {
    path: "/beers",
    name: "Beers",
    component: BeersHomePage
  },
  {
    path: "/brands/:brand_id",
    name: "BrandPage",
    component: BrandPage
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
  },
  {    
    path: "/cart",
    name: "Cart",
    component: Cart
    },
  {
    path: "/customers/:customer_id/order_history",
    name: "CustomerOrderHistory",
    component: CustomerOrderHistory,
  },
  {
    path: "/customers/:customer_id/:order_id",
    name: "CustomerDetailedOrder",
    component: CustomerDetailedOrder,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
