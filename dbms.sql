-- Create main database
CREATE DATABASE IF NOT EXISTS advanced_attendance_system;
USE advanced_attendance_system;

-- Users table
CREATE TABLE register (
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50),
    contact VARCHAR(15) NOT NULL,
    email VARCHAR(100) PRIMARY KEY,
    securityQ VARCHAR(200) NOT NULL,
    securityA VARCHAR(200) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Students table
CREATE TABLE student (
    Department VARCHAR(255),
    Course VARCHAR(255),
    Year VARCHAR(255),
    Semester VARCHAR(255),
    ID VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255),
    Division VARCHAR(255),a
    USN VARCHAR(255),
    Gender VARCHAR(255),
    DOB VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(255),
    Address VARCHAR(255),
    Teacher VARCHAR(255),
    PhotoSample VARCHAR(255)
);
