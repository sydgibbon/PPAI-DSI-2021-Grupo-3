from datetime import date

tarifas = [
    {
        'fechaFinVigencia' : date(2023, 7, 10),
        'monto' : 3000,
        'montoAdicionalGuia': 1000
    },
    {
        'fechaFinVigencia' : date(2023, 7, 11),
        'monto' : 4000,
        'montoAdicionalGuia': 1000
    },
    {
        'fechaFinVigencia' : date(2023, 7, 12),
        'monto' : 4500,
        'montoAdicionalGuia': 1000
    },
    ] 
    

from myApp.models import Tarifa
for tarifa in tarifas:
    obj = Tarifa.objects.create(**tarifa)
    print(obj.pk)