# smells_examples.py
# Exemplos de code smells para análise em aula

# 1. LONG METHOD
def process_order(order_items, customer_info, payment_data, shipping_address, discount_codes):
    """Processa um pedido com múltiplas responsabilidades"""
    # Validação (15+ linhas)
    if not order_items:
        raise ValueError("Pedido vazio")
    if not customer_info.get('email'):
        raise ValueError("Email obrigatório")
    # ... mais validações
    
    # Cálculos (10+ linhas)
    subtotal = sum(item['price'] * item['quantity'] for item in order_items)
    discount = calculate_discount(subtotal, discount_codes)
    tax = calculate_tax(subtotal - discount, customer_info['state'])
    total = subtotal - discount + tax
    
    # Processamento de pagamento (8+ linhas)
    payment_result = process_payment(payment_data, total)
    if not payment_result['success']:
        raise Exception("Pagamento falhou")
    
    # Criação de registro (5+ linhas)
    order_record = create_order_record(order_items, customer_info, total)
    
    # Envio de emails (7+ linhas)
    send_confirmation_email(customer_info['email'], order_record)
    send_notification_to_admin(order_record)
    
    # Logging (3+ linhas)
    log_order_creation(order_record)
    
    return order_record

# 2. DUPLICATE CODE
def calculate_area_square(side):
    return side * side

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_triangle(base, height):
    return (base * height) / 2
# ^^ Código duplicado: cada função faz cálculo similar mas separado

# 3. POOR NAMING
def proc(d, l):  # What does this do?
    r = []
    for i in l:
        if i in d:
            r.append(d[i])
    return r

# 4. LONG PARAMETER LIST
def create_user_profile(first_name, last_name, email, phone, address, 
                       city, state, zip_code, country, date_of_birth,
                       gender, occupation, interests, preferences):
    # Muitos parâmetros!
    pass

# 5. DEAD CODE
def old_calculation_method(a, b):
    # Esta função não é mais usada
    result = a * b + 100
    return result

def new_calculation_method(a, b):
    return a * b

# A função antiga não é chamada em lugar nenhum