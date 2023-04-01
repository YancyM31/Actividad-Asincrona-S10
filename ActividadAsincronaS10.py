# Inicializar la variable total a 0
total = 0

# Pedir al usuario el número de compras que desea registrar
num_compras = int(input("Ingrese el número de compras que desea registrar: "))

# Inicializar la variable contador en 0
contador = 0

# Mientras el contador sea menor que el número de compras
while contador < num_compras:
    # Pedir al usuario el precio de la compra actual
    precio = float(input("Ingrese el precio de la compra número " + str(contador+1) + ": "))
    # Agregar el precio al total
    total += precio
    # Incrementar el contador en 1
    contador += 1
    
print("El total a pagar es de: ", total)

# Aplicar descuentos según el total de compras
if total > 1000:
    descuento = total * 0.10
elif total > 500:
    descuento = total * 0.05
else:
    descuento = 0

# Calcular el total a pagar después de aplicar el descuento
total_descuento = total - descuento

# Imprimir el total a pagar, y si se aplicó algún descuento
if descuento > 0:
    print("Se ha aplicado un descuento de " + str(descuento) + " (" + str(descuento/total*100) + "%)")
print("El total a pagar es: ", total_descuento)