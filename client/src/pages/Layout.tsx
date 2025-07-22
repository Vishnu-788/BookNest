import React from "react";
import { Outlet } from "react-router-dom";
import AppNavbar from "../components/header/AppNavBar";

const Layout: React.FC = () => {
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
      <h1>Footer</h1>
    </>
  );
};

export default Layout;
