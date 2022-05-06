'''PROGRAMA MERCADINHO'''
 
prod = []
 
def main():
    menu()
 
 
def menu():  # Menu de opcoes
    tituloTxt('| MERCADINHO DO GLAUCIO |')
    print('1. Vender\n2. Cadastro\n3. Listar\n4. Apagar Cadastro')
    op1 = int(input('Escolher Opção (1 a 4): '))
    while op1 < 1 or op1 > 4: 
        print('Erro: Essa opcao nao existe!')
        while True:
            try:
                op1 = int(input('Escolher Opção (1 a 4): '))
                break
            except ValueError:
                print('Erro: Digite apenas Números!')
        if op1 > 0 and op1 < 5:
            break
                                  
    if op1 == 1:
        pagamento()
    elif op1 == 2:
        cadastroProdutos()
    elif op1 == 3:
        listarProdutos()
    elif op1 == 4:              
        apagarProdutos()   
                 
 
def tituloTxt(str1):  # Titulo especial
    print('=' * len(str1))
    print(str1)
    print('=' * len(str1))
 
 
def pagamento():  # Calculo do pagamento com troco
    tituloTxt('| Processo de Compra |')
    global prod
    pagl = []
    while True:
        cod = int(input('Código do Produto: '))    
        if cod not in prod[::3]:
            while True:
                print('Erro: Produto não cadastrado!')
                cod = int(input('Código do Produto: '))
                if cod in prod[::3]:
                    break

        pagl.append(prod[prod.index(cod)])
        pagl.append(prod[prod.index(cod) + 1])
        pagl.append(prod[prod.index(cod) + 2])
 
        a = pagl[::3]
        b = pagl[1::3]
        c = pagl[2::3]
        totalpag = 0
        for i in range(int(len(pagl) / 3)):
            print(f'| Cod: {a[i]:<3} | Produto: {b[i]:<15} | Preço: R$ {c[i]:<6.2f}|')
            totalpag += c[i]
 
        opc1 = input('Continuar Comprando? (S/N): ').upper()[0]
        if opc1 == 'N':
            break
 
    print(f'Total a Pagar: R$ {totalpag}')
    pag = float(input('Efetuar Pagamento: R$ '))
    troco = pag - totalpag
    print(f'Troco: R$ {troco:.2f}')
 
    menu()
 
 
def cadastroProdutos():  # Cadastro dos produtos
    tituloTxt('|Cadastre Seus Produtos|')
    global prod 
    while True:
        cod = int(input('Código do Produto: '))
        while cod in prod[::3]:
            print('Este código já existe!')
            cod = int(input('Código do Produto:  ')) 
            if cod not in prod[::3]:
              break    
        desc = str(input('Descrição: '))
        while desc in prod[1::3]:
            print('Este produto já existe!')
            desc = (input('Descrição:  '))
            if desc not in prod[1::3]:
              break     
        prec = float(input('Preço: '))
        prod.append(cod)
        prod.append(desc)
        prod.append(prec)
        opc = input('Continuar? (S/N): ').upper()[0]
        if opc == 'N':
            break
    menu()
 
 
def listarProdutos():  # Lista de produtos cadastrados.
    global prod
    tituloTxt('| Lista de Produtos |')
    a = prod[::3]
    b = prod[1::3]
    c = prod[2::3]
    for i in range(int(len(prod) / 3)):
        print(f'| Cod: {a[i]:<3} | Produto: {b[i]:<15} | Preço: R$ {c[i]:<6.2f}|')
    menu()
 
 
def apagarProdutos():  # Apagar cadastro pelo codigo.
    tituloTxt('| Apagar Produto |')
    global prod
    while True:
        cod = int(input('Codigo do produto a deletar: '))
        if cod not in prod[::3]:
          while True:
            print('Erro: Produto não está cadastrado ou já foi apagado!')
            cod = int(input('Codigo do produto a deletar: '))
            if cod in prod[::3]:
              break
             
        del prod[prod.index(cod) + 2]
        del prod[prod.index(cod) + 1]
        del prod[prod.index(cod)]
        opc1 = input('Produto foi apagado!, Continuar? (S/N): ').upper()[0]
        if opc1 == 'N':
            break
    menu()
  
main()