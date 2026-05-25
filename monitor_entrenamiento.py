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
 
def calcular_rmse(predicciones, reales):
    """
    Usa la biblioteca 'math' para calcular el Root Mean Squared Error (RMSE).
    Requisitos: 3 llamadas distintas a la biblioteca 'math'.
    """

    print("\n--- CÁLCULO DE RMSE ---")
 
    n = len(predicciones)
    suma_cuadrados = 0
 
    for i in range(n):
        diferencia = predicciones[i] - reales[i]
 
        # 1: pow() eleva la diferencia al cuadrado
        cuadrado = math.pow(diferencia, 2)
        suma_cuadrados = suma_cuadrados + cuadrado
 
    promedio_cuadrados = suma_cuadrados / n
 
    # 2: sqrt() raíz cuadrada del promedio (RMSE)
    rmse = math.sqrt(promedio_cuadrados)
 
    #  3: fabs() valor absoluto del RMSE 
    rmse_absoluto = math.fabs(rmse)
 
    # Calcular cantidad de epochs adicionales recomendados con ceil
    epochs_recomendados = math.ceil(rmse_absoluto * 10)
 
    print(f"  RMSE calculado: {rmse_absoluto:.4f}")
    print(f"  Epochs adicionales rec.: {epochs_recomendados}")
 
    return rmse_absoluto
 
 
# ==========================================
# 4. PROGRAMA PRINCIPAL (PUNTO DE ENTRADA)
# ==========================================

if __name__ == "__main__":
    print("=" * 52)
    print("   INICIANDO SIMULADOR DE AGENTES DE IA")
    print("=" * 52)
    
    # Validar entorno del sistema
    obtener_info_sistema()
    
    # Simulador 
    print("--- SIMULACIÓN DE ENTRENAMIENTO ---")
    lista_loss, lista_latencia = simular_metricas_entrenamiento(MAX_EPOCHS)
    
    # Rendimiento con statistics
    media_loss = analizar_rendimiento(lista_loss, lista_latencia)
    
    # Calcular RMSE simulados de predicción y reales
    predicciones = [random.uniform(0.1, 0.9) for _ in range(MAX_EPOCHS)]
    reales       = [random.uniform(0.1, 0.9) for _ in range(MAX_EPOCHS)]
    rmse = calcular_rmse(predicciones, reales)
    
    # Verificar si las métricas son críticas y actuar en consecuencia
    print("\n--- EVALUACIÓN FINAL ---")
    print(f"  Media de loss           : {media_loss:.4f}")
    print(f"  Umbral crítico          : {UMBRAL_ERROR_CRITICO}")
    
    if media_loss >= UMBRAL_ERROR_CRITICO:
        print("\n  [CRÍTICO] La media de loss supera el umbral permitido.")
        print("  El proceso de entrenamiento se detendrá de forma segura.")
        print("=" * 52)
        # Llamada sys.exit(): forzar salida limpia cuando las métricas son críticas
        sys.exit(1)
    else:
        print("\n Métricas dentro del rango aceptable.")
        print("  Entrenamiento completado con éxito.")
        print("=" * 52)

# ==========================================
# 5. Cuestionario
# ==========================================

"""
Uso de Objetos y Métodos: En tu código, al usar datetime.datetime.now(),
¿cuál es el objeto/clase y cuál es el método que estás llamando? Explica
cómo se relaciona esto con el concepto de biblioteca externa

En datetime.datetime.now(), datetime (la clase) es el objeto y .now() es el método
La biblioteca es el módulo externo: 
solo se importa para usar sus clases y métodos sin escribirlos desde cero



Diferenciación Técnica: ¿Qué diferencia existe en la sintaxis de tu código
al importar un módulo completo (ej: import math) versus importar un método
específico (ej: from math import sqrt) al momento de invocar sus funciones?

Con import math se usa el prefijo en cada llamada: math.sqrt() 
Con from math import sqrt la función llega directo al código y la llamas solo como sqrt(). 
La direncia solo es el uso del prefijo



Flujo y Lógica: Describe brevemente la secuencia lógica de pasos que
implementaste para conectar los datos generados por tu función de
simulación con la función que calcula el error (RMSE).

simular_metricas_entrenamiento() genera y regresa lista_loss y lista_latencia 
Esas listas se pasan a analizar_rendimiento() para obtener la media_loss
Luego se generan dos listas nuevas con random.uniform() y se pasan a calcular_rmse()
El programa principal usa media_loss para la evaluación crítica



Mapeo de Tipos de Datos: Identifica al menos dos tipos de datos
complejos (colecciones) que utilizaste para organizar los resultados de tus
análisis y justifica por qué elegiste esa estructura en lugar de variables
simples.

Se usan dos listas: lista_loss y lista_latencia
Se usan listas en lugar de variables simples porque una variable simple solo 
guarda un valor y cada epoch lo sobreescribiría
La lista conserva todos los valores del proceso



Autoevaluación de Abstracción: Al utilizar las funciones de la biblioteca
statistics, ¿tuviste que programar la fórmula matemática matemática de la
desviación estándar? Relaciona esto con el concepto de Abstracción visto
en clase.

No fue necesario ya que la biblioteca hace todo el trabajo
"""