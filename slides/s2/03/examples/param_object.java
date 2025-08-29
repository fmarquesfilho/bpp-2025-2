// Objeto de parâmetro - mais claro e flexí­vel
public class DadosUsuario {
    public String nome;
    public String email;
    public String telefone;
    public String endereco;
    public int idade;
    public boolean ativo;
    public String departamento;
}

public void criarUsuario(DadosUsuario dados) {
    // Implementação...
}

// Chamada mais clara e menos propensa a erros
DadosUsuario dados = new DadosUsuario();
dados.nome = "JoÃÂ£o";
dados.email = "joao@email.com";
criarUsuario(dados);