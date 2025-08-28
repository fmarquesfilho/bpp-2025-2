// Função com efeito colateral inesperado
public boolean autenticarUsuario(String usuario, String senha) {
    if (validarCredenciais(usuario, senha)) {
        // Efeito colateral: inicia sessão
        iniciarSessao(usuario);
        return true;
    }
    return false;
}