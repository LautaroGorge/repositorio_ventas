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


def main():
    pass