import axios from "axios";

axios.defaults.withCredentials = true; // Allow cookies for session-based auth

const API_URL = "http://127.0.0.1:8000/api";

export const login = async (username, password) => {
  try {
    const response = await axios.post(
      `${API_URL}/login/`,  // Ensure this matches your Django login endpoint
      { username, password },
      {
        headers: {
          "Content-Type": "application/json",
          "Cache-Control": "no-cache",  // Prevents browser caching
          "Pragma": "no-cache",
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error("Login failed", error);
    throw error;
  }
};


export const register = async (email, password) => {
  try {
    const response = await axios.post(
      `http://127.0.0.1:8000/api/register/?nocache=${new Date().getTime()}`,  // ✅ Prevent caching
      { email, password },
      { 
        headers: { 
          "Content-Type": "application/json",
          "Cache-Control": "no-cache", // ✅ Disable caching
          "Pragma": "no-cache",
        } 
      }
    );
    return response.data;
  } catch (error) {
    console.error("Registration failed", error);
    throw error;
  }
};


export const getUserData = async () => {
  const token = localStorage.getItem("access_token");
  if (!token) return null;

  try {
    const response = await axios.get(`${API_URL}/user/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error("Failed to fetch user data", error);
    return null;
  }
};

export const logout = () => {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
};
