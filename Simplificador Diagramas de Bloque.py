from sympy import symbols, simplify, sympify
import re

def reemplazar_funciones(expresion):
    while re.search(r"rn\(([^()]+(?:\([^()]*\))?),([^)]+(?:\([^()]*\))?)\)", expresion) or re.search(r"rp\(([^()]+(?:\([^()]*\))?),([^)]+(?:\([^()]*\))?)\)", expresion):
        expresion = re.sub(r"rn\(([^()]+(?:\([^()]*\))?),([^)]+(?:\([^()]*\))?)\)", r"(\1/(1 + \1*\2))", expresion)
        expresion = re.sub(r"rp\(([^()]+(?:\([^()]*\))?),([^)]+(?:\([^()]*\))?)\)", r"(\1/(1 - \1*\2))", expresion)

    expresion = re.sub(r"rn\(([^,]+),([^)]+)\)", r"(\1/(1 + \1*\2))", expresion)
    expresion = re.sub(r"rp\(([^,]+),([^)]+)\)", r"(\1/(1 - \1*\2))", expresion)

    return expresion

expresion_str = input("Ingresa la expresión matemática que deseas simplificar: ")
expresion_reemplazada = reemplazar_funciones(expresion_str)

print("Expresión formulada:", expresion_reemplazada)
print("Expresión simplificada:", simplify(sympify(expresion_reemplazada)))
