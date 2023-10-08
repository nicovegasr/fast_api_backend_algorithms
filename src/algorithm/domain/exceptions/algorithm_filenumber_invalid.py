class FileNumberInvalid(Exception):
    def __init__(self, filename: str):
        super().__init__(f'The file number of the file: {filename} is invalid')

        