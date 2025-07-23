import React, { useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";
import { useForm } from "react-hook-form";
import { API_ENDPOINTS } from "../../utils/api";
import "./styles/auth-form.css";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../hooks/useAuthContext";
import { Link } from "react-router-dom";

type SignInForm = {
  username: string;
  password: string;
};

const LibrarianSignIn: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignInForm>();

  const navigate = useNavigate();
  const { login } = useAuth();
  const [error, setError] = useState<string | null>();

  const onSubmit = async (data: SignInForm) => {
    const formData = new FormData();

    formData.append("username", data.username);
    formData.append("password", data.password);

    try {
      const response = await fetch(API_ENDPOINTS.SIGN_IN, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        console.error("Error in not ok");
        setError(data.detail);
      } else {
        console.log("Response: ", data);
        const userData = {
          username: data.username,
          email: data.email,
          role: data.role,
        };
        const token = data.access_token;
        login(userData, token);
        navigate("/librarian");
      }
    } catch (err) {
      console.error("Error fetching, : ", err);
      setError("Something went wrong. Try again later");
    }
  };

  return (
    <div className="d-flex align-items-center justify-content-center vh-100">
      <div className="auth-container">
        {/* Left Panel */}
        <div className="auth-left">
          <h2 style={{ color: "var(--primary-color)", fontWeight: "bold" }}>
            Sign In
          </h2>
          <p style={{ color: "var(--text-color)" }}>
            Welcome back! Please sign in to your account.
          </p>
          {error && <Alert variant="danger">{error}</Alert>}
          <Form onSubmit={handleSubmit(onSubmit)}>
            {/* Username */}
            <Form.Group className="mb-3">
              <Form.Label>Username</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Username"
                isInvalid={!!errors.username}
                {...register("username", {
                  required: "Username is required",
                  pattern: {
                    value: /^[a-zA-Z0-9_]+$/,
                    message: "Only letters, numbers, and underscores allowed",
                  },
                })}
              />
              <Form.Control.Feedback type="invalid">
                {errors.username?.message}
              </Form.Control.Feedback>
            </Form.Group>

            {/* Password */}
            <Form.Group className="mb-3">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Password"
                isInvalid={!!errors.password}
                {...register("password", {
                  required: "Password is required",
                  minLength: {
                    value: 6,
                    message: "Password must be at least 6 characters",
                  },
                })}
              />
              <Form.Control.Feedback type="invalid">
                {errors.password?.message}
              </Form.Control.Feedback>
            </Form.Group>

            <Button
              variant="primary"
              type="submit"
              style={{
                backgroundColor: "var(--primary-color)",
                border: "none",
              }}
              className="w-100"
            >
              Sign In
            </Button>
          </Form>

          <p className="mt-3">
            Don't have an account? <Link to="/librarian/signup">Signup</Link>
          </p>
        </div>

        {/* Right Panel */}
        <div className="auth-right">
          <span>📚 Library Illustration</span>
        </div>
      </div>
    </div>
  );
};

export default LibrarianSignIn;
