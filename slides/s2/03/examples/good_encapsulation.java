// Encapsulamento adequado
public class ContaBancaria {
    private double saldo; // Privado - protegido
    
    public ContaBancaria(double saldo) {
        if (saldo >= 0) {
            this.saldo = saldo;
        }
    }
    
    public boolean sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            return true;
        }
        return false;
    }
    
    public double getSaldo() {
        return saldo;
    }
}