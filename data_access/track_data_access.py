import model
from data_access.base_data_access import BaseDataAccess


class TrackDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_track(
            self,
            name: str,
            media_type: model.MediaType,
            milliseconds: int,
            unit_price: float,
            album: model.Album = None,
            genre: model.Genre = None,
            composer: str = None,
            track_bytes: int = None
    ) -> model.Track:
        if name is None:
            raise ValueError("Track name is required")
        if media_type is None:
            raise ValueError("Track media type is required")
        if milliseconds is None:
            raise ValueError("Track milliseconds is required")
        if unit_price is None:
            raise ValueError("Track unit price is required")

        sql = """
        INSERT INTO Track (Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = tuple([
            name,
            album.album_id if album else None,
            media_type.media_type_id,
            genre.genre_id if genre else None,
            composer if composer else None,
            milliseconds,
            track_bytes if track_bytes else None,
            unit_price
        ])

        last_row_id, row_count = self.execute(sql, params)

        return model.Track(
            track_id=last_row_id,
            name=name,
            album=album,
            media_type=media_type,
            genre=genre,
            composer=composer,
            milliseconds=milliseconds,
            track_bytes=track_bytes,
            unit_price=unit_price
        )

    def read_track_by_id(self, track_id: int) -> model.Track | None:
        if track_id is None:
            raise ValueError("Track id is required")

        sql = """
        SELECT 
            TrackId, 
            Name, 
            AlbumId, 
            MediaTypeId, 
            GenreId, 
            Composer, 
            Milliseconds, 
            Bytes, 
            UnitPrice
        FROM Track
        WHERE TrackId = ?
        """
        params = tuple([track_id])
        result = self.fetchone(sql, params)
        if result:
            (
                track_id,
                name,
                album_id,
                media_type_id,
                genre_id,
                composer,
                milliseconds,
                track_bytes,
                unit_price
            ) = result
            return model.Track(
                track_id,
                name,
                model.MediaType.from_id(media_type_id),
                milliseconds,
                unit_price,
                composer=composer,
                # TODO: genre = ...
                track_bytes=track_bytes
            )
        else:
            return None

    def read_tracks_by_album(self, album: model.Album) -> list[model.Track]:
        sql = """
        SELECT 
            TrackId, 
            Name, 
            AlbumId, 
            MediaTypeId, 
            GenreId, 
            Composer, 
            Milliseconds, 
            Bytes, 
            UnitPrice
        FROM Track WHERE AlbumId = ?
        """
        params = tuple([album.album_id])
        tracks = self.fetchall(sql, params)

        return [
            model.Track(
                track_id,
                name,
                model.MediaType.from_id(media_type_id),
                milliseconds,
                unit_price,
                album=album,
                composer=composer,
                # TODO: genre = ...
                track_bytes=track_bytes,
            )
            for (
                track_id,
                name,
                album_id,
                media_type_id,
                genre_id,
                composer,
                milliseconds,
                track_bytes,
                unit_price
            )
            in tracks
        ]
