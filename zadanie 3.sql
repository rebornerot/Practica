CREATE DATABASE IF NOT EXISTS Tourism;
USE Tourism;

CREATE TABLE Clients (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Phone VARCHAR(20)
);

CREATE TABLE Tours (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    TourName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL
);

CREATE TABLE Statuses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    StatusName VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Orders (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE NOT NULL,
    ClientID INT NOT NULL,
    TourID INT NOT NULL,
    StatusID INT NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL DEFAULT 0, 
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    FOREIGN KEY (ClientID) REFERENCES Clients(ID),
    FOREIGN KEY (TourID) REFERENCES Tours(ID),
    FOREIGN KEY (StatusID) REFERENCES Statuses(ID)
);

INSERT INTO Clients (FullName, Phone) VALUES
('Шафранова Карина', '+7 (928) 244-25-99'),
('Гришин Артем', '+7 (968) 838-14-92'),
('Ковалев Вячеслав', '+7 (944) 567-12-58');

INSERT INTO Tours (TourName, Price) VALUES
('Париж', 350000.00),
('Вашингтон', 400000.00),
('Ярославль', 20000.00);

INSERT INTO Statuses (StatusName) VALUES
('Новый'), ('Подтверждён'), ('Оплачен'), ('Отменён');

INSERT INTO Orders (OrderDate, ClientID, TourID, StatusID, TotalAmount, StartDate, EndDate) VALUES
('2026-11-20', 1, 1, 1, 0, '2026-12-10', '2027-02-03'),
('2026-11-21', 2, 2, 2, 0, '2026-12-11', '2027-02-02'),
('2026-11-22', 3, 3, 1, 0, '2026-12-12', '2027-02-01');

UPDATE Orders o
JOIN Tours t ON o.TourID = t.ID
SET o.TotalAmount = t.Price;

SELECT * FROM Orders;