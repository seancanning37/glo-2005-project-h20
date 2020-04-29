import axios from "axios";

const API_CUSTOMER_URL = "http://localhost:5000/customers";

export const getCustomer = function(customerId) {
  const path = API_CUSTOMER_URL + "/" + customerId;
  axios
    .get(path)
    .then(response => {
      const data = response.data;
      return data;
    })
    .catch(error => {
      console.log(error);
    });
};
