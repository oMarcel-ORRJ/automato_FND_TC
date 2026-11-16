print()
print("==============================================")
print("        PROJETO BIMESTRAL")
print("  AUTOMATO FINITO DETERMINISTICO")
print("==============================================")
print(" ALUNO: MARCELO ROBERTO ROSA JUNIOR")
print(" RA: 05223-018")
print(" CURSO: ENGENHARIA DE COMPUTACAO")
print(" PROFESSOR: ME. SAULO SAVIO LEITE SANTOS")
print("==============================================")
print()

class AutomatoFinitoDeterministico:
    def __init__(self, estados, alfabeto, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estado_atual = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def transicao(self, entrada):
        self.estado_atual = self.transicoes[self.estado_atual][entrada]

    def checa_simbolos(self, palavra):
        self.estado_atual = self.estado_inicial
        caminho = [self.estado_atual]

        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False, caminho, simbolo

            self.transicao(simbolo)
            caminho.append(self.estado_atual)

        resultado = self.estado_atual in self.estados_finais

        return resultado, caminho, None


# ESCOLHA DO MODO DE FUNCIONAMENTO ====================================================================================================================================================

print("===================================")
print("  CONSTRUTOR DE AUTOMATO FINITO")
print("===================================")

print("\nEscolha o modo de funcionamento:")
print("1 - Preenchimento manual")
print("2 - Executar teste automatico")

while True:
    modo = input("\nOpcao: ").strip()

    if modo == "1" or modo == "2":
        break

    print("Opcao invalida. Escolha 1 ou 2.")


# CONFIGURACAO AUTOMATICA =============================================================================================================================================================

if modo == "2":

    print("\n===================================")
    print("       TESTE AUTOMATICO")
    print("===================================")

    estados = ["q0", "q1", "q2", "q3", "q4", "q5"]
    alfabeto = ["0", "1"]
    estado_inicial = "q0"
    estados_finais = ["q5"]

    transicoes = {
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q2", "1": "q1"},
        "q2": {"0": "q0", "1": "q3"},
        "q3": {"0": "q2", "1": "q4"},
        "q4": {"0": "q5", "1": "q1"},
        "q5": {"0": "q5", "1": "q5"}
    }

    testes = [
        "10110",
        "001011011",
        "1110101100",
        "1011",
        "111000",
        "0001011",
        "101102"
    ]


# CONFIGURACAO MANUAL =================================================================================================================================================================

else:

    print("\n===================================")
    print("       CONSTRUCAO MANUAL")
    print("===================================")

    while True:
        estados = input("\nInforme os estados: ").split()

        if len(estados) > 0 and len(set(estados)) == len(estados):
            break

        print("Informe estados validos, sem repeticoes.")

    while True:
        entrada = input("Informe o alfabeto: ").strip()
        alfabeto = list(entrada.replace(" ", ""))

        if len(alfabeto) > 0 and len(set(alfabeto)) == len(alfabeto):
            break

        print("Informe simbolos diferentes e validos.")

    estado_inicial = input("Informe o estado inicial: ").strip()

    while estado_inicial not in estados:
        print("Esse estado nao existe.")
        estado_inicial = input("Informe novamente o estado inicial: ").strip()

    while True:
        entrada = input("Informe os estados finais: ").strip()

        if entrada == "-":
            estados_finais = []
            break

        estados_finais = entrada.split()
        invalidos = []

        for estado in estados_finais:
            if estado not in estados:
                invalidos.append(estado)

        if len(estados_finais) > 0 and len(invalidos) == 0:
            break

        print("Um ou mais estados informados nao existem.")

    print("\n===================================")
    print("       CONFIGURANDO TRANSICOES")
    print("===================================")

    transicoes = {}

    for estado in estados:
        transicoes[estado] = {}

        for simbolo in alfabeto:
            destino = input(
                "Destino de " + estado + " ao ler " + simbolo + ": "
            ).strip()

            while destino not in estados:
                print("O estado informado nao existe.")
                destino = input("Informe novamente o destino: ").strip()

            transicoes[estado][simbolo] = destino


# CRIACAO DO AUTOMATO =================================================================================================================================================================

automato = AutomatoFinitoDeterministico(
    estados,
    alfabeto,
    estado_inicial,
    estados_finais,
    transicoes
)


# EXIBICAO DOS PARAMETROS =============================================================================================================================================================

print("\n===================================")
print("       AUTOMATO CONFIGURADO")
print("===================================")

if modo == "2":
    print("Objetivo: reconhecer palavras que contenham a sequencia 10110.")

print("Estados:", estados)
print("Alfabeto:", alfabeto)
print("Estado inicial:", estado_inicial)
print("Estados finais:", estados_finais)

print("\nTabela de transicoes:")

for estado in estados:
    for simbolo in alfabeto:
        print(estado, "+", simbolo, "->", transicoes[estado][simbolo])


# TESTE AUTOMATICO ====================================================================================================================================================================

if modo == "2":

    print("\n===================================")
    print("       RESULTADO DOS TESTES")
    print("===================================")

    for palavra in testes:

        resultado, caminho, simbolo_invalido = automato.checa_simbolos(palavra)

        print("\nPalavra:", palavra)
        print("Caminho percorrido:", " -> ".join(caminho))

        if simbolo_invalido is not None:
            print("Resultado: REJEITADA")
            print("Motivo: simbolo", simbolo_invalido, "nao pertence ao alfabeto.")

        elif resultado:
            print("Resultado: PALAVRA ACEITA!")

        else:
            print("Resultado: PALAVRA REJEITADA!")

    print("\n===================================")
    print("       TESTE FINALIZADO")
    print("===================================")


# TESTE MANUAL ========================================================================================================================================================================

else:

    print("\n===================================")
    print("          TESTE DO AUTOMATO")
    print("===================================")

    print("Digite uma palavra para testar.")
    print("Pressione ENTER para testar a palavra vazia.")
    print("Digite 'sair' para encerrar.")

    while True:

        palavra = input("\nPalavra: ")

        if palavra.lower() == "sair":
            print("Programa encerrado.")
            break

        resultado, caminho, simbolo_invalido = automato.checa_simbolos(palavra)

        print("Caminho percorrido:", " -> ".join(caminho))

        if simbolo_invalido is not None:
            print("Resultado: REJEITADA")
            print("Motivo: simbolo", simbolo_invalido, "nao pertence ao alfabeto.")

        elif resultado:
            print("Resultado: PALAVRA ACEITA!")

        else:
            print("Resultado: PALAVRA REJEITADA!")