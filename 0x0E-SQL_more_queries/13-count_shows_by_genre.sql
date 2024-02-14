-- 13-count_shows_by_genre.sql

-- Use the 'hbtn_0d_tvshows' database
USE hbtn_0d_tvshows;

-- Select genres and count of shows linked to each genre
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
ORDER BY number_of_shows DESC;

