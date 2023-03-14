-- https://gist.github.com/haggen/ff4dda6cffa4ee295c6a27d05b73332b

DROP schema PUBLIC cascade;
CREATE schema public;
CREATE TABLE users(id serial PRIMARY key, name text);
CREATE TABLE invoices(id serial PRIMARY key, description text, user_id INTEGER REFERENCES users(id));
INSERT INTO users(id, name) VALUES (1, 'alice'), (2,'bob');
INSERT INTO invoices(description, user_id) VALUES ('invoice1',1), ('invoice2',1);
