while True:
    name = input("Informe a base de conversão B para binário, O para octal e H para hexadecimal, ou N para Sair: ")
    exp = name.upper()
    
    if exp == 'B':
        print("binario")
        num = int(input("informe um numero decimal: "))
        binario = bin(num)
        print(f"O numero {num} em bináro é: " + binario[2::])
            
    elif exp == 'O':
        print("octal") 
        num = int(input("informe um numero decimal: "))
        octal = oct(num)
        print(f'O numero {num} em octal é: '+ octal[2::])
        continue
    
    elif exp == 'H':
        print("hexadecimal")
        num = int(input("Informe um numero decimal: "))
        hexa = hex(num)
        print(f'O numéro {num} em hexadecimal é: ' + hexa[2::])
        continue
    
    elif exp == 'N':
        cont = input("deseja realmente sair [S]im ou [N]ão ?: ")
        nai = cont.upper()
        if nai == 'S':
            break
        elif nai != 'S' or nai != 'N':
            print("sim ou não")
        else:
            continue
    else:
        print("Informe somente as opções informadas ! ")
        continue

        
