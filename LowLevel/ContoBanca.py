class ContoCorrente:
    def __init__ (self, nome, conto, importo):
        self.__privNome = nome
        self.__privConto = conto
        self.__privSaldo = importo
    
    def preleva(self, importo):
        if( not importo > self.__privSaldo ):
            self.__privSaldo -= importo
        else:
            print("Importo non disponibile!")
    
    def deposita(self, importo):
        self.__privSaldo += importo
    
    def descrizione(self):
        print("Nome titolare: ", self.__privNome, ", Conto: ", self.__privConto, ", Saldo: ", self.__privSaldo, end="\n\n")

rossi = ContoCorrente("Rossi", "1012", 2000)
verdi = ContoCorrente("Verdi", "1023", 2000)

rossi.deposita(1000)
verdi.preleva(200)

rossi.descrizione()
verdi.descrizione()