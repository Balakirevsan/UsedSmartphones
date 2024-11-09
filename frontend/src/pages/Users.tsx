import React, { useEffect, useState } from "react";
import axiosInstance from "../api/axiosInstance";
import { User } from "../types/user";
import { useLocation } from "react-router-dom";

const Users: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const location = useLocation();

  const fetchUsers = async () => {
    const loadingTimer = setTimeout(() => {
      setLoading(true);
    }, 100);

    try {
      const response = await axiosInstance.get("/users");
      setUsers(response.data);
    } catch (err: any) {
      setError(err.customMessage || "An unexpected error occurred.");
      console.error(err);
    } finally {
      clearTimeout(loadingTimer);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, [location.state?.refresh]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-500">{error}</div>;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Users</h1>
      <table className="min-w-full border border-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left">Username</th>
            <th className="px-6 py-3 text-left">Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id} className="border-b">
              <td className="px-6 py-4">{user.username}</td>
              <td className="px-6 py-4">{user.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Users;
