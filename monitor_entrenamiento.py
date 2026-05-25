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
 
 
def simular_metricas_entrenamiento(cantidad_epochs):
    """
    Usa las bibliotecas 'random' y 'datetime' para simular los datos de entrenamiento.
    Requisitos: 3 llamadas a 'random' y 3 llamadas a 'datetime'.
    """
    # --- Llamadas a datetime ---
 
    # 1: obtener fecha y hora exacta de inicio
    inicio = datetime.datetime.now()
 
    # 2: formato (Día/Mes/Año Hora:Minuto:Segundo)
    inicio_formateado = inicio.strftime("%d/%m/%Y %H:%M:%S")
    print(f"  Simulación: {inicio_formateado}")
 
    # Eventos posibles para log
    eventos_log = ["Epoch exitoso", "Gradiente inestable", "Actualización de pesos",
                   "Convergencia detectada", "Regularización aplicada"]
 
    lista_loss = []
    lista_latencia = []
 
    print(f"\n  Simulando {cantidad_epochs} epochs...\n")
 
    for epoch in range(1, cantidad_epochs + 1):
 
        # 1: generar fluctuación del error de pérdida (loss) con float aleatorio
        loss = random.uniform(0.1, 1.0)
 
        # 2: simular probabilidad de éxito de la iteración
        probabilidad_exito = random.random()   # valor entre 0.0 y 1.0
 
        # 3: seleccionar aleatoriamente un evento de log de la lista
        evento = random.choice(eventos_log)
 
        # Simular latencia en milisegundos para este epoch
        latencia_ms = random.uniform(50, 300)
 
        lista_loss.append(loss)
        lista_latencia.append(latencia_ms)
 
        estado = "ÉXITO" if probabilidad_exito >= 0.4 else "FALLO"
        print(f"    Epoch {epoch:02d} | Loss: {loss:.4f} | "
              f"Prob. éxito: {probabilidad_exito:.2f} | "
              f"Estado: {estado} | Evento: {evento}")
 
    # 3: calcular diferencia de tiempo entre inicio y fin
    fin = datetime.datetime.now()
    duracion = fin - inicio
    duracion_segundos = duracion.total_seconds()
 
    print(f"\n  Fin de simulación       : {fin.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"  Duración total          : {duracion_segundos:.4f} segundos")
 
    return lista_loss, lista_latencia

def analizar_rendimiento(lista_loss, lista_latencia):

    """
    Usa la biblioteca 'statistics' para analizar el comportamiento del entrenamiento.
    Requisitos: 3 llamadas distintas a la biblioteca 'statistics'.
    """

    print("\n--- ANÁLISIS DE RENDIMIENTO ---")
 
    # 1: calcula la media de los valores de pérdida
    media_loss = statistics.mean(lista_loss)
    print(f"  Media de loss: {media_loss:.4f}")
 
    # 2: calcula la desviación estándar para medir estabilidad
    desviacion_loss = statistics.stdev(lista_loss)
    print(f"  Desviación estándar: {desviacion_loss:.4f}")
 
    # 3: calcula la mediana de la latencia del proceso
    mediana_latencia = statistics.median(lista_latencia)
    print(f"  Mediana de latencia: {mediana_latencia:.2f} ms")
 
    return media_loss
 
