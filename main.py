from Dados_analizados import Dados_estudados
from Conecta_Com_Banco import Conecta_Com_Banco
from datetime import datetime

# limpa a tela
def limpar():
    print ("\n" * 50)


def main():
        dados = Dados_estudados()         # cria o objeto Dados_estudados para pegar a funsao dessa classe
        banco = Conecta_Com_Banco()       # cria o objeto Conecta_Com_Banco para pegar a funsao dessa classe

        banco.conectando()                # conectando com o banco

        while True:
                valores = dados.atualizaDados()    # pega os valores dos sensores e atualiza no JSON
                horario = datetime.now().time()    # pega Horario do computador
                data = datetime.now().date()       # pega DATA do computador

                escolhe_banco = int(input('Escolha a alternativa do banco:\n'
                                    '   1 - Insere para o banco;\n'
                                    '   2 - Select da tabela do banco;\n'
                                    '   3 - Deleta uma linha da tabela do banco;\n'
                                    '   0 - Passar para Consulta\n'
                                    ))

                if (escolhe_banco == 1): # pega os valores do JSON e grava no banco
                        banco.insertTabela(valores["Valor_Bateria"] , valores["Estado_Bateria"] , valores["Temperatura"],valores["Frequencia"], horario , data)
                elif (escolhe_banco == 2): # seleciona o dados do banco
                        banco.selectTABELA()
                elif (escolhe_banco == 3): # seleciona o banco e escolhe o ID do elemento que vai ser DELETADO
                        banco.selectTABELA()
                        deletar = input('-----Escolha Linha que quer deletar:\n')
                        banco.deletaTABELA(deletar)
                else:
                        print(" ------------PASSANDO PARA CONSULTA -------------- ")

                        escolhe_consulta = int(input('Escolha a Consulta do banco:\n'
                                             '   1 - Maior e menor valor da coluna;\n'
                                             '   2 - Contagem dos valores que são Maior,menor,igual ou diferente a um numero de referencia;\n'
                                             '   3 - Media de uma coluna;\n'
                                             '   4 - ENTRE VALORES\n'
                                             '   5 - ENTRE datas;\n'
                                             '   6 - Maior entre Valores da bateria\n'
                                             '   0 - Não faz nenhuma consulta\n'
                                             ))
                        if(escolhe_consulta != 0 ):
                            if (escolhe_consulta != 5 and escolhe_consulta != 6):

                                Escolhe_coluna = int(input('Qual coluna?:\n'
                                                           '   1 - Valor_Bateria\n'
                                                           '   2 - Estado_bateria\n'
                                                           '   3 - Temperatura\n'
                                                           '   4 - Frequencia\n'
                                                           '   5 - Horario\n'
                                                           '   6 - Data\n'
                                                           '   0 - Não faz nenhuma consulta\n'
                                                           ))

                                if  (Escolhe_coluna == 1): coluna = "Valor_Bateria"
                                elif  (Escolhe_coluna == 2): coluna = "Estado_Bateria"
                                elif  (Escolhe_coluna == 3): coluna = "Temperatura"
                                elif  (Escolhe_coluna == 4): coluna = "Frequencia"
                                elif  (Escolhe_coluna == 5): coluna = "Horario"
                                elif  (Escolhe_coluna == 6): coluna = "Data"

                            if (escolhe_consulta == 1):
                                    banco.Maior_E_Menor(coluna)
                            if (escolhe_consulta == 2):
                                    valor = int(input('Digita o numero de referencia:\n'))
                                    operacao = int(input('Qual operação?:\n'
                                                               '   0 - Valores da tabela é IGUAL ao numero de referencia;\n'
                                                               '   1 - Valores da tabela é DIFERENTE ao numero de referencia;\n'
                                                               '   2 - Valores da tabela é MAIOR ao numero de referencia;\n'
                                                               '   3 - Valores da tabela é Menor ao numero de referencia;\n'
                                                               '   4 - Valores da tabela é MAIOR e IGUAL ao numero de referencia;\n'
                                                               '   5 - Valores da tabela é Menor e IGUAL ao numero de referencia;\n'

                                                               ))

                                    banco.contagem(coluna, operacao,valor)

                            if (escolhe_consulta == 3):
                                    banco.media(coluna)
                            if (escolhe_consulta == 4):
                                inicio = str(input('Valor inicial?:\n'))
                                fim = str(input('Valor Final?:\n'))

                                banco.entreValores(coluna,inicio,fim)
                            if (escolhe_consulta == 5):
                                inicio = str(input('Data inicial?:\n'))
                                fim = str(input('Data Final?:\n'))

                                print(banco.entreDatas(inicio,fim))
                            if (escolhe_consulta == 6):
                                banco.maiorEntreValores("0" , "11" )
                                banco.maiorEntreValores("11" , "21" )
                                banco.maiorEntreValores("21" , "31" )
                                banco.maiorEntreValores("31" , "41" )
                                banco.maiorEntreValores("41" , "51" )
                                banco.maiorEntreValores("51" , "61" )
                                banco.maiorEntreValores("61" , "71" )
                                banco.maiorEntreValores("71" , "81" )
                                banco.maiorEntreValores("81" , "91" )
                                banco.maiorEntreValores("91" , "101" )

                print("\n")
                quer_limpa = int(input('Quer Limpa a tela?:\n'
                                       '0 - não\n'
                                       '1 - sim \n' ))
                if (quer_limpa == 1):
                    limpar()



if __name__ == '__main__':
    main()



