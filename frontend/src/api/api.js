const BASE_URL = "http://localhost:8000/api/users/user/";
function getToken() {
  return localStorage.getItem("access");
}

export async function apiRequest({ method = "GET", action, data }) {
  let url = BASE_URL;
  if (action) url += `?action=${action}`;

  const headers = {
    "Content-Type": "application/json",
  };
  const token = getToken();
  if (token) headers["Authorization"] = `Bearer ${token}`;

  const options = {
    method,
    headers,
  };
  if (data) options.body = JSON.stringify(data);

  const res = await fetch(url, options);
  const json = await res.json();
  if (!res.ok) throw json;
  return json;
} 