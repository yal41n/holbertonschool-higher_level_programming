-- Lists all shows that have at least one genre linked
-- Output: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT TV_SHows.title, TV_Show_genres.genre_id
FROM TV_Shows
INNER JOIN TV_Show_genres ON TV_Shows.id = TV_Show_genres.show_id
ORDER BY TV_Shows.title ASC, TV_Show_genres.genre_id ASC;
