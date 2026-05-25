"""
Nombre del Alumno: [Alan Dominguez Velazquez]
Matrícula: [UX25II206]
Fecha: [25/05/2026]
Examen Segundo Parcial - Programación Estructurada
"""

# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys
 
# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================

MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95
 
# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
 
def obtener_info_sistema():

    """
    Usa la biblioteca 'sys' para validar el entorno de ejecución.
    Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
    """

    print("\n--- INFORMACIÓN DEL SISTEMA ---")
 
    # 1: sys.platform - nos muestra en consula el sistema operativo

    plataforma = sys.platform
    print(f"  Sistema opreativo: {plataforma}")
 
    # 2: sys.version - nos muestra la vercion de python que utilizamos

    version_python = sys.version
    print(f"  Versión de Python: {version_python}")
 
    # 3: sys.executable - nos muestra la ruta intérprete de Python

    ruta_interprete = sys.executable
    print(f"  Ruta intérprete: {ruta_interprete}")
 
 
