import Cookies from "js-cookie";

export const addBeerToCart = (beer_id, quantity) => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  let cookieCart = cookie["cart"];
  const cookieToken = cookie["token"];
  const cookieCustomerId = cookie["customer_id"];
  const itemToAdd = {
    beer_id: beer_id,
    quantity: quantity
  };
  cookieCart.push(itemToAdd);
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

export const checkout = () => {
  let orderToCheckout = {};
  orderToCheckout.items = getCartItems();
  orderToCheckout.order = {
    order_date: "",
    status: "",
    total_price: "",
    comment: ""
  };
  orderToCheckout.customer_id = JSON.parse(Cookies.get("beerbender-token"))[
    "customer_id"
  ];
  console.log(orderToCheckout);
};
