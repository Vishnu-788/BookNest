import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import "./navbar.css";

const AppNavbar: React.FC = () => {
  return (
    <Navbar
      expand="lg"
      style={{
        backgroundColor: "var(--background-color)",
        padding: "0.5rem 1rem", // minimal padding
      }}
    >
      {/* Left side - Dashboard name */}
      <Navbar.Brand
        style={{
          color: "var(--primary-color)",
          fontWeight: "bold",
          fontSize: "1.4rem",
        }}
      >
        📚 Library Dashboard
      </Navbar.Brand>

      <Navbar.Toggle aria-controls="basic-navbar-nav" />

      <Navbar.Collapse id="basic-navbar-nav">
        {/* Right side - Items */}
        <Nav className="ms-auto" style={{ gap: "1rem" }}>
          <Nav.Link href="#books" style={{ color: "var(--text-color)" }}>
            Books
          </Nav.Link>
          <Nav.Link href="#members" style={{ color: "var(--text-color)" }}>
            Members
          </Nav.Link>
          <Nav.Link href="#reports" style={{ color: "var(--text-color)" }}>
            Reports
          </Nav.Link>
          <Nav.Link href="#logout" style={{ color: "var(--accent-color)" }}>
            Logout
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default AppNavbar;
