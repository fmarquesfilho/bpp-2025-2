import pytest
from base import Produto, CarrinhoDeCompras

def test_adicionar_produto_quantidade_valida():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 50.0, "Roupas")
    
    carrinho.adicionar_produto(produto, 2)
    
    assert len(carrinho.itens) == 1
    assert carrinho.itens[0]['produto'] == produto
    assert carrinho.itens[0]['quantidade'] == 2

def test_adicionar_produto_quantidade_invalida():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 50.0, "Roupas")
    
    with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
        carrinho.adicionar_produto(produto, 0)
    
    with pytest.raises(ValueError, match="Quantidade deve ser maior que zero"):
        carrinho.adicionar_produto(produto, -1)

def test_calcular_subtotal_carrinho_vazio():
    carrinho = CarrinhoDeCompras()
    
    assert carrinho.calcular_subtotal() == 0

def test_calcular_subtotal_multiplos_produtos():
    carrinho = CarrinhoDeCompras()
    produto1 = Produto("Camiseta", 50.0, "Roupas")
    produto2 = Produto("Calça", 100.0, "Roupas")
    
    carrinho.adicionar_produto(produto1, 2)
    carrinho.adicionar_produto(produto2, 1)
    
    assert carrinho.calcular_subtotal() == 200.0  # 50*2 + 100*1

def test_aplicar_desconto_desc10():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 1)
    
    total_com_desconto = carrinho.aplicar_desconto("DESC10")
    
    assert total_com_desconto == 90.0  # 100 * 0.9

def test_aplicar_desconto_desc20():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 1)
    
    total_com_desconto = carrinho.aplicar_desconto("DESC20")
    
    assert total_com_desconto == 80.0  # 100 * 0.8

def test_aplicar_desconto_frete_gratis():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 1)
    
    total_com_desconto = carrinho.aplicar_desconto("FRETEGRATIS")
    
    assert total_com_desconto == 100.0  # Sem desconto no subtotal

def test_aplicar_desconto_cupom_invalido():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 1)
    
    with pytest.raises(ValueError, match="Cupom inválido"):
        carrinho.aplicar_desconto("CUPOM_INVALIDO")

def test_desconto_categoria_2_produtos():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    
    carrinho.adicionar_produto(produto, 2)
    
    desconto = carrinho.calcular_desconto_categoria()
    assert desconto == 0.05  # 5% de desconto

def test_desconto_categoria_3_produtos():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    
    carrinho.adicionar_produto(produto, 3)
    
    desconto = carrinho.calcular_desconto_categoria()
    assert desconto == 0.10  # 10% de desconto

def test_desconto_categoria_5_produtos():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    
    carrinho.adicionar_produto(produto, 5)
    
    desconto = carrinho.calcular_desconto_categoria()
    assert desconto == 0.15  # 15% de desconto

def test_desconto_categoria_maximo():
    carrinho = CarrinhoDeCompras()
    produto1 = Produto("Camiseta", 100.0, "Roupas")
    produto2 = Produto("Tênis", 200.0, "Calçados")
    produto3 = Produto("Livro", 50.0, "Livros")
    
    # Adiciona produtos suficientes para ultrapassar 30%
    carrinho.adicionar_produto(produto1, 5)  # 15%
    carrinho.adicionar_produto(produto2, 5)  # +15% = 30%
    carrinho.adicionar_produto(produto3, 5)  # +15% mas limitado a 30%
    
    desconto = carrinho.calcular_desconto_categoria()
    assert desconto == 0.30  # máximo de 30%

def test_finalizar_compra_carrinho_vazio():
    carrinho = CarrinhoDeCompras()
    
    with pytest.raises(ValueError, match="Carrinho vazio"):
        carrinho.finalizar_compra()

def test_finalizar_compra_sem_cupom():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 2)
    
    resultado = carrinho.finalizar_compra()
    
    assert resultado['subtotal'] == 200.0
    assert resultado['desconto_categoria'] == 0.05  # 2 produtos = 5%
    assert resultado['total'] == 190.0  # 200 * 0.95

def test_finalizar_compra_com_cupom():
    carrinho = CarrinhoDeCompras()
    produto = Produto("Camiseta", 100.0, "Roupas")
    carrinho.adicionar_produto(produto, 2)
    
    resultado = carrinho.finalizar_compra("DESC10")
    
    assert resultado['subtotal'] == 180.0  # 200 * 0.9
    assert resultado['desconto_categoria'] == 0.05  # 2 produtos = 5%
    assert resultado['total'] == 171.0  # 180 * 0.95
