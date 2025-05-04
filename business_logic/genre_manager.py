import os

import model
import data_access

class GenreManager:
    def __init__(self):
        self.__genre_da = data_access.GenreDataAccess()

    def read_genre_by_name(self, genre_name: str) -> model.Genre | None:
        return self.__genre_da.read_genre_by_name(genre_name)

    def read_all_genre(self) -> list[model.Genre]:
        return self.__genre_da.read_all_genre()




