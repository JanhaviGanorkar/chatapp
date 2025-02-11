import { useState } from "react";
import { login } from "../api/ApiCall";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const userData = await login(email, password); // ✅ Make sure login() expects email
      localStorage.setItem("user", JSON.stringify(userData)); // Store user info
      navigate("/dashboard"); // Redirect after successful login
    } catch (error) {
      alert("Invalid credentials");
    }
  };
  
  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default Login;
