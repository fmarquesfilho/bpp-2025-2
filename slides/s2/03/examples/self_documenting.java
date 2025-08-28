// Código autoexplicativo - melhor que comentários
public boolean isQuartoDisponivelParaReserva(Quarto quarto, Date data) {
    return !quarto.isOcupado() && 
           !existeReservaNaData(quarto, data) &&
           quarto.isAtivo();
}