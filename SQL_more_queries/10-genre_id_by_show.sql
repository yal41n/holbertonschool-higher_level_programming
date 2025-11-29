-- Lists all shows that have at least one genre linked
-- Output: tv_shows.title - tv_show_genres.genre_id
-- Sorted by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT TV_SHOWS.TITLE, TV_SHOW_GENRES.GENRE_ID
FROM TV_SHOWS
INNER JOIN TV_SHOW_GENRES ON TV_SHOWS.ID = TV_SHOW_GENRES.SHOW_ID
ORDER BY TV_SHOWS.TITLE ASC, TV_SHOW_GENRES.GENRE_ID ASC;
