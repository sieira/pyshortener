CREATE TABLE url (
    ID int NOT NULL UNIQUE AUTO_INCREMENT,
    long_url VARCHAR(2000) NOT NULL UNIQUE,
    short_url VARCHAR(6) NOT NULL UNIQUE,
    click_count INT DEFAULT 0,
    expiration_date INT
);

CREATE EVENT IF NOT EXISTS
  ClearExpiredUrls
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
DELETE FROM
  url
WHERE expiration_date < NOW();
END