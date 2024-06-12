-- Create the database
CREATE DATABASE IF NOT EXISTS company_db;

-- Switch to the new database
USE company_db;

-- Create the manager table
CREATE TABLE IF NOT EXISTS manager (
    manager_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    mail VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    project_id INT
);

-- Create the project table
CREATE TABLE IF NOT EXISTS project (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget DECIMAL(15, 2) NOT NULL,
    manager_id INT,
    n_of_employee INT
);

-- Create the employee table
CREATE TABLE IF NOT EXISTS employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    mail VARCHAR(100) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    project_id INT,
    manager_id INT
);


