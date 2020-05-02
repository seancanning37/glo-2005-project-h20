import Cookies from "js-cookie";

export const addBeerToCart = (beer_id, quantity) => {
  let cookie = JSON.parse(Cookies.get("beerbender-token"));
  let cookieCart = cookie["cart"];
  const cookieToken = cookie["token"];
  const cookieCustomerId = cookie["customer_id"];
  cookieCart[beer_id] = quantity;
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

export const getCartItems = () => {
  const cookie = JSON.parse(Cookies.get("beerbender-token"));
  return cookie["cart"];
};
