.open a5-1.db
DROP TABLE IF EXISTS events;
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL
);
INSERT INTO events (event_name, event_date, location) VALUES
('東京オリンピック', '2021-07-23', '東京'),
('北京オリンピック', '2022-02-04', '北京'),
('ロンドンオリンピック', '2012-07-27', 'ロンドン'),
('リオデジャネイロオリンピック', '2016-08-05', 'リオデジャネイロ'),
('パリオリンピック', '2024-07-26', 'パリ'),
('ロサンゼルスオリンピック', '2028-07-21', 'ロサンゼルス'),
('カタールワールドカップ', '2022-11-20', 'ドーハ'),
('ロシアワールドカップ', '2018-06-14', 'モスクワ'),
('ブラジルワールドカップ', '2014-06-12', 'リオデジャネイロ'),
('アメリカ・カナダ・メキシコワールドカップ', '2026-06-08', 'ニューヨーク');
SELECT * FROM events;
SELECT * FROM events WHERE event_name LIKE '%オリンピック%';
SELECT * FROM events WHERE event_date > DATE('now');
SELECT * FROM events WHERE event_date < DATE('now') AND event_name LIKE '%オリンピック%';
