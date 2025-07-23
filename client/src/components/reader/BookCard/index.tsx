import React from "react";
import { Card } from "react-bootstrap";

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

type BookCardProps = {
  book: Book;
  handleBookClick: (book: Book) => void;
};

const BookCard: React.FC<BookCardProps> = ({ book, handleBookClick }) => {
  const URL: string = "http://127.0.0.1:8000";

  return (
    <Card
      key={book.id}
      style={{ width: "140px", cursor: "pointer" }}
      onClick={() => handleBookClick(book)}
    >
      <Card.Img variant="top" src={`${URL}${book.img_url}`} />
      <Card.Body>
        <Card.Title style={{ fontSize: "14px" }}>{book.title}</Card.Title>
        <Card.Text style={{ fontSize: "12px" }}>{book.author}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default BookCard;
