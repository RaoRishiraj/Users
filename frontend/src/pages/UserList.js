import React, { useEffect, useState } from "react";
import { apiRequest } from "../api/api";
import Message from "../components/Message";

export default function UserList() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    apiRequest({ method: "GET", action: "list-users" })
      .then(setUsers)
      .catch(err => setError(err.detail || JSON.stringify(err)));
  }, []);

  return (
    <div className="max-w-2xl mx-auto mt-8">
      <h2 className="text-xl mb-4">All Users</h2>
      <Message type="error">{error}</Message>
      <table className="user-table w-full rounded-lg overflow-hidden shadow">
        <thead>
          <tr className="bg-violet text-white">
            <th className="p-3 text-left">Username</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Role</th>
          </tr>
        </thead>
        <tbody>
          {users.map((u, i) => (
            <tr key={u.id} className={i % 2 === 0 ? "bg-gray-50" : "bg-white"}>
              <td className="p-3">{u.username}</td>
              <td className="p-3">{u.email}</td>
              <td className="p-3">{u.role}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
} 