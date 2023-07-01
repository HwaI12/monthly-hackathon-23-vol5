CREATE TABLE users (
  id serial,
  user_name TEXT,
  password TEXT
  primary key (id)
);

INSERT INTO users (user_name, password) VALUES ('hoge', 'hoge');


