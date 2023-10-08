class AlgorithmNotFound(Exception):
    def __init__(self):
        super().__init__(f"Algorithm not found in server, check the folder models")
        