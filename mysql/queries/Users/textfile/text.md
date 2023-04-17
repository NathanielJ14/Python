SELECT * FROM users;
INSERT INTO users (first_name, last_name, email) VALUES ("Nathan", "Albert", "na@gmail.com");
INSERT INTO users (first_name, last_name, email) VALUES ("Kennedy", "Pearl", "kp@gmail.com");
INSERT INTO users (first_name, last_name, email) VALUES ("Kygo", "Dannis", "KD@gmail.com");
SELECT * FROM users;

SELECT * FROM users WHERE email = "na@gmail.com";

SELECT * FROM users WHERE id = 3;

UPDATE users SET last_name = "Pancakes" 
WHERE id = 3;


DELETE FROM users WHERE id = 2;
SELECT * FROM users
WHERE id = 1 OR id = 2
ORDER BY first_name;