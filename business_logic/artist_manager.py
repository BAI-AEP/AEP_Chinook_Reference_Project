import os

import pandas as pd

import model
import data_access

class ArtistManager:
    def __init__(self):
        self.__artist_da = data_access.ArtistDataAccess()

    def create_artist(self, name: str):
        return self.__artist_da.create_new_artist(name)

    def read_artist(self, artist_id: int):
        return self.__artist_da.read_artist_by_id(artist_id)

    def read_all_artists(self) -> list[model.Artist]:
        return self.__artist_da.read_all_artists()

    def read_all_artists_as_df(self) -> pd.DataFrame:
        return self.__artist_da.read_all_artists_as_df()

    def read_artists_by_similar_name(self, name: str) -> list[model.Artist]:
        return self.__artist_da.read_artists_like_name(name)

    def read_artists_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
        return self.__artist_da.read_artists_like_name_as_df(name)

    def update_artist(self, artist: model.Artist) -> None:
        self.__artist_da.update_artist(artist)

    def delete_artist(self, artist: model.Artist) -> None:
        self.__artist_da.delete_artist(artist)

