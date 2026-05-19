CREATE TABLE roles (
role_id SERIAL PRIMARY KEY,
role_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(100) NOT NULL,
role_id INT,
FOREIGN KEY (role_id) REFERENCES roles(role_id)
ON DELETE SET NULL
);

CREATE TABLE habitats (
habitat_id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
location VARCHAR(100),
type VARCHAR(50)
);

CREATE TABLE animals (
animal_id SERIAL PRIMARY KEY,
species VARCHAR(100) NOT NULL,
tag_id VARCHAR(50) UNIQUE,
age INT CHECK (age >= 0),
health_status VARCHAR(50),
habitat_id INT,
FOREIGN KEY (habitat_id) REFERENCES habitats(habitat_id)
ON DELETE SET NULL
);

CREATE TABLE staff (
staff_id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
role VARCHAR(50),
assigned_habitat INT,
FOREIGN KEY (assigned_habitat) REFERENCES habitats(habitat_id)
ON DELETE SET NULL
);

CREATE TABLE observations (
observation_id SERIAL PRIMARY KEY,
animal_id INT,
staff_id INT,
observation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
location VARCHAR(100),
notes TEXT,
FOREIGN KEY (animal_id) REFERENCES animals(animal_id)
ON DELETE CASCADE,
FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
ON DELETE SET NULL
);

CREATE TABLE incidents (
incident_id SERIAL PRIMARY KEY,
animal_id INT,
incident_type VARCHAR(50),
description TEXT,
incident_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (animal_id)
REFERENCES animals(animal_id)
ON DELETE CASCADE
);
