"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar os mouses, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. Foi requisitado que você desenvolva um programa em Python para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
•necessita da esfera;
•necessita de limpeza;
•necessita troca do cabo ou conector;
•quebrado ou inutilizado

Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação:                                 Quantidade   Percentual
1 - necessita da esfera                           40          40%
2 - necessita de limpeza                          30          30%
3 - necessita troca do cabo ou conector           15          15%
4 - quebrado ou inutilizado                       15          15%
"""

from exer91_chamar_menu import chamar_menu
from exer91_registrar import registrar


dic = {}
tipo_defeitos = {
    1 : '1 - necessita da esfera',
    2 : '2 - necessita de limpeza',
    3 : '3 - necessita troca do cabo ou conector',
    4 : '4 - quebrado ou inutilizado'
}
while True:
    registrar(dic, tipo_defeitos)
