import model
from data_access.base_data_access import BaseDataAccess
from model import Genre, genre


class GenreDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_genre(self, genre_id: int) -> model.Genre:
        pass

    def read_genre_by_name(self, genre_name: str) -> model.Genre | None:
        sql = """
        SELECT GenreId, Name FROM Genre WHERE Name = ?
        """
        params = tuple([genre_name])

        result = self.fetchone(sql, params)
        if result:
            genre_id, name = result
            return Genre(genre_id, name)
        else:
            return None

    def read_all_genre(self) -> list[model.Genre]:
        sql = """
        SELECT GenreId, Name FROM Genre ORDER BY GenreId
        """

        genres = self.fetchall(sql)
        return [
            Genre(genre_id, genre_name)
            for genre_id, genre_name in genres
        ]

