def mensagemsinal(): 
    print("vamos verificar como esta o semáfaro")
    print("exemplo.")
    print("1 = verde")
    print("2 = amarelo")
    print("3 = vermelho")

    semafaro = int(input("digite o numero da cor que esta o semafaro \n"))

    if semafaro == 3:
        print("🚫  PARE E ESPERE O SINAL VERDE 🚫 🚷 \n")

    elif semafaro == 2:
      print("⚠️  ⚠️ ⚠️  DIMINUA A VELOCIDADE E AUMENTE A ATENÇÃO    ⚠️   ⚠️  ⚠️ \n")

    elif semafaro == 1:
        print("PODE CONTINUAR PROSSEGUINDO 🆗 \n")

    else:
        print("VC DIGITOU O NÚMERO ERRADO, VOLTE  E TENTE OS NUMEROS DE 1 ATE 3!!")




mensagemsinal()

    