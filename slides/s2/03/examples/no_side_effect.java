// Separação clara de responsabilidades
public boolean validarSenha(String senha) {
    return senha.length() > 8;
}

public void fazerLogin(String senha) {
    if (validarSenha(senha)) {
        iniciarSessao();
    }
}