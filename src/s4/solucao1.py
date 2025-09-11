# solucao1.py - Versão refatorada
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import json
import os

@dataclass
class UserData:
    name: str
    email: str
    age: int
    address: str
    phone: str
    country: str
    city: str
    zipcode: str
    company: str
    department: str
    salary: float
    manager_email: str

@dataclass  
class User:
    id: int
    name: str
    email: str
    password_hash: str
    age: int
    score: int
    created_at: str
    status: str = 'active'
    verified: bool = False

class UserValidator:
    """Responsável pela validação de dados de usuário"""
    
    def validate(self, user_data: UserData) -> bool:
        """Valida todos os dados do usuário"""
        return (
            self._validate_name(user_data.name) and
            self._validate_email(user_data.email) and
            self._validate_age(user_data.age) and
            self._validate_phone(user_data.phone)
        )
    
    def _validate_name(self, name: str) -> bool:
        return name and len(name.strip()) >= 2
    
    def _validate_email(self, email: str) -> bool:
        return email and "@" in email and "." in email
        
    def _validate_age(self, age: int) -> bool:
        return 18 <= age <= 120
        
    def _validate_phone(self, phone: str) -> bool:
        return phone and len(phone.replace("-", "").replace(" ", "")) >= 10

class ScoreCalculator:
    """Calcula score do usuário baseado em critérios"""
    
    def calculate(self, user_data: UserData, password: str) -> int:
        score = 0
        score += self._age_score(user_data.age)
        score += self._password_score(password)
        score += self._location_score(user_data.country)
        score += self._salary_score(user_data.salary)
        return score
    
    def _age_score(self, age: int) -> int:
        if age > 45:
            return 45
        elif age > 35:
            return 25  
        elif age > 25:
            return 10
        return 0
    
    def _password_score(self, password: str) -> int:
        score = 0
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
        return score
    
    def _location_score(self, country: str) -> int:
        return 15 if country.lower() == "brazil" else 0
        
    def _salary_score(self, salary: float) -> int:
        if salary > 10000:
            return 50
        elif salary > 5000:
            return 20
        return 0

class UserRepository:
    """Gerencia persistência de usuários"""
    
    def __init__(self, filename: str = "users.json"):
        self.filename = filename
    
    def save(self, user: User) -> None:
        users = self._load_users()
        users.append(user.__dict__)
        self._save_users(users)
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        users = self._load_users()
        for user_data in users:
            if user_data['id'] == user_id:
                return User(**user_data)
        return None
    
    def _load_users(self) -> List[dict]:
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)
    
    def _save_users(self, users: List[dict]) -> None:
        with open(self.filename, 'w') as f:
            json.dump(users, f, indent=2)

class NotificationService:
    """Serviço de notificações por email"""
    
    def send_welcome_email(self, email: str, name: str) -> None:
        print(f"Enviando email de boas-vindas para {email}")
    
    def send_manager_notification(self, manager_email: str, name: str) -> None:
        print(f"Notificando manager {manager_email} sobre novo usuário {name}")

class UserManager:
    """Orquestra o processo de registro de usuários"""
    
    def __init__(self):
        self.validator = UserValidator()
        self.score_calculator = ScoreCalculator()
        self.repository = UserRepository()
        self.notification_service = NotificationService()
        self._user_counter = 0
    
    def register_user(self, user_data: UserData, password: str) -> bool:
        """Registra um novo usuário no sistema"""
        if not self.validator.validate(user_data):
            return False
        
        score = self.score_calculator.calculate(user_data, password)
        
        user = User(
            id=self._get_next_id(),
            name=user_data.name.strip().title(),
            email=user_data.email.lower().strip(),
            password_hash=self._hash_password(password),
            age=user_data.age,
            score=score,
            created_at=datetime.now().isoformat()
        )
        
        self.repository.save(user)
        self.notification_service.send_welcome_email(user.email, user.name)
        self.notification_service.send_manager_notification(
            user_data.manager_email, 
            user.name
        )
        
        return True
    
    def _get_next_id(self) -> int:
        self._user_counter += 1
        return self._user_counter
    
    def _hash_password(self, password: str) -> str:
        return f"hash_{password}_{len(password)}"

if __name__ == "__main__":
    user_data = UserData(
        name="João Silva",
        email="joao@email.com", 
        age=30,
        address="Rua das Flores, 123",
        phone="(84) 99999-9999",
        country="Brazil",
        city="Natal", 
        zipcode="59000-000",
        company="Tech Corp",
        department="Desenvolvimento",
        salary=8000,
        manager_email="manager@techcorp.com"
    )
    
    manager = UserManager()
    success = manager.register_user(user_data, "senhaSegura123!")
    print(f"Registro {'bem-sucedido' if success else 'falhou'}")
