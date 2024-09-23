class ALU:
    def __init__(self):
        # Este es el estado interno de la ALU.
        self.result = 0

    # Operaciones aritméticas
    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        if b != 0:
            self.result = a / b
        else:
            raise ValueError("No se puede dividir por cero.")
        return self.result

    # Operaciones lógicas
    def logical_and(self, a, b):
        self.result = a & b  # Operación AND bit a bit
        return self.result

    def logical_or(self, a, b):
        self.result = a | b  # Operación OR bit a bit
        return self.result

    def logical_not(self, a):
        self.result = ~a  # Operación NOT bit a bit
        return self.result

    # Método para seleccionar operación basada en una instrucción
    def execute(self, operation, a, b=None):
        if operation == "ADD":
            return self.add(a, b)
        elif operation == "SUBTRACT":
            return self.subtract(a, b)
        elif operation == "MULTIPLY":
            return self.multiply(a, b)
        elif operation == "DIVIDE":
            return self.divide(a, b)
        elif operation == "AND":
            return self.logical_and(a, b)
        elif operation == "OR":
            return self.logical_or(a, b)
        elif operation == "NOT":
            return self.logical_not(a)
        else:
            raise ValueError(f"Operación {operation} no soportada.")

# Ejemplo de uso
alu = ALU()

# Ejecución de operaciones
print("Suma:", alu.execute("ADD", 10, 5))  # Suma 10 + 5
print("Resta:", alu.execute("SUBTRACT", 10, 5))  # Resta 10 - 5
print("Multiplicación:", alu.execute("MULTIPLY", 10, 5))  # Multiplicación 10 * 5
print("AND:", alu.execute("AND", 0b1010, 0b1100))  # AND entre dos números binarios
print("NOT:", alu.execute("NOT", 0b1010))  # NOT de un número binario
