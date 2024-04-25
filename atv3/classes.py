class Estoque:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print("Produto adicionado ao estoque:", produto)

    def remover_produto(self, produto):
        if produto in self.itens:
            self.itens.remove(produto)
            print("Produto removido:", produto)
            #deveria ter um else aqui
        else:
            print("Produto não encontrado no estoque.")

    def exibir_estoque(self):
        print("Estoque:")
        for produto in reversed(self.itens):
            print(produto)

    def vazio(self):
        return len(self.itens) == 0



class Pedidos:
    def __init__(self, estoque, vendas): #novo, adicionado o vendas como parametro
        self.pedidos = []
        self.estoque = estoque
        self.vendas = vendas #novo

    def registrar_pedido(self, produto):
        self.pedidos.append(produto)

    def processar_pedido(self):
        if not self.estoque.vazio():
            if self.pedidos:
                produto = self.pedidos.pop(0)
                if produto in self.estoque.itens:
                    self.estoque.remover_produto(produto)
                    print("Pedido processado:", produto)
                    print("Obrigado pela compra")
                    self.vendas.registrar_venda(produto, self.estoque)  #novo, passa o pedido para vendas
                else:
                    print("Produto não encontrado no estoque.")
            else:
                print("Não há pedidos para processar.")
        else:
            print("Não é possível processar o pedido. Estoque vazio.")

    def exibir_pedidos(self):
        print("Pedidos:")
        for produto in self.pedidos:
            print(produto)



class Vendas:
    def __init__(self):
        self.pilha = []

    def registrar_venda(self, produto, estoque):
        if produto:
            self.pilha.append(produto)
            estoque.remover_produto(produto)  #novo, remove do estoque o produto falado
            print("Venda registrada:", produto)
        else:
            print("Não é possível fazer a venda. Produto inválido.")

    def desfazer_venda(self, estoque):
        if self.pilha:
            produto = self.pilha.pop()
            estoque.adicionar_produto(produto)  #novo, adiciona o produto no estoque novamente
            print("Venda desfeita:", produto)
        else:
            print("Não há vendas para desfazer.")

    def exibir_vendas(self):
        print("Vendas:")
        for produto in reversed(self.pilha):
            print(produto)