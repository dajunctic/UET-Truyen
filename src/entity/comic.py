import pyre_base
import os
import json

class Comic:
    # Function for interacting with JSON files.

    list_of_comics = dict()  # Static LOCAL dictionary of the comics.

    # Loads the contents from the comic's online Firebase into the local runtime dictionary.
    # YOU MUST ENSURE THAT THIS FUNCTION HAS BEEN CALLED WHEN THE APP RUNS!
    @classmethod
    def load_comic_list(cls):
        # with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="r", encoding="utf-8") as json_file:
        #     cls.list_of_comics = json.load(json_file)
        cls.update_local_comic_list()

    # This should be called after every update of the Firebase data;
    @classmethod
    def update_local_comic_list(cls):
        # pass
        cls.list_of_comics = dict(pyre_base.firebase.database().child("comics").get().val())

    # Saving the comics list.
    # @classmethod
    # def save_comic_list(cls):
    #     with open(os.path.join(os.getcwd(), "assets/data/data.json"), mode="w", encoding="utf-8") as json_file:
    #         json.dump(cls.list_of_comics, json_file, indent=4, ensure_ascii=False)
