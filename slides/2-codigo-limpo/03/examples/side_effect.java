// Função com efeito colateral inesperado
public boolean validarSenha(String senha) {
    if (senha.length() > 8) {
        // Efeito colateral: inicia sessão
        iniciarSessao();
        return true;
    }
    return false;
}