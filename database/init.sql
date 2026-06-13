CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specialist VARCHAR(100)
);

INSERT INTO doctors(name,specialist)
VALUES
('dr. Budi','Umum'),
('dr. Ani','Anak'),
('dr. Citra','Penyakit Dalam');

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_id INTEGER,
    queue_number INTEGER,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);