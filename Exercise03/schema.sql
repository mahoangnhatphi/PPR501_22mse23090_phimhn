DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id int NOT NULL AUTO_INCREMENT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, 
    title varchar(255),
    content varchar(255),
    PRIMARY KEY (id)
);