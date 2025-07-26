import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ChangePassword from "./pages/ChangePassword";
import EditProfile from "./pages/EditProfile";
import UserProfile from "./pages/UserProfile";
import UserList from "./pages/UserList";

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/" element={<ProtectedRoute><UserProfile /></ProtectedRoute>} />
        <Route path="/edit" element={<ProtectedRoute><EditProfile /></ProtectedRoute>} />
        <Route path="/change-password" element={<ProtectedRoute><ChangePassword /></ProtectedRoute>} />
        <Route path="/users" element={<ProtectedRoute><UserList /></ProtectedRoute>} />
      </Routes>
    </BrowserRouter>
  );
}
