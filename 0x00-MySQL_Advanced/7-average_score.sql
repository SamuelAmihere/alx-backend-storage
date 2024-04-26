-- A SQL script that creates a stored procedure 
-- ComputeAverageScoreForUser that computes and store 
-- the average score for a student. Note: An average score can be a decimal
-- Requirements:
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id INT
)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_projects INT DEFAULT 0;
    DECLARE average_score FLOAT DEFAULT 0;
    
    SELECT SUM(score) INTO total_score FROM corrections
        WHERE user_id = user_id;
    SELECT COUNT(project_id) INTO total_projects FROM corrections
        WHERE user_id = user_id;
    IF total_projects > 0 THEN
        SET average_score = total_score / total_projects;
    END IF;
    UPDATE users
        SET average_score = average_score
        WHERE id = user_id;
END $$
