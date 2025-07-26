import React, { useState, useEffect } from "react";
import { apiRequest } from "../api/api";
import Message from "../components/Message";

export default function EditProfile() {
  const [form, setForm] = useState({ username: "", email: "" });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  useEffect(() => {
    apiRequest({ method: "GET" }).then(data => setForm({ username: data.username, email: data.email }));
  }, []);

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    setError(null); setSuccess(null);
    try {
      await apiRequest({ method: "PUT", data: form });
      setSuccess("Profile updated.");
    } catch (err) {
      setError(err.detail || JSON.stringify(err));
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-xl mb-4">Edit Profile</h2>
      <Message type="error">{error}</Message>
      <Message type="success">{success}</Message>
      <form onSubmit={handleSubmit} className="space-y-4">
        <input name="username" placeholder="New Username"  onChange={handleChange} className="w-full p-2 border" />
        <input name="email" placeholder="New Email"  onChange={handleChange} className="w-full p-2 border" />
        <br />
        <button className="w-full bg-blue-600 text-white p-2 rounded">Save</button>
      </form>
    </div>
  );
} 