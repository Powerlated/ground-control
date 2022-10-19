class Plugin:
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        print(f'initialized {self.identifier}')
