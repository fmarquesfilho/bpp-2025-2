# problema1.py - Exemplo com múltiplos code smells
import os
import json
import requests
from datetime import datetime

class UserManager:
    def __init__(self):
        self.users = []
        self.temp_data = {}
        
    def process_user_registration(self, name, email, password, age, address, phone, country, city, zipcode, company, department, salary, manager_email):
        # Validação (método muito longo - Long Method)
        if name == None or name == "" or len(name) < 2:
            print("Nome inválido")
            return False
        if email == None or email == "" or "@" not in email or "." not in email:
            print("Email inválido")
            return False
        if password == None or password == "" or len(password) < 8:
            print("Senha muito fraca")
            return False
        if age == None or age < 18 or age > 120:
            print("Idade inválida")
            return False
        if address == None or address == "":
            print("Endereço obrigatório")
            return False
        if phone == None or phone == "" or len(phone) < 10:
            print("Telefone inválido")
            return False
            
        # Formatação
        formatted_name = name.strip().title()
        formatted_email = email.lower().strip()
        formatted_phone = phone.replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
        
        # Cálculo de score (lógica complexa - High Complexity)
        score = 0
        if age > 25:
            score += 10
        if age > 35:
            score += 15
        if age > 45:
            score += 20
        if len(password) > 12:
            score += 5
        if any(c.isupper() for c in password):
            score += 5
        if any(c.islower() for c in password):
            score += 5
        if any(c.isdigit() for c in password):
            score += 5
        if any(c in "!@#$%^&*" for c in password):
            score += 10
        if country.lower() == "brazil":
            score += 15
        if salary > 5000:
            score += 20
        if salary > 10000:
            score += 30
            
        # Criação do objeto usuário
        user_data = {
            'id': len(self.users) + 1,
            'name': formatted_name,
            'email': formatted_email,
            'password': self.hash_password(password),
            'age': age,
            'address': address,
            'phone': formatted_phone,
            'country': country,
            'city': city,
            'zipcode': zipcode,
            'company': company,
            'department': department,
            'salary': salary,
            'manager_email': manager_email,
            'score': score,
            'created_at': datetime.now().isoformat(),
            'status': 'active',
            'verified': False
        }
        
        # Persistência
        self.users.append(user_data)
        self.save_to_file(user_data)
        self.send_welcome_email(formatted_email, formatted_name)
        self.send_manager_notification(manager_email, formatted_name)
        self.log_registration(user_data)
        self.update_statistics()
        
        return True
        
    def hash_password(self, password):
        # Implementação simplificada (não use em produção!)
        return f"hash_{password}_{len(password)}"
        
    def save_to_file(self, user_data):
        # Código duplicado - Duplicate Code
        filename = "users.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing_users = json.load(f)
        else:
            existing_users = []
        existing_users.append(user_data)
        with open(filename, 'w') as f:
            json.dump(existing_users, f, indent=2)
            
    def send_welcome_email(self, email, name):
        # Simulação de envio de email
        print(f"Enviando email de boas-vindas para {email}")
        
    def send_manager_notification(self, manager_email, name):
        # Simulação de notificação
        print(f"Notificando manager {manager_email} sobre novo usuário {name}")
        
    def log_registration(self, user_data):
        # Log simples
        print(f"LOG: Usuário {user_data['name']} registrado em {user_data['created_at']}")
        
    def update_statistics(self):
        # Atualização de estatísticas
        unused_var = "esta variável não é usada"  # Dead Code
        print(f"Total de usuários: {len(self.users)}")
        
    def generate_user_report(self, user_id):
        # Código duplicado - mesmo padrão de carregamento de arquivo
        filename = "users.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing_users = json.load(f)
        else:
            existing_users = []
            
        user = None
        for u in existing_users:
            if u['id'] == user_id:
                user = u
                break
                
        if not user:
            return None
            
        # Geração do relatório
        report = f"""
        === RELATÓRIO DO USUÁRIO ===
        Nome: {user['name']}
        Email: {user['email']}
        Idade: {user['age']}
        Score: {user['score']}
        Status: {user['status']}
        Criado em: {user['created_at']}
        """
        
        # Salvar relatório
        report_filename = f"report_{user_id}.txt"
        with open(report_filename, 'w') as f:
            f.write(report)
            
        # Enviar por email
        print(f"Relatório salvo em {report_filename}")
        return report

# Classe com poucos métodos - Too Few Public Methods
class EmailValidator:
    def is_valid(self, email):
        return "@" in email and "." in email

# Função com nome inadequado - Poor Naming  
def doStuff(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

# Variável global não utilizada - Dead Code
UNUSED_CONSTANT = "Esta constante nunca é usada"

if __name__ == "__main__":
    manager = UserManager()
    
    # Teste com muitos parâmetros - Long Parameter List
    success = manager.process_user_registration(
        "João Silva", 
        "joao@email.com", 
        "senhaSegura123!", 
        30, 
        "Rua das Flores, 123", 
        "(84) 99999-9999",
        "Brazil",
        "Natal",
        "59000-000",
        "Tech Corp",
        "Desenvolvimento",
        8000,
        "manager@techcorp.com"
    )
    
    print(f"Registro {'bem-sucedido' if success else 'falhou'}")
