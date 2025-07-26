import React, { useState } from "react";
import { loginUser } from "../api/auth";
import { useNavigate } from "react-router-dom";
import Message from "../components/Message";

export default function Login() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = async e => {
    e.preventDefault();
    setError(null);
    try {
      await loginUser(form);
      navigate("/");
    } catch (err) {
      setError(err.detail || "Login failed");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-xl mb-4">Login</h2>
      <Message type="error">{error}</Message>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="email" placeholder="Email" value={form.email} onChange={handleChange} className="w-full p-2 border" />
        <input name="password" type="password" placeholder="Password" value={form.password} onChange={handleChange} className="w-full p-2 border" />
        <br />
        <button style={{ marginTop: "10px",  marginLeft : "10px" }} className="w-full bg-blue-600 text-white p-2 rounded">Login</button>
      </form>
    </div>
  );
} 