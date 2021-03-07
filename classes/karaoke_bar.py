class KaraokeBar:

    def __init__(self, name, rooms, till, entry_fee):
        self.name = name
        self.rooms = rooms
        self.till = till
        self.entry_fee = entry_fee

    def charge_guest_entry_fee(self, guest):
        guest.wallet -= self.entry_fee
        self.till += self.entry_fee

    def add_guest_to_room(self, room, guest):
        room.guests.append(guest)

    def check_out_guest(self, room, guest):
        room.guests.remove(guest)

# Checks whether guest can afford entry, and whether the room has space. If they can takes money and assigns them to the room
    def check_in_guest(self, room, guest):
        if guest.wallet < self.entry_fee:
            return "Guest can't afford entry"

        if room.capacity - len(room.guests) == 0:
            return "Room is full"

        self.charge_guest_entry_fee(guest)
        self.add_guest_to_room(room, guest)
        