import pickle
import os

class database_interface():

    def __init__(self, pickle_file_name = "rock_paper_scissors.pkl"):
        self.file_name = pickle_file_name

    def store(self, data_to_store):
        file_to_use = open(self.file_name, "wb")
        pickle.dump(data_to_store, file_to_use)
        file_to_use.close()

    def read(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "rb") as file_to_use:
                data = pickle.load(file_to_use)
        else: 
            data = {}
        return data
