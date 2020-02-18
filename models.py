class Evento:
	def __init__(self, nome, data_inicio, data_fim, id=None):
		self.id = id
		self.nome = nome
		self.data_inicio = data_inicio
		self.data_fim = data_fim
