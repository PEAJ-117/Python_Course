class Coordinates:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    # Igualdad

    def __eq__(self, other):
        return self.lat == other.lat and self.lon == other.lon
    # Negacion de igualdad

    # def __ne__(self, other):
    #    return self.lat != other.lat or self.lon != other.lon
    # Menor que

    def __lt__(self, other):
        return self.lat + self.lon < other.lat + other.lon
    # Menor o igual que

    def __le__(self, other):
        return self.lat + self.lon <= other.lat + other.lon


coord = Coordinates(37, 122)
coord2 = Coordinates(137, 122)
# print(coord == coord2)
# print(coord != coord2)
# print(coord < coord2)
# print(coord > coord2)
# print(coord <= coord2)
# print(coord >= coord2)

print(coord, coord2)
