// src/components/Sidebar.tsx
import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Sidebar: React.FC = () => {
  const navigate = useNavigate();

  const handleUsersClick = (e: React.MouseEvent) => {
    e.preventDefault();
    // Force navigation with state update
    navigate("/users", {
      state: { refresh: Date.now() },
      replace: true,
    });
  };

  return (
    <div className="w-[280px] border-black border-dashed border-2 rounded-lg my-2 ml-2">
      <div className="flex items-center justify-between p-4">
        <h1 className="text-2xl font-bold">Logo</h1>
      </div>
      <hr className="border-t-2 border-dashed border-black" />
      <div className="p-4">
        <ul>
          <li className="pb-2">
            <Link to="/">Dashboard</Link>
          </li>
          <li className="py-2">
            <Link onClick={handleUsersClick} to="/users">
              Users
            </Link>
          </li>
          <li className="py-2">Item 3</li>
          <li className="py-2">Item 4</li>
        </ul>
      </div>
    </div>
  );
};

export default Sidebar;
