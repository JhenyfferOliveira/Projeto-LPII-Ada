import json
from os import system

def cadastro_produto(ids) -> dict:

    print("bem vindo ao cadastro de produtos!")
    id_max = max(ids)
    produto = {}
    produto["id"] = id_max + 1
    produto["nome"] = input("Digite o nome do produto a ser cadastrado: ")
    while True:
        try:
            produto["valor"] = float(input("Digite o valor do produto: "))
        except ValueError:
            print("Valor digitado incorretamente, por favor digite novamente")
        else:
            break
    while True:
        try:
            produto["quantidade"] = int(input("Digite a quantidade do produto em estoque: "))
        except ValueError:
            print("Valor digitado incorretamente, por favor digite novamente")
        else:
            break
    while True:
        especificacao = input("Digite o tipo de especificação que deseja adicionar ou S para sair: ").lower()
        if especificacao == "s":
            break
        produto[especificacao]  = input("Digite o dado da especificação: ")
    texto_descrivo = input("Caso deseje adicionar um texto descritivo, digite S: ").lower()
    if texto_descrivo == "s":
        produto["descricao"] = input("Digite o texto descritivo: ")
    system("cls")
    print("Produto cadastrado com sucesso!")
    for key, value in produto.items():
        print(f"{key}: {value}")
    return produto


def atualizar_cadastro(produtos, id_produto):
    for produto in produtos:
        if produto['id'] == id_produto:
            print("Produto encontrado. Atualize as informações:")
            
            while True:
                print("""Escolha a informação a ser atualizada:
                    1 - Nome
                    2 - Valor
                    3 - Quantidade
                    4 - Descrição
                    5 - Sair""")
                escolha = int(input("Digite o número correspondente à informação que deseja atualizar: "))

                if escolha == 5:
                    break
                elif escolha == 1:
                    produto["nome"] = input("Digite o novo nome do produto: ")
                elif escolha == 2:
                    produto["valor"] = float(input("Digite o novo valor do produto: "))
                elif escolha == 3:
                    produto["quantidade"] = int(input("Digite a nova quantidade do produto em estoque: "))
                elif escolha == 4:
                    texto_descrivo = input("Digite o novo texto descritivo ou 'S' para manter o mesmo: ").lower()
                    if texto_descrivo != "s":
                        produto["descricao"] = texto_descrivo
                else:
                    print("Opção inválida. Tente novamente.")

            print("Cadastro atualizado com sucesso!")
            return
    
    print("Produto não encontrado.")


def consultar_produto(produtos, produto_consultar):
    while True:
        chave_consult = 'id' if produto_consultar.isdigit() else 'nome'
        produto_encontrado = None

        for produto in produtos:
            if str(produto[chave_consult]) == produto_consultar:
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            print("Produto encontrado. Detalhes do produto:")
            for chave, valor in produto_encontrado.items():
                print(f"{chave.capitalize()}: {valor}")
        else:
            print("Produto não encontrado.")

        sair = input('Digite (S) para sair ou Enter para continuar a consulta ')
        if sair.upper() == 'S':
            return
        else:
            produto_consultar = input("Digite o ID ou nome do produto que deseja consultar: ")


def listar_produtos(produtos) -> None:
    if len(produtos) == 0:
        print("Não existem produtos cadastrados.")
    else:
        print('-'*5 + "Produtos cadastrados: " + '-'*5)
        for item in produtos:
            print(f"id: {item['id']}, Nome: {item['nome']}")
            
                  
def excluir_cadastro(produtos, id_produto):
    count = 0
    id_produto = int(id_produto)
    plinha = '\n'
    for id in produtos:
        if id["id"] == id_produto:
            print(f'''{plinha*2}Produto localizado!{plinha*2}> > ID: {id['id']} - Nome: {id['nome']} < <{plinha}''')
            confirmar = input(f'Você confirma a exclusão desse produto?{plinha}(Digite s para confirmar): ').lower() 
            if confirmar == 's':
                produtos.remove(id)
                count = 1
    if count == 1:
        print('Produto excluído com sucesso')
        system("cls")
        return produtos
    else:
        print('Produto não localizado.')
        return produtos


def main():
    with open(file="dados/dados_produtos.json", mode="r", encoding="utf8") as arquivo:
        data = json.load(arquivo)
    if  data:
        produtos = data
    else:
        produtos = []
    while True:
        print("""Menu principal: 
            1 - Cadastro produto
            2 - Consultar produto
            3 - Listar produtos
            4 - Atualizar produtos
            5 - Excluir cadastro
            6 - Sair""")
        escolha = int(input("Escolha uma das opções acima: "))
        system("cls")
        match escolha:
            case 1:
                ids = [i["id"] for i in produtos]
                produtos.append(cadastro_produto(ids))
            case 2:               
                produto_consultar = input("Digite o ID ou nome do produto que deseja consultar: ")
                consultar_produto(produtos, produto_consultar)
            case 3:
                listar_produtos(produtos=produtos)
            case 4:
                id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
                atualizar_cadastro(produtos, id_produto)               
            case 5:
                while True:
                    id_produto = input("Digite o ID do produto que deseja excluir: ")
                    if id_produto.isdigit():
                        id_produto = int(id_produto)
                        excluir_cadastro(produtos,id_produto)
                        break
                    else:
                        system("cls")
                        print('Erro de digitação, favor digite novamente.')
            case 6:
                with open(file="dados/dados_produtos.json", mode="w", encoding="utf8") as arquivo:
                    json.dump(produtos, arquivo, indent= 4 * " ")
                break
            case _:
                print("Opção inválida!")


if __name__ == '__main__':
    main()