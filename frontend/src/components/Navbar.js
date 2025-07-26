import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { isAuthenticated, logoutUser } from "../api/auth";

export default function Navbar() {
  const navigate = useNavigate();
  const handleLogout = () => {
    logoutUser();
    navigate("/login");
  };

  return (
    <nav className="p-4 bg-gray-800 text-white flex justify-between">
      <div>
        <Link to="/">Profile</Link>
        {isAuthenticated() && (
          <>
            <Link to="/edit" className="ml-4">Edit Profile</Link>
            <Link to="/change-password" className="ml-4">Change Password</Link>
            <Link to="/users" className="ml-4">User List</Link>
          </>
        )}
      </div>
      <div>
        {isAuthenticated() ? (
          <button onClick={handleLogout}>Logout</button>
        ) : (
          <>
            <Link to="/login" className="mr-4">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
}