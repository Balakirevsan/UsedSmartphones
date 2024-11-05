// src/App.tsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./components/sidebar";
import Main from "./pages/Main";
import Users from "./pages/Users";

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex min-h-screen w-screen">
        <Sidebar />
        <div
          id="main"
          className="flex-1 p-4 m-2 border-black border-dashed border-2 rounded-lg w-full"
        >
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/users" element={<Users />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
