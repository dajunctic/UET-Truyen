from src.entity.comic import *
from src.entity.comic_modules.comic_getter import *
from datetime import datetime


# Functions for querying and searching the comic database
class ComicQuery:
    # Returning a list of Comic IDs whose types have an entry matching with that of the parameter.
    @classmethod
    def query_comics_of_category(cls, category_name):
        return [comic_id for comic_id in Comic.list_of_comics
                if category_name in Comic.list_of_comics[comic_id]["type"]]

    # Returning a list of Comic IDs whose names matches the search query.
    @classmethod
    def query_comics_of_author_name(cls, author_name):
        return [comic_id for comic_id in Comic.list_of_comics
                if Comic.list_of_comics[comic_id]["name"] == author_name]

    # Returns a list of Comic IDs sorted by recency
    # Leaving the comic_list parameter alone will return the entire catalogue of stories
    @classmethod
    def sort_comics_on_recency(cls, comic_list=None, return_count=None):
        if comic_list is None:
            comic_list = []

        comic_recency_list = []

        if len(comic_list) == 0:
            for comic_id in Comic.list_of_comics:
                comic_recency_list.append(
                    [
                        str(comic_id),
                        ComicGetters.get_comic_last_updated_date(str(comic_id))
                        # datetime.fromisoformat(Comic.list_of_comics[str(comic_id)]["last_updated"])
                    ]
                )
        else:
            for comic_id in comic_list:
                comic_recency_list.append(
                    [
                        str(comic_id),
                        ComicGetters.get_comic_last_updated_date(str(comic_id))
                    ]
                )

        comic_recency_list.sort(key=lambda listo: listo[1], reverse=True)

        if return_count is not None:
            return comic_recency_list[:return_count]
        return comic_recency_list
