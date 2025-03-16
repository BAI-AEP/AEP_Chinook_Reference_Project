import os

import model
import data_access

class GenreManager:
    def __init__(self):
        self.__genre_dal = data_access.GenreDal()

    def read_genre_by_name(self, genre_name: str) -> model.Genre | None:
        return self.__genre_dal.read_genre_by_name(genre_name)

    def read_all_genre(self) -> list[model.Genre]:
        return self.__genre_dal.read_all_genre()




