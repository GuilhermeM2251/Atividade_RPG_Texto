#Criando um Loop para poder ser possível reiniciar o jogo (se for da vontade do jogador)
import random
import time
while True:
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
    print("🏹 Arqueiro  | HP = 10  → Caçador preciso, veloz como o vento.")
    print("🗡️  Assassino | HP = 10  → Ágil e silencioso, mestre das sombras.")
    print("✨ Mago      | HP =  8  → Sábio arcano, molda a realidade com feitiços.\n")
    print("Lembre-se: As classes apesar de terem diferentes HPs possuem vantagens diferentes das demais, escolha com atenção!\n")
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
    #O jogador se depara com uma escolha logo de cara, será que ele conseguirá escolher da maneira correta de acordo com sua classe ?
    print("\nVocê chega a uma encruzilhada: \n(c) 🕳️  À esquerda, uma caverna escura e úmida. \n(f) 🌲 À direita, uma floresta densa e misteriosa. \n")
    #Envia uma mensagem alertando sobre como a escolha das classes pode afetar no decorrer da aventura.
    print("\nTenha em mente que as classes podem beneficiá-lo ou prejudicá-lo no caminho que escolher\n")

    desistiu_inicio = False
    while True:
        caminho = input("Qual caminho você seguirá (c) ou (f)? (ou 'd' para desistir) ").lower().strip()
        if caminho in ("c","f"):
            break
        elif caminho in ("d", "desistir", "sair"):
            desistiu_inicio = True
            break
        else:
            print("\nEscolha inválida. Digite 'c', 'f' ou 'd'.\n")

    if desistiu_inicio:
        print("\nVocê decidiu encerrar a aventura antes de começar. Tudo bem! \nA Relíquia Perdida estará te esperando quando quiser voltar. 😉")

        jogar_novamente = input("\nDeseja jogar novamente? [s] / [n]\n").lower().strip()
        if jogar_novamente == "n":
            print("\nNovamente, agradeço por jogar, até a próxima!")
            break   # sai do while True principal
        else:
            print("\nReiniciando a aventura...\n")
            continue  # recomeça o while True principal

    while hp > 0:
        if caminho == "f":
            print ("\nVocê escolheu o caminho da Floresta 🌲")
            if classe == "paladino" or classe == "guerreiro":
                print("\nSua armadura protege dos espinhos. Sem dano!")
                print(f"\nHP atual: {hp}")
            else:
                print("\nEspinhos arranham sua pele. -2 HP.")
                hp -= 2
            while True:
                print("\nUm goblin aparece na sua frente, qual decisão você tomará ? \nLeve em consideração que o goblin é um inimigo veloz, porém com ataques fracos.\n")
                dec_floresta1= input ("[1] Atacar o goblin \n[2] Defender o ataque e contra-atacar \n[3] Esquivar do goblin e contra-atacar.\n").lower().strip()
                if dec_floresta1 == "1":
                    print("\nVocê consegue atacar o inimigo e derrotá-lo, porém ele era muito veloz e lhe acerta um golpe. -2 HP.")
                    hp -= 2
                    print(f"\nHP atual: {hp}")
                    break

                elif dec_floresta1 == "2":
                    print("\nVocê defende o ataque do goblin e consegue executar um contra-ataque perfeitamente. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break

                elif dec_floresta1 == "3":
                    print("\nVocê consegue esquivar, mas o goblin lhe acerta de raspão graças à sua velocidade. -1 HP.")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break

                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            while True:
                print("\nO Sol começa a se pôr e você precisa decidir aonde você irá dormir.")
                print("\n[1] À sua esquerda, você vê luzes acesas em uma cabana 🏡 solitária, com um formato de um chapéu, bem peculiar! ")
                print("[2] À sua direita, você avista uma árvore 🌳 com algumas pessoas pequenas e com um chapéu, parecem amigáveis, mas será que são mesmo ?")
                print("[3] Apesar de tudo não parece uma floresta 🌲🌲🌲 tão perigosa, quem sabe dormir em uma moita ou em cima de uma árvore não seja tão ruim ?")
                dec2_floresta2 = input("\nQual a sua decisão ? ").lower().strip()

                if dec2_floresta2 == "1":
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
                            print(f"\nHP atual: {hp}")
                            break

                        elif dec_velhinha == "n":
                            print("Você foge do local, mas a bruxa ainda consegue lançar uma magia em você, pegando de raspão. -1 HP")
                            hp -=1
                            print(f"\nHP atual: {hp}")
                            break

                        else:
                            print("Digite 's' (sim) ou 'n' (não).")

                    else:
                        print("Ela lhe dá boa noite e pergunta se precisa de ajuda \nLogo você responde que precisa de um local pra dormir.")
                        print("A senhorinha lhe oferece então que durma na cabana e lhe oferece comida também.")
                        print("Na manhã seguinte você acorda passando mal e sai da cabana e percebe que foi envenenado.")
                        print("Você corre do local, fugindo da bruxa que poderia lhe matar. -2 HP")
                        hp -= 2
                        print(f"\nHP atual: {hp}")
                        break

                elif dec2_floresta2 == "2" or dec2_floresta2 == "arvore":
                    print("\nVocê decide ir para a árvore 🌳")
                    print("\nChegando no local você avista umas criaturinhas pequenas com um chapéu pontudo.")
                    print("Você dá as devidas saudações aos pequeninos e eles apesar de assustados com seu tamanho, perguntam o motivo de você ter ido até eles")
                    print("Dialogando calmamente você tenta acalmá-los e fala que busca um local seguro para dormir.")
                    print("Os gnomos mais calmos se apresentam e falam para você dormir logo abaixo na árvore deles que nesse local eles ficam seguros pela aura da árvore")
                    print("logo após você agradece eles e deita-se e dorme.")
                    hp += 2
                    print(f"\nHP atual: {hp}")
                    break

                elif dec2_floresta2 == "3":
                    print("\nVocê decide deitar-se na floresta em algum lugar que possa descansar.")
                    print("Ao avistar uma moita que parece relativamente segura e confortável, você deita-se e tenta dormir.")
                    print("Porém no outro dia, apesar do descanso (+2 HP), percebe que vários bichos lhe morderam, o deixando com algumas feridas. -2 HP")
                    hp += 2
                    hp -= 2
                    print(f"\nHP atual: {hp}")
                    break

                else:
                    print("\nDigite um local válido para descansar.")

            if hp <= 0:
                break

            print(f"\nLogo após descansar o jogador segue seu caminho pela floresta.")
            print("Mas logo no início, após você andar pouco, você encontra um Ogro das Árvores.")
            print("Você terá que enfrentá-lo para seguir adiante.")
            while True:
                print("\nLembre-se, ele é inimigo mais lento devido ao seu porte e carrega um machado grande e letal, o que o deixa ainda mais devagar\n")
                dec3_floresta3 = input("Você pode:\n[1] Atacar o Ogro \n[2] Defender o ataque e contra-atacar \n[3] Esquivar do Ogro e contra-atacar.\n").lower().strip()
                if dec3_floresta3 == "1":
                    print("Você é mais veloz que ele, reage rápido, o fere gravemente e derrota o Ogro. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                elif dec3_floresta3 == "2":
                    print ("Você tenta defender, mas o Ogro tem um ataque muito poderoso, mas apesar disso você se mantém de pé após a pancada e o derrota com um golpe certeiro. -3 HP")
                    hp -= 3
                    print(f"\nHP atual: {hp}")
                    break
                elif dec3_floresta3 == "3":
                    print ("Você consegue se esquivar efetivamente do Ogro e lança um contra-ataque mortífero nele! Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                else:
                    print("Digite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            print("\nO Ogro dropou um baú, tente adivinhar o número para ganhar uma poção de cura.")
            segredo = random.randint(1, 6)
            tentativas = 3
            while tentativas > 0:
                    palpite = input("Tente adivinhar o número do baú (1 a 6): ").strip()
                    if not palpite.isdigit():
                        print("Digite um número válido entre 1 e 6.")
                        continue
                    palpite = int(palpite)
                    if palpite < 1 or palpite > 6:
                        print("O número deve estar entre 1 e 6.")
                        continue
                    if palpite == segredo:
                        print("Você acertou! O baú se abre e revela uma poção de cura. +2 HP")
                        hp += 2
                        break
                    else:
                        tentativas -= 1
                        if tentativas > 0:
                            print(f"Número errado! Você ainda tem {tentativas} tentativa(s)...")
                        else:
                            print("O baú desaparece em fumaça! Você perdeu a chance.")

            if hp <= 0:
                break

            #Batalha com o Boss - Luta final.
            print("\nO jogador caminha pelas profundezas da floresta, onde tudo parece mais escuro e mais perigoso.")
            print("Mas em um instante o jogador avista uma pilha de ouro cheia de tesouros, iluminando o ambiente com o reflexo.")
            print("Contudo, o jogador ouve um rugido amedrontador, um Orc aparece em frente ao jogador, bloqueando-o de seu principal objetivo, A Relíquia Perdida.")
            while True:
                print("Agora o jogador tem duas opções: enfrentar a besta diante dele ou correr")
                decf_floresta = input("O jogador deve:\n[1] Correr\n[2] Batalhar\nEscolha com sabedoria: ").lower().strip()
                if decf_floresta == "1":
                    print("O jogador corre do local, deixando a Besta para trás.\nContudo o jogador nunca saberá qual era A Relíquia Perdida")
                    print("Apesar de tudo o jogador viveu uma experiência de altos e baixos.")
                    print("=====================================")
                    print("             Fim de jogo")
                    print("            Final Neutro")
                    print("=====================================")
                    break
                elif decf_floresta == "2":
                    print("O jogador decide encarar o desafio final dessa jornada de frente, se tornando um herói ou cavando sua própria cova.")
                    break
                else:
                    print("\nDigite uma das ações apresentadas. '1' ou '2'")

            if decf_floresta == "1":
                break

            if hp <= 0:
                break

            #Primeira parte da batalha com o boss:
            while True:
                print("O jogador dá um passo a frente, se preparando para a batalha.")
                print("No mesmo instante o Orc prepara um ataque avassalador")
                batalha1_floresta= input ("Qual sua ação ? \n[1] Tenta atacar antes do orc e bloquear seu ataque \n[2] Tenta defender o golpe do Orc \n[3] Tenta se esquivar do golpe e na sequência atacar o orc \n").strip()
                if batalha1_floresta == "1":
                    print("\nApesar de sua coragem louvável, você acaba acertando o orc, mas na sequência ele continua o ataque, acertando em cheio. -3 HP")
                    hp -= 3
                    print(f"\nHP atual: {hp}")
                    break
                elif batalha1_floresta == "2":
                    if classe == "guerreiro" or classe == "paladino":
                        print("\nSua resistência e força permitem que bloqueie o ataque do orc, na sequência você contra ataca e acerta um golpe em cheio. Sem dano!")
                        print(f"\nHP atual: {hp}")
                        break
                    else:
                        print("\nSeus esforços não são páreos para o ataque avassalador do Orc, recebendo o golpe. Apesar disso, você se recompõe rapidamente e acerta um golpe. -3 HP")
                        hp -= 3
                        print(f"\nHP atual: {hp}")
                        break
                elif batalha1_floresta == "3":
                    print("\nO jogador consegue se esquivar parcialmente do ataque do Orc, recebendo o ataque de raspão. Mas consegue atacar o Orc em cheio. -1 HP")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break
                else:
                    print("")

            if hp <= 0:
                break

            #Segunda parte da batalha:
            while True:
                print("\nO orc apesar de ter recebido um golpe em cheio permanece de pé, soltando um rugido feroz.")
                batalha2_floresta = input("Qual sua próxima ação ? \n[1] Tampar os ouvidos tentando evitar e recuando, perdendo sua vantagem inicial. \n[2] Esconder-se em uma árvore, usando como proteção \n[3] Avança para atacar o Orc, sofrendo o rugido em cheio. \n").strip()
                if batalha2_floresta == "1":
                    print("\nVocê consegue minimizar o dano do rugido, mas perde sua chance. -1 HP")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break
                elif batalha2_floresta == "2":
                    print("\nVocê agiu de maneira veloz, evitando o rugido e mantendo posição. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                elif batalha2_floresta == "3":
                    print("\nVocê avança com coragem, mas o rugido é muito forte, lhe deixando mais fraco. O Orc aproveita a oportunidade e lhe acerta de maneira mortal.")
                    hp -= 20
                    break
                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            #Terceira parte da batalha (final):
            while True:
                print("\nVocê percebe que a floresta pode te ajudar durante a batalha, então você se esconde e se move ágilmente, deixando o Orc confuso.")
                print("Com a confusão do Orc é o momento perfeito para tentar finalizá-lo")
                batalha3_floresta = input("Qual sua próxima ação ? \n[1] Atacar pelas costas do Orc, tentando neutralizá-lo. \n[2] Atirar uma pedra ou um galho para distraí-lo, tentando pegar o tesouro e correr.\n[3] Você sobe em uma árvore sorrateiramente e pula para acertar um golpe fatal.\n").strip()
                if batalha3_floresta == "1":
                    print("\nVocê consegue acertar um golpe fatal no Orc, mas com o pouco de força que ainda lhe restava joga o jogador para longe. -1 HP")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break

                elif batalha3_floresta == "2":
                    print("\nO Orc percebe a distração em um instante, indo em sua direção e lhe acertando um golpe mortal.")
                    hp -= 20
                    break

                elif batalha3_floresta == "3":
                    print("\nO Orc não consegue reagir a tempo, com você acertando sua cabeça em cheio, derrubando-o num instante. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break

                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            print("\nApós finalizar o Orc, Você chegou ao fim da aventura, finalmente alcançando A Relíquia Perdida, porém...")
            if classe == "guerreiro" or classe == "paladino":
                print("Você se aproxima do tesouro e encontra uma armadura sensacional e uma espada lendária, melhorando seu equipamento ao máximo.")
                print("Sua vida continuará com novas aventuras ainda mais emocionantes, mas esta chegou ao seu fim.")
                print("\n===================================================")
                print("                 Parabéns Jogador!")
                print("Você alcançou o final pretendido para sua classe!")
                print("             Muito Obrigado por jogar!")
                print("===================================================")
                break

            else:
                print("Você se aproxima do tesouro e encontra uma armadura sensacional e uma espada lendária ?!")
                print("Imagino que não era muito o que você esperava como recompensa, mas todo o tesouro certamente compensará.")
                print("Afinal A Relíquia Perdida não lhe ajudou tanto, mas a aventura com certeza lhe garantiu a experiência para continuar a vida como aventureiro.")
                print("\n===================================================")
                print("                 Parabéns Jogador!")
                print(" Você escolheu um final não ideal para sua classe.")
                print("    Jogue novamente e busque o final pretendido!")
                print("             Muito Obrigado por jogar!")
                print("===================================================")
                break



        if caminho == "c":
            print ("\nVocê escolheu o caminho da Caverna 🕳️")
            if classe == "assassino":
                print("\nAs sombras não são um problema para você, sua navegação não é afetada. Sem dano!")
                print(f"\nHP atual: {hp}")
            elif classe == "mago":
                print("\nSuas habilidades em magia lhe permitem invocar uma luz que lhe guiará no caminho. Sem dano!")
                print(f"\nHP atual: {hp}")
            else:
                print("\nA navegação pelo escuro lhe prejudica e você acaba caindo. -2 HP.")
                hp -= 2
            while True:
                print("\nUm slime aparece na sua frente, qual decisão você tomará ? \nLembre-se, o slime é um inimigo fraco, porém gosmento.\n")
                dec_caverna1= input ("[1] Atacar o slime \n[2] Defender o ataque e contra-atacar \n[3] Esquivar do slime e contra-atacar de maneira precisa.\n ").lower().strip()
                if dec_caverna1 == "1":
                    print("\nVocê consegue atacar o inimigo e derrotá-lo, porém a gosma cai em sua cara e você acaba caindo. -2 HP.")
                    hp -= 2
                    print(f"\nHP atual: {hp}")
                    break

                elif dec_caverna1 == "2":
                    print("\nVocê defende o ataque do slime e executa um contra-ataque. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break

                elif dec_caverna1 == "3":
                    print("\nVocê consegue esquivar e acerta um golpe no ar, a gosma não lhe atinge. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break

                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            while True:
                print("\nApós caminhar bastante pela caverna você começa a se cansar.")
                print("Logo você procura um lugar seguro para descansar e ao chegar em uma parte grande da caverna com um lago você pode:")
                print("\n[1] Você avista uma cabana 🏚️ pelo caminho, parece um local de descanso de aventureiros, que mal pode fazer perguntar ?")
                print("[2] Permanecer na região do lago 🕳️ 🌊 💧, descansando próximo à margem, aproveitando que é feito de areia fina e argila.")
                print("[3] Ao fundo, para a direita do lago, você avista uma tribo 🏕️ 🛖 🔥 de pessoas verdes, parecem da mesma estatura que você, mas será que são amigáveis ?")
                dec2_caverna2 = input("\nQual a sua decisão ? ").lower().strip()

                if dec2_caverna2 == "1":
                    print("\nVocê decide ir para a cabana 🏚️")
                    print("Você bate na porta e é recebido por um senhor, sem uma das mãos e sem um pé, parece um ferreiro.")
                    print("Ele lhe dá boa noite e pergunta se precisa de ajuda \nLogo você responde que precisa de um local pra dormir.")
                    print("O senhor então lhe oferece que durma na cabana e lhe oferece comida também.")
                    print("Na manhã seguinte você acorda, agradece o senhor pela hospitalidade e diz que precisa continuar sua aventura.")
                    print("O senhor então diz que costumava ser um aventureiro até perder sua mão e sua perna, e o mesmo lhe informa que há um Golem perigoso no fim da caverna.")
                    print("O jogador, animado, responde que derrotará o Golem em nome do senhor e se despede.")
                    print("O descanso foi tranquilo e o jogador conseguiu se recuperar bem. +2 HP")
                    hp += 2
                    print(f"\nHP atual: {hp}")
                    break

                elif dec2_caverna2 == "2":
                    print("\nVocê decide descansar no lago 🕳️ 🌊 💧")
                    print("\nVocê encontra um local próximo à margem feito de areia e de argila e descansa por ali mesmo.")
                    print("Você acorda sem interrupções durante a noite, mas apesar de dormir na areia não foi uma noite tão boa de descanso.")
                    print("Mas mesmo assim você continua sua aventura. +1 HP")
                    hp += 1
                    print(f"\nHP atual: {hp}")
                    break

                elif dec2_caverna2 == "3":
                    print("\nVocê decide ir para a vila onde as pessoas verdes estão.")
                    print("Você se aproxima do local tranquilamente")
                    if classe == "assassino":
                        print("Você percebe pelo seu instinto aguçado que são Trolls, sendo extremamente perigosos e agressivos.")
                        dec_trolls=input("Ainda deseja continuar ?\n[s] ou [n]\n")
                        if dec_trolls == "n":
                            print("Você foge do local, mas ainda é perseguido por um troll que atira uma lança em você, acertando você de raspão. -1 HP")
                            hp -= 1
                            print(f"\nHP atual: {hp}")
                            break
                        elif dec_trolls == "s":
                            print("Você se aproxima do local e tenta diálogo com os Trolls, mas...")
                            time.sleep(2)
                            print("Os Trolls se juntam e atacam o jogador juntos, levando a sua fatalidade.")
                            hp -= 20
                            break
                        else:
                            print("Digite uma ação válida. 's' ou 'n'")

                    else:
                        print("Você se aproxima do local e tenta diálogo com os Trolls, mas...")
                        time.sleep(2)
                        print("Os Trolls se juntam e atacam o jogador juntos, levando a sua fatalidade.")
                        hp -= 20
                        break

                else:
                    print("\nDigite um número válido correspondente ao local. '1', '2' ou '3'")

            if hp <= 0:
                break

            print(f"\nLogo após descansar o jogador segue seu caminho adiante pela caverna.")
            print("Mas logo no início, após você andar pouco, você encontra um esqueleto com uma espada.")
            print("Você terá que enfrentá-lo para seguir adiante.")
            print("\nLembre-se, o esqueleto tem a estatura de um humano e possivelmente uma certa experiência com batalhas.\n")
            while True:
                dec3_caverna3 = input("Você pode:[1] Atacar o esqueleto \n[2] Defender o ataque e contra-atacar \n[3] Esquivar do esqueleto e contra-atacar.\n").lower().strip()
                if dec3_caverna3 == "1":
                    print("Você tenta avançar no esqueleto, mas por sua astúcia ele bloqueia e o joga pra longe. Após o impacto você se recompõe e elimina o esqueleto. -1 HP")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break
                elif dec3_caverna3 == "2":
                    print ("Você tenta defender, mas o esqueleto é astuto e já enfrentou situações similares, acertando-o. Apesar do golpe você consegue revidar e eliminá-lo. -3 HP")
                    hp -= 3
                    print(f"\nHP atual: {hp}")
                    break
                elif dec3_caverna3 == "3":
                    print ("Você consegue se esquivar efetivamente do esqueleto e lança um contra-ataque mortífero nele! Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'\n")

            if hp <= 0:
                break

            print("\nO Esqueleto dropou um baú, tente adivinhar o número para ganhar uma poção de cura.")
            segredo = random.randint(1, 6)
            tentativas = 3
            while tentativas > 0:
                    palpite = input("Tente adivinhar o número do baú (1 a 6): ").strip()
                    if not palpite.isdigit():
                        print("Digite um número válido entre 1 e 6.")
                        continue
                    palpite = int(palpite)
                    if palpite < 1 or palpite > 6:
                        print("O número deve estar entre 1 e 6.")
                        continue
                    if palpite == segredo:
                        print("Você acertou! O baú se abre e revela uma poção de cura. +2 HP")
                        hp += 2
                        break
                    else:
                        tentativas -= 1
                        if tentativas > 0:
                            print(f"Número errado! Você ainda tem {tentativas} tentativa(s)...")
                        else:
                            print("O baú desaparece em fumaça! Você perdeu a chance.")

            if hp <= 0:
                break

            #Batalha com o Boss - Luta final.
            print("\nO jogador caminha pelas profundezas da caverna, onde tudo fica silencioso e assustador.")
            print("Mas em um instante o jogador avista uma pilha de ouro cheia de tesouros, atraindo a atenção do jogador.")
            if dec2_caverna2 == "1":
                print("O jogador chega ansioso pela batalha contra o Golem, já preparado para derrotá-lo assim como prometeu ao ferreiro.")
                print("Em um instante vê a pedra se transformando no Golem e ele animado se prepara para o desafio final antes da Relíquia Perdida.")
            else:
                print("Contudo, olha pro lado e vê a pedra se mexer, um Golem aparece em frente ao jogador, bloqueando-o de seu principal objetivo, A Relíquia Perdida.")

            while True:
                print("Agora o jogador tem duas opções: enfrentar o Golem diante dele ou correr")
                decf_caverna = input("O jogador deve:\n[1] Correr\n[2] Batalhar\nEscolha com sabedoria: ").lower().strip()
                if decf_caverna == "1":
                    print("O jogador corre do local, deixando o Golem para trás.\nContudo o jogador nunca saberá qual era A Relíquia Perdida")
                    print("Apesar de tudo o jogador viveu uma experiência de altos e baixos.")
                    print("=====================================")
                    print("             Fim de jogo")
                    print("            Final Neutro")
                    print("=====================================")
                    break
                elif decf_caverna == "2":
                    print("O jogador decide encarar o desafio final dessa jornada de frente, se tornando um herói ou cavando sua própria cova.")
                    break
                else:
                    print("Digite uma ação válida. '1' ou '2'")

            if decf_caverna == "1":
                break

            if hp <= 0:
                break

            #Primeira parte da batalha com o boss:
            while True:
                print("O jogador dá um passo a frente, se preparando para a batalha.")
                print("No mesmo instante o Golem prepara um ataque avassalador, estremecendo o chão.")
                batalha1_caverna= input ("Qual sua ação ? \n[1] Tenta atacar pulando, evitando a onda de choque \n[2] Tenta defender o ataque e contra-atacar \n[3] Tenta se esquivar do golpe e na sequência atacar o Golem \n").strip()
                if batalha1_caverna == "1":
                    print("\nAo avançar pulando o ataque inimigo resulta em um ataque direto no Golem, sem que o jogador receba dano. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                elif batalha1_caverna == "2":
                    if classe == "guerreiro" or classe == "paladino":
                        print("\nSua resistência e força permitem que bloqueie o ataque do Golem, na sequência você contra ataca e acerta um golpe em cheio. Sem dano!")
                        print(f"\nHP atual: {hp}")
                        break
                    else:
                        print("\nSeus esforços não são páreos para o ataque avassalador do Golem, recebendo o golpe. Apesar disso, você se recompõe rapidamente e acerta um golpe. -3 HP")
                        hp -= 3
                        print(f"\nHP atual: {hp}")
                        break
                elif batalha1_caverna == "3":
                    print("\nO jogador consegue se esquivar parcialmente do ataque do Golem, recebendo o ataque de raspão. Mas consegue atacar o Golem após se recompor. -1 HP")
                    hp -= 1
                    print(f"\nHP atual: {hp}")
                    break
                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            #Segunda parte da batalha:
            while True:
                print("\nO Golem após ter recebido um ataque em cheio avança em sua direção, furioso e determinado a matá-lo.")
                batalha2_caverna = input("Qual sua próxima ação ? \n[1] Usa o terreno como vantagem, jogando areia nos olhos do Golem e se esquivando da investida.  \n[2] Contra-atacar o Golem, tentando pará-lo. \n[3] Corre um pouco e pula o Golem. \n").strip()
                if batalha2_caverna == "1":
                    print("\nVocê consegue se esquivar por pouco, graças à cegueira do Golem, que colide com a parede. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break
                elif batalha2_caverna == "2":
                    print("\nVocê avança com coragem, mas a investida do Golem é muito forte, acertando-o em cheio e matando-o.")
                    hp -= 20
                    break
                elif batalha2_caverna == "3":
                    if classe == "arqueiro" or classe == "assassino":
                        print("\nO Golem passa direto por você e colide com a parede, graças a sua velocidade e movimentos você sai ileso, aterrissando de maneira esplêndida. Sem dano!")
                        print(f"\nHP atual: {hp}")
                        break
                    else:
                        print("Você consegue pular o Golem, que colide com a parede, e se esquivar dele, mas acaba caindo na aterrissagem. -1 HP")
                        hp -= 1
                        print(f"\nHP atual: {hp}")
                        break
                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            #Terceira parte da batalha (final):
            while True:
                print("\nVocê percebe que o Golem ficou nocauteado após colidir contra a parede, sendo sua chance de finalizá-lo.")
                batalha3_caverna = input("Qual sua próxima ação ? \n[1] Finalizar o Golem com um ataque direto em seu núcleo. \n[2] Ignorar o Golem e pegar o tesouro.\n[3] Tentar soterar o Golem, ao perceber as fissuras na parede.\n").strip()
                if batalha3_caverna == "1":
                    print("\nVocê se aproxima do Golem para executar o golpe final quando ele começa a se mover e... ")
                    time.sleep(3)
                    print("\nVocê finaliza o Golem sem mais problemas. Sem dano!")
                    print(f"\nHP atual: {hp}")
                    break

                elif batalha3_caverna == "2":
                    print("\nVocê vai se movendo até o tesouro e em um instante o Golem acorda novamente e avança uma investida em você, pela falta de preparo você sofre um ataque letal e morre.")
                    hp -= 20
                    break

                elif batalha3_caverna == "3":
                    print("\nVocê enterra o Golem e vira-se em direção ao tesouro, porém...")
                    time.sleep(3)
                    print("O Golem se levanta novamente, porém muito debilitado, você avança rapidamente e finaliza-o atacando o seu núcleo, mas ele desmorona sobre você, lhe causando algum dano. -2 HP")
                    hp -= 2
                    print(f"\nHP atual: {hp}")

                else:
                    print("\nDigite um número válido correspondendo à ação. '1', '2' ou '3'")

            if hp <= 0:
                break

            if dec2_caverna2 == "1":
                print("O jogador finaliza o Golem e cumpre o prometido ao ferreiro, finalmente chegando na Relíquia Perdida, porém...")
            else:
                print("\nApós finalizar o Golem, Você chegou ao fim da aventura, finalmente alcançando A Relíquia Perdida, porém...")
            time.sleep(2)
            if classe == "mago":
                print("Você se aproxima do tesouro e encontra um cajado lendário e ... uma faca invisível ?!")
                print("O cajado lhe auxiliará em próximas aventuras, a faca por outro lado... vendê-la talvez seja a melhor opção.")
                print("Sua aventura chega ao fim, com um equipamento digno de um herói.")
                print("\n===================================================")
                print("                 Parabéns Jogador!")
                print("Você alcançou o final pretendido para sua classe!")
                print("             Muito Obrigado por jogar!")
                print("===================================================")
                break

            elif classe == "assassino":
                print("Você se aproxima do tesouro e encontra uma faca invisível e ... um cajado lendário ?!")
                print("A faca lhe auxiliará a se tornar um assassino do mais alto nível, o cajado por outro lado... vendê-lo talvez seja a melhor opção.")
                print("Sua aventura chega ao fim, com um equipamento digno de um herói.")
                print("\n===================================================")
                print("                 Parabéns Jogador!")
                print("Você alcançou o final pretendido para sua classe!")
                print("             Muito Obrigado por jogar!")
                print("===================================================")
                break

            else:
                print("Você se aproxima do tesouro e encontra um cajado e uma faca invisível ?!")
                print("Imagino que não era muito o que você esperava como recompensa, mas todo o tesouro certamente compensará.")
                print("Afinal A Relíquia Perdida não lhe ajudou tanto, mas a aventura com certeza lhe garantiu a experiência para continuar a vida como aventureiro.")
                print("\n===================================================")
                print("                 Parabéns Jogador!")
                print(" Você escolheu um final não ideal para sua classe.")
                print("    Jogue novamente e busque o final pretendido!")
                print("             Muito Obrigado por jogar!")
                print("===================================================")
                break

    if hp <= 0:
        print("\n==========================================================")
        print("              Sua vida acabou e você perdeu.")
        print("                       GAME OVER")
        print("==========================================================")

    jogar_novamente=input("\nO Jogador deseja jogar novamente ? \n [s] / [n]\n").lower().strip()
    if jogar_novamente == "n":
        print("\nNovamente, agradeço por jogar, até a próxima!")
        break
    else:
        print("\nReiniciando a aventura...\n")

