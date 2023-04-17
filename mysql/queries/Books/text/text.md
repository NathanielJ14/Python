INSERT INTO users (name) VALUES ("Emily Dixon");
INSERT INTO users (name) VALUES ("Theodore Dostoevsky");
INSERT INTO users (name) VALUES ("Jane Amsden");
INSERT INTO users (name) VALUES ("William Shapiro");
INSERT INTO users (name) VALUES ("Loa Xiu");

INSERT INTO books (title) VALUES ("C Sharp");
INSERT INTO books (title) VALUES ("Java");
INSERT INTO books (title) VALUES ("Python");
INSERT INTO books (title) VALUES ("PHP");
INSERT INTO books (title) VALUES ("Ruby");

UPDATE books SET title = "C#" WHERE id = 1;
UPDATE users SET name = "Bill Shapiro" WHERE id = 4;

INSERT INTO favorites (book_id, user_id) VALUES (1, 1)
INSERT INTO favorites (book_id, user_id) VALUES (2, 1)

INSERT INTO favorites (book_id, user_id) VALUES (1, 2);
INSERT INTO favorites (book_id, user_id) VALUES (2, 2);
INSERT INTO favorites (book_id, user_id) VALUES (3, 2);

INSERT INTO favorites (book_id, user_id) VALUES (1, 3);
INSERT INTO favorites (book_id, user_id) VALUES (2, 3);
INSERT INTO favorites (book_id, user_id) VALUES (3, 3);
INSERT INTO favorites (book_id, user_id) VALUES (4, 3);

INSERT INTO favorites (book_id, user_id) VALUES (1, 4);
INSERT INTO favorites (book_id, user_id) VALUES (2, 4);
INSERT INTO favorites (book_id, user_id) VALUES (3, 4);
INSERT INTO favorites (book_id, user_id) VALUES (4, 4);
INSERT INTO favorites (book_id, user_id) VALUES (5, 4);

SELECT * FROM favorites WHERE book_id = 3; 
DELETE FROM favorites WHERE id = 5;

INSERT INTO favorites (book_id, user_id) VALUES(2, 5);
SELECT * FROM favorites WHERE user_id = 3; 