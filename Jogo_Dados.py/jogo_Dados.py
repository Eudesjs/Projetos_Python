import random

def lancar_dado():
    return random.randint(1, 6)

def main():
    jogar_novamente = True

    while jogar_novamente:
        input("Pressione Enter para Lancar o Dado...")
        resultado = lancar_dado()
        print("O Dado Mostra: ", resultado)

        jogar_novamente = input("Deseja Lancar o Dado Novamente? (S/N): ").lower() == 's'

    print("Obrigado por Jogar!")

if __name__ == "__main__":
    main()