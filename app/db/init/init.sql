--ユーザーの作成
CREATE USER postgres;
--DBの作成
CREATE DATABASE postgres;
--ユーザーにDBの権限をまとめて付与
GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;
--ユーザーを切り替え
\c postgres

CREATE TABLE users (
  id serial,
  user_name TEXT,
  password TEXT
  primary key (id)
);

INSERT INTO users (user_name, password) VALUES ('hoge', 'hoge');

