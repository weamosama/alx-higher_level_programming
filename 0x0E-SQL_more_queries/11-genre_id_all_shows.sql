-- 11-genre_id_all_shows.sql

-- Use the 'hbtn_0d_tvshows' database
USE hbtn_0d_tvshows;

-- Select all shows and their linked genres (or NULL if no genre)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

