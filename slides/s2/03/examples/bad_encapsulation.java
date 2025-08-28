// Violação do encapsulamento
public class ContaBancaria {
    public double saldo; // Público - perigoso!
    
    public ContaBancaria(double saldo) {
        this.saldo = saldo;
    }
}

// Uso perigoso
ContaBancaria conta = new ContaBancaria(1000);
conta.saldo = -500; // Permite saldo negativo!