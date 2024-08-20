import os
from sklearn.model_selection import train_test_split
import pandas as pd

def loadFiles(diretorio_raiz):
    """
    Carrega os caminhos dos arquivos e seus rótulos a partir das pastas de test, train e valid.
    
    Args:
        diretorio_raiz (str): O diretório raiz onde estão localizadas as pastas test, train e valid.
    
    Returns:
        (list, list, list): Tupla contendo as listas de caminhos, rótulos e nomes das classes.
    """
    caminhos = []
    rotulos = []
    classes = os.listdir(diretorio_raiz)
    
    for classe in classes:
        classe_dir = os.path.join(diretorio_raiz, classe)
        for arquivo in os.listdir(classe_dir):
            caminhos.append(os.path.join(classe_dir, arquivo))
            rotulos.append(classe)
    
    return caminhos, rotulos, classes

def division(caminhos, rotulos, test_size=0.2, val_size=0.2, random_state=42):
    """
    Divide os dados em conjuntos de treinamento, validação e teste sem estratificação.
    
    Args:
        caminhos (list): Lista de caminhos dos arquivos.
        rotulos (list): Lista de rótulos correspondentes aos caminhos dos arquivos.
        test_size (float): A proporção do conjunto de teste (padrão é 0.2).
        val_size (float): A proporção do conjunto de validação (padrão é 0.2).
        random_state (int): O estado aleatório para reprodutibilidade (padrão é 42).
    
    Returns:
        (tuple): Tupla contendo os conjuntos de treinamento, validação e teste divididos.
    """
    X_train, X_temp, y_train, y_temp = train_test_split(caminhos, rotulos, test_size=(test_size + val_size), random_state=random_state)
    
    test_ratio = test_size / (test_size + val_size)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=test_ratio, random_state=random_state)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

def countClass(caminhos, rotulos):
    """
    Conta o número de imagens por classe.
    
    Args:
        caminhos (list): Lista de caminhos dos arquivos.
        rotulos (list): Lista de rótulos correspondentes aos caminhos dos arquivos.
    
    Returns:
        dict: Dicionário com o número de imagens por classe.
    """
    num_imagens_por_classe = {}
    for rotulo in rotulos:
        if rotulo not in num_imagens_por_classe:
            num_imagens_por_classe[rotulo] = 0
        num_imagens_por_classe[rotulo] += 1
    return num_imagens_por_classe

def coutNumberClass(num_imagens_por_classe, nome_dataset):
    """
    Imprime o número de imagens por classe em um conjunto de dados.
    
    Args:
        num_imagens_por_classe (dict): Dicionário com o número de imagens por classe.
        nome_dataset (str): O nome do conjunto de dados.
    """
    print(f'Número de imagens por classe no conjunto de {nome_dataset}:')
    for classe, num_imagens in num_imagens_por_classe.items():
        print(f'Classe {classe}: {num_imagens}')
    print()

def exportCsv(diretorio_dados, arquivo_csv):
    """
    Exporta os dados de um diretório para um arquivo CSV.
    
    Args:
        diretorio_dados (str): O diretório onde os dados estão armazenados.
        arquivo_csv (str): O nome do arquivo CSV de saída.
    """
    classes = os.listdir(diretorio_dados)
    caminhos = []
    rotulos = []

    for classe in classes:
        classe_dir = os.path.join(diretorio_dados, classe)
        for arquivo in os.listdir(classe_dir):
            caminho_arquivo = os.path.join(classe_dir, arquivo)
            caminhos.append(caminho_arquivo)
            rotulos.append(classe)

    dados = pd.DataFrame({'Caminho': caminhos, 'Rótulo': rotulos})
    dados.to_csv(arquivo_csv, index=False)


diretorio_raiz = '/home/iara/pos-graduação/yolov8/dataset'

#caminhos, rotulos, classes = loadFiles(diretorio_raiz)
#
#X_train, X_val, X_test, y_train, y_val, y_test = division(caminhos, rotulos)
#
#num_imagens_por_classe_treinamento = countClass(X_train, y_train)
#num_imagens_por_classe_validacao = countClass(X_val, y_val)
#num_imagens_por_classe_teste = countClass(X_test, y_test)
#
#coutNumberClass(num_imagens_por_classe_treinamento, 'Treinamento')
#coutNumberClass(num_imagens_por_classe_validacao, 'Validação')
#coutNumberClass(num_imagens_por_classe_teste, 'Teste')
