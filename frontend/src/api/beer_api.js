import axios from "axios";

const API_URL = "http://localhost:5000";

export const getBeer = (id) => {
  const path = `${API_URL}/beers/${id}`;
  return axios.get(path).catch((error) => {
    console.log(error);
  });
};
