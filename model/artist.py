from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.album import Album


class Artist:
    """
    Model Class Artist
    """

    def __init__(self, artist_id: int, name: str):
        # Ensure values for not nullable attributes
        if not artist_id:
            raise ValueError("artist_id is required")
        if not isinstance(artist_id, int):
            raise ValueError("artist_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")

        self.__artist_id: int = artist_id
        self.__name: str = name
        self.__albums: list[Album] = []

    def __repr__(self):
        return f"Artist(id={self.__artist_id!r}, name={self.__name!r})"

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")
        self.__name = name

    @property
    def albums(self) -> list[Album]:
        # Return a copy so that the caller cannot modify the private list directly.
        return self.__albums.copy()

    def add_album(self, album: Album) -> None:
        """
        Adds an album to this artist's album list.
        Also sets the album's artist to this artist.
        """
        from model import Album

        if not album:
            raise ValueError("album is required")
        if not isinstance(album, Album):
            raise ValueError("album must be an instance of Album")
        if album not in self.__albums:
            self.__albums.append(album)
            album.artist = self

    def remove_album(self, album: Album) -> None:
        """
        Removes an album from this artist's album list.
        Also clears the album's artist.
        """
        from model.album import Album

        if not album:
            raise ValueError("album is required")
        if not isinstance(album, Album):
            raise ValueError("album must be an instance of Album")
        if album in self.__albums:
            self.__albums.remove(album)
            album.artist = None
