import React, { useState } from "react";
import { Modal, Button, Form, Row, Col, Alert } from "react-bootstrap";
import "./style.css";
import { API_ENDPOINTS } from "../../../utils/api";
import { useAuth } from "../../../hooks/useAuthContext";

interface BookFormData {
  image: File | null;
  title: string;
  author: string;
  description?: string;
  stock_count: number;
  in_stock: boolean;
}

const BookCreateForm = () => {
  const initialFormData: BookFormData = {
    image: null,
    title: "",
    author: "",
    description: "",
    stock_count: 0,
    in_stock: true,
  };
  const [show, setShow] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [formData, setFormData] = useState<BookFormData>(initialFormData);

  const { token } = useAuth();

  const handleShow = () => setShow(true);
  const handleClose = () => setShow(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value, type, checked } = e.target as HTMLInputElement;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files ? e.target.files[0] : null;
    setFormData((prev) => ({ ...prev, image: file }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const form = new FormData();
    form.append("title", formData.title);
    form.append("author", formData.author);
    form.append("in_stock", String(formData.in_stock));
    form.append("stock_count", String(formData.stock_count));
    if (formData.description) {
      form.append("description", formData.description);
    }
    if (formData.image) {
      form.append("image", formData.image);
    }

    try {
      const response = await fetch(API_ENDPOINTS.BOOK_CREATE, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: form,
      });
      const result = await response.json();

      if (!response.ok) {
        setError(result.detail);
      } else {
        setFormData(initialFormData);
        handleClose();
      }
    } catch (err) {
      setError("Something wen wrong. Try again later");
      console.log("Error occured", err);
    }
  };

  return (
    <>
      {/* Trigger Button */}
      <Button variant="primary" className="open-modal-btn" onClick={handleShow}>
        + Add Book
      </Button>

      {/* Modal */}
      <Modal show={show} onHide={handleClose} centered>
        <Modal.Header
          closeButton
          style={{ background: "var(--primary-color)", color: "#fff" }}
        >
          <Modal.Title>Add a New Book</Modal.Title>
        </Modal.Header>

        {error && <Alert variant="danger">{error}</Alert>}
        <Modal.Body>
          <Form onSubmit={handleSubmit} className="custom-form">
            {/* Image Upload */}
            <Form.Group controlId="bookImage" className="mb-3">
              <Form.Label>Book Image</Form.Label>
              <Form.Control
                type="file"
                accept="image/*"
                onChange={handleFileChange}
              />
            </Form.Group>

            {/* Title & Author */}
            <Row>
              <Col md={6}>
                <Form.Group controlId="title" className="mb-3">
                  <Form.Label>Title</Form.Label>
                  <Form.Control
                    type="text"
                    name="title"
                    placeholder="Enter book title"
                    value={formData.title}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="author" className="mb-3">
                  <Form.Label>Author</Form.Label>
                  <Form.Control
                    type="text"
                    name="author"
                    placeholder="Enter author name"
                    value={formData.author}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
            </Row>

            {/* Description */}
            <Form.Group controlId="description" className="mb-3">
              <Form.Label>Description</Form.Label>
              <Form.Control
                as="textarea"
                rows={2}
                name="description"
                placeholder="Enter a brief description"
                value={formData.description}
                onChange={handleChange}
                required
              />
            </Form.Group>

            {/* Stock & Availability */}
            <Row>
              <Col md={6}>
                <Form.Group controlId="stock_count" className="mb-3">
                  <Form.Label>Stock Count</Form.Label>
                  <Form.Control
                    type="number"
                    name="stock_count"
                    min="0"
                    value={formData.stock_count}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
              <Col md={6} className="d-flex align-items-center">
                <Form.Check
                  type="switch"
                  id="in_stock"
                  label="In Stock"
                  name="in_stock"
                  checked={formData.in_stock}
                  onChange={handleChange}
                  className="mt-4"
                />
              </Col>
            </Row>

            {/* Submit */}
            <div className="text-center">
              <Button type="submit" className="submit-btn">
                Add Book
              </Button>
            </div>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default BookCreateForm;
