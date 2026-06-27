"""
Modulo que incluye la clase de reproductor
de Musica
"""


class Player:
    """
    Esta clase crea un
    reproductor de mp3
    """

    def play(self, song):
        """
        Reproduce la cancion que
        recibio en el constructor

        Parameters:
        song(str):String con el parametro de la musica

        Returns:
        int: Devuelve 1 si reproduce con exito, de lo contrario es 0
        """
        print("Reproduciendo musica")

    def stop(self):
        print("Deteniendo")
