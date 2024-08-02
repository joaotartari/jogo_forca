import numpy as np
from unidecode import unidecode
import os
corpo = {'0': '(*_*)\n', '1': ' _', '2': '|', '3':'_\n', '4':' /', '5':' \\n'.replace('n', '')}
def show_body(lifes:int):
    body = ''
    if lifes == 2:
        body = '(*_*)\n  |'
    else:
        for i in range(lifes):
            body+=corpo[f'{i}']
    print(body)


palavras_forca = {
    "Animal que vive na água": "golfinho",
    "Fruto cítrico e azedo": "limão",
    "Maior planeta do Sistema Solar": "júpiter",
    "Principal órgão do sistema nervoso": "cérebro",
    "Cidade das luzes": "paris",
    "Pássaro símbolo da paz": "pomba",
    "Elemento químico essencial para a respiração": "oxigênio",
    "Local onde os astronautas vivem e trabalham no espaço": "estação espacial",
    "Corpo celeste que gira ao redor de um planeta": "lua",
    "Pessoa que escreve livros": "autor",
    "Grande corpo de água salgada": "oceano",
    "Famosa obra de Leonardo da Vinci": "mona lisa",
    "Ingrediente principal do pão": "farinha",
    "Instrumento musical de cordas": "violão",
    "País dos cangurus": "austrália",
    "Grande continente com muitos desertos": "áfrica",
    "Pequeno dispositivo de armazenamento de dados": "pendrive",
    "Estilo de música originado nos Estados Unidos": "jazz",
    "Casa onde vive o presidente dos EUA": "casa branca",
    "Desenho animado com uma esponja do mar": "bob esponja",
    "Inseto que produz mel": "abelha",
    "Esporte com raquete e bola": "tênis",
    "Órgão do corpo responsável pelo bombeamento do sangue": "coração",
    "Estação do ano mais quente": "verão",
    "Fruta vermelha com pequenas sementes": "morango",
    "Peça de roupa usada no pescoço para proteger do frio": "cachecol",
    "Astro que brilha durante o dia": "sol",
    "Comida japonesa feita de peixe cru": "sushi",
    "Personagem principal de 'O Rei Leão'": "simba",
    "Capital da Itália": "roma",
    "Animal conhecido por sua capacidade de imitar sons": "papagaio",
    "País conhecido por suas tulipas": "holanda",
    "Famoso monumento em Paris": "torre eiffel",
    "Sistema de ensino superior": "universidade",
    "Ajudante do Papai Noel": "duende",
    "Elemento químico símbolo do amor": "ouro",
    "Grande felino da selva": "tigre",
    "Símbolo da matemática para representar multiplicação": "x",
    "Filme sobre dinossauros ressuscitados": "jurassic park",
    "Parte mais alta de uma montanha": "pico",
    "Planeta vermelho": "marte",
    "Filme de animação sobre brinquedos": "toy story",
    "Alimento base da culinária italiana": "massa",
    "Antigo império com gladiadores": "roma",
    "Animal símbolo da sabedoria": "coruja",
    "Arte de se comunicar através de gestos": "mímica",
    "Doce feito com chocolate e leite condensado": "brigadeiro",
    "Maior órgão do corpo humano": "pele",
    "Invenção que revolucionou a comunicação": "telefone",
    "Bebida quente feita de grãos torrados": "café",
    "Famoso detetive criado por Arthur Conan Doyle": "sherlock holmes",
    "Música mais popular em um álbum": "single",
    "Estilo de vida baseado em sustentabilidade": "ecológico",
    "Antiga civilização conhecida por suas pirâmides": "egito",
    "Local para guardar dinheiro": "cofre",
    "Processo de converter luz solar em energia": "fotossíntese",
    "Objeto usado para escrever": "caneta",
    "Símbolo de proteção na cultura egípcia": "âncora",
    "Cidade conhecida como a grande maçã": "nova iorque",
    "Doença transmitida por mosquitos": "dengue",
    "Objeto para contar o tempo": "relógio",
    "Substância usada para limpar e lavar": "sabão"
}
def show_first_menu():
    valor = input("Digite uma das opções abaixo:\n1. Iniciar novo jogo;\n0. Sair.\n")
    os.system('clear')
    return valor
def show_second_menu():
    valor = input("Escolha uma opção abaixo:\n1. Digitar uma letra da Palavra;\n2. Digitar a palavra inteira;\n0. Desistir.\n")
    return valor
if __name__ == '__main__':
    print("""
██████╗░███████╗███╗░░░███╗░░░░░░██╗░░░██╗██╗███╗░░██╗██████╗░░█████╗░  ░█████╗░░█████╗░
██╔══██╗██╔════╝████╗░████║░░░░░░██║░░░██║██║████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗
██████╦╝█████╗░░██╔████╔██║█████╗╚██╗░██╔╝██║██╔██╗██║██║░░██║██║░░██║  ███████║██║░░██║
██╔══██╗██╔══╝░░██║╚██╔╝██║╚════╝░╚████╔╝░██║██║╚████║██║░░██║██║░░██║  ██╔══██║██║░░██║
██████╦╝███████╗██║░╚═╝░██║░░░░░░░░╚██╔╝░░██║██║░╚███║██████╔╝╚█████╔╝  ██║░░██║╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░  ╚═╝░░╚═╝░╚════╝░

░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ███████╗░█████╗░██████╗░░█████╗░░█████╗░██╗
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║  █████╗░░██║░░██║██████╔╝██║░░╚═╝███████║██║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══██║╚═╝
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝██║░░██║██╗
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝""")
    print("\n")
    while True:
        first_option = show_first_menu()
        if first_option == '1':
            vidas = 6
            palavra_escolhida = np.random.choice(list(palavras_forca.keys()))
            target = unidecode(palavras_forca[palavra_escolhida].lower())
            palavra = ['_' if p != ' ' else p for p in target]
            palavra = ' '.join(palavra)
            letras_escolhidas = []
            while vidas > 0:
                print('\n')
                show_body(vidas)
                print('\n')
                print(palavra_escolhida)
                print('\n')
                print(palavra)
                print('\n')
                second_option = show_second_menu()
                if second_option == '0':
                    break
                elif second_option == '1':
                    letra = input('Digite uma letra: \n')
                    os.system('clear')
                    letra = letra.lower()
                    if letra in letras_escolhidas:
                        print('Você já escolheu essa letra.')
                    elif letra in target:                       
                        palavra = ' '.join([p if p == letra else p if p in letras_escolhidas else p if p == ' ' else '_' for p in target])
                        if not '_' in palavra:
                            print(f'Parabéns, você acertou! A palavra correta era {target}\n')
                            break
                    else:
                        vidas-= 1
                    letras_escolhidas.append(letra)
                elif second_option == '2':
                    chute = input('Digite a palavra:\n')
                    os.system('clear')
                    chute = chute.lower()
                    if chute == target:
                        print(f'Parabéns, você acertou! A palavra correta era {target}\n')
                        break
                    else:
                        vidas -= 1
                elif second_option == ' ':
                    print('Opção inválida.\n')
                else:
                    print('Opção inválida.\n')
                if vidas == 0:
                    print(f'Você perdeu. A palavra correta era {target}.\n')

        elif first_option == '0':
            break
        else:
            print('Opção inválida, digite uma opção válida.\n')