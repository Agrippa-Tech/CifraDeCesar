import random
import time
import os

'''X1 = Entrada em texto claro
   K = Chave 
   Y = Texto cifrado, (Y = E(K,X))
   X2 = Texto decriptado, (X = D(K,Y))'''

componentes_frases_cifradas = {
    'sujeito': [
        'O gato', 'O cachorro', 'Maria', 'João', 'A professora',
        'O aluno', 'A criança', 'O médico', 'A enfermeira', 'O motorista'
    ],
    'verbo': [
        'correu', 'pulou', 'estudou', 'trabalhou', 'comeu', 'dormiu',
        'cantou', 'dançou', 'escreveu', 'leu',
    ],
    'complemento': [
        'no parque', 'em casa', 'na escola', 'rapidamente', 'muito bem',
        'com alegria', 'ontem', 'hoje cedo', 'à noite', 'pela manhã'
    ]
}

while True:
    tentativas_menu_programa = 4
    while tentativas_menu_programa > 0:
        try:
            print("\n" + "=" * 40," CIFRA DE CÉSAR ","=" * 40)
            
            print()
            print(f"{'[1] Encriptar mensagem:':<50}")
            print(f"{'[2] Decriptar mensagem:':<50}")
            print(f"{'[3] Quebrar cifra manualmente:':<50}")
            print(f"{'[4] Testar todas as chaves:':<50}")
            print(f"{'[5] Sair':<50}")
                        
            opcao_menu = int(input("\nEscolha uma opção: "))
            
            if opcao_menu == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                plaintext_X1 = input("\nDigite a mensagem a ser encriptada: ")
                chave_K = int(input("Digite a chave [0-25]: "))
                
                if not (0 <= chave_K <= 25):
                    raise ValueError      
            
                plaintext_X2 = ""
                for letra in plaintext_X1:
                    if letra.isalpha():
                        conversao_alpha_ascii = ord('A') if letra.isupper() else ord('a')
                        conversao_ascii_alpha = chr((ord(letra) - conversao_alpha_ascii + chave_K) % 26 + conversao_alpha_ascii)
                        plaintext_X2 += conversao_ascii_alpha
                    else:
                        plaintext_X2 += letra
                print(f"\nTexto cifrado: {plaintext_X2}")
                input("\nPressione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
            
            elif opcao_menu == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                plaintext_X1 = input("\nDigite a mensagem a ser decriptada: ")
                chave_K = int(input("Digite a chave [0-25]: "))
                
                if not (0 <= chave_K <= 25):
                    raise ValueError
                
                plaintext_X2 = ""
                for letra in plaintext_X1:
                    if letra.isalpha():
                        conversao_alpha_ascii = ord('A') if letra.isupper() else ord('a')
                        conversao_ascii_alpha = chr((ord(letra) - conversao_alpha_ascii - chave_K) % 26 + conversao_alpha_ascii)
                        plaintext_X2 += conversao_ascii_alpha
                    else:
                        plaintext_X2 += letra
                print(f"\nTexto decifrado: {plaintext_X2}")
                input("\nPressione Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

            
            elif opcao_menu == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                frase_aleatoria_Y = ""
                chave_K = random.randint(1, 25)
                frase_aleatoria_X1 = f"{random.choice(componentes_frases_cifradas['sujeito'])} {random.choice(componentes_frases_cifradas['verbo'])} {random.choice(componentes_frases_cifradas['complemento'])}"
                for letra in frase_aleatoria_X1:
                    if letra.isalpha():
                        conversao_alpha_ascii = ord('A') if letra.isupper() else ord ('a') 
                        conversao_ascii_alpha = chr((ord(letra) - conversao_alpha_ascii + chave_K) % 26 + conversao_alpha_ascii)
                        frase_aleatoria_Y += conversao_ascii_alpha
                    else:
                        frase_aleatoria_Y += letra
                print(frase_aleatoria_Y)
                tentativa_user = input("\nDigite a mensagem decifrada: ")
                if tentativa_user == frase_aleatoria_X1:
                    print("\nParabéns!")
                    input('\nPressione Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')

                else: 
                    print("\nVocê falhou.")
                    input('\nPressione Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')

            
            elif opcao_menu == 4:  
                os.system('cls' if os.name == 'nt' else 'clear')
                
                ciphertext_Y = input("\nDigite o texto cifrado: ")
                
                print("\n", "= " * 3, "TESTANDO TODAS AS CHAVES", "= " * 3)
                for K_teste in range(26):
                    tentativa_K = ""
                    for letra in ciphertext_Y:
                        if letra.isalpha():
                            conversao_alpha_ascii = ord('A') if letra.isupper() else ord ('a')
                            conversao_ascii_alpha = chr((ord(letra) - conversao_alpha_ascii - K_teste) % 26 + conversao_alpha_ascii)
                            tentativa_K += conversao_ascii_alpha
                            time.sleep(0.01)
                        else:
                            tentativa_K += letra
                    print(f"Chave {K_teste}: {tentativa_K}")
                input('\nPressione Enter para continuar...')
                os.system('cls' if os.name == 'nt' else 'clear')

            
            elif opcao_menu == 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nAté logo!")
                exit()
            
            else:
                raise ValueError
        
        except ValueError:
            tentativas_menu_programa -= 1
            if tentativas_menu_programa == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nA última tentativa será possível em 30 segundos.")
                for i in range(30, 0, -1):
                    print(f"\r{i} segundos.", end = " ", flush = True)
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            if tentativas_menu_programa > 0:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nERRO: Digite apenas as alternativas válidas!")
                print(f"Você tem somente {tentativas_menu_programa} tentativas restantes.")
                continue
            else:
                print("\n⁴⁰⁴ Error ⁴⁰⁴: TENTATIVAS ESGOTADAS.")
                print()
                exit()
                
                       
                