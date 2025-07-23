import React, { useState } from "react";
import { Form, Button, Alert } from "react-bootstrap";
import { useForm } from "react-hook-form";
import { API_ENDPOINTS } from "../../utils/api";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../hooks/useAuthContext";
import { Link } from "react-router-dom";
import "./styles/auth-form.css";

type FormData = {
  username: string;
  email: string;
  password: string;
  role: string;
};

const LibrarianSignUp: React.FC = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>();

  const [error, setError] = useState<string | null>();
  const navigate = useNavigate();
  const { login } = useAuth();

  const onSubmit = async (formData: FormData) => {
    formData.role = "librarian";
    try {
      const response = await fetch(API_ENDPOINTS.SIGN_UP, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      if (!response.ok) {
        setError(data.message);
      }

      console.log(data);
      const userData = {
        username: data.username,
        email: data.email,
        role: data.role,
      };
      const token = data.access_token;
      login(userData, token);
      navigate("/librarian");
    } catch (err) {
      console.error("Error posting", err);

      setError("Something went wrong, Try agin later");
    }
  };

  return (
    <div className="d-flex align-items-center justify-content-center vh-100">
      <div className="auth-container">
        {/* Left Panel */}
        <div className="auth-left">
          <h2 style={{ color: "var(--primary-color)", fontWeight: "bold" }}>
            Sign Up
          </h2>
          <p style={{ color: "var(--text-color)" }}>
            Create your account and join the library!
          </p>

          {error && <Alert variant="danger">error</Alert>}
          <Form onSubmit={handleSubmit(onSubmit)}>
            {/* Username */}
            <Form.Group className="mb-3">
              <Form.Label>Username</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter your username"
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

            {/* Email */}
            <Form.Group className="mb-3">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="Enter email"
                isInvalid={!!errors.email}
                {...register("email", {
                  required: "Email is required",
                })}
              />
              <Form.Control.Feedback type="invalid">
                {errors.email?.message}
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
              Sign Up
            </Button>
          </Form>

          <p className="mt-3">
            Already have an account? <Link to="/library/signin">SignIn</Link>
          </p>
        </div>

        {/* Right Panel */}
        <div className="auth-right">
          <span>✨ Welcome to the Library!</span>
        </div>
      </div>
    </div>
  );
};

export default LibrarianSignUp;
