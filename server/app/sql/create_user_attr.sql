CREATE TABLE app.user_attr (
	user_id int8 NOT NULL,
	interest varchar NOT NULL,
	CONSTRAINT user_attr_pk PRIMARY KEY (user_id, interest)
);