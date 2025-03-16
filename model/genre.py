from __future__ import annotations
from typing import TYPE_CHECKING

import model

if TYPE_CHECKING:
    from model.artist import Artist
    from model.track import Track


class Genre:
    """
    Model Class Genre
    """


    def __init__(self, genre_id: int, name: str):
        # Ensure values for not nullable attributes
        if not genre_id:
            raise ValueError("genre_id is required")
        if not isinstance(genre_id, int):
            raise ValueError("genre_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")

        self.__genre_id = genre_id
        self.__name = name

    def __repr__(self):
        return f"Genre(id={self.__genre_id}, name={self.__name})"

    @property
    def genre_id(self):
        return self.__genre_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")
        self.__name = name
