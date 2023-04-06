-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users As user, (SELECT user.id, SUM(score * weight) / SUM(weight) wavg FROM users AS user JOIN corrections AS correction ON user.id=correction.user_id JOIN projects AS project ON correction.project_id=project.id GROUP BY user.id) AS avg SET user.average_score = avg.wavg WHERE user.id=avg.id;
END
$$
DELIMITER ;
