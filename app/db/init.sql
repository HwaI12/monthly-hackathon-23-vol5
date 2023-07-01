CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  user_name TEXT,
  password TEXT
);

INSERT INTO users (user_name, password) VALUES ('hoge', 'hoge');

