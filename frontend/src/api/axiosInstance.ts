// src/api/axiosInstance.ts
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/",
  timeout: 5000,
});

// Add a response interceptor
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    console.log("Interceptor Error:", error);
    if (error.code === "ECONNABORTED") {
      error.customMessage = "Request timed out. Please try again later.";
    } else if (!error.response) {
      error.customMessage = "Cannot connect to the server.";
    } else if (
      error.response.status === 500 &&
      error.response.data.message === "DB_CONNECTION_ERROR"
    ) {
      error.customMessage = "Database connection failed.";
    } else {
      error.customMessage = "Failed to fetch users.";
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
