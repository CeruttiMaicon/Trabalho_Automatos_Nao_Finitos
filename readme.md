# AFN

Na Teoria dos autômatos, um sub-tópico da Ciência da computação teórica, um autômato finito determinístico — também chamado máquina de estados finita determinística (AFD) — é uma Máquina de estados finita que aceita ou rejeita cadeias de símbolos gerando um único ramo de computação para cada cadeia de entrada. "Determinística" refere-se à unicidade do processamento. O primeiro conceito similar ao de autômatos finitos foi apresentado por McCulloch e Pitts em 1943. Modelo esse que foi produzido na busca por estruturas mais simples para a reprodução de máquinas de estado finitas.

A figura à direita representa um autômato finito determinístico através de um Diagrama de transição de estados. Nesse autômato há três estados: S0, S1 e S2 (representados graficamente por círculos). A entrada é constituída por uma sequência finita de caracteres 1s e 0s. Para cada estado da máquina, existe um arco de transição levando a um outro estado para ambos caracteres 0 e 1. Isso significa que, em um dado estado, após a leitura de cada símbolo a máquina determinística transita para um único estado referente à aresta associada ao símbolo. Por exemplo, esteja o autômato atualmente no estado S0 e o símbolo de entrada para aquela instância um 1, então ele salta deterministicamente para o estado S1. Todo AFD possui um estado inicial (denotado graficamente por uma seta de origem anônima) onde a sua computação começa e um conjunto de estados de aceitação (denotados graficamente por um círculo de borda dupla) o qual indica a aceitação da cadeia de entrada.

Um Autômato finito determinístico é normalmente definido como um conceito matemático abstrato, mas devido à seu fator determinístico, ele pode ser implementado através de Hardware e Software para resolver diversos problemas específicos. Por instância, DFAs são utilizados para modelar softwares que validam entradas de usuário tal como o seu e-mail em um servidor de correio eletrônico.

AFDs reconhecem exatamente o conjunto de Linguagens Regulares que são, dentre outras coisas, úteis para a realização de Análise lexica e reconhecimento de padrões. Uma AFD pode ser construído a partir de um Autômato finito não determinístico através de uma Construção do conjunto das partes.


## Algoritmo

O algoritmo em si deve ler uma entrada em um arquivo (arquivos/ler/entrada_automotos), e com base nele fazer toda uma sequencia de eventos conforme o estado inicial do automato permitir proeguir. É o estado do automoto que delimita a proxima função do algoritmo conforme as entradas são lidas.

O algoritmo ao final do procecedimento deve retornar um arquivo com as saidas dos estados de cada etapa percorria com os dados de entrada, e nele deve conter se o estado do algoritmo é "ACEITO" ou "REJEITADO".