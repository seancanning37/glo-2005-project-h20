import axios from "axios";

const path = "http://localhost:5000/signup";

export const signup = async (email, name, username, password) => {
  const response = await axios
    .post(path, {
      email: email,
      name: name,
      username: username,
      password: password
    })
    .catch(error => {
      console.log(error.response.data);
    });
  return response.status
};
