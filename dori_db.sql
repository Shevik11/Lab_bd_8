CREATE DATABASE abdc_6;
USE abdc_6;

-- Створення таблиці exxxpert
CREATE TABLE exxxpert (
    id INT AUTO_INCREMENT PRIMARY KEY,
    personal_number INT,
    S_M_P VARCHAR(255) NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    addres VARCHAR(255) NOT NULL,
    phone_number INT,
    office_number INT
);

-- Створення таблиці MedicalRecords
CREATE TABLE MedicalRecords (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15)
);

-- Створення таблиці RegistrationJournal
CREATE TABLE RegistrationJournal (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    specialist_id INT,
    visit_number INT NOT NULL,
    visit_date DATE NOT NULL,
    complaints TEXT,
    diagnosis VARCHAR(255),
    treatment TEXT,
    service_cost DECIMAL(10, 2),
    CONSTRAINT fk_patient_id FOREIGN KEY (patient_id) REFERENCES MedicalRecords(record_id),
    CONSTRAINT fk_specialist_id FOREIGN KEY (specialist_id) REFERENCES exxxpert(id)
);

-- Створення таблиці ReferralJournal
CREATE TABLE ReferralJournal (
    referral_id INT AUTO_INCREMENT PRIMARY KEY,
    procedure_analysis_name VARCHAR(255),
    patient_id INT,
    referring_specialist_id INT,
    performing_specialist_id INT,
    procedure_date DATE NOT NULL,
    results TEXT,
    CONSTRAINT fk_patient_id_referral FOREIGN KEY (patient_id) REFERENCES MedicalRecords(record_id),
    CONSTRAINT fk_referring_specialist_id_referral FOREIGN KEY (referring_specialist_id) REFERENCES exxxpert(id),
    CONSTRAINT fk_performing_specialist_id_referral FOREIGN KEY (performing_specialist_id) REFERENCES exxxpert(id)
);


INSERT INTO exxxpert (personal_number, S_M_P, specialization, addres, phone_number, office_number)
VALUES
    (0685491236, "Krasko Olena Borusivna", "Doctor", "Soborna", "0549631084", 44),
    (0673219824, "Bila Irina Ivanivna", "Nurse", "Konovalsa", "0436971205", 2),
    (0681234568, "Kudrava Margarita Petrovna", "Doctor", "Shewchenka", "0574102973", 15),
    (0677894563, "Muronuk Antonona Volodumurivna", "Surgeon", "Kotlarewscogo", "0435715908", 13),
    (0688461397, "Berezuk Vita Igorivna", "Oculist", "Pasichna", "0319728640", 77),
    (0661112233, 'Ivanova Inna Ihorivna', 'General Practitioner', 'Shevchenka St., 10', '0501234567', 101),
    (0672223344, 'Petrenko Petro Petrovich', 'Dermatologist', 'Gagarina St., 15', '0669876543', 202),
    (0683334455, 'Koval Mykhailo Oleksandrovich', 'Ophthalmologist', 'Poltavska St., 20', '0971112233', 303),
    (0664445566, 'Sydorova Svitlana Mykolaivna', 'Therapist', 'Sadova St., 7', '0665555777', 404),
    (0675556677, 'Zaharova Olena Viktorivna', 'Gynecologist', 'Chervonoarmiiska St., 30', '0988888999', 505);

INSERT INTO MedicalRecords (full_name, gender, birth_date, address, phone_number)
VALUES
    ('Ivanov Ivan Ivanovich', 'Male', '1980-05-15', 'Pushkinska St., 123', '+380991234567'),
    ('Petrova Maria Petrovna', 'Female', '1990-07-20', 'Shevchenka St., 45', '+380997654321'),
    ('Sydorenko Oleksandr Viktorovich', 'Male', '1975-03-10', 'Gagarina St., 67', '+380998765432'),
    ('Kovalchuk Iryna Sergiivna', 'Female', '1988-12-05', 'Poltavska St., 78', '+380991112233'),
    ('Melnik Pavlo Petrovich', 'Male', '1995-08-30', 'Lisova St., 56', '+380994455566'),
    ('Popova Olga Volodymyrivna', 'Female', '1978-09-25', 'Kyivska St., 67', '+380996655544'),
    ('Lysenko Ihor Mykhailovych', 'Male', '1985-03-18', 'Hrushevskoho St., 12', '+380992233411'),
    ('Smirnov Vasyl Vasylovych', 'Male', '1992-11-02', 'Sadova St., 34', '+380995577789'),
    ('Zaytseva Tetiana Vitaliyivna', 'Female', '1982-06-07', 'Chervonyi Lis St., 89', '+380998888111'),
    ('Danyliuk Olena Petrovna', 'Female', '2000-01-12', 'Molodizhna St., 5', '+380999999999');

INSERT INTO RegistrationJournal (patient_id, specialist_id, visit_number, visit_date, complaints, diagnosis, treatment, service_cost)
VALUES
     (1, 1, 1, '2023-09-01', 'Sore throat', 'Angina', 'Antibiotics', 200.00),
    (2, 2, 1, '2023-09-02', 'Itchy skin', 'Dermatitis', 'Topical cream', 150.50),
    (3, 3, 1, '2023-09-03', 'Vision problems', 'Cataract', 'Eye surgery', 800.00),
    (4, 4, 1, '2023-09-04', 'Abdominal pain', 'Gastritis', 'Blood test', 120.00),
    (5, 1, 2, '2023-09-05', 'High blood pressure', 'Hypertension', 'Prescribed medication', 75.50),
    (6, 2, 2, '2023-09-06', 'Back pain', 'Osteochondrosis', 'Physical therapy', 180.00),
    (7, 3, 2, '2023-09-07', 'Eye inflammation', 'Conjunctivitis', 'Eye drops', 35.00),
    (8, 4, 3, '2023-09-08', 'Abdominal pain', 'Gastritis', 'Blood test', 120.00),
    (9, 1, 3, '2023-09-09', 'Toothache', 'Caries', 'Tooth filling', 95.00),
    (10, 2, 3, '2023-09-10', 'Skin rash', 'Dermatitis', 'Calming cream', 55.50);

INSERT INTO ReferralJournal (procedure_analysis_name, patient_id, referring_specialist_id, performing_specialist_id, procedure_date, results)
VALUES
    ('Complete blood count', 1, 1, 4, '2023-09-05', 'Normal values'),
    ('Abdominal ultrasound', 2, 2, 5, '2023-09-10', 'No abnormalities'),
    ('Ophthalmologist examination', 3, 3, 6, '2023-09-15', 'Scheduled examination'),
    ('Chest X-ray', 4, 4, 7, '2023-09-12', 'No abnormalities'),
    ('Color Doppler of arteries', 5, 1, 8, '2023-09-18', 'Normal blood circulation'),
    ('Urinalysis', 6, 2, 9, '2023-09-20', 'Normal values'),
    ('Complete blood count', 7, 3, 10, '2023-09-25', 'Leukocytosis'),
    ('Gastrofibroscopy', 8, 4, 1, '2023-09-30', 'Pathological changes in mucous membrane'),
    ('Electrocardiogram (ECG)', 9, 1, 2, '2023-10-05', 'Normal heart rhythm'),
    ('Blood glucose test', 10, 2, 3, '2023-10-10', 'Elevated glucose levels');


-- Виведення списку всіх таблиць у поточній базі даних
SHOW TABLES;

-- Виведення опису структури таблиці exxxpert
DESC exxxpert;

-- Виведення опису структури таблиці MedicalRecords
DESC MedicalRecords;

-- Виведення опису структури таблиці RegistrationJournal
DESC RegistrationJournal;

-- Виведення опису структури таблиці ReferralJournal
DESC ReferralJournal;

-- Виведення даних з таблиці exxxpert
SELECT * FROM exxxpert;

-- Виведення даних з таблиці MedicalRecords
SELECT * FROM MedicalRecords;

-- Виведення даних з таблиці RegistrationJournal
SELECT * FROM RegistrationJournal;

-- Виведення даних з таблиці ReferralJournal
SELECT * FROM ReferralJournal;

