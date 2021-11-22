class No:
	conteudo = 0
	bin = ""
	def __init__(self, conteudo, freq, bin, left, right):
		self.conteudo = conteudo
		self.freq = freq
		self.bin = bin
		self.left = left
		self.right = right

	def __repr__(self):
		return repr((self.conteudo, self.freq, self.bin))

	def isLeaf(self):
		return self.left is None and self.right is None