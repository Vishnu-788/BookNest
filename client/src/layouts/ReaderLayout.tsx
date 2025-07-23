import React from "react";
import { Outlet } from "react-router-dom";
import AppNavbar from "../components/reader/NavBar";

const ReaderLayout: React.FC = () => {
  return (
    <>
      <header>
        <nav>
          <AppNavbar />
        </nav>
      </header>
      <main>
        <Outlet />
      </main>
    </>
  );
};

export default ReaderLayout;
