class FilesEmpty(Exception):
    def __init__(self):
        super().__init__(f"The files of the algorithm are empty")
        