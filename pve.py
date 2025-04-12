import PySAM.Pvwattsv7 as pv
import PySAM.Lcoefcr as Lcoefcr
import pandas as pd

# Nombre del archivo CSV con datos horarios (el que mostraste)
solar_resource_file = "/home/cparrado/datasciencesolar/antofagasta.csv"

# Parámetros de ejemplo para el sistema PV
system_capacity_kw = 1000.0
fixed_charge_rate = 0.07
capital_cost = 1_000_000
fixed_operating_cost = 50_000
variable_operating_cost = 0.01

# Crear un modelo PVWatts "desde cero" y asignar el recurso solar
pv_model = pv.new()
pv_model.SolarResource.solar_resource_file = solar_resource_file

# Configurar parámetros mínimos del sistema PV
pv_model.SystemDesign.system_capacity = system_capacity_kw
pv_model.SystemDesign.dc_ac_ratio = 1.2
pv_model.SystemDesign.array_type = 1
pv_model.SystemDesign.azimuth = 180
pv_model.SystemDesign.tilt = 20
pv_model.SystemDesign.gcr = 0.4
pv_model.SystemDesign.inv_eff = 96
pv_model.SystemDesign.losses = 14.0

# Ejecutar la simulación PVWatts
pv_model.execute()

# Obtener la generación anual de energía (kWh)
annual_energy = pv_model.Outputs.annual_energy
print(f"Generación anual de energía PV: {annual_energy} kWh")

# Crear el modelo para cálculo de LCOE
lcoe_model = Lcoefcr.new()

# Asignar valores para el cálculo del LCOE
lcoe_model.SimpleLCOE.annual_energy = annual_energy
lcoe_model.SimpleLCOE.capital_cost = capital_cost
lcoe_model.SimpleLCOE.fixed_charge_rate = fixed_charge_rate
lcoe_model.SimpleLCOE.fixed_operating_cost = fixed_operating_cost
lcoe_model.SimpleLCOE.variable_operating_cost = variable_operating_cost

# Ejecutar el cálculo del LCOE
lcoe_model.execute()

# Obtener el LCOE calculado
lcoe = lcoe_model.Outputs.lcoe_fcr
print(f"LCOE: {lcoe} $/kWh")

# Guardar resultados en un CSV
import pandas as pd
df_results = pd.DataFrame({
    "System_Capacity_kW": [system_capacity_kw],
    "Annual_Energy_kWh": [annual_energy],
    "Capital_Cost_$": [capital_cost],
    "Fixed_Charge_Rate": [fixed_charge_rate],
    "LCOE_$kWh": [lcoe]
})

df_results.to_csv("pv_lcoe_results.csv", index=False)
print("Resultados guardados en pv_lcoe_results.csv")

# ------------------------------------------------------
# Variables que puedes cambiar o iterar:
# - system_capacity_kw: tamaño del sistema PV
# - fixed_charge_rate: tasa de carga fija para el LCOE
# - capital_cost: costo total de la planta
# - fixed_operating_cost: costo operativo fijo anual
# - variable_operating_cost: costo operativo variable ($/kWh)
#
# Además, puedes ajustar parámetros del arreglo PV (azimuth, tilt, gcr, etc.)
# o probar con diferentes archivos de recursos solares.
# ------------------------------------------------------

# Crear un modelo PVWatts "desde cero" y asignar el recurso solar
pv_model = pv.new()
pv_model.SolarResource.solar_resource_file = solar_resource_file

# Configurar parámetros mínimos del sistema PV

    