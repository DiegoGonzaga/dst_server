import os

os.system("cls")

RESPOSTAS_POSITIVAS = ["SIM", "S"]

SERVIDORES_CADASTRADOS = ["mundo_zybro", "galera", "galera2"]

PATH_NULLRENDER = "c:/Program Files (x86)/Steam/steamcmd/steamapps/common/Don't Starve Together Dedicated Server/bin/"


def informa_servidores():
    """ Imprime na tela todos os servidores e o index das mesmas """
    print("Servidores:\n")
    i = 0
    tamanho = len(SERVIDORES_CADASTRADOS)
    while i < tamanho:
        print(i, " - ", SERVIDORES_CADASTRADOS[i])
        i += 1


def atualiza_servidor():
    """ Realiza a atualização do servidor """
    opcao = input("Deseja ATUALIZAR o inicializador de servidor?[s/n]: ")
    opcao = checa_lista(opcao, RESPOSTAS_POSITIVAS)
    if opcao:
        os.system(
            '"c:/Program Files (x86)/Steam/steamcmd/steamcmd.exe" +login anonymous +app_update 343050 validate +quit'
        )


def define_inicializacao_servidor():
    """ Recebe os dados do servidor que será inicializado. """
    print("Deseja inicializar um servidor?[s/n]")
    opcao = input()
    if not (checa_lista(opcao, RESPOSTAS_POSITIVAS)):
        print("Nenhum servidor foi inicializado.\nPrograma finalizado.")
        return
    informa_servidores()
    print("\nQual servidor deseja iniciar?")
    opcao = -1
    while opcao < 0 or opcao > (len(SERVIDORES_CADASTRADOS) - 1):
        opcao = int(input())
    global servidor_escolhido
    servidor_escolhido = SERVIDORES_CADASTRADOS[opcao]


def inicializa_servidor(servidor, shard):
    """São informados duas String, snedo que que @servidor é a nome do mesmo
    enquanto @shard é o fragmento do servidor que será inicializado."""
    # Define o PATH_NULLRENDER do inicializador de servidores
    global PATH_NULLRENDER
    os.chdir(PATH_NULLRENDER)

    # Inicializa o servidor escolhido
    complemento = (
        'start "'
        + servidor
        + ": "
        + shard
        + '" dontstarve_dedicated_server_nullrenderer -console -cluster '
        + servidor
        + " -shard "
        + shard
    )
    os.system(complemento)


def ativa_inicializacao_servidor():
    """Ativa a inicialização do servidor escolhido e questiona
    se deseja que as Caves sejam inicializadas também"""
    print("Inicializando servidor ", servidor_escolhido, "...")
    print("Deseja inicializar Caves?[s/n]?:")
    opcao = input()
    opcao = checa_lista(opcao, RESPOSTAS_POSITIVAS)
    inicializa_servidor(servidor_escolhido, "Master")
    if opcao:
        inicializa_servidor(servidor_escolhido, "Caves")


def checa_lista(resposta, lista_permitidos):
    """ Retorna True caso um item de @lista_permitidos seja igual a @resposta """
    resposta = resposta.upper().strip()
    for p in lista_permitidos:
        if resposta == p:
            return True
    return False


def main():
    print("INICIALIZADOR DE SERVIDORES DO DON'T STARVE TOGETHER\n")
    atualiza_servidor()
    define_inicializacao_servidor()
    ativa_inicializacao_servidor()


main()
