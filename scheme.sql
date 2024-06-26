-- Create the database
CREATE DATABASE IF NOT EXISTS libraryDB;

-- Switch to the new database
USE libraryDB;

-- Create the books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100)
);

-- Create the borrowers table
CREATE TABLE IF NOT EXISTS borrowers (
    borrower_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(100)
);

-- Create the transactions table
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    borrower_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id)
);

-- Trigger to ensure book_id and borrower_id exist
DELIMITER //
CREATE TRIGGER before_transaction_insert
BEFORE INSERT ON transactions
FOR EACH ROW
BEGIN
    DECLARE book_count INT;
    DECLARE borrower_count INT;
    SELECT COUNT(*) INTO book_count FROM books WHERE book_id = NEW.book_id;
    SELECT COUNT(*) INTO borrower_count FROM borrowers WHERE borrower_id = NEW.borrower_id;
    IF book_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Book ID does not exist';
    END IF;
    IF borrower_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Borrower ID does not exist';
    END IF;
END;
//
DELIMITER ;

-- Trigger to update return_date when a transaction is updated
DELIMITER //
CREATE TRIGGER after_transaction_update
AFTER UPDATE ON transactions
FOR EACH ROW
BEGIN
    IF NEW.return_date IS NOT NULL THEN
        UPDATE transactions SET return_date = NEW.return_date WHERE transaction_id = NEW.transaction_id;
    END IF;
END;
//
DELIMITER ;
