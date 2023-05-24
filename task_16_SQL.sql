-- Practice

-- 1. Write SQL queries for table creation for data model that you crated for prev homework (AirBnb model)

CREATE TABLE  hosts (
    id serial PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(13) NOT NULL
    address VARCHAR(200) NOT NULL
);


CREATE TABLE  quests (
    id serial PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(13) NOT NULL
    address VARCHAR(200) NOT NULL
);


CREATE TABLE rooms (
    id serial PRIMARY KEY,
    host_id INTL,
    name VARCHAR(50) NOT NULL,
    residents_capacity INT NOT NULL,
    price DECIMAL NOT NULL,
    air_conditioning BOOLEAN,
    refrigerator BOOLEAN,
  
    FOREIGN KEY (host_id) 
        REFERENCES hosts(id)
);


CREATE TABLE reservations (
    id serial PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in_date TIMESTAMP NOT NULL,
    check_out_date TIMESTAMP NOT NULL,
    total_price DECIMAL NOT NULL,
    
    FOREIGN KEY (guest_id) 
        REFERENCES guests(id),
    FOREIGN KEY (room_id) 
        REFERENCES rooms(id)
);


CREATE TABLE reviews (
    id serial PRIMARY KEY,
    guest_id INT,
    host_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    comment VARCHAR,
    
    FOREIGN KEY (guest_id) 
        REFERENCES guests(id),
    FOREIGN KEY (host_id) 
        REFERENCES hosts(id)
);


CREATE TABLE payments (
  id serial PRIMARY KEY,
  guest_id INT,
  reservation_id INT,
  payment_date TIMESTAM NOT NULL,
  amount DECIMA LNOT NULL,
  
  FOREIGN KEY (guest_id) 
      REFERENCES guests(id),
  FOREIGN KEY (reservation_id)
      REFERENCES reservations(id)
);



-- 2. Write 3 rows (using INSERT queries) for each table in the data model

INSERT INTO hosts (first_name, last_name, phone_number, address) VALUES
('John', 'Doe', '1234567890', '123 Main St'),
('Jane', 'Smith', '9876543210', '456 Elm St'),
('David', 'Johnson', '5555555555', '789 Oak St');

INSERT INTO guests (first_name, last_name, phone_number, address) VALUES
('Alice', 'Brown', '1111111111', '321 Maple Ave'),
('Bob', 'Davis', '9998887777', '654 Pine St'),
('Eva', 'Wilson', '4444444444', '987 Cedar Ln');

INSERT INTO rooms (host_id, name, residents_capacity, price, air_conditioning, refrigerator) VALUES
(1, 'Cozy Room', 2, 50.00, true, true),
(1, 'Spacious Suite', 4, 100.00, true, false),
(2, 'Modern Loft', 2, 75.00, true, true);

INSERT INTO reservations (guest_id, room_id, check_in_date, check_out_date, total_price) VALUES
(2, 1, '2023-05-26', '2023-05-29', 150.00),
(3, 3, '2023-06-01', '2023-06-05', 300.00),
(1, 2, '2023-06-10', '2023-06-15', 500.00);

INSERT INTO reviews (guest_id, host_id, rating, comment) VALUES
(2, 1, 4, 'Great host and comfortable stay!'),
(3, 2, 5, 'Amazing experience, highly recommended!'),
(1, 3, 3, 'Decent room, could use some improvements.');

INSERT INTO payments (guest_id, reservation_id, payment_date, amount) VALUES
(2, 1, '2023-05-25', 150.00),
(3, 2, '2023-05-30', 300.00),
(1, 3, '2023-06-05', 500.00);


--3. Create next analytic queries:
--    1. Find a user who had biggest amount of reservation. Return user name and user_id

SELECT g.id as user_id, g.first_name AS first_name, g.last_name AS last_name
FROM guests as g
JOIN reservation as r on g.id = r.guest_id
GROUP BY g.id
ORDER BY COUNT(r.id) DESC
LIMIT 1;




