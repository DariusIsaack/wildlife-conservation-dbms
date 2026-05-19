INSERT INTO roles (role_name)
VALUES
('Admin'),
('Ranger'),
('Researcher');

INSERT INTO users (username, password, role_id)
VALUES
('admin1', 'admin123', 1),
('ranger1', 'ranger123', 2),
('researcher1', 'research123', 3);

INSERT INTO habitats (name, location, type)
VALUES
('Savannah Zone', 'Kenya', 'Grassland'),
('Rainforest Zone', 'Amazon', 'Forest'),
('Mountain Reserve', 'Nepal', 'Mountain');

INSERT INTO animals (species, tag_id, age, health_status, habitat_id)
VALUES
('Elephant', 'E001', 25, 'Healthy', 1),
('Lion', 'L001', 10, 'Healthy', 1),
('Tiger', 'T001', 8, 'Injured', 2),
('Panda', 'P001', 6, 'Healthy', 3);

INSERT INTO staff (name, role, assigned_habitat)
VALUES
('John Doe', 'Ranger', 1),
('Jane Smith', 'Researcher', 2),
('Mike Johnson', 'Ranger', 3);

INSERT INTO observations (animal_id, staff_id, location, notes)
VALUES
(1, 1, 'North Savannah', 'Animal grazing normally'),
(2, 1, 'East Savannah', 'Lion resting under tree'),
(3, 2, 'Central Rainforest', 'Tiger limping, possible injury'),
(4, 3, 'Mountain Reserve', 'Panda playing with bamboo');

INSERT INTO incidents (animal_id, incident_type, description)
VALUES
(1, 'Injury', 'Elephant injured near river'),
(2, 'Poaching Attempt', 'Suspicious activity detected');
