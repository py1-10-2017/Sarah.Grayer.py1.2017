SELECT * FROM followers 
JOIN users as leaders ON leader_id = leaders.id
JOIN users as followees ON follower_id = followees.id;

SELECT * FROM followers 
WHERE follower_id = 1;

SELECT *
FROM users
JOIN followers ON users.id = followers.users_id
JOIN users AS users2 ON users2.id = followers.follower_id



