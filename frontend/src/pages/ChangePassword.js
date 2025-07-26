import React, { useState } from "react";
import { apiRequest } from "../api/api";
import Message from "../components/Message";

export default function ChangePassword() {
  const [form, setForm] = useState({ old_password: "", new_password: "" });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    setError(null); setSuccess(null);
    try {
      await apiRequest({ method: "POST", action: "change-password", data: form });
      setSuccess("Password changed successfully.");
      setForm({ old_password: "", new_password: "" });
    } catch (err) {
      setError(err.detail || JSON.stringify(err));
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-xl mb-4">Change Password</h2>
      <Message type="error">{error}</Message>
      <Message type="success">{success}</Message>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="old_password" type="password" placeholder="Old Password" value={form.old_password} onChange={handleChange} className="w-full p-2 border" />
        <input name="new_password" type="password" placeholder="New Password" value={form.new_password} onChange={handleChange} className="w-full p-2 border" />
        <br />
        <button className="w-full bg-blue-600 text-white p-2 rounded">Change Password</button>
      </form>
    </div>
  );
} 