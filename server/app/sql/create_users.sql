CREATE TABLE app.users (
	id serial,
	username varchar NOT NULL,
	email varchar NOT NULL,
	"password" varchar NOT NULL,
	country varchar NOT NULL,
	city varchar NOT NULL,
	CONSTRAINT users_pk PRIMARY KEY (id),
	CONSTRAINT users_unique UNIQUE (username),
	CONSTRAINT users_unique_1 UNIQUE (email)
);
