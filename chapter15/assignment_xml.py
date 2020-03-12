# In this assignment you will parse an XML list of albums, artists, and Genres
# and produce a properly normalized database using a Python program.

import xml.etree.ElementTree as ET
import sqlite3

######## criando uma tabela usando SQL

#criei a base de dados 'musica_db'
conn = sqlite3.connect('musicas_db.sqlite')
cur = conn.cursor()

# criar uma tabela para cada item pedido em uma série de comandos SQL
# comecar com Artist e Genre, que só tem primary keys
#(create the ends of the arrows before you create the beginnings of the arrows)
# Próximos: Album e Track, que possuem foreing keys
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    artist_id INTEGER,
    album_id INTEGER,
    genre_id INTEGER
);
''')

#print('tabela criada!')

tracks_file = open('Library.xml')
xml = ET.parse('Library.xml')

#function to find the key values in the xml mess
#(imported from dr Chuck worked example)
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

xml_all = xml.findall('dict/dict/dict')

for entry in xml_all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, artist_id, album_id, genre_id)
        VALUES ( ?, ?, ?, ? )''',
        ( name, artist_id, album_id, genre_id) )

    conn.commit()

cur.executescript('''SELECT Track.title, Album.title, Genre.name, Artist.name
     FROM Track JOIN Album JOIN Genre JOIN Artist
     ON Track.album_id = Album.id
     AND Track.genre_id = Genre.id
	 AND Album.artist_id = Artist.id''')
