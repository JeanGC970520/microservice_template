class Name:
    def __init__(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty")
        self.value = value
