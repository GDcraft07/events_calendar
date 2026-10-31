class Organization:
    def __init__(self, id: int, organization_name: str, color: tuple[int, int, int], password: str) -> None:
        self.id = id
        self.organization_name = organization_name
        self.events = []
        self.color = color
        self.password = password


    def add_event(self, event) -> None:
        self.events += [event]


    def get_attributes(self) -> dict:
        return {
            "id": self.id,
            "organization_name": self.organization_name, 
            "color": self.color,
            "password": self.password
        }
    