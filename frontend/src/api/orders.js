import axios from "axios";

const API_URL = "http://localhost:5000";

export const getOrderItems = async order_id => {
  const path = `${API_URL}/orders/${order_id}/items`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getOrder = async order_id => {
  const path = `${API_URL}/orders/${order_id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getDetailedOrders = async customer_id => {
  const path = `${API_URL}/orders/customer/${customer_id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};
