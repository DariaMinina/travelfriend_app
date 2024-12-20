INSERT INTO app.users (username, email, password, country, city) VALUES ('serg_petrov', 'sergpetrov@gmail.com', 'nv43vn3ivub', 'Russia', 'Vladimir'),
('alex_pavlov', 'alexpavlov@gmail.com', '93ghubi2lk', 'Russia', 'Moscow'),
('lena_trifonova', 'lenatrifonova@gmail.com', '4holnbwf', 'Russia', 'Saratov'),
('sam_willson', 'samwillson@gmail.com', 'h39fh3onlkono', 'USA', 'Chicago'),
('andrew_lawrence', 'andrewlawrence@gmail.com', 'n4uu32nof', 'USA', 'Austin'),
('jane_tomson', 'janetomson@gmail.com', 'kfvjnigevr9hi', 'USA', 'Phoenix'),
('alfred_klein', 'alfredklein@gmail.com', '34hnkvlwmevp', 'Germany', 'Muenchen'),
('agnes_weber', 'agnesweber@gmail.com', 'zdsvet4', 'Germany', 'Leipzig'),
('eric_carriere', 'ericcarriere@gmail.com', '94nvlkwfei', 'France', 'Paris'),
('lise_pretre', 'lisepretre@gmail.com', 'rh7gyduhfink', 'France', 'Strasbourg');



INSERT INTO app.user_attr (user_id, interest) VALUES ((SELECT id FROM app.users WHERE username = 'serg_petrov'), 'astronomy'),
((SELECT id FROM app.users WHERE username = 'serg_petrov'), 'mathematics'),
((SELECT id FROM app.users WHERE username = 'serg_petrov'), 'history'),
((SELECT id FROM app.users WHERE username = 'alex_pavlov'), 'programming'),
((SELECT id FROM app.users WHERE username = 'alex_pavlov'), 'mathematics'),
((SELECT id FROM app.users WHERE username = 'lena_trifonova'), 'yoga'),
((SELECT id FROM app.users WHERE username = 'lena_trifonova'), 'history'),
((SELECT id FROM app.users WHERE username = 'sam_willson'), 'comics'),
((SELECT id FROM app.users WHERE username = 'sam_willson'), 'cycling'),
((SELECT id FROM app.users WHERE username = 'sam_willson'), 'programming'),
((SELECT id FROM app.users WHERE username = 'andrew_lawrence'), 'history'),
((SELECT id FROM app.users WHERE username = 'jane_tomson'), 'comics'),
((SELECT id FROM app.users WHERE username = 'jane_tomson'), 'history'),
((SELECT id FROM app.users WHERE username = 'alfred_klein'), 'sport'),
((SELECT id FROM app.users WHERE username = 'alfred_klein'), 'mathematics'),
((SELECT id FROM app.users WHERE username = 'alfred_klein'), 'astronomy'),
((SELECT id FROM app.users WHERE username = 'agnes_weber'), 'yoga'),
((SELECT id FROM app.users WHERE username = 'agnes_weber'), 'cycling'),
((SELECT id FROM app.users WHERE username = 'eric_carriere'), 'programming'),
((SELECT id FROM app.users WHERE username = 'eric_carriere'), 'mathematics'),
((SELECT id FROM app.users WHERE username = 'lise_pretre'), 'programming'),
((SELECT id FROM app.users WHERE username = 'lise_pretre'), 'history'),
((SELECT id FROM app.users WHERE username = 'lise_pretre'), 'cycling');

INSERT INTO app.friendship (user_id, friend_id) VALUES ((SELECT id FROM app.users WHERE username = 'serg_petrov'), (SELECT id FROM app.users WHERE username = 'alex_pavlov')),
((SELECT id FROM app.users WHERE username = 'alex_pavlov'), (SELECT id FROM app.users WHERE username = 'serg_petrov')),
((SELECT id FROM app.users WHERE username = 'serg_petrov'), (SELECT id FROM app.users WHERE username = 'lena_trifonova')),
((SELECT id FROM app.users WHERE username = 'lena_trifonova'), (SELECT id FROM app.users WHERE username = 'serg_petrov')),
((SELECT id FROM app.users WHERE username = 'alex_pavlov'), (SELECT id FROM app.users WHERE username = 'lena_trifonova')),
((SELECT id FROM app.users WHERE username = 'lena_trifonova'), (SELECT id FROM app.users WHERE username = 'alex_pavlov')),
((SELECT id FROM app.users WHERE username = 'sam_willson'), (SELECT id FROM app.users WHERE username = 'andrew_lawrence')),
((SELECT id FROM app.users WHERE username = 'andrew_lawrence'), (SELECT id FROM app.users WHERE username = 'sam_willson')),
((SELECT id FROM app.users WHERE username = 'sam_willson'), (SELECT id FROM app.users WHERE username = 'jane_tomson')),
((SELECT id FROM app.users WHERE username = 'jane_tomson'), (SELECT id FROM app.users WHERE username = 'sam_willson')),
((SELECT id FROM app.users WHERE username = 'andrew_lawrence'), (SELECT id FROM app.users WHERE username = 'jane_tomson')),
((SELECT id FROM app.users WHERE username = 'jane_tomson'), (SELECT id FROM app.users WHERE username = 'andrew_lawrence')),
((SELECT id FROM app.users WHERE username = 'alfred_klein'), (SELECT id FROM app.users WHERE username = 'agnes_weber')),
((SELECT id FROM app.users WHERE username = 'agnes_weber'), (SELECT id FROM app.users WHERE username = 'alfred_klein')),
((SELECT id FROM app.users WHERE username = 'eric_carriere'), (SELECT id FROM app.users WHERE username = 'lise_pretre')),
((SELECT id FROM app.users WHERE username = 'lise_pretre'), (SELECT id FROM app.users WHERE username = 'eric_carriere'));
