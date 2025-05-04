import model
import data_access


class TrackManager:
    def __init__(self):
        self.__track_da = data_access.TrackDataAccess()

    def create_track(self,
                     name: str,
                     media_type: model.MediaType,
                     milliseconds: int,
                     unit_price: float,
                     album: model.Album = None,
                     genre: model.Genre = None,
                     composer: str = None,
                     track_bytes: int = None
                     ) -> model.Track:
        return self.__track_da.create_new_track(
            name=name,
            album=album,
            media_type=media_type,
            genre=genre,
            composer=composer,
            milliseconds=milliseconds,
            track_bytes=track_bytes,
            unit_price=unit_price
        )

    def read_track(self, track_id: int) -> model.Track:
        return self.__track_da.read_track_by_id(track_id)

    def read_tracks_by_album(self, album: model.Album) -> list[model.Track]:
        return self.__track_da.read_tracks_by_album(album)
