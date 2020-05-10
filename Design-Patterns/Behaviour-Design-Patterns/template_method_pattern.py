import abc


class DataMining:
    def __init__(self, path: str):
        self.path = path

    def analyze_document(self):
        pass

    def send_report(self):
        pass

    @abc.abstractmethod
    def open_document(self):
        pass

    @abc.abstractmethod
    def extract_data(self):
        pass

    @abc.abstractmethod
    def parse_data(self):
        pass

    @abc.abstractmethod
    def close_file(self):
        pass

    # template method responsible for the step by step execution of algorithm
    def mine_data(self):
        self.open_document()
        self.extract_data()
        self.parse_data()
        self.analyze_document()
        self.send_report()
        self.close_file()


class PdfMining(DataMining):

    def open_document(self):
        pass

    def extract_data(self):
        pass

    def parse_data(self):
        pass

    def close_file(self):
        pass

# Client Interface


pdf_mining = PdfMining(path="asds")
pdf_mining.mine_data()
