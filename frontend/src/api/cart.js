import Cookies from "js-cookie";
import axios from "axios";
import Router from "../router";

export const addBeerToCart = (beer_id, quantity) => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  let cookieCart = cookie["cart"];
  const cookieToken = cookie["token"];
  const cookieCustomerId = cookie["customer_id"];
  // eslint-disable-next-line no-unused-vars
  let index = -1;
  for (let i = 0; i < cookieCart.length; i++) {
    if (cookieCart[i].beer_id === beer_id) {
      index = i;
    }
  }
  if (index !== -1) {
    cookieCart[index].quantity = quantity;
  } else {
    const itemToAdd = {
      beer_id: beer_id,
      quantity: quantity
    };
    cookieCart.push(itemToAdd);
  }
  const cartCookie = {
    token: cookieToken,
    customer_id: cookieCustomerId,
    cart: cookieCart
  };
  let date = new Date();
  const minutes = 180;
  date.setTime(date.getTime() + minutes * 60 * 1000);
  Cookies.set("beerbender-token", cartCookie, { expires: date });
  console.log(cartCookie);
};

export const getCartItems = () => {
  const cookie = JSON.parse(Cookies.get("beerbender-token"));
  const cart = cookie["cart"];
  return cart;
};

const getOrderToCheckout = () => {
  let orderToCheckout = {};
  orderToCheckout.items = getCartItems();
  const date = new Date();
  orderToCheckout.order = {
    order_date:
      date.getFullYear() + "-" + date.getMonth() + "-" + date.getDay(),
    status: "",
    total_price: 3,
    comment: ""
  };
  orderToCheckout.customer_id = JSON.parse(Cookies.get("beerbender-token"))[
    "customer_id"
  ];
  return orderToCheckout;
};

export const checkout = () => {
  const orderToCheckout = getOrderToCheckout();
  axios
    .post("http://localhost:5000/orders/buy", orderToCheckout)
    .then(function() {
      const customer_id = JSON.parse(Cookies.get("beerbender-token"))[
        "customer_id"
      ];
      let token = {
        token: token,
        customer_id: customer_id,
        cart: []
      };
      let date = new Date();
      const minutes = 180;
      date.setTime(date.getTime() + minutes * 60 * 1000);
      Cookies.set("beerbender-token", JSON.stringify(token), { expires: date });
      Router.push("/");
    });
};
