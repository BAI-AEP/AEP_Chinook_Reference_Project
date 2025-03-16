from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.artist import Artist
    from model.track import Track


# TODO: Explain on the slides how multiple objects work in
#  memory and why you might only should have one album of the actual album
class Album:
    """
    Model Class Album
    """

    def __init__(self, album_id: int, title: str, artist: Artist = None):
        # Ensure values for not nullable attributes
        if not album_id:
            raise ValueError("album_id is required")
        if not isinstance(album_id, int):
            raise ValueError("album_id must be an integer")
        if not title:
            raise ValueError("title is required")
        if not isinstance(title, str):
            raise ValueError("title must be an string")

        self.__album_id: int = album_id
        self.__title: str = title  # Private title attribute
        self.__artist: Artist = artist  # Private artist attribute
        if artist is not None:
            artist.add_album(self)
        self.__tracks: list[Track] = []

    def __repr__(self):
        return f"Album(id={self.__album_id!r}, title={self.__title!r}, artist={self.__artist!r})"

    @property
    def album_id(self) -> int:
        return self.__album_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if not title:
            raise ValueError("title is required")
        if not isinstance(title, str):
            raise ValueError("title must be an string")
        self.__title = title

    @property
    def artist(self) -> Artist:
        return self.__artist

    @artist.setter
    def artist(self, artist: Artist) -> None:
        from model import Artist
        if artist is not None and not isinstance(artist, Artist):
            raise ValueError("artist must be an instance of Artist")
        # Only do something if the artist is not already the same, prevents recursion!
        if self.__artist is not artist:
            if self.__artist is not None:
                self.__artist.remove_album(self)
            self.__artist = artist
            # TODO: Add comment here why we check for None (if we not actually delete the artist)
            if artist is not None and self not in artist.albums:
                artist.add_album(self)

    @property
    def tracks(self) -> list[Track]:
        # Return a copy so that the caller cannot modify the private list directly.
        return self.__tracks.copy()

    def add_track(self, track: Track) -> None:
        from model import Track

        if not track:
            raise ValueError("track is required")
        if not isinstance(track, Track):
            raise ValueError("track must be an instance of Track")
        if track not in self.__tracks:
            self.__tracks.append(track)
            track.album = self

    def remove_track(self, track: Track) -> None:
        from model import Track

        if not track:
            raise ValueError("track is required")
        if not isinstance(track, Track):
            raise ValueError("track must be an instance of Track")
        if track in self.__tracks:
            self.__tracks.remove(track)
            track.album = None
