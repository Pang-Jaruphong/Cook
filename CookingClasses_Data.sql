USE CookingClasses;

-- Participants
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (1,'Jason Roger Marc','Edmonds', '0761234567', 'jason.edmonds@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (2,'Sofian','Hussein', '0762345678', 'sofian.hussein@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (3,'Loïc','Roux', '0763456789', 'loïc.roux@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (4,'Amil','Sabotic', '0764567890', 'amil.sabotic@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (5,'Rodrigo','Silva Riço', '0765678901', 'rodrigo.silva riço@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (6,'Milo','Soupper', '0766789012', 'milo.soupper@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (7,'Samuel','Theytaz', '0767890123', 'samuel.theytaz@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (8,'Samuel','Antunes', '0768901234', 'samuel.antunes@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (9,'Joel','Cunha Faria', '0769012345', 'joel.cunha faria@eduuvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (10,'Léo','Del Duca', '0760123456', 'léo.del duca@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (11,'Iago','Dolfini De Paula', '0799876543', 'iago.dolfini@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (12,'Dani','Dordevic', '0798765432', 'dani.dordevic@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (13,'Even','Gebregergs', '0797654321', 'even.gebregergs@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (14,'Antoine','Jaccard', '0796543210', 'antoine.jaccard@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (15,'Cédric','Jankiewicz', '0795432109', 'cédric.jankiewicz@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (16,'Oleksii','Kamarali', '0794321098', 'oleksii.kamarali@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (17,'Timmy','Marendaz', '0793210987', 'timmy.marendaz@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (18,'Dylan','Martini', '0792109876', 'dylan.martini@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (19,'Thierry','Perroud', '0791098765', 'thierry.perroud@eduvaud.ch');
INSERT INTO `participants` (id,first_name, last_name, phone, mail) VALUES (20,'Melva','Zerda Macias', '0781234567', 'melva.zerda macias@eduvaud.ch');

-- Lieux
INSERT INTO `places` (id,name, address, town, phone) VALUES (1,'Thai Siri Restaurant','Rue de la gare 12', 'Ste. Croix', '0243800790');
INSERT INTO `places` (id,name, address, town, phone) VALUES (2,'Mont Blanc','Rue de Lausanne 3', 'Yverdon-les-bains', '0245556070');
INSERT INTO `places` (id,name, address, town, phone) VALUES (3,'Turkey Kitchen','Rue de Génève 12', 'Yverdon-les-bains', '0245581412');
INSERT INTO `places` (id,name, address, town, phone) VALUES (4,'Asia Shop','Rue César Roux 2', 'Lausanne', '0213161212');
INSERT INTO `places` (id,name, address, town, phone) VALUES (5,'Tong Bay Restaurant','Grand Rue 5', 'Payerne', '0266002535');

-- Profs
INSERT INTO `teachers` (id,firstname, lastname, phone, mail) VALUES (1,'Jaruphong','Plancherel', '0763800790', 'pv82wpf@eduvaud.ch');
INSERT INTO `teachers` (id,firstname, lastname, phone, mail) VALUES (2,'Gaëtan','Gendroz', '0791290787', 'gaetan.gendroz@eduvaud.ch');
INSERT INTO `teachers` (id,firstname, lastname, phone, mail) VALUES (3,'Ahmet','Karabulut', '0782024120', 'ahmet.karabulut@eduvaud.ch');
INSERT INTO `teachers` (id,firstname, lastname, phone, mail) VALUES (4,'Fabian','Rostello', '0764286076', 'fabian.rostello@eduvaud.ch');

-- Cours a lieu et le prof
INSERT INTO `cook_courses` (id,name, begin_time, finish_time, price, max_place, last_inscription, places_id, teachers_id) VALUES (NULL, 'Thai','2025-05-09 10:00', '12:00', 50.00, 5, '2025-05-02', 1, 1);
INSERT INTO `cook_courses` (id,name, begin_time, finish_time, price, max_place, last_inscription, places_id, teachers_id) VALUES (NULL, 'Suisse','2025-05-10 09:30', '11:30', 40.00, 10, '2025-05-03', 2, 2);
INSERT INTO `cook_courses` (id,name, begin_time, finish_time, price, max_place, last_inscription, places_id, teachers_id) VALUES (NULL,'Turc','2025-05-11 17:00', '19:00', 45.00, 5, '2025-05-04', 3, 3);
INSERT INTO `cook_courses` (id,name, begin_time, finish_time, price, max_place, last_inscription, places_id, teachers_id) VALUES (NULL,'Chinoise','2025-05-12 09:00', '12:00', 50.00, 6, '2025-05-05', 4, 4);
INSERT INTO `cook_courses` (id,name, begin_time, finish_time, price, max_place, last_inscription, places_id, teachers_id) VALUES (NULL,'Salade Asiatique','2025-05-12 15:00', '17:30', 50.00, 6, '2025-05-05', 5, 1);

-- Participants inscrivent aux cours
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'1', '1');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'2', '1');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'3', '1');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'4', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'5', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'6', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'7', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'8', '3');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'9', '3');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'10', '3');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'11', '3');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'12', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'13', '2');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'14', '4');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'15', '4');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'16', '5');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'17', '5');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'18', '5');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'19', '4');
INSERT INTO `participants_has_cook_courses` (id,participants_id, cook_courses_id) VALUES (NULL,'20', '1');
