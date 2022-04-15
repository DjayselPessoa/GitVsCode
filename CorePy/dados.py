
class Dados:

    def dadosObtidos(self, dados):
        self.dados = dados
        self.dados += 10
        print("Processado: ", self.dados)
        return self.dados


ObjDados = Dados()
