import { Routes, Route } from "react-router-dom";
import ReaderLayout from "../layouts/ReaderLayout";
import Home from "../pages/reader/Home";
import SignIn from "../pages/reader/SignIn";
import SignUp from "../pages/reader/SignUp";
import LibrarianSignUp from "../pages/librarian/LibrarianSignUp";
import LibrarianSignIn from "../pages/librarian/LibrarianSignIn";

const PublicRoutes = () => {
  return (
    <Routes>
      <Route element={<ReaderLayout />}>
        <Route index element={<Home />} />
        <Route path="signin" element={<SignIn />} />
        <Route path="signup" element={<SignUp />} />
        <Route path="library/signup" element={<LibrarianSignUp />} />
        <Route path="library/signin" element={<LibrarianSignIn />} />
      </Route>
    </Routes>
  );
};

export default PublicRoutes;
