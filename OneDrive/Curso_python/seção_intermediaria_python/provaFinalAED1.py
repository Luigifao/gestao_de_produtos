def inclusao_de_prod (database):
  global cod_produto, valor_prod, contador, dic_pra_add 
  cod_produto = input("Digite o código do produto: ")
  if any(cod_produto in d for d in lista_de_prod):
    print("Produto já cadastrado ! ")
    return
  else:
    valor_prod = input("Digite o valor do produto: ")
    print("Produto cadastrado ! ")
    dic_pra_add["codigo"] = cod_produto
    dic_pra_add["valor"] = valor_prod
    dic_pra_add["database"] = database
    lista_de_prod.append(dic_pra_add) 
    dic_pra_add = ""
    return

#------------------------------------------------------------------------------#

def exclusao_de_prod():
  global contador, cod_produto, valor_prod
  verifi_cod_prod = input("Digite o código do produto: ")
  for produto in lista_de_prod:
    if verifi_cod_prod in produto.values():
       opcao = input("Produto encontrado! \nDeseja excluir? ")
       if opcao.lower()  == "sim":
        lista_de_prod.remove(produto)
        print("Produto excluído ! ")
        return
       elif opcao.lower == "nao":
         print("Voltando para o menu")
         return
    else:
      continue
  print("Produto não encontrado!")

  return

#------------------------------------------------------------------------------#

def atuali_de_prod(database):
  verifi_cod_prod = input("Digite o código do produto: ")
  for produto in lista_de_prod:
    if verifi_cod_prod in produto.values():
      novo_valor = input("Produto encontrado!\nDigite o novo valor para atualizar: ")
      produto["valor"] = novo_valor
      produto["database"] = database
      print("Produto atualizado com sucesso! \nVoltando para o menu principal\n")
      return
    else:
      continue

  print("Produto não encontrado!\nVoltando para o menu principal\n")
  return
  
#------------------------------------------------------------------------------#

def pesqui_de_prod():
  codigo_para_pesquisar = input("Digite o código do produto que deseja buscar: ")
  for produto in lista_de_prod:
    if codigo_para_pesquisar in produto.values():
      print("Bem encontrado !\n")
      print("código = ",produto["codigo"])   
      print("Valor = ",produto["valor"])
      print("Data da última alteração = ",produto["database"])
      print("Voltando para o menu principal\n")
      return
    else:
      continue
  print("Produto não encontrado !\nVoltando ao menu principal")
  return


#------------------------------------------------------------------------------#
    
def listagem_de_bem():
  lista_ordenada = sorted(lista_de_prod, key=lambda d: d["valor"])
  for produto in lista_ordenada:
    print("código = ",produto["codigo"])
    print("valor = ",produto["valor"])
    print("data da última alteração = ",produto["database"],"\n")
  
  print("Fim ! \nVoltando ao menu principal")
  return

#------------------------------------------------------------------------------#

opcao = 0
lista_de_prod = []
dic_pra_add = {

}
while (opcao != 6):
  print()
  print("Digite a ação que vc deseja do programa: ")
  print("1- Inclusão de produto")
  print("2- Exclusão do produto")
  print("3- Atualização do produto")
  print("4- Pesquisa do produto")
  print("5- Listagem dos produtos")
  print("6- Sair do programa")
  opcao = input("Opção: ")
  print()
  if (opcao == "6"):
    break
   
  elif (opcao == "1"):
    database = input("Por favor, antes nos informe a data base: ")
    inclusao_de_prod(database)

  elif (opcao == "2"):
    exclusao_de_prod()

  elif (opcao == "3"):
    database = input("Por favor, antes nos informe a data base: ")
    atuali_de_prod(database)

  elif (opcao == "4"):
    pesqui_de_prod()

  elif (opcao == "5"):
    listagem_de_bem(lista_de_prod)
