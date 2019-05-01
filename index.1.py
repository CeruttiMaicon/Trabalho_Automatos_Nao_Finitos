

class DFA():
    def __init__(self):
        self.numeroDeEstados='3'
        self.numberOfaplhabets='2'
        self.numberOfFinalStates='1'
        self.firstState='0'
        self.finalState='2'
        self.alphabets=['0','1']
        self.dfa=[[0 for x in range(int(self.numberOfaplhabets))] for y in range(int(self.numeroDeEstados))]
        self.dfa=[ ['1','0'], ['1','2'], ['2','2']]


    def setDfa(self):
        self.numeroDeEstados=4
        self.numberOfaplhabets=2
        self.numberOfFinalStates=1
        self.firstState='q1'
        self.finalState='4'

        entrada_automotos = open('arquivos/ler/entrada_automotos.txt', 'r')
        for linha in entrada_automotos:
            self.alphabets=[0 for x in range(int(self.numberOfaplhabets))]
            for i in range(0, int(self.numberOfaplhabets)):
                self.alphabets[i]= linha
    
        self.dfa=[[0 for x in range(int(self.numberOfaplhabets))] for y in range(int(self.numeroDeEstados))]

        print("Enter Transition Table")
        for i in range(0,int(self.numeroDeEstados)):
            for j in range(0, int(self.numberOfaplhabets)):
                self.dfa[i][j]=input("(q"+str(i)+","+str(j)+")--> q")


    def setDfaParam(self,ns,na,nf,fs,ff,a,d):
        self.numeroDeEstados=ns
        self.numberOfaplhabets=na
        self.numberOfFinalStates=nf
        self.firstState=fs
        self.finalState=ff
        self.alphabets=a
        self.dfa=d



    def showTupleSet(self):
        print("===========================================")
        print("                 TUPLE SET                 ")
        print("===========================================")
        print("Aplhabets:")
        for i in range(0, int(self.numberOfaplhabets)):
            print(self.alphabets[i]),
        print("\n")

        print("States:")
        for i in range(0, int(self.numeroDeEstados)):
            print("q"+str(i)+" "),
        print("\n")

        print("Transitions:")
        arquivo = open('arquivos/ler/saida_automotos.txt','w')
        for i in range(0,int(self.numeroDeEstados)):
            for j in range(0, int(self.numberOfaplhabets)):
                arquivo.write("(q"+str(i)+","+str(j)+")--> q"+str(self.dfa[i][j])+"\n")

        arquivo.write("\nFirst State: q0")
        arquivo.write("\nFinal State: q"+str(self.finalState))
        arquivo.write("\nQxE->Q\n\n")
        

if __name__ == "__main__":
    dfaObj=DFA()
    i = True
    while (i):
        print("================= AFN ==================setDfa==")
        dfaObj.setDfa()
        dfaObj.showTupleSet()
        i = False
        
       

