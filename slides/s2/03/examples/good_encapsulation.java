// Encapsulamento adequado
public class ContaBancaria {
    private double saldo;
    private String numero;
    
    public ContaBancaria(String numero, double saldoInicial) {
        if (numero == null || numero.isEmpty()) {
            throw new IllegalArgumentException("Número inválido");
        }
        this.numero = numero;
        this.saldo = Math.max(0, saldoInicial);
    }
    
    public void depositar(double valor) {
        if (valor > 0) {
            this.saldo += valor;
        }
    }
    
    public boolean sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            this.saldo -= valor;
            return true;
        }
        return false;
    }
    
    public double getSaldo() {
        return saldo;
    }
}