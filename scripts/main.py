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


def mostrar_indicadores():
    pass




def main():
    pass