import axios from "axios";
const API_URL = "http://localhost:5000";

export const requestParametersChanges = async (path, modified_parameters) => {
    return axios
        .put(API_URL+path, modified_parameters)
        .catch(error => {
            console.log(error.response.data);
        });
};