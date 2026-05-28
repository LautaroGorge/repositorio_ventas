import csv
from datetime import datetime

def leer_archivo_ventas(nombre_archivo):
    ventas = []
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                venta = {
                    'id': int(fila['id']),
                    'fecha': fila['sales_date'],
                    'monto': float(fila['sales_amount'])
                }
                ventas.append(venta)
        
        print(f" Archivo '{nombre_archivo}' cargado exitosamente")
        print(f" Total de registros: {len(ventas)}\n")
        return ventas
    
    except FileNotFoundError:
        print(f" Error: No se encontró el archivo '{nombre_archivo}'")
        return []
    except ValueError as e:
        print(f" Error al convertir datos: {e}")
        return []
    except Exception as e:
        print(f" Error inesperado: {e}")
        return []


def calcular_ventas_totales(ventas):
    total = 0

    for venta in ventas:
        total += venta['monto']

    return total

def dia_mayor_venta(ventas):
    if not ventas:
        return None, 0

    venta_max = max(ventas, key=lambda v: v['monto'])

    return venta_max['fecha'], venta_max['monto']


def calcular_ventas_por_mes(ventas):
    ventas_por_mes = {}

    for venta in ventas:
        fecha_str = venta['fecha']

        try:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d')
            mes = fecha_obj.strftime('%Y-%m')

            if mes in ventas_por_mes:
                ventas_por_mes[mes] += venta['monto']
            else:
                ventas_por_mes[mes] = venta['monto']

        except ValueError:
            print(f"Advertencia: Fecha invalida encontrada: {fecha_str}")
            continue

    ventas_por_mes_ordenado = dict(sorted(ventas_por_mes.items()))
    return ventas_por_mes_ordenado


def mostrar_indicadores(ventas, total_ventas, fecha_max, monto_max, ventas_por_mes):
    print("="*75)
    print("Indicadores de ventas - Resumen ejecutivo")
    print("="*75)

    print(f"\n Ventas totales: ${total_ventas:,.2f}")

    print(f"\n Cantidad de Transacciones: {len(ventas)}")


    if ventas:
        promedio = total_ventas / len(ventas)
        print(f"Promedio diario de ventas: ${promedio:,.2f}")
    
    print(f"\n Día de mayor de ventas: {fecha_max}")
    print(f"    Monto registrado: ${monto_max:,.2f}")

    print(f"\n VENTAS POR MES:")
    print("-"*75)

    for mes, monto in ventas_por_mes.items():
        print(f"   {mes}: ${monto:,.2f}")

    print("-" * 75)
    print("\n" + "=" * 75 + "\n")


def crear_tabla_ventas_por_mes(ventas_por_mes):
    print("\nTABLA: EVOLUCION DE VENTAS POR MES")
    print("=" * 70)

    if not ventas_por_mes:
        return

    max_venta = max(ventas_por_mes.values())

    for mes, monto in ventas_por_mes.items():
        largo_barra = int((monto/ max_venta) * 40)
        barra = "█" * largo_barra
        print(f"{mes} | {barra:40} ${monto:,.2f}")

    print("="*75 + "\n")


def guardar_resultados(nombre_archivo_salida, total_ventas, fecha_max, monto_max, ventas_por_mes):
    try:
        with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write("=" * 60 + "\n")
            archivo.write("Resultados de análisis de ventas\n")
            archivo.write("=" * 60 + "\n")

            archivo.write(f"VENTAS TOTALES: ${total_ventas:,.2f}\n\n")

            archivo.write(f"DIA DE MAYOR VENTA: {fecha_max}\n")
            archivo.write(f"MONTO: ${monto_max:,.2f}\n\n")

            archivo.write("VENTAS POR MES:\n")
            archivo.write("-" * 60 + "\n")
            for mes, monto in ventas_por_mes.items():
                archivo.write(f"  {mes}: ${monto:,.2f}\n")

            archivo.write("=" * 60 + "\n")

        print(f"Resultados guardados en: {nombre_archivo_salida}")
    
    except Exception as e:
        print(f"Error al guardar resultados {e}")


def main():
    print("\n" + "=" * 75)
    print("SISTEMA DE ANALISIS DE VENTAS - PEQUEÑA EMPRESA")
    print("=" * 75 + "\n")

    nombre_archivo_entrada = 'datos/sales_sample_2024.csv'
    ventas = leer_archivo_ventas(nombre_archivo_entrada)

    if not ventas:
        print("No se pudo cargar el archivo de ventas")
        return

    print("Calculando indicadores...\n")

    total_ventas = calcular_ventas_totales(ventas)
    fecha_max, monto_max = dia_mayor_venta(ventas)
    ventas_por_mes = calcular_ventas_por_mes(ventas)

    mostrar_indicadores(ventas, total_ventas, fecha_max, monto_max, ventas_por_mes)

    crear_tabla_ventas_por_mes(ventas_por_mes)

    print("Guardando resultados...\n")
    guardar_resultados('resultados/reporte_ventas.txt', total_ventas, fecha_max, monto_max, ventas_por_mes)

    print("Analisis completado exitosamente.")


if __name__ == '__main__':
    main()