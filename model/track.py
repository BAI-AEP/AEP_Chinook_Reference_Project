from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.album import Album
    from model.media_type import MediaType
    from model.genre import Genre


class Track:
    """
    Model Class Track
    """


    def __init__(
            self,
            track_id: int,
            name: str,
            media_type: MediaType,
            milliseconds: int,
            unit_price: float,
            album: Album = None,
            genre: Genre = None,
            composer: str = None,
            track_bytes: int = None,
    ):
        from model import Album, Genre, MediaType  # explicit import types in this constructor.
        # Ensure values for not nullable attributes
        if not track_id:
            raise ValueError("track_id is required")
        if not isinstance(track_id, int):
            raise TypeError("track_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise TypeError("name must be an string")
        if not media_type:
            raise ValueError("media_type is required")
        if not isinstance(media_type, MediaType):
            raise TypeError("media_type must be an instance of MediaType")
        if not milliseconds:
            raise ValueError("milliseconds is required")
        if not isinstance(milliseconds, int):
            raise TypeError("milliseconds must be an integer")
        if not unit_price:
            raise ValueError("unit_price is required")
        if not isinstance(unit_price, float):
            raise TypeError("unit_price must be an float")

        if album is not None and not isinstance(album, Album):
            raise TypeError("album must be an instance of Album")
        if genre is not None and not isinstance(genre, Genre):
            raise TypeError("genre must be an instance of Genre")
        if composer is not None and not isinstance(composer, str):
            raise TypeError("composer must be an string")
        if track_bytes is not None and not isinstance(track_bytes, int):
            raise TypeError("track_bytes must be an integer")

        self.__track_id: int = track_id
        self.__name: str = name
        self.__media_type: MediaType = media_type
        self.__milliseconds: int = milliseconds
        self.__unit_price: float = unit_price
        self.__album: Album = album
        if album is not None:
            album.add_track(self)
        self.__genre: Genre = genre
        self.__composer: str = composer
        self.__track_bytes: int = track_bytes

    def __repr__(self):
        return (f"Track(id={self.__track_id!r}, name={self.__name!r}, album={self.__album!r}, "
                f"media_type={self.__media_type!r}, genre={self.__genre!r}, composer={self.__composer!r}, "
                f"milliseconds={self.__milliseconds!r}, bytes={self.__track_bytes!r}, unit_price={self.__unit_price!r})")

    @property
    def track_id(self) -> int:
        return self.__track_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise TypeError("name must be an string")
        self.__name = name

    @property
    def media_type(self) -> MediaType:
        return self.__media_type

    @media_type.setter
    def media_type(self, media_type: MediaType) -> None:
        if not media_type:
            raise ValueError("media_type is required")
        if not isinstance(media_type, MediaType):
            raise TypeError("media_type must be an instance of MediaType")
        self.__media_type = media_type

    @property
    def genre(self) -> Genre:
        return self.__genre

    @genre.setter
    def genre(self, genre: Genre) -> None:
        if genre is not None and not isinstance(genre, Genre):
            raise TypeError("genre must be an instance of Genre")
        self.__genre = genre

    @property
    def album(self) -> Album:
        return self.__album

    @album.setter
    def album(self, album: Album) -> None:
        """
        Sets the album for this track.
        Also adds this track to the album's track list if it isn't already present.
        If the track already belonged to a different album, it removes itself from that album.
        Passing `None` as the album clears the current album.
        """
        from model import Album  # explicit import types in this method.
        if album is not None and not isinstance(album, Album):
            raise TypeError("album must be an instance of Album")

        if self.__album is not album:
            if self.__album is not None:
                self.__album.remove_track(self)
            self.__album = album

            if album is not None and self not in album.tracks:
                album.add_track(self)

    @property
    def composer(self) -> str:
        return self.__composer

    @composer.setter
    def composer(self, composer: str) -> None:
        if composer is not None and not isinstance(composer, str):
            raise TypeError("composer must be an string")
        self.__composer = composer

    @property
    def milliseconds(self) -> int:
        return self.__milliseconds

    @milliseconds.setter
    def milliseconds(self, milliseconds: int) -> None:
        if not milliseconds:
            raise ValueError("milliseconds is required")
        if not isinstance(milliseconds, int):
            raise TypeError("milliseconds must be an integer")
        self.__milliseconds = milliseconds

    @property
    def track_bytes(self) -> int:
        return self.__track_bytes

    @track_bytes.setter
    def track_bytes(self, track_bytes: int) -> None:
        if track_bytes is not None and not isinstance(track_bytes, int):
            raise TypeError("track_bytes must be an integer")
        self.__track_bytes = track_bytes

    @property
    def unit_price(self) -> float:
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, unit_price: float) -> None:
        if not unit_price:
            raise ValueError("unit_price is required")
        if not isinstance(unit_price, float):
            raise TypeError("unit_price must be a float")
        self.__unit_price = unit_price

