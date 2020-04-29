import Cookies from "js-cookie";
import axios from "axios";
import Router from "../router";

const API_URL = "http://localhost:5000/login";

export const login = function(email, password) {
  axios
    .post(API_URL, {
      email: email,
      password: password
    })
    .then(response => {
      let date = new Date();
      const minutes = 180;
      date.setTime(date.getTime() + minutes * 60 * 1000);
      Cookies.set("beerbender-token", response.data.token, { expires: date });
      Router.push("/");
    })
    .catch(error => {
      console.log(error.response.data);
    });
};

export const getToken = function() {
  return Cookies.get("beerbender-token");
};
