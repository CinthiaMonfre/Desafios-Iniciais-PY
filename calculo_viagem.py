# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal
# Entrada de dados
tempo_viagem = int (valores [0])
velocidade_media = int (valores [1])
consumo_carro = 12

# Calculo de distância percorrida e litros utilizados
distancia = tempo_viagem * velocidade_media
litros = distancia / consumo_carro

# Saída de resultado em 3 casas decimais
print ("{:.3f}".format(litros))