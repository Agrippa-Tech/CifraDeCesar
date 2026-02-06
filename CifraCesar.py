import random
import time
import os

'''X1 = Entrada em texto claro
   K = Chave 
   Y = Texto cifrado, (Y = E(K,X))
   X2 = Texto decriptado, (X = D(K,Y))'''

componentes_frases_cifradas = {
    'sujeito': [
        'Maria', 'João', 'Pedro', 'Ana', 'Carlos', 'Juliana',
        'Roberto', 'Fernanda', 'Lucas', 'Beatriz', 'Rafael', 'Camila',
        'A professora', 'O aluno', 'A médica', 'O enfermeiro', 'O motorista',
        'A engenheira', 'O artista', 'A cientista', 'A vendedora', 'O cozinheiro',
        'A bailarina', 'O pianista', 'A jornalista', 'Meu irmão', 'Minha avó',
        'O presidente', 'A diretora', 'O bombeiro', 'A advogada', 'O arquiteto',
        'A dentista', 'O policial', 'A psicóloga', 'O professor', 'A estudante',
        'O gerente', 'A secretária', 'O mecânico', 'A fotógrafa', 'O desenvolvedor',
        'A designer', 'O veterinário', 'A farmacêutica', 'O contador', 'A chef',
        'O atleta', 'A escritora', 'O músico', 'Minha mãe', 'Meu pai'
    ],
    'verbo': [
        'correu', 'pulou', 'estudou', 'trabalhou', 'comeu', 'dormiu',
        'cantou', 'dançou', 'escreveu', 'leu', 'pintou', 'desenhou',
        'viajou', 'nadou', 'dirigiu', 'cozinhou', 'limpou', 'conversou',
        'brincou', 'jogou', 'pensou', 'sorriu', 'chorou', 'gritou',
        'sussurrou', 'corrigiu', 'aprendeu', 'ensinou', 'descobriu', 'construiu',
        'plantou', 'colheu', 'pesquisou', 'inventou', 'criou', 'observou',
        'fotografou', 'filmou', 'apresentou', 'competiu', 'venceu', 'perdeu',
        'treinou', 'praticou', 'meditou', 'relaxou', 'descansou', 'organizou',
        'planejou', 'decidiu', 'comprou', 'vendeu', 'entregou', 'recebeu'
    ],
    'complemento': [
        'no parque', 'em casa', 'na escola', 'rapidamente', 'muito bem',
        'com alegria', 'ontem', 'hoje cedo', 'à noite', 'pela manhã',
        'no jardim', 'na praia', 'na montanha', 'no shopping', 'no hospital',
        'na biblioteca', 'no museu', 'no teatro', 'no cinema', 'no restaurante',
        'com entusiasmo', 'com calma', 'com pressa', 'com cuidado', 'com carinho',
        'durante a tarde', 'ao amanhecer', 'ao entardecer', 'na madrugada', 'todo dia',
        'frequentemente', 'raramente', 'sempre', 'nunca', 'às vezes',
        'silenciosamente', 'barulhentamente', 'cuidadosamente', 'apressadamente', 'elegantemente',
        'no laboratório', 'na cozinha', 'no escritório', 'na fazenda', 'na cidade',
        'com os amigos', 'sozinho', 'em grupo', 'com a família', 'com dedicação',
        'sob a chuva', 'sob o sol', 'debaixo da árvore', 'perto do rio', 'longe daqui',
        'no estádio', 'na academia', 'no consultório', 'na universidade', 'no aeroporto'
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
                tentativa_opcao_3 = 5
                tempo_tentativa_user = time.time()
                while tentativa_opcao_3 > 0:
                    tentativa_user = input("\nDigite a mensagem decifrada: ")
                    if tentativa_user == frase_aleatoria_X1:
                        tempo_tentativa_final = time.time()
                        tempo_total = tempo_tentativa_final - tempo_tentativa_user
                        print(f"\nParabéns! Você decifrou em {tempo_total:2.2f} segundos!")
                        input('\nPressione Enter para continuar...')
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    
                    else:
                        tentativa_opcao_3 -= 1
                        if tentativa_opcao_3 > 0:
                            print("\nTente novamente.")
                            print(f"Você tem {tentativa_opcao_3} tentativas.")
                            time.sleep(5)
                            os.system('cls' if os.name == 'nt' else 'clear')

                        else: 
                            tentativa_opcao_3 < 1
                            print("\nVocê falhou.")
                            input('Pressione Enter para continuar...')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
            
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
                
                       
                