class HuffmanTree:

	def navegar(self,no):
		if no is None: return

		if no.left is not None: self.navegar(no.left)

		if no.isLeaf(): print (no)

		if no.right is not None: self.navegar(no.right)

		return

	def codifica(self,no):
					
			if no is None: return

			if no.left is not None:
				no.left.bin = no.bin +'1'
				self.codifica(no.left)

			if no.right is not None:
				no.right.bin = no.bin + '0'
				self.codifica(no.right)

			return


	def getTextBin(self,arv,texto):
							
		result = ''
		for letter in texto:
			result += self.getBinLetter(arv,letter) 
		
		
		return result

	def getBinLetter(self,arv,letter):

		bin = ''

		if arv.conteudo == letter:
			bin = arv.bin

		if arv.left is not None: bin = self.getBinLetter(arv.left,letter)

		if bin == '':
			if arv.right is not None: bin = self.getBinLetter(arv.right,letter)

		return bin

	def arvToBin(self,arv):
		result = ''

		if arv is None: return

		if arv.left is None and arv.right is None:
			result += arv.conteudo

		if arv.left is not None: result += '1'+ self.arvToBin(arv.left)

		if arv.right is not None: result += '0'+ self.arvToBin(arv.right)

		return result

	

	def decodeBin(self,arv,textBin):
		arvore = arv
		result =''
		for bin in textBin:
			if bin == '1':
				if arvore.left is not None:
					arvore = arvore.left
					if arvore.left is None and arvore.right is None:
					
						result += (arvore.conteudo)		
						arvore = arv
			else:
				if arvore.right is not None:
					arvore = arvore.right
					if arvore.left is None and arvore.right is None:
					
						result += (arvore.conteudo)	
						arvore = arv

		return result
