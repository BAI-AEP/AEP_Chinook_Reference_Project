from unittest import result

import pandas as pd

import model
from data_access.base_data_access import BaseDataAccess


class ArtistDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_artist(self, name: str) -> model.Artist:
        if name is None:
            raise ValueError("Artist name is required")

        sql = """
        INSERT INTO Artist (Name) VALUES (?)
        """
        params = tuple([name])
        last_row_id, row_count = self.execute(sql, params)
        return model.Artist(artist_id=last_row_id, name=name)

    def read_artist_by_id(self, artist_id: int) -> model.Artist | None:
        if artist_id is None:
            raise ValueError("ArtistId is required")

        sql = """
        SELECT ArtistId, Name FROM Artist WHERE ArtistId = ?
        """
        params = tuple([artist_id])
        result = self.fetchone(sql, params)
        if result:
            artist_id, name = result
            return model.Artist(artist_id=artist_id, name=name)
        else:
            return None

    def read_all_artists(self) -> list[model.Artist]:
        sql = """
        SELECT ArtistId, Name FROM Artist
        """
        artists = self.fetchall(sql)

        return [model.Artist(artist_id=artist_id, name=name) for artist_id, name in artists]

    def read_all_artists_as_df(self) -> pd.DataFrame:
        sql = """
        SELECT ArtistId, Name FROM Artist
        """
        return pd.read_sql(sql, self._connect(), index_col='ArtistId')

    def read_artists_like_name(self, name: str) -> list[model.Artist]:
        sql = """
        SELECT ArtistId, Name FROM Artist WHERE Name LIKE ?
        """
        params = tuple([f"%{name}%"])
        artists = self.fetchall(sql, params)
        return [model.Artist(artist_id=artist_id, name=name) for artist_id, name in artists]

    def read_artists_like_name_as_df(self, name: str) -> pd.DataFrame:
        sql = """
                SELECT ArtistId, Name FROM Artist WHERE Name LIKE ?
                """
        params = tuple([f"%{name}%"])
        return pd.read_sql(sql, self._connect(), params=params, index_col='ArtistId')

    def update_artist(self, artist: model.Artist) -> None:
        if artist is None:
            raise ValueError("Artist cannot be None")

        sql = """
        UPDATE Artist SET Name = ? WHERE ArtistId = ?
        """
        params = tuple([artist.name, artist.artist_id])
        last_row_id, row_count = self.execute(sql, params)

    def delete_artist(self, artist: model.Artist) -> None:
        if artist is None:
            raise ValueError("Artist cannot be None")

        sql = """
        DELETE FROM Artist WHERE ArtistId = ?
        """
        params = tuple([artist.artist_id])
        last_row_id, row_count = self.execute(sql, params)
