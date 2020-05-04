import axios from "axios";

const API_URL = "http://localhost:5000";

export const getOrderItems = async (order_id) => {
    if (this.order.order_id === "") {
        return;
    }
    const path = `${API_URL}/${order_id}/items`;
    try {
        return axios
            .get(path)
            .then(response => {
                this.order_items = response.data;
                this.getBeers();
            })
            .catch(error => {
                console.log(error);
            });
    } catch (error) {
        console.log(error);
    }
};