print("### Costo final de Netflix asumiendo valor bruto de $1000 ###")
costo_servicio = 1000
# IVA 21%
costo_servicio_iva = costo_servicio * 0.21
# Impuesto pais 8%
costo_servicio_pais = costo_servicio * 0.08
# Ganancias 30%
costo_servicio_g = costo_servicio * 0.3
# IIBB CABA 2%
costo_servicio_iibb = costo_servicio * 0.02

valor_final = costo_servicio + costo_servicio_iva + costo_servicio_pais + costo_servicio_g + costo_servicio_iibb

print("El valor final a pagar es: $", valor_final)
