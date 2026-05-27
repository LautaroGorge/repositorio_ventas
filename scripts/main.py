import csv


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


def producto_mas_vendido(ventas):
    cantidad_por_producto = {}

    for venta in ventas:
        producto = venta['producto']
        cantidad = venta['cantidad']

        if producto in cantidad_por_producto:
            cantidad_por_producto[producto] += cantidad
        else:
            cantidad_por_producto[producto] = cantidad

    if not cantidad_por_producto:
        return None,0

    producto_max = max(cantidad_por_producto, key=cantidad_por_producto.get)
    cantidad_max = cantidad_por_producto[producto_max]

    return producto_max, cantidad_max






def main():
    pass