import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="min-h-screen bg-gray-500">
      <nav className="bg-white shadow-lg w-full">
        <div className="container mx-auto px-4">
          <div className="flex justify-between items-center py-4">
            <div className="flex space-x-4">
              <img src={viteLogo} className="h-8 w-8" alt="Vite logo" />
              <img src={reactLogo} className="h-8 w-8" alt="React logo" />
            </div>
            <h1 className="text-xl font-bold">Vite + React + Tailwind</h1>
          </div>
        </div>
      </nav>

      <main className="container mx-auto h-[calc(100vh-4rem)] flex items-center justify-center px-4">
        <div className="w-full max-w-xl">
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="text-center">
              <button
                onClick={() => setCount((count) => count + 1)}
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              >
                Count is {count}
              </button>
              <p className="mt-4 text-gray-600">
                Edit{" "}
                <code className="bg-gray-100 px-2 py-1 rounded">
                  src/App.tsx
                </code>
                and save to test HMR
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
