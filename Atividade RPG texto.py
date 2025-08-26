#Iniciando o RPG com o nome e uma breve apresentação
print ("==============================================================")
print ("                    A Relíquia Perdida                    ")
print ("       Um RPG de Texto por Guilherme, Nicolas e Rayra")
print ("==============================================================")
#Dá as boas vindas ao jogador
print ("\nBem Vindo jogador(a)")
#Solicita um input com o nome do jogador
nome = input("Qual seu nome? ")
#Faz as devidas saudações, com uma breve frase + iniciando a escolha de classes
print(f"\nSaudações, {nome.capitalize()}! Sua jornada está prestes a começar...")
print("\nMas primeiro escolha sua classe:\n")


#Processo de escolha de classe:
#Apresentar as classes:
print("⚔️  Paladino  | HP = 12  → Guardião sagrado, escudo da justiça.")
print("🛡️  Guerreiro | HP = 12  → Força bruta e coragem inabalável.")
print("🏹  Arqueiro | HP = 10  → Caçador preciso, veloz como o vento.")
print("🗡️  Assassino | HP = 10  → Ágil e silencioso, mestre das sombras.")
print("✨  Mago     | HP =  8  → Sábio arcano, molda a realidade com feitiços.\n")
print("Lembre-se: As classes apesar de terem diferentes Hp's podem possuir habilidades diferentes ou vantagens diferentes das demais, escolha com atenção!\n")
#Criar uma lista com as variáveis das classes:
classes_validas = ["paladino","guerreiro","arqueiro","mago","assassino"]


#Iniciar um loop para caso haja algum erro do usuário:
while True:
    #Criar uma variável classe:
    classe = input("Digite o nome da sua classe: ").lower().strip()
    #Identificar se há números no input, com o comando .isdigit() (caso haja algum número apresentar uma mensagem amigável apresentando um erro)
    if classe.isdigit():
        print("\nNão digite números, escolha uma classe válida.\n")
    #Identificar se o input consta como uma classe (caso esteja correto quebrar o loop).
    elif classe in classes_validas:
        print(f"\nVocê escolheu a classe: {classe.capitalize()}!")
        break
    #Caso esteja incorreto apresentar uma mensagem amigável, reiniciando o loop
    else:
        print("\nClasse inválida \nDigite uma das classes existentes\n")


#Define o valor do hp do jogador
hp = 0
#Estabele o valor de acordo com a classe escolhida pelo jogador
if classe == "paladino" or classe == "guerreiro":
    hp = 12
elif classe == "arqueiro" or classe == "assassino":
    hp = 10
else:
    hp = 8


#Se inicia a aventura do jogador, apresentando seu objetivo.
print(f"\nBem-vindo à aventura, {nome}!")
print(f"Você é um {classe.capitalize()} em busca da Relíquia Perdida.")
print("Dizem que esse artefato é capaz de trazer poder inimaginável... mas o caminho será perigoso.")
#O jogador se depara com uma escolha logo de cara, será que ele coseguirá escolher da maneira correta de acordo com sua classe ?
print("\nVocê chega a uma encruzilhada: \n(c) 🕳️  À esquerda, uma caverna escura e úmida. \n(f) 🌲 À direita, uma floresta densa e misteriosa. \n(m) ⛰️  À sua frente, uma montanha rochosa e traiçoeira")
#Envia uma mensagem alertando sobre como a escolha das classes pode afetar no decorrer da aventura.
print("\nTenha em mente que as classes podem beneficiá-lo ou prejudicá-lo no caminho que escolher\n")


while True:
    caminho = input("Qual caminho você seguirá (c), (f) ou (m)? ").lower().strip()
    if caminho in ("c","f","m"):
        break
    else:
        print("\nEscolha inválida. Digite 'c', 'f' ou 'm'.\n")


while hp > 0:
    if caminho == "f":

        print ("\nVocê escolheu o caminho da Floresta 🌲")
        if classe == "paladino" or classe == "guerreiro":
            print("\nSua armadura protege dos espinhos. Sem dano!")
            print(f"HP atual {hp}")
        else:
            print("\nEspinhos arranham sua pele. -2 HP.")
            hp -= 2
        while True:
            print("\nUm goblin aparece na sua frente, qual decisão você tomará ? \nLeve em consideração que o goblin é um inimigo veloz, porém com ataques fracos.\n")
            dec_floresta1= input ("Atacar \nDefender \nEsquivar\nEscolha sua ação: ").lower().strip()
            if dec_floresta1 == "atacar":
                print("\nVocê consegue atacar o inimigo e derrotá-lo, porém ele era muito veloz e lhe acerta um ataque. -2 HP.")
                hp -= 2
                print(f"HP atual {hp}")
                break

            elif dec_floresta1 == "defender":
                print("\nVocê defender o ataque do goblin e consegue executar um contra-ataque perfeitamente. Sem dano!")
                print(f"HP atual {hp}")
                break

            elif dec_floresta1 == "esquivar":
                print("\nVocê consegue esquivar mas o goblin lhe acerta de raspão graças à sua velocidade. -1 HP.")
                hp -= 1
                print(f"HP atual {hp}")
                break

            else:
                print("\nDigite uma das ações apresentadas. 'atacar', 'defender' ou 'esquivar'.")


        while True:
            print("\nO Sol começa a se pôr e vc precisa decidir aonde você irá dormir.")
            print("\n(cabana 🏡) À sua esquerda, você vê luzes acessas em uma cabana solitária, com um formato de um chapéu, bem peculiar! ")
            print("(árvore 🌳) À sua direita, você avista uma árvore com algumas pessoas pequenas e com um chapéu, parecem amigáveis, mas será que são mesmo ?")
            print("(floresta 🌲🌲🌲) Apesar de tudo não parece uma floresta tão perigosa, quem sabe dormir em uma moita ou em cima de uma árvore não seja tão ruim ?")
            dec2_floresta2 = input("\nQual a sua decisão ? ").lower().strip()

            if dec2_floresta2 == "cabana":
                print("\nVocê decide ir para a cabana 🏡")
                print("Você bate na porta e é recebido por uma senhorinha, com um chapéu na cabeça, que mal uma senhorinha pode fazer ?")

                if classe == "mago":
                    print("Você identifica a velhinha como uma bruxa que pode lhe fazer mal e acabar lhe prejudicando na aventura.")
                    dec_velhinha = input ("Ainda deseja prosseguir para a casa da bruxa ? - digite s (sim) ou n (não) ").lower().strip()

                    if dec_velhinha == "s":
                        print("Ela lhe dá boa noite e pergunta se precisa de ajuda \nLogo você responde que precisa de um local pra dormir.")
                        print("A senhorinha lhe oferece então que durma na cabana e lhe oferece comida também.")
                        print("Na manhã seguinte você acorda passando mal e sai da cabana, percebendo que foi envenenado.")
                        print("Você corre do local, fugindo da bruxa que poderia lhe matar. -3 HP")
                        hp -= 3
                        print(f"\nHP atual {hp}")
                        break

                    elif dec_velhinha == "n":
                        print("Você foge do local, mas a bruxa ainda consegue lançar uma magia em você, pegando de raspão. -1 HP")
                        hp -=1
                        print(f"\nHP atual {hp}")
                        break

                    else:
                        print("\nDigite uma das opções apresentadas \n")

                else:
                    print("Ela lhe dá boa noite e pergunta se precisa de ajuda \nLogo você responde que precisa de um local pra dormir.")
                    print("A senhorinha lhe oferece então que durma na cabana e lhe oferece comida também.")
                    print("Na manhã seguinte você acorda passando mal e sai da cabana e percebe que foi envenenado.")
                    print("Você corre do local, fugindo da bruxa que poderia lhe matar. -2 HP")
                    hp -= 2
                    print(f"\nHP atual {hp}")
                    break

            elif dec2_floresta2 == "árvore" or dec2_floresta2 == "arvore":
                print("\nVocê decide ir para a árvore 🌳")
                print("\nChegando no local você avista umas criaturinhas pequenas com um chapéu pontudo.")
                print("Você dá as devidas saudações aos pequeninos e eles apesar de asustados com seu tamanho, perguntam o motivo de você ter ido até eles")
                print("Dialogando calmamente você tenta acalmá-los e fala que busca um local seguro para dormir.")
                print("Os gnomos mais calmos se apresentam e falam para você dormir logo abaixo na árvore deles que nesse local eles ficam seguros pela aura da árvore")
                print("logo após você agradece eles e deita-se e dorme.")
                hp += 2
                print(f"\nHP atual {hp}")
                break

            elif dec2_floresta2 == "floresta":
                print("Você decide deitar-se na floresta em algum lugar que possa descansar.")
                print("Ao avistar uma moita que parece relativamente segura e confortável, você deita-se e tenta dormir.")
                print("Porém no outro dia, apesar do descanso, percebe que vários bixos lhe morderam, o deixando com algumas feridas.")
                print(f"\nHP atual {hp}")
                break

            else:
                print("\nDigite um local válido para descansar.")

        print(f"\nLogo após sua aventura dormindo na {dec2_floresta2}, você segue seu caminho pela floresta.")
        print("Mas logo no início, após você andar pouco, você encontra um goblin gordo.")
        print("Você terá que enfrentá-lo para seguir adiante.")
        while True:
            print("\nLembre-se ele é um goblin mais lento devido ao seu físico e carrega um machado grande e letal, deixando-o ainda mais lento\n")
            dec3_floresta3 = input("Você pode:\nAtacar \nDefender \nEsquivar\nQual decisão você tomará ?").lower().strip()
            if dec3_floresta3 == "atacar":
                print("Você é mais veloz que o goblin, conseguindo reagir rápido contra ele, o ferindo gravemente e derrotando o goblin. Sem dano!")
                print(f"HP atual {hp}")
                break
            elif dec3_floresta3 == "defender":
                print ("Você tenta defender, mas o goblin tem um ataque muito poderoso, mas apesar disso você se mantém de pé após a pancada e o derrota com um golpe certeiro. -3 HP")
                hp -= 3
                print(f"HP atual {hp}")
                break
            elif dec3_floresta3 == "esquivar":
                print ("Você consegue se esquivar efetivamente do goblin e lança um contra-ataque mortífero nele! Sem dano!")
                print(f"HP atual {hp}")
                break
            else:
                print("\nDigite uma das ações informadas. 'atacar', 'defender' ou 'esquivar'\n")

        #Batalha com o Boss - Luta final.
        while True:
            print("O jogador caminha pelas profundezas da floresta, onde tudo parece mais escuro e mais perigoso.")
            print("Mas em um instante o jogador avista uma pilha de ouro cheia de tesouros, iluminando o ambiente com o reflexo.")
            print("Contudo, o jogador ouve um rugido amedrontador, um Orc aparece em frente ao jogador, bloqueando-o de seu principal objetivo, A Relíquia Perdida.")
            print("Agora o jogador tem duas opções: enfrentar a besta diante dele ou correr")
            decf_floresta = input("O jogador deve:\nCorrer\nBatalhar\nEscolha com sabedoria: ").lower().strip()
            if decf_floresta == "correr":
                print("O jogador corre do local, deixando a Besta para trás.\nContudo o jogador nunca saberá qual era A Relíquia Perdida")
                print("Apesar de tudo o jogador viveu uma experiência de altos e baixos.")
                print("=====================================")
                print("             Fim de jogo")
            elif decf_floresta == "atacar":
                print("O jogador decide encarar o desafio final dessa jornada de frente, se tornando um herói ou cavando sua própria cova.")
                print("sla")