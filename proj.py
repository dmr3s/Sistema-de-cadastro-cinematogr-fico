filmes = [[],[],[],[],[]]





def cadastro():
    filme = input('Qual o nome do filme?: ')
    filmes[0].append(filme)
    genero = input('Qual o gênero do filme?: ')
    filmes[1].append(genero)
    while True:
        try:
            ano = int(input('Qual o ano de lançamento do filme?: '))
            filmes[2].append(ano)
            break
        except ValueError:
            print("Insira apenas o ano, somente números")
    while True:
        try:
            nota = int(input('Qual a nota do filme?: '))
            filmes[3].append(nota)
            if nota > 10:
                print('As notas devem ir  1 a 10')
                continue
                    
            if nota <= 3:
                filmes[4].append('Ruim')
            elif nota >3 <= 7:
                filmes[4].append('Regular')
            elif nota > 7 <=10:
                filmes[4].append('Ótimo')

                break
            break
           
        except ValueError:
            print("Insira apenas a nota, somente números")

def lista():
    if len(filmes[0]) == 0:
         print('Nenhum filme encontrado: ')
    else:
        for i in range(len(filmes[0])):
            print(f'{i+1}. Filme: {filmes[0][i]}, Ano de lançamento:{filmes[2][i]}, Gênero: {filmes[1][i]}, Nota: {filmes[3][i]}, Avaliação: {filmes [4][i]}')

def deletar():
    encontrar = False
    deletado = input('Informe o nome do filme a qual deseja deletar: ')
    encontrar = True 
    for i in range(len(filmes)):
        if filmes[0] == deletado:
            conf = input(f'{i+1}. Deseja deletar {filmes[0][i]}, Ano de lançamento:{filmes[2][i]}, Gênero: {filmes[1][i]}, Nota: {filmes[3][i]}, Avaliação: {filmes [4][i]} (sim / não)')
            if conf == "sim":
                print('Filme deletado.')
                filmes[0].pop(i)
                filmes[1].pop(i)
                filmes[3].pop(i)
                filmes[2].pop(i)
                
                break
        elif not encontrar: 
             print('Filme não cadastrado no sistema: ')

def busca():

    encontrar = False
    buscar = input('Informe o nome do filme: ')

    for i in range(len(filmes)):

        if filmes[0] == buscar:
            print('Filme identificado: ')
            print(f'{i+1}. Filme: {filmes[0][i]}, Ano de lançamento:{filmes[2][i]}, Gênero: {filmes[1][i]}, Nota: {filmes[3][i]}, Avaliação: {filmes [4][i]}')
            encontrar = True 
            break

        if not encontrar: 
             print('Filme não cadastrado no sistema: ')
          
def quan():

    print('1.Quantidade de filmes presente no sistema.')
    print('2.Media das notas.')
    print('3.Gênero mais cadastrados.')
    print('4.Filmes com notas superior ou igual a 8.')
    print('5.Voltar ao menu.')
    q = input('Selecione uma opção')
    if q == 1:
        q()
    elif q == 2:
        m()
    elif q == 3:
        g()
    elif q == 4:
        oito()
    elif q == 5:
        menu()
    else:
        print('Opção invalida.')
    def q():

        quant = len(filmes[0])
        print(f'Quatidade de filmes cadastrados: {quant} ')

    def m():
        media_notas = sum(filmes[3]) / len(filmes[3])
        print(f'Média das notas dos filmes: {media_notas:.2f}')

       
    def g():
        if filmes[1]:
            mc= max(filmes[1], key=filmes[1].count)
            print(f'Gênero mais comum: {mc}')
        else:
            print('Nenhum gênero cadastrado.')

    def oito():
        for i in range(len(filmes[0])):  
            for j in range(1):  
                if filmes[3][i] < 8:
                    continue  
                print(f'{i+1}. ->  {filmes[0][i]} (Nota: {filmes[3][i]})')
def menu():
    while True:
        b ='1. Cadastrar filme. '
        c ='2. Listar filmes.'
        d ='3. Buscar filmes.'
        e= '4. Remover filme.'
        f='5. Estatisticas.'
        g='6. Sair.'
        print(b.upper())
        print(c.upper())
        print(d.upper())
        print(e.upper())
        print(f.upper())
        print(g.upper())
        try: 
            a = int(input('Selecione uma opção: '))
            if a == 1:
                cadastro()
            elif a == 2:
                lista()
            elif a== 3:
                busca()
            elif a==4:
                deletar()
            elif a==5:
                quan()
            elif a == 6:
                break
        except ValueError:
            print ('digite apenas numeros')





menu()