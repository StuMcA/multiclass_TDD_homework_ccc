class KaraokeBar:

    def __init__(self, name, rooms, till, entry_fee):
        self.name = name
        self.rooms = rooms
        self.till = till
        self.entry_fee = entry_fee

    def fail_affordability_check(self, room, guest):
        return guest.wallet < self.entry_fee

    def fail_space_check(self, room, guest):
        return room.capacity - len(room.guests) == 0

    def charge_guest_entry_fee(self, guest):
        guest.wallet -= self.entry_fee
        self.till += self.entry_fee

    def add_guest_to_room(self, room, guest):
        room.guests.append(guest)

    def check_out_guest(self, room, guest):
        room.guests.remove(guest)

# Checks whether guest can afford entry, and whether the room has space. If they can takes money and assigns them to the room
    def check_in_guest(self, room, guest):

        if self.fail_affordability_check(room, guest):
            return "Guest can't afford entry"

        if self.fail_space_check(room, guest):
            return "Room is full"

        self.charge_guest_entry_fee(guest)
        self.add_guest_to_room(room, guest)

        # Checks whether favourite song is in room playlist
        for song in room.playlist:
            if guest.favourite_song.name == song.name and guest.favourite_song.artist == song.artist:
                return "Yaasss! Belter!"
        