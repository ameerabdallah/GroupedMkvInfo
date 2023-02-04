class TrackInfo:
    id: int = -1
    name: str = ""
    lang: str = ""
    type: str = ""

    def __init__(self, id: int, name: str, lang: str, type: str):
        self.id = id
        self.name = name
        self.lang = lang
        self.type = type

    def __hash__(self):
        return hash((self.id, self.name, self.lang, self.type))
    
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.lang == other.lang and self.type == other.type
    
    def __str__(self):
        return "["+ self.type + " track];  id: " + str(self.id) + ", name: " + str(self.name) + ", lang: " + str(self.lang)
