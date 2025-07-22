import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
import "./navbar.css";
import { useAuth } from "../../hooks/useAuthContext";

const AppNavbar: React.FC = () => {
  const { user, logout } = useAuth();
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    logout();
  };

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
        as={Link}
        to={"/"}
        style={{
          color: "var(--primary-color)",
          fontWeight: "bold",
          fontSize: "1.4rem",
        }}
      >
        Dashboard
      </Navbar.Brand>

      <Navbar.Toggle aria-controls="basic-navbar-nav" />

      <Navbar.Collapse id="basic-navbar-nav">
        {/* Right side - Items */}
        <Nav className="ms-auto" style={{ gap: "1rem" }}>
          {user ? (
            <>
              <Nav.Link style={{ color: "var(--text-color)" }}>Books</Nav.Link>
              <Nav.Link style={{ color: "var(--text-color)" }}>
                Members
              </Nav.Link>
              <Nav.Link style={{ color: "var(--text-color)" }}>
                Reports
              </Nav.Link>
              <Nav.Link
                href="#logout"
                style={{ color: "var(--accent-color)" }}
                onClick={handleClick}
              >
                Logout
              </Nav.Link>
            </>
          ) : (
            <>
              <Nav.Link style={{ color: "var(--text-color)" }}>Books</Nav.Link>
              <Nav.Link
                as={Link}
                to={"/signin"}
                style={{ color: "var(--text-color)" }}
              >
                SignIn
              </Nav.Link>
              <Nav.Link
                as={Link}
                to={"/signup"}
                style={{ color: "var(--text-color)" }}
              >
                SignUp
              </Nav.Link>
            </>
          )}
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default AppNavbar;
