SELECT * FROM dojos;

INSERT INTO dojos (name) VALUE ("Coding Dojo")
INSERT INTO dojos (name) VALUE ("Sonic Dojo")
INSERT INTO dojos (name) VALUE ("Planet Dojo")

DELETE FROM dojos WHERE id = 1;
DELETE FROM dojos WHERE id = 2;
DELETE FROM dojos WHERE id = 3;

INSERT INTO dojos (name) VALUE ("Ape Dojo");
INSERT INTO dojos (name) VALUE ("Green Dragon Dojo");
INSERT INTO dojos (name) VALUE ("Napalm Dojo");

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Gandalf", "Grey", 50, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Jon", "Bellion", 23, 4);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Mark", "Walburgh", 50, 4);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Snake", "Eyes", 23, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Darth", "Maul", 18, 5);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Sidious", "Maul", 18, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Marco", "Polo", 80, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Harry", "Potter", 19, 6);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUE ("Ricardo", "Diaz", 31, 6);

SELECT * FROM ninjas WHERE dojo_id = 4;
SELECT * FROM ninjas WHERE dojo_id = 6;
SELECT * FROM dojos WHERE name = "Ricardo";
