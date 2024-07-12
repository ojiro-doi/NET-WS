.open a7-1.db
DROP TABLE IF EXISTS events;
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL
);
INSERT INTO events (event_id, event_name, event_date, location) VALUES
(1,'東京オリンピック', '2021-07-23', '東京'),
(2,'北京オリンピック', '2022-02-04', '北京'),
(3,'ロンドンオリンピック', '2012-07-27', 'ロンドン'),
(4,'リオデジャネイロオリンピック', '2016-08-05', 'リオデジャネイロ'),
(5,'パリオリンピック', '2024-07-26', 'パリ'),
(6,'ロサンゼルスオリンピック', '2028-07-21', 'ロサンゼルス'),
(7,'カタールワールドカップ', '2022-11-20', 'ドーハ'),
(8,'ロシアワールドカップ', '2018-06-14', 'モスクワ'),
(9,'ブラジルワールドカップ', '2014-06-12', 'リオデジャネイロ'),
(10,'アメリカ・カナダ・メキシコワールドカップ', '2026-06-08', 'ニューヨーク');
SELECT * FROM events;
SELECT * FROM events WHERE event_name LIKE '%オリンピック%';
SELECT * FROM events WHERE event_date > DATE('now');
SELECT * FROM events WHERE event_date < DATE('now') AND event_name LIKE '%オリンピック%';
