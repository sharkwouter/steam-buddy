class App:
    def __init__(self, name: str, params, hidden: bool = False, banner: str = ""):
        self.name = name
        self.hidden = hidden
        self.banner = banner
        self.params = params
