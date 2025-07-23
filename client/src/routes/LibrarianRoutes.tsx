import { Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuthContext";
import LibrarianLayout from "../layouts/LibrarianLayout";
import LibrarianHome from "../pages/librarian/LibrarianHome";

const LibrarianRoutes = () => {
  const { user } = useAuth();

  if (!user || user.role !== "librarian") {
    return <Navigate to="/library/signin" replace />;
  }

  return (
    <Routes>
      <Route element={<LibrarianLayout />}>
        <Route index element={<LibrarianHome />} />
      </Route>
    </Routes>
  );
};

export default LibrarianRoutes;
