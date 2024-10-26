CREATE TABLE app.friendship (
	user_id int8 NOT NULL,
	friend_id int8 NOT null,
	CONSTRAINT friendship_pk PRIMARY KEY (user_id, friend_id)
);


ALTER TABLE app.friendship ADD CONSTRAINT friendship_users_fk FOREIGN KEY (user_id) REFERENCES app.users(id) ON UPDATE CASCADE;
ALTER TABLE app.friendship ADD CONSTRAINT friendship_users_fk_1 FOREIGN KEY (friend_id) REFERENCES app.users(id) ON UPDATE CASCADE;