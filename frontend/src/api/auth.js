import { apiRequest } from "./api";

export async function loginUser(data) {
  const res = await apiRequest({ method: "POST", action: "login", data });
  localStorage.setItem("access", res.access);
  localStorage.setItem("refresh", res.refresh);
  return res;
}

export function logoutUser() {
  localStorage.removeItem("access");
  localStorage.removeItem("refresh");
}

export function isAuthenticated() {
  return !!localStorage.getItem("access");
} 