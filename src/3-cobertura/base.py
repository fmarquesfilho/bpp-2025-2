
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
    
    def adicionar_produto(self, produto, quantidade=1):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        
        self.itens.append({
            'produto': produto,
            'quantidade': quantidade
        })
    
    def calcular_subtotal(self):
        return sum(item['produto'].preco * item['quantidade'] 
                   for item in self.itens)
    
    def aplicar_desconto(self, codigo_cupom):
        subtotal = self.calcular_subtotal()
        
        if codigo_cupom == "DESC10":
            return subtotal * 0.90
        elif codigo_cupom == "DESC20":
            return subtotal * 0.80
        elif codigo_cupom == "FRETEGRATIS":
            # Desconto só no frete, não no subtotal
            return subtotal
        else:
            raise ValueError("Cupom inválido")
    
    def calcular_desconto_categoria(self):
        """Aplica desconto progressivo por categoria"""
        categorias = {}
        
        for item in self.itens:
            cat = item['produto'].categoria
            if cat not in categorias:
                categorias[cat] = 0
            categorias[cat] += item['quantidade']
        
        desconto_total = 0
        for cat, qtd in categorias.items():
            if qtd >= 5:
                desconto_total += 0.15
            elif qtd >= 3:
                desconto_total += 0.10
            elif qtd >= 2:
                desconto_total += 0.05
        
        return min(desconto_total, 0.30)  # máximo 30%
    
    def finalizar_compra(self, codigo_cupom=None):
        if not self.itens:
            raise ValueError("Carrinho vazio")
        
        subtotal = self.calcular_subtotal()
        
        if codigo_cupom:
            subtotal = self.aplicar_desconto(codigo_cupom)
        
        desconto_categoria = self.calcular_desconto_categoria()
        total = subtotal * (1 - desconto_categoria)
        
        return {
            'subtotal': subtotal,
            'desconto_categoria': desconto_categoria,
            'total': total
        }
