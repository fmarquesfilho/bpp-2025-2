# problema2.py - Exemplo com Dead Code
import sys
import os
from datetime import datetime, timedelta

# Constante nunca usada
UNUSED_CONFIG = {
    'timeout': 30,
    'retries': 3,
    'debug': True
}

class DataProcessor:
    def __init__(self):
        self.data = []
        self.backup_data = []  # nunca usado
        self.temp_storage = {}
        
    def process_data(self, items):
        """Processa lista de itens"""
        result = []
        for item in items:
            processed = self._transform_item(item)
            result.append(processed)
        return result
        
    def _transform_item(self, item):
        """Transforma um item individual"""
        return item.upper() if isinstance(item, str) else str(item)
        
    def _backup_data(self, data):
        """Método nunca chamado"""
        self.backup_data = data.copy()
        print("Backup realizado")
        
    def _legacy_method(self):
        """Método antigo que não é mais usado"""
        old_format = "formato antigo"
        return old_format
        
    def get_stats(self):
        """Retorna estatísticas"""
        unused_var = "esta variável não é usada"
        return {
            'total': len(self.data),
            'processed_at': datetime.now()
        }

def old_utility_function(x, y):
    """Função que não é mais chamada"""
    return x + y * 2

def another_unused_function():
    """Outra função nunca usada"""
    temp = []
    for i in range(10):
        temp.append(i * 2)
    return temp

if __name__ == "__main__":
    processor = DataProcessor()
    data = ["hello", "world", 123, "python"]
    result = processor.process_data(data)
    print(f"Resultado: {result}")
    print(f"Stats: {processor.get_stats()}")