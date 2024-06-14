.open sample.db
.mode box
DROP TABLE IF EXISTS tigers2023;
CREATE TABLE tigers2023(id INTEGER PRIMARY KEY AUTOINCREMENT, number INT, position TEXT, name TEXT);
INSERT INTO tigers2023(number, position, name) VALUES(5,'外野手','近本');
INSERT INTO tigers2023(number, position, name) VALUES(8,'内野手','佐藤');
INSERT INTO tigers2023(number, position, name) VALUES(65,'投手','湯浅');
SELECT * FROM tigers2023;