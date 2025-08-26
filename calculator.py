import re
#DEMO
functions_derivate = [
        '2x',
        '3x**2',
        '4x**5',
        'x**3', # Caso sin coeficiente explícito
        'x',    # Caso con exponente y coeficiente 1
        '10x',
        '5',
        '9x',
        '7y**4', # Demo con otra variable
        'z'      # Demo con otra variable
]

#INPUT 
fun_input = input("Introduce una función separada por espacios (o presiona Enter para usar el demo): ")

if fun_input:
        functions_to_process = fun_input.split(' ')
else:
        functions_to_process = functions_derivate

def calculate_derivative(func_str):
        """
        Calcula la derivada de una función simple en formato 'av**b' (a=coeficiente, v=variable, b=exponente).
        Es robusta y maneja casos especiales como 'x', '3x', 'x**2'.
        Ahora acepta cualquier letra como variable.
        """
        # Si no hay ninguna letra en la cadena, es una constante.
        if not any(c.isalpha() for c in func_str):
                return "0"  # La derivada de una constante es 0

        # Usamos una expresión regular para extraer el coeficiente, la variable y el exponente.
        # Patrón: (número opcional)(letra)(**número opcional)
        match = re.match(r"(\d*)([a-zA-Z])(?:\*\*(\d+))?", func_str)
       
        if not match:
                return "Formato no válido"

        coeff_str, var, exp_str = match.groups()

        try:
            # Si no hay número antes de la variable, el coeficiente es 1.
            coefficient = int(coeff_str) if coeff_str else 1
            # Si no hay '**', el exponente es 1.
            exponent = int(exp_str) if exp_str else 1
        except ValueError:
            # Aunque la regex actual previene este error, es una buena práctica de
            # programación defensiva para futuras modificaciones.
            return "Coeficiente o exponente no es un entero válido"

        # Regla de la potencia: (a*v^b)' = (a*b)*v^(b-1) donde v es la variable
        new_coefficient = coefficient * exponent
        new_exponent = exponent - 1

        # --- Formateo de salida mejorado ---

        # Si el nuevo coeficiente es 0, la derivada es 0 (ej. (5x**0)' -> 0)
        if new_coefficient == 0:
            return "0"

        # Si el nuevo exponente es 0, el resultado es solo el coeficiente (ej. (2x)' -> 2)
        if new_exponent == 0:
            return str(new_coefficient)
        
        # Para new_exponent > 0, construimos la cadena de salida
        coeff_part = str(new_coefficient) if new_coefficient != 1 else ""
        var_part = f"{var}**{new_exponent}" if new_exponent != 1 else var
        
        return f"{coeff_part}{var_part}"


# Usamos una comprensión de listas más "Pythonica" para aplicar la función
functions_derivated = [calculate_derivative(f) for f in functions_to_process]

print("\nDerivadas calculadas:")
print(functions_derivated)