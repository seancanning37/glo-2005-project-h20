import axios from "axios";

const API_URL = "http://localhost:5000";

export const getAllBrands = async () => {
  const path = `${API_URL}/brands`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};
