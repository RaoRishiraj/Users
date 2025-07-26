import React, { useState } from "react";
import { apiRequest } from "../api/api";
import Message from "../components/Message";

export default function Register() {
  const [form, setForm] = useState({ username: "", password: "", email: "", role: "staff" });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    setError(null); setSuccess(null);
    try {
      await apiRequest({ method: "POST", action: "register", data: form });
      setSuccess("Registration successful! You can now log in.");
    } catch (err) {
      setError(err.detail || JSON.stringify(err));
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-xl mb-4">Register</h2>
      <Message type="error">{error}</Message>
      <Message type="success">{success}</Message>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="username" placeholder="Username" value={form.username} onChange={handleChange} className="w-full p-2 border" />
        <input name="email" placeholder="Email" value={form.email} onChange={handleChange} className="w-full p-2 border" />
        <input
          name="password"
          type="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          className="w-full p-2 border"
        />
        <div className="role-field">
          <label htmlFor="role" className="role-label">
            Role
          </label>
          <select
            id="role"
            name="role"
            value={form.role}
            onChange={handleChange}
            className="role-select"
          >
            <option value="staff">Staff</option>
            <option value="administrator">Administrator</option>
          </select>
        </div>
        <button className="w-full bg-blue-600 text-white p-2 rounded">Register</button>
      </form>
    </div>
  );
}