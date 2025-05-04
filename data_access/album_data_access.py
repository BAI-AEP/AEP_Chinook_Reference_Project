from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class AlbumDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_album(self, title: str, artist: model.Artist = None) -> model.Album:
        sql = """
        INSERT INTO Album (Title, ArtistId) VALUES (?, ?)
        """
        params = (
            title,
            artist.artist_id if artist else None,
        )

        last_row_id, row_count = self.execute(sql, params)
        return model.Album(last_row_id, title, artist)

    def read_album_by_id(self, album_id: int) -> model.Album | None:
        sql = """
        SELECT AlbumId, Title FROM Album WHERE AlbumId = ?
        """
        params = tuple([album_id])
        result = self.fetchone(sql, params)
        if result:
            album_id, title = result
            return model.Album(album_id, title)
        else:
            return None

    def read_albums_by_artist(self, artist: model.Artist) -> list[model.Album]:
        sql = """
        SELECT AlbumId, Title FROM Album WHERE ArtistId = ?
        """
        if artist is None:
            raise ValueError("Artist can not be None")

        params = tuple([artist.artist_id])
        albums = self.fetchall(sql, params)
        return [
            model.Album(album_id, title, artist)
            for album_id, title in albums
        ]
