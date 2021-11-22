from No import No

class ListaNos:

	raiz = 0
	texto = ''

	def __init__(self, lista):
		self.texto = lista

	def insereRaiz(self, novo):
		self.raiz = [novo] 
		return

	def insere(self, novo):
		
		for item in self.raiz:
			if item.conteudo == novo.conteudo:
				item.freq += 1				
				self.raiz = sorted(self.raiz, key=lambda no: no.freq)
				return						

		self.raiz += [novo]				
		self.raiz= sorted(self.raiz, key=lambda no: no.freq)
		
		return

	def criaLista(self):
		for letter in self.texto:
			if self.raiz == 0:							
															

				self.insereRaiz(No(letter,1,'', None, None))

			
			else: 
														
				self.insere(No(letter,1,'', None, None))

			
		return

	def printLista(self):
		for tup in self.raiz:
			print (tup)
		return

	def criaArv(self):
		
		self.criaLista()

		while len(self.raiz)>1:

			novo= No("",self.raiz[0].freq + self.raiz[1].freq,'',self.raiz[0],self.raiz[1])
			
			del self.raiz[0]
			del self.raiz[0]

			self.raiz += [novo]
			self.raiz = sorted(self.raiz, key=lambda no: no.freq)

		return