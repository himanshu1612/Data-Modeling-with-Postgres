# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = (""" create table if not exists songplays (songplay_id serial Primary Key, start_time timestamp NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar)
""")

user_table_create = (""" create table if not exists users (user_id int Primary Key, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = (""" create table if not exists songs (song_id varchar Primary Key, title varchar, artist_id varchar NOT NULL, year int, duration numeric)
""")

artist_table_create = ("""create table if not exists artists (artist_id varchar Primary Key, name varchar, location varchar, latitude numeric, longitude numeric)
""")

time_table_create = ("""create table if not exists time (start_time timestamp, hour numeric , day numeric, week numeric, month numeric, year numeric, weekday numeric)
""")

# INSERT RECORDS

songplay_table_insert = (""" Insert into songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
values (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" Insert into users (user_id, first_name, last_name, gender, level) \
values (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level = EXCLUDED.level\
""")

song_table_insert = ("""Insert into songs (song_id, title, artist_id, year, duration) \
values (%s, %s, %s, %s, %s) ON CONFLICT(song_id) DO NOTHING\
""")

artist_table_insert = ("""Insert into artists (artist_id, name, location, latitude, longitude) \
values (%s, %s, %s, %s, %s) ON CONFLICT(artist_id) DO NOTHING\
""")

time_table_insert = (""" Insert into time (start_time, hour, day, week, month, year, weekday) \
values (%s, %s, %s, %s, %s, %s, %s) \
""")

# FIND SONGS

song_select = (""" SELECT songs.song_id, artists.artist_id \
                            FROM songs \
                            JOIN artists ON songs.artist_id = artists.artist_id \
                            WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]