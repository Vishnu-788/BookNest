import { Routes, Route } from "react-router-dom";
import PublicRoutes from "./routes/PublicRoutes";
import LibrarianRoutes from "./routes/LibrarianRoutes";
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route path="/*" element={<PublicRoutes />} />
        <Route path="/librarian/*" element={<LibrarianRoutes />} />
      </Routes>
    </AuthProvider>
  );
}

export default App;
