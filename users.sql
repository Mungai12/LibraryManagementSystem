CREATE TABLE users(
  id bigserial,
  first_name varchar(50),
  last_name varchar(50),
  year_of_registration int,
  registration_number varchar(20),
  password varchar(50),
);
-- Just a few users to work with
INSERT INTO users(first_name, last_name, year_of_registration, registration_number, password)
VALUES ('Levi', 'Mungai', 2023, 'll|1562|2023', 'lad'),
       ('Adam', 'Eve', 2024, 'll|6723|2024', 'eve');


CREATE TABLE books(
    id bigserial,
    title varchar(50),
    author varchar(50),
    genre varchar(50),
    isbn bigint,
    year_of_publication integer,
    borrow_status varchar(50),
    return_date date
);
-- I add just a few books to work with
INSERT INTO books(title, author, genre, isbn, year_of_publication ,borrow_status, return_date)
VALUES ('EMERGING VIRUSES', 'Stephen S. Morse', 'Biology', 7018783554342, 1993, 'Available', null),
        ('PROPHETS AND KINGS', 'E.G White', 'Religion', 2067817747313, 1896, 'Available', null),
        ('PRINCIPLES OF ECONOMICS', 'N. Gregory Mankiw', 'Economics', 3532992839882, 2001, 'Available', null),
        ('THE FAMILY ROMANOV', 'Fleming Candace', 'History', 1306252531828, 2007, 'Available', null);