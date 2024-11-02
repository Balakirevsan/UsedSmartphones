import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0", // Позволяет внешний доступ
    port: 3000, // Порт по вашему выбору
  },
});
