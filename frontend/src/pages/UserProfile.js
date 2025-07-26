import React, { useEffect, useState } from "react";
import { apiRequest } from "../api/api";

export default function UserProfile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    apiRequest({ method: "GET" }).then(setProfile);
  }, []);

  if (!profile) return <div>Loading...</div>;

  return (
    <div className="max-w-md mx-auto mt-8">
      <h2 className="text-xl mb-4">My Profile</h2>
      <div className="p-4 border rounded">
        <div className="mb-4"><b>Username:</b> {profile.username}</div>
        <div className="mb-4"><b>Email:</b> {profile.email}</div>
        <div><b>Role:</b> {profile.role}</div>
      </div>
    </div>
  );
} 