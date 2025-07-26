export default function Message({ type, children }) {
  if (!children) return null;
  return (
    <div className={`p-2 my-2 rounded ${type === "error" ? "bg-red-200 text-red-800" : "bg-green-200 text-green-800"}`}>
      {children}
    </div>
  );
} 