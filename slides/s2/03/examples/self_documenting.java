// Melhor: código autoexplicativo
public boolean isValidSocialSecurityNumber(String input) {
    String ssnPattern = "^[0-9]{3}-[0-9]{2}-[0-9]{4}$";
    return input.matches(ssnPattern);
}

// Uso claro sem necessidade de comentários
if (isValidSocialSecurityNumber(userInput)) {
    processApplication(userInput);
}