import random

# Intro
print("Bem-vindo ao nosso jogo!"
      "O teu Objetivo é descobrir a palavra secreta, em português, constituída por 5 letras.")
print("VERDE significa letra correta no espaço correto.")
print("AMARELO significa letra correta no espaço errado.")
print("VERMELHO significa que essa letra não existe nessa palavra.")

# Palavra secreta
palavras_possiveis = [ 'abrir', 'acaso', 'achar', 'advem', 'anjos', 'agudo', 'algum', 'alibi', 'aluno', 'ambas', 'amigo', 'anais', 'andar', 'antes', 'apelo', 'arder', 'atual', 'audaz', 'autor', 'aviar', 'axila', 'banal', 'barao', 'bocal', 'busca', 'calao', 'calda', 'calor', 'campa', 'campo', 'carma', 'carro', 'certa', 'chama', 'chata', 'chefe', 'chuva', 'civil', 'clero', 'cocho', 'corar', 'coser', 'corpo', 'cozer', 'credo', 'crise', 'custo', 'daqui', 'debil', 'deixa', 'desde', 'desse', 'deter', 'diabo', 'digno', 'disso', 'enfim', 'enjoo', 'estar', 'facto', 'fauna', 'favor', 'feira', 'feliz', 'farpa', 'ficha', 'filho', 'finjo', 'firma', 'flora', 'forte', 'fossa', 'fugiu', 'gerir', 'gosto', 'grupo', 'homem', 'ideal', 'jazia', 'juizo', 'karma', 'lapis', 'lapso', 'legal', 'letra', 'ligar', 'limbo', 'linha', 'louco', 'louca', 'macro', 'magia', 'magoa', 'maior', 'manga', 'manso', 'meiga', 'miope', 'misto', 'molde', 'mover', 'museu', 'neste', 'noite', 'norma', 'nuvem', 'oasis', 'obter', 'orcas', 'ouvir', 'paira', 'pajem', 'pardo', 'patio', 'pedra', 'pegar', 'penta', 'perda', 'pluma', 'porem', 'posse', 'prado', 'preto', 'prole', 'porto', 'pudor', 'rente', 'repor', 'salsa', 'saude', 'seita', 'selar', 'senda', 'serao', 'serio', 'sesta', 'setor', 'senha', 'sorte', 'tecer', 'temer', 'tenso', 'tento', 'tenue', 'treta', 'torso', 'tribo', 'turva', 'valer', 'vasto', 'vedar', 'velar', 'velho', 'vendo', 'verde', 'verme', 'versa', 'vetor', 'video', 'viril', 'vista', 'votar', 'voraz', 'vosso']
palavra_secreta = random.choice(palavras_possiveis)
lista_palavra_secreta = list(palavra_secreta)
print(lista_palavra_secreta)

# Contador de vidas
vidas = 5

# Resposta
while vidas > 0:
      p1 = input("Palavra:")
      p1 = p1.lower()
      p1_lista = list(p1)
      if p1 == palavra_secreta:
          print("Acertaste!")
          acertou = True
          break
      else:
          # Primeira letra
            if p1_lista[0] == lista_palavra_secreta[0]:
                  print("VERDE")
            elif p1_lista[0] == lista_palavra_secreta[1] or p1_lista[0] == lista_palavra_secreta[2] or p1_lista[0] == lista_palavra_secreta[3] or p1_lista[0] == palavra_secreta[4]:
                  print("AMARELO")
            else:
                  print("VERMELHO")
            # Segunda letra
            if p1_lista[1] == palavra_secreta[1]:
                print("VERDE")
            elif p1_lista[1] == palavra_secreta[0] or p1_lista[1] == palavra_secreta[2] or p1_lista[1] == palavra_secreta[3] or p1_lista[1] == palavra_secreta[4]:
                print("AMARELO")
            else:
                print("VERMELHO")
            # Terceira letra
            if p1_lista[2] == palavra_secreta[2]:
                print("VERDE")
            elif p1_lista[2] == palavra_secreta[0] or p1_lista[2] == palavra_secreta[1] or p1_lista[2] == palavra_secreta[3] or p1_lista[2] == palavra_secreta[4]:
                print("AMARELO")
            else:
                print("VERMELHO")
            # Quarta letra
            if p1_lista[3] == palavra_secreta[3]:
                print("VERDE")
            elif p1_lista[3] == palavra_secreta[0] or p1_lista[3] == palavra_secreta[1] or p1_lista[3] == palavra_secreta[2] or p1_lista[3] == palavra_secreta[4]:
                print("AMARELO")
            else:
                print("VERMELHO")
            # Quinta letra
            if p1_lista[4] == palavra_secreta[4]:
                print("VERDE")
            elif p1_lista[3] == palavra_secreta[0] or p1_lista[3] == palavra_secreta[1] or p1_lista[3] == palavra_secreta[2] or p1_lista[3] == palavra_secreta[3]:
                print("AMARELO")
            else:
                print("VERMELHO")
            vidas -= 1
            print(f"Tens {vidas} vidas restantes.")
if vidas == 0:
    print("Ficaste sem vidas. GAME OVER")
