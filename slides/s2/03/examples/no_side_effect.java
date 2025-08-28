// Separação clara de responsabilidades
public boolean autenticarUsuario(String usuario, String senha) {
    return validarCredenciais(usuario, senha);
}

public void iniciarSessaoSeAutenticado(String usuario, String senha) {
    if (autenticarUsuario(usuario, senha)) {
        iniciarSessao(usuario);
    }
}