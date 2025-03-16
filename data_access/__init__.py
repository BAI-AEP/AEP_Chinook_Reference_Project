from datetime import date, datetime
import sqlite3

from .base_dal import BaseDal
from .artist_dal import ArtistDAL
from .album_dal import AlbumDAL
from .track_dal import TrackDAL
from .genre_dal import GenreDal

# Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, lambda d: d.isoformat())

# Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", lambda s: datetime.strptime(s.decode(), "%Y-%m-%d").date())
