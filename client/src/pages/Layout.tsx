import React from "react";
import { Outlet } from "react-router-dom";

const Layout: React.FC = () => {
  return (
    <>
      <h1>Header</h1>
      <main>
        <Outlet />
      </main>
      <h1>Footer</h1>
    </>
  );
};

export default Layout;
