// Violação do encapsulamento
public class ContaBancaria {
    public double saldo;
    public String numero;
}

// Uso problemático
ContaBancaria conta = new ContaBancaria();
conta.saldo = -100; // Permite saldo negativo!
conta.numero = null; // Permite dados inválidos