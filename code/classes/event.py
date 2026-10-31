class Event:
    def __init__(self, venue, organization, day, start_id: int, end_id: int, event_name: str, bio: str) -> None:
        self.venue = venue
        self.organization = organization
        self.day = day
        self.start_id = start_id
        self.end_id = end_id
        self.event_name = event_name
        self.bio = bio

        self.venue.add_event(self)
        self.organization.add_event(self)
        self.day.add_event(self)


    def add_event_in_mask(self, mask: list) -> list:
        mask[self.start_id:self.end_id] = [self.organization.id] * (self.end_id - self.start_id + 1)
        return mask


    def get_attributes(self) -> dict:
        return {
            "venue": self.venue.id,
            "organization": self.organization.id,
            "day": self.day.id,
            "start_id": self.start_id,
            "end_id": self.end_id,
            "event_name": self.event_name,
            "bio": self.bio
        }