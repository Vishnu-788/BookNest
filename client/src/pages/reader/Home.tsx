import { useState, useEffect } from "react";
import { Container, Row, Col, Button, Offcanvas } from "react-bootstrap";
import BookCard from "../../components/reader/BookCard";
import { API_ENDPOINTS } from "../../utils/api";

type Book = {
  id: number;
  lib_id: number;
  title: string;
  author: string;
  description: string;
  in_stock: boolean;
  stock_count: number;
  img_url: string;
};

const Home = () => {
  const [selectedBook, setSelectedBook] = useState<Book | null>(null);
  const [showDetail, setShowDetail] = useState(false);
  const [isMobile, setIsMobile] = useState(false);
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    const fetchBook = async () => {
      const response = await fetch(API_ENDPOINTS.BOOKS, {
        method: "GET",
      });

      const result = await response.json();
      console.log("Books: ", result);
      setBooks(result);
    };
    fetchBook();
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768); // Bootstrap md breakpoint
    };

    handleResize(); // Run on mount
    window.addEventListener("resize", handleResize);

    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const handleBookClick = (book: Book) => {
    setSelectedBook(book);
    if (isMobile) {
      setShowDetail(true);
    }
  };

  const handleClose = () => {
    setShowDetail(false);
    if (!isMobile) {
      setSelectedBook(null);
    }
  };

  return (
    <Container fluid style={{ height: "100vh", overflow: "hidden" }}>
      <Row className="h-100">
        {/* Left Panel */}
        <Col
          xs={12}
          md={selectedBook && !isMobile ? 8 : 12}
          className="d-flex align-items-center overflow-auto"
          style={{
            whiteSpace: "nowrap",
            backgroundColor: "#f8f9fa",
            padding: "20px",
          }}
        >
          <div className="d-flex gap-3">
            {books.map((book) => (
              <BookCard
                key={book.id}
                book={book}
                handleBookClick={handleBookClick}
              />
            ))}
          </div>
        </Col>

        {/* Right Panel - Desktop only */}
        {!isMobile && selectedBook && (
          <Col
            md={4}
            className="d-flex flex-column p-4"
            style={{ backgroundColor: "#fff", borderLeft: "1px solid #ccc" }}
          >
            <Button
              variant="secondary"
              onClick={handleClose}
              className="align-self-end mb-3"
            >
              Close
            </Button>
            <h3>{selectedBook.title}</h3>
            <p>
              <strong>Author:</strong> {selectedBook.author}
            </p>
            <p>{selectedBook.description}</p>
          </Col>
        )}
      </Row>

      {/* Offcanvas for Mobile Only */}
      {isMobile && (
        <Offcanvas show={showDetail} onHide={handleClose} placement="end">
          <Offcanvas.Header closeButton>
            <Offcanvas.Title>{selectedBook?.title}</Offcanvas.Title>
          </Offcanvas.Header>
          <Offcanvas.Body>
            {selectedBook && (
              <>
                <p>
                  <strong>Author:</strong> {selectedBook.author}
                </p>
                <p>{selectedBook.description}</p>
              </>
            )}
          </Offcanvas.Body>
        </Offcanvas>
      )}
    </Container>
  );
};

export default Home;
