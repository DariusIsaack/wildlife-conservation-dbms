CREATE OR REPLACE FUNCTION count_animals_in_habitat(h_id INT)
RETURNS INT AS
$$
DECLARE
total INT;
BEGIN
SELECT COUNT(*)
INTO total
FROM animals
WHERE habitat_id = h_id;

RETURN total;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE add_new_animal(
p_species VARCHAR,
p_tag_id VARCHAR,
p_age INT,
p_health VARCHAR,
p_habitat INT
)
LANGUAGE plpgsql
AS
$$
BEGIN
INSERT INTO animals (species, tag_id, age, health_status, habitat_id)
VALUES (p_species, p_tag_id, p_age, p_health, p_habitat );
END;
$$;

CREATE OR REPLACE FUNCTION check_animal_age()
RETURNS TRIGGER AS
$$
BEGIN
IF NEW.age < 0 THEN
RAISE EXCEPTION 'Age cannot be negative';
END IF;

RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER animal_age_trigger
BEFORE INSERT OR UPDATE
ON animals
FOR EACH ROW
EXECUTE FUNCTION check_animal_age();

CREATE OR REPLACE FUNCTION auto_incident_date()
RETURNS TRIGGER AS
$$
BEGIN
NEW.incident_date = CURRENT_TIMESTAMP;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER incident_date_trigger
BEFORE INSERT
ON incidents
FOR EACH ROW
EXECUTE FUNCTION auto_incident_date();

CREATE OR REPLACE FUNCTION count_staff_observations(s_id INT)
RETURNS INT AS
$$
DECLARE
total INT;
BEGIN
SELECT COUNT(*)
INTO total
FROM observations
WHERE staff_id = s_id;
RETURN total;
END;
$$ LANGUAGE plpgsql;

