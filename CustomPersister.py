from main import SCRAPPED_FILE
from storage import Persistor


class CustomPersister(Persistor):

    def read_raw_data(self):
        pass

    def save_raw_data(self, data):
        raw_data_file = open(SCRAPPED_FILE, 'w')
        raw_data_file.write(data)
        raw_data_file.close()
        pass

    def save_csv(self, data):
        pass

    def append_data(self, data):
        pass