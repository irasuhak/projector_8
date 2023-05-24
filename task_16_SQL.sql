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



