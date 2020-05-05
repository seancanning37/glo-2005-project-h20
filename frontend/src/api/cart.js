import Cookies from "js-cookie";
import axios from "axios";
import { getBeer } from "./beer_api";

const API_URL = "http://localhost:5000";

export const addBeerToCart = async (beer_id, quantity, beer_name) => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  let cookieCart = cookie["cart"];
  const cookieToken = cookie["token"];
  const cookieCustomerId = cookie["customer_id"];
  let index = -1;
  for (let i = 0; i < cookieCart.length; i++) {
    if (cookieCart[i].beer_id === beer_id) {
      index = i;
    }
  }
  if (index !== -1) {
    cookieCart[index].quantity += quantity;
  } else {
    const itemToAdd = {
      beer_id: beer_id,
      quantity: quantity,
      name: beer_name
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
};

export const getRewards = () => {
  const customer_id = JSON.parse(Cookies.get("beerbender-token"))["customer_id"];
  const path = `${API_URL}/rewards/${customer_id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getCustomerId = () => {
  return JSON.parse(Cookies.get("beerbender-token"))["customer_id"];
}

export const getCartItems = () => {
  const cookie = JSON.parse(Cookies.get("beerbender-token"));
  const cart = cookie["cart"];
  return cart;
};

const getOrderToCheckout = async (comment) => {
  let orderToCheckout = {};
  orderToCheckout.items = getCartItems();
  const date = new Date();
  orderToCheckout.order = {
    order_date:
      date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate(),
    status: "pending",
    total_price: await calculateTotal(orderToCheckout.items),
    comment: comment.toString()
  };
  orderToCheckout.customer_id = JSON.parse(Cookies.get("beerbender-token"))[
    "customer_id"
  ];
  return orderToCheckout;
};

export const checkout = async (comment) => {
  const orderToCheckout = await getOrderToCheckout(comment);
  if (orderToCheckout.items.length === 0) {
    return 400;
  }
  const response = await axios
    .post("http://localhost:5000/orders/buy", orderToCheckout)
    .catch(error => {
      console.log(error);
      return 500;
    });
  return setCheckoutCookie(response);
};

export const setCheckoutCookie = response => {
  console.log(response);
  const code = response.status;
  const customer_id = JSON.parse(Cookies.get("beerbender-token"))[
    "customer_id"
  ];
  const sessionToken = JSON.parse(Cookies.get("beerbender-token"))[
      "token"
      ];
  let token = {
    token: sessionToken,
    customer_id: customer_id,
    cart: []
  };
  let date = new Date();
  const minutes = 180;
  date.setTime(date.getTime() + minutes * 60 * 1000);
  Cookies.set("beerbender-token", JSON.stringify(token), { expires: date });
  return code;
};

export const calculateTotal = async cartItems => {
  let total = 0.0;
  for (let i = 0; i < cartItems.length; i++) {
    const beer = (await getBeer(cartItems[i].beer_id)).data;
    total += beer.price * cartItems[i].quantity;
  }
  return total;
};

export const removeItem = async itemId => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  const cart = getCartItems();
  let index = -1;
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].beer_id === itemId) {
      index = i;
      break;
    }
  }
  cart.splice(index, 1);
  cookie.cart = cart;
  let date = new Date();
  const minutes = 180;
  date.setTime(date.getTime() + minutes * 60 * 1000);
  Cookies.set("beerbender-token", cookie, { expires: date });
};

export const changeQuantity = async (itemId, quantity) => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  const cart = getCartItems();
  let index = -1;
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].beer_id === itemId) {
      index = i;
      break;
    }
  }
  cart[index].quantity = quantity;
  cookie.cart = cart;
  let date = new Date();
  const minutes = 180;
  date.setTime(date.getTime() + minutes * 60 * 1000);
  Cookies.set("beerbender-token", cookie, { expires: date });
};
