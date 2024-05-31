class Figurita:
    def __init__(self, pais_j, num_j, nom_j, pos_j, valor_fig):
        self.pais = pais_j
        self.numero = num_j
        self.nombre = nom_j
        self.posicion = pos_j
        self.valor = valor_fig

    def __str__(self):
        return f'| Pais del jugador: {self.pais} | Numero del jugador: {self.numero} | Nombre del jugador: {self.nombre} ' \
            f'| Posicion del jugador: {self.posicion} | Valor de canje de la figurita: {self.valor} |'