-- A SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes and
-- store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    ALTER TABLE users
        ADD total_weight INT NOT NULL;
    ALTER TABLE users
        ADD total_weighted_score INT NOT NULL;

    UPDATE users
        SET total_weighted_score = (
            SELECT SUM(corrections.score * projects.weight)
                FROM corrections
                    INNER JOIN projects ON corrections.project_id = projects.id
                WHERE corrections.user_id = users.id
        ),total_weight = (
            SELECT SUM(projects.weight)
                FROM corrections
                    INNER JOIN projects ON corrections.project_id = projects.id
                WHERE corrections.user_id = users.id
        ), users.average_score = IF(
            users.total_weight = 0, 0,
            users.total_weighted_score / users.total_weight
        );
    ALTER TABLE users
        DROP COLUMN total_weighted_score,
        DROP COLUMN total_weight;
END $$
DELIMITER ;
