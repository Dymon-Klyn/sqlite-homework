import sqlite3

conn = sqlite3.connect('chinook.sqlite')
c = conn.cursor()

c.execute("INSERT INTO Artist(Name) VALUES('Bad Bunny')")
c.execute("INSERT INTO Album(Title, ArtistId) VALUES('YHLQMDLG', 276)")
c.execute('''INSERT INTO Track(Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
            VALUES('Safaera', 348, 1, 7, 'Bad Bunny, Nengo Flow and Jowell & Randy', 273000, 6760000, 1.29)''')

conn.commit()

conn.close()
