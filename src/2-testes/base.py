
def validar_senha(senha):
    """
    Valida se uma senha atende aos critérios de segurança.
    Retorna True se válida, False caso contrário.
    """
    if len(senha) < 8:
        return False
    
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    
    return tem_maiuscula and tem_minuscula and tem_numero

def calcular_forca_senha(senha):
    """
    Calcula força da senha: Fraca, Média, Forte
    """
    if not validar_senha(senha):
        return "Inválida"
    
    pontos = 0
    pontos += len(senha) >= 12
    pontos += any(c in "!@#$%^&*()" for c in senha)
    pontos += len(set(senha)) > len(senha) * 0.7  # caracteres únicos
    
    if pontos >= 2:
        return "Forte"
    elif pontos == 1:
        return "Média"
    return "Fraca"
