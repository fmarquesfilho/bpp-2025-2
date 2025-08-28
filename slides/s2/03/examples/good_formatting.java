// Formatação adequada - fácil de ler
public class Cliente {
    private String nome;
    private int idade;
    
    public Cliente(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public String getNome() {
        return nome;
    }
}