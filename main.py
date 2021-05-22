# Programa de alinhamento de strings
 
def init_matrix(M, N):
    
    """ O user entra duas strings e a funcao devolve uma matriz de comparacoes
        dessas duas strings"""
    
    # variaveis alteradas para melhor identificacao linhas/colunas
    n_linhas = len(M)+1
    n_colunas = len(N)+1
    
    # criar matriz com todas as entradas a zero
    C = [[0]*n_colunas for _ in range(n_linhas)]
   
    # preparar valores laterais
    
    # valores horizontais
    n = 0
    for i in range(0, n_linhas):
        C[i][0] = n
        n -= 1
        
    # valores verticais
    n = 0
    for j in range(0, n_colunas):
        C[0][j] = n
        n -=1
    return C
 
 
def fill_matrix(M, N, C):
    
    """ O user entra duas strings e a matriz inicial de comparacoes, e a 
        funcao devolve a mesma matriz preenchida"""
    
    # variaveis alteradas para melhor identificacao linhas/colunas
    n_linhas = len(M)+1
    n_colunas = len(N)+1
    
    # chamar funcao anterior para mais facil entrada de dados
    C = init_matrix(M, N)
    
    # criterios para preenchimento das entradas da matriz
    for i in range(0, n_linhas-1):
        for j in range(0, n_colunas-1):
            if M[i] == N[j]:
                C[i+1][j+1] = C[i][j] + 1
            else:
                C[i+1][j+1] = C[i][j] - 1
            C[i+1][j+1] = max(C[i+1][j]-1, C[i][j+1]-1, C[i+1][j+1])
 
    return C
 
def path_in_matrix(M, N, C):
    
    """ O user entra duas strings e a matriz de comparacoes preenchida, e a 
        funcao devolve uma lista com o melhor caminho para o alinhamento  """
    
    # atribuicao de menos um valor as linhas e colunas da matriz para nao 
    # exceder os limites da matriz
    i = len(M)-1
    j = len(N)-1
    
    # chamar funcao anterior para mais facil entrada de dados na consola
    C = fill_matrix(M, N, C)
    
    # criar um vetor com a ultima posicao
    P = [(i+1, j+1)]
    
    # criterios para encontrar as posicoes ideais para o alinhamento das strs
    while i >= 0 or j >= 0:
        
        if (C[i+1][j+1] == C[i][j] + 1) and (C[i][j] >= 0):
            P = [(i, j)] + P
            i, j = i-1, j-1
 
        elif (C[i+1][j+1] == C[i][j+1] - 1):
            P = [(i, j+1)] + P
            i = i - 1
        
        elif (C[i+1][j+1] == C[i+1][j] - 1):
            P = [(i+1, j)] + P
            j = j-1
        
    return P
 
def align_by_matrix(M, N, P):
    
    """ O user entra duas strings e a respetiva lista com o melhor
        alinhamento, e a funcao devolve as duas strings alinhadas"""
    
    # preparar strings que serao retornadas pela funcao alinhadas
    m = ''
    n = ''
    
    # chamar funcoes anteriores para mais facil entrada de dados na consola
    C = init_matrix(M, N)
    C = fill_matrix(M, N, C)
    P = path_in_matrix(M, N, C)
    
    # criterios para o alinhamento de strings
    k = len(P)
    for i in range(1, k):
        if P[i][0] == P[i-1][0]:
            m = m + '-'
        else:
            m = m + M[P[i-1][0]]
 
        if P[i][1] == P[i-1][1]:
            n = n + '-'
        else:
            n = n + N[P[i-1][1]]
 
    return m, n
 
def align_sequences(M, N):
    """ O user apenas entra as duas strings e a funcao devolve as mesmas
        alinhadas e o valor do alinhamento obtido """
    
    # chamar funcoes anteriores para mais facil entrada de dados na consola
    C = init_matrix(M, N)
    C = fill_matrix(M, N, C)
    P = path_in_matrix(M, N, C)
    
    # atribuicao das strs calculadas
    m, n = align_by_matrix(M, N, P)
    
    # retorno das strings alinhadas e valor do alinhamento
    return ((m, n), C[len(M)][len(N)])