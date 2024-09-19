CREATE DATABASE Gym_membership_db;

CREATE TABLE Members(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(250) NOT NULL,
age INT NOT NULL);

CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY auto_increment,
    member_id INT,
    date DATE NOT NULL,
    duration_minutes INT NOT NULL,
    calories_burned INT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);

select * from Members;

select * from WorkoutSessions;