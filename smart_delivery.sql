-- CREATE DATABASE smart_delivery_system;
USE smart_delivery_system;
-- CREATE TABLE locations (
    -- location_id INT PRIMARY KEY AUTO_INCREMENT,
    -- location_name VARCHAR(100) UNIQUE NOT NULL
-- );
 -- CREATE TABLE roads (
-- 	road_id INT PRIMARY KEY AUTO_INCREMENT,
-- 	source_location INT,
-- 	destination_location INT,
-- 	distance INT,
--     traffic_level INT DEFAULT 1,
    
-- 	FOREIGN KEY (source_location) REFERENCES locations(location_id),
 --    FOREIGN KEY (destination_location) REFERENCES locations(location_id)
--  );
-- CREATE TABLE deliveries (
  --   delivery_id INT PRIMARY KEY AUTO_INCREMENT,
 --    order_name VARCHAR(100),
 --    source_location INT,
 --    destination_location INT,
 --    status VARCHAR(50) DEFAULT 'Pending',
 --    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

 --    FOREIGN KEY (source_location) REFERENCES locations(location_id),
 --    FOREIGN KEY (destination_location) REFERENCES locations(location_id)
-- );
-- CREATE TABLE delivery_queue (
--     queue_id INT PRIMARY KEY AUTO_INCREMENT,
 --    delivery_id INT,
 --    queue_position INT,

 --    FOREIGN KEY (delivery_id) REFERENCES deliveries(delivery_id)
-- );
-- INSERT INTO locations(location_name) VALUES
-- ('Warehouse'),
-- ('AreaA'),
-- ('AreaB'),
-- ('AreaC'),
-- ('AreaD'),
-- ('AreaE'),
-- ('AreaF'),
-- ('AreaG'),
-- ('AreaH'),
-- ('AreaI'),
-- ('AreaJ'),
-- ('AreaK'),
-- ('AreaL'),
-- ('AreaM'),
-- ('AreaN');
-- INSERT INTO roads(source_location, destination_location, distance, traffic_level) VALUES
-- (1,2,5,1),
-- (1,3,8,2),
-- (1,4,6,1),
-- (2,3,3,1),
-- (2,5,7,2),
-- (3,6,4,1),
-- (4,6,5,2),
-- (5,7,6,1),
-- (6,7,3,1),
-- (7,8,4,2),
-- (8,9,5,1),
-- (9,10,7,2),
-- (10,11,4,1),
-- (11,12,6,2),
-- (12,13,5,1),
-- (13,14,8,3),
-- (14,15,6,2),
-- (2,8,9,2),
-- (3,9,7,1),
-- (4,10,10,3),
-- (5,11,6,1),
-- (6,12,7,2),
-- (7,13,8,2),
-- (8,14,9,3),
-- (9,15,5,1),
-- (1,5,9,2),
-- (2,6,4,1),
-- (3,7,6,2),
-- (4,8,7,2),
-- (5,9,8,1),
-- (6,10,6,2),
-- (7,11,5,1),
-- (8,12,7,2),
-- (9,13,9,3),
-- (10,14,6,2),
-- (11,15,8,2),
-- (3,4,2,1),
-- (4,5,3,1),
-- (5,6,4,2),
-- (6,8,5,1),
-- (7,9,3,1),
-- (8,10,4,2),
-- (9,11,5,1),
-- (10,12,6,2),
-- (11,13,7,1),
-- (12,14,5,2),
-- (13,15,4,1),
-- (1,7,12,3),
-- (2,9,10,2),
-- (3,11,11,3);

INSERT INTO deliveries(order_name, source_location, destination_location) VALUES
('Order_001',1,10),
('Order_002',1,7),
('Order_003',2,9),
('Order_004',3,12),
('Order_005',4,14),
('Order_006',5,8),
('Order_007',6,13),
('Order_008',7,11),
('Order_009',8,15),
('Order_010',9,14),
('Order_011',2,10),
('Order_012',3,8),
('Order_013',4,12),
('Order_014',5,13),
('Order_015',6,14),
('Order_016',7,15),
('Order_017',8,11),
('Order_018',9,12),
('Order_019',10,13),
('Order_020',11,15);