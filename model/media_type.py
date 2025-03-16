from __future__ import annotations

from enum import Enum


class MediaType(Enum):
    """
    Model Class MediaType, represented by an Enumeration
    """

    MPEG = (1, "MPEG audio file")
    PROTECTED_AAC = (2, "Protected AAC audio file")
    PROTECTED_MPEG_4 = (3, "Protected MPEG-4 video file")
    PURCHASED_AAC = (4, "Purchased AAC audio file")
    AAC = (5, "AAC audio file")

    def __init__(self, media_type_id: int, name: str):
        self.__media_type_id = media_type_id
        self.__name = name

    @classmethod
    def build_lookup(cls) -> None:
        """Build lookup dictionaries for fast access"""
        cls._id_to_enum = {media.__media_type_id: media for media in cls}
        cls._name_to_enum = {media.__name: media for media in cls}

    @classmethod
    def from_id(cls, id_value: int) -> MediaType:
        """Get MediaType by ID"""
        value = cls._id_to_enum.get(id_value, None)
        return value  # Returns None if not found

    @classmethod
    def from_name(cls, name_value):
        """Get MediaType by Name"""
        return cls._name_to_enum.get(name_value, None)  # Returns None if not found

    @property
    def media_type_id(self):
        """Return the database ID for the media type"""
        return self.__media_type_id

    @property
    def name(self):
        """Return the database name for the media type"""
        return self.__name


# Build the lookup dictionaries once at class definition time
MediaType.build_lookup()
