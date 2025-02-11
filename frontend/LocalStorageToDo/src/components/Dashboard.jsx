import { useEffect, useState } from "react";
import { getUserData, logout } from "../api/ApiCall";
import { useNavigate } from "react-router-dom";
import Button from '@mui/material/Button';
const Dashboard = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      const data = await getUserData();
      if (data) setUser(data);
      else navigate("/login");
    };
    fetchUser();
  }, [navigate]);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div>
      <h2>Dashboard</h2>
      {user ? <p>Welcome, {user.email}!</p> : <p>Loading...</p>}
      <Button onClick={handleLogout}>Logout</Button>
      <Button variant="contained">Hello world</Button>
    </div>
  );
};
export default Dashboard;

