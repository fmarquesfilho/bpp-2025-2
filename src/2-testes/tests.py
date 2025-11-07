import pytest
from base import validar_senha, calcular_forca_senha

def test_senha_muito_curta():
    assert validar_senha("Ab1") == False

def test_senha_sem_maiuscula():
    assert validar_senha("senhaforte123") == False

def test_senha_sem_numero():
    assert validar_senha("SenhaForte") == False

def test_senha_valida():
    assert validar_senha("SenhaForte123") == True

def test_senha_forte():
    assert calcular_forca_senha("SenhaForte123!@#") == "Forte"

def test_senha_media():
    assert calcular_forca_senha("SenhaForte1") == "Média"

def test_senha_fraca():
    assert calcular_forca_senha("Bppppppp1") == "Fraca"

def test_senha_invalida_retorna_invalida():
    assert calcular_forca_senha("fraca") == "Inválida"
