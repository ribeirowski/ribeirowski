#The Great Code of the Compound Fees
print('''O que você deseja fazer por aqui?
[1] Calcular o PV
[2] Calcular o FV
[3] Calcular a Taxa de Juros (i)
[4] Calcular o Período (n) 
[5] Calcular o Juros (j) ''')

while True:
        option = int((input('Bem vindo ao Menu Principal! Escolha a sua opção: ')))

        if option == 1: #PV

                print('Você escolheu a opção "Calcular o PV", vamos lá!')
                FV = float(input("Digite o valor Futuro:"))
                n = float(input("Digite o valor do Período:"))
                i = float(input("Digite o valor da Taxa de Juros:"))
                PV = float(FV / (1 + i) ** n)
                print('O seu resultado é:', round(PV, 2))

        elif option == 2: #FV

                print('Você escolheu a opção "Calcular o FV", vamos lá!')
                PV = float(input("Digite o valor Presente:"))
                i = float(input("Digite o valor da Taxa de Juros:"))
                n = float(input("Digite o Período:"))
                FV = float(PV * (1 + i) ** n)
                print('O seu resultado é:', round(FV, 2))

        elif option == 3: #i

                print('Você escolheu a opção "Calcular a Taxa de Juros (i)", vamos lá!')
                FV= float(input("Digite o valor Futuro:"))
                PV= float(input("Digite o valor Presente:"))
                n= float(input("Digite o Período:"))
                i= ((FV/PV)**(1/n))-1
                print('O seu resultado é:', round(i, 3))

        elif option == 4: #n

                print('Você escolheu a opção "Calcular o Período (n)", vamos lá!')
                import math
                FV= float(input("Digite o valor Futuro:"))
                PV= float(input("Digite o valor Presente:"))
                i= float(input("Digite o valor da Taxa de Juros:"))
                n= (math.log(FV)/math.log(PV))/math.log(1+i)
                print('O seu resultado é:', round(n, 2))

        elif option == 5: #j
                print('Você escolheu a opção "Calcular o Juros (j)", vamos lá!')

                print('''Você deseja encontrar o valor do Juros, como quer fazer isso:
                [1] Só sei o valor Presente
                [2] Só sei o valor Futuro
                [3] Sei o valor Futuro e Presente ''')

                while True:
                    option = int((input('Este é o Menu dos Juros! Escolha a sua opção: ')))

                    if option == 1:

                                        print("Para começar você vai precisar saber o PV, a Taxa de Juros e o Período")
                                        PV = float(input("Digite o valor Presente:"))
                                        i = float(input("Digite o valor da taxa de Juros:"))
                                        n = float(input("Digite o Período:"))
                                        j = float(PV * (((1 + i) ** n) - 1))
                                        print('O seu resultado é:', round(j, 2))

                    elif option == 2:

                                        print('Para começar você vai precisar saber o FV, a Taxa de Juros e o Período')
                                        FV = float(input("Digite o valor Futuro:"))
                                        i = float(input("Digite o valor da Taxa de Juros:"))
                                        n = float(input("Digite o Período:"))
                                        j = float(FV * (1 - (1 / ((1 + i) ** n))))
                                        print('O seu resultado é:', round(j, 2))

                    elif option == 3:

                                        print('Para começar você vai precisar saber o PV e o FV')
                                        PV = float(input("Digite o valor Presente:"))
                                        FV = float(input("Digite o valor Futuro:"))
                                        j = float(FV - PV)
                                        print('O seu resultado é:', round(j, 2))

                    continua = input('Você conseguiu! Agora, digite "q" para encerrar o programa ou ENTER para calcular Juros novamente:')
                    if (continua == 'q'):
                        break

        continua = input('Você quer encerrar o programa? Digite "q" para encerrar ou ENTER para voltar ao Menu Principal')
        if (continua == 'q'):
            break