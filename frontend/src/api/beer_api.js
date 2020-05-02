import axios from "axios";

const API_URL = "http://localhost:5000";

export const getAllBeers = async () => {
  const path = `${API_URL}/beers`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getBeer = async id => {
  const path = `${API_URL}/beers/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getBrand = async id => {
  const path = `${API_URL}/brands/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getStyle = async id => {
  const path = `${API_URL}/styles/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getType = async id => {
  const path = `${API_URL}/types/${id}`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};

export const getBrandBeers = async brand_id => {
  const path = `${API_URL}/brands/${brand_id}/beers`;
  try {
    return axios.get(path);
  } catch (error) {
    console.log(error);
  }
};
