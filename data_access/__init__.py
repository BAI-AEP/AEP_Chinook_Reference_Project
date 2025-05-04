from datetime import date, datetime
import sqlite3

from .base_data_access import BaseDataAccess
from .artist_data_access import ArtistDataAccess
from .album_data_access import AlbumDataAccess
from .track_data_access import TrackDataAccess
from .genre_data_access import GenreDataAccess

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)
## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)
