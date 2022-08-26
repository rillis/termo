import random

#Clase com as cores (Unix/Win)
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    YELLOW2 = '\033[33m'
    RED = '\033[91m'
    BLUE = '\033[34m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    lista_cores = [GREEN, YELLOW, YELLOW2, RED, END, BOLD, UNDERLINE, BLUE]

#Método para printar com cores/espaçamento e bordas
def log(s, end="\n", input_mode=False):
    txtcru = s
    for cor in bcolors.lista_cores:
        txtcru = txtcru.replace(cor, "")
    s = f"{bcolors.BLUE}|{bcolors.END}{s.center(41 + (len(s)-len(txtcru)))}{bcolors.BLUE}|{bcolors.END}"
    if not input_mode: print(f"{s}{bcolors.END}", end=end)
    else: return input(f"{s}{bcolors.END}")

#Método de pula linha
def hr(type=-1):
    if type == -1: print("")
    if type == 0: log(bcolors.BLUE+''.join(["-"]*41))
    if type == 1: print(f'{bcolors.BLUE}┌{"".join(["-"]*41)}┐{bcolors.END}')
    if type == 2: print(f'{bcolors.BLUE}└{"".join(["-"]*41)}┘{bcolors.END}')

#Método tradutor de cores
def cor(l, n):
    d = {-1: bcolors.END, 0: bcolors.YELLOW2, 1: bcolors.GREEN}
    return f"{d[n]}{l}{d[-1]}"

#Pegar palavra aleatória do arquivo
def pick_word():
    with open("word_new.txt", "r", encoding="utf8") as ox:
        return random.choice(ox.readlines()).replace("\n", "")

#UTF-8
def decode(s):
    d = {'ã': 'a', 'á': 'a', 'é': 'e', 'ú': 'u', 'í': 'i', 'ç': 'c', 'ô': 'o', 'ê': 'e', 'õ': 'o', 'ó': 'o', 'â': 'a'}
    for l in d:
        s = s.replace(l, d[l])
    return s

#Método que compara a palavra escolhida aleatoriamente (a) com a digitada (b) e retorna uma matriz numerica com resultados:
# -1 : Não tem
# 0 : Ainda tem, mas não nessa posição
# 1 : Acertou a posição
def compare(a, b):
    t = [-1, -1, -1, -1, -1]
    sobrantes = []
    pos = 0
    for x, y in zip(a.lower(), b.lower()):
        if x == y:
            t[pos] = 1
        else:
            sobrantes.append(x)
        pos += 1
    pos = 0
    for x, y in zip(a, b):
        if x != y and y in sobrantes:
            t[pos] = 0
        pos += 1
    return t

#Método do jogo
def game(args):
    listachutes = []
    hr()
    hr(type=1)
    log(f"{bcolors.RED}----- {bcolors.GREEN}Term.ooo {bcolors.RED}-----")
    log(f"{bcolors.YELLOW}Press {bcolors.GREEN}[ENTER]{bcolors.YELLOW} to start.", input_mode=True)



    w = pick_word()
    if args["debug"]: log(f"{bcolors.BLUE}Palavra escolhida: {bcolors.RED}{w}")
    wd = decode(w)

    win = False

    for n in range(1, args["tries"]+1):
        hr(type=0)
        log(f"{bcolors.YELLOW}Tentativa {bcolors.END}{n}")
        t = ""
        while len(t) != 5:
            t = log(f"{bcolors.YELLOW}Digite uma palavra: {bcolors.END}", input_mode=True)
        td = decode(t)
        c = compare(wd, td)

        word_p = ""
        for l,y in zip(range(len(w)),c):
            if y == 1: word_p+=cor(w[l],y)
            else: word_p+=cor(t[l],y)
        listachutes.append(word_p)
        lista_print = listachutes + ["_____"]*(args["tries"] - len(listachutes))

        log("")
        for t in lista_print: log(t)
        log("")
        if sum(c) == 5:
            log(f"{bcolors.GREEN}Você ganhou!")
            win = True
            break
    if not win:
        log(f"{bcolors.RED}Você perdeu :( A palavra era: {bcolors.END}{w}")
    hr(type=2)
    hr()

game({"tries":6, "debug":False})
