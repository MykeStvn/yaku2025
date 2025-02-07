from django.shortcuts import render
from django.db.models import Count
from django.db.models import Sum
from django.db.models.functions import ExtractYear


from Aplicaciones.Gestion.models import Detalle, HistorialPropietario, Lectura, Medidor, Recaudacion, Socio

# Create your views here.
def dashboard(request):
    #tipos de socios
    socios_tipo = Socio.objects.values('tipo_soc').annotate(count=Count('id_soc'))
    # numero de medidores por ruta            
    medidores = Medidor.objects.select_related('fk_id_rut').values('fk_id_rut__nombre_rut').annotate(count=Count('id_med'))
    # estado de los medidores
    medidores_estado = Medidor.objects.values('estado_med').annotate(count= Count('id_med'))
    # Consulta lecturas por año
    lecturas_anio = Lectura.objects.values('anio_lec').annotate(count=Count('id_lec'))

    # 3 lecturas más altas del mes de enero de 2024
    lecturas_mas_altas_enero_2024 = (
    Lectura.objects.filter(mes_lec='ENERO', anio_lec=2024)
    .select_related('fk_id_his__fk_id_soc')  # Precarga relaciones
    .order_by('-lectura_actual_lec')[:3]
    )
    # Mostrar resultados en la consola
    for lectura in lecturas_mas_altas_enero_2024:
        print(f"Socio: {lectura.fk_id_his.fk_id_soc.nombres_soc} {lectura.fk_id_his.fk_id_soc.primer_apellido_soc}, Lectura: {lectura.lectura_actual_lec}")

    #6) MEDIDORES CON SUS RESPECTIVAS TARIFAS
    
    medidores_tarifas = Medidor.objects.values('fk_id_tar__nombre_tar').annotate(count=Count('id_med'))

    for medidor in medidores_tarifas:
        print(f"Tarifa: {medidor['fk_id_tar__nombre_tar']}, Cantidad: {medidor['count']}")
    
    #7) 2 RUTAS CON MENOR NÚMERO DE MEDIDORES

    rutas_medidores = Medidor.objects.select_related('fk_id_rut').values('fk_id_rut__nombre_rut').annotate(count=Count('id_med')).order_by('count')[:2]

    #8) USUARIOS CON MÁS DE UN MEDIDOR
    
    # Consulta para obtener los socios con más medidores
    socios_mas_medidores = (
    HistorialPropietario.objects.values(
        'fk_id_soc__id_soc', 'fk_id_soc__nombres_soc', 'fk_id_soc__primer_apellido_soc', 'fk_id_soc__segundo_apellido_soc'
    )
    .annotate(total_medidores=Count('fk_id_med'))
    .order_by('-total_medidores')[:5]
    )

    # 9) SOCIOS INACTIVOS DENTRO DEL SISTEMA
    socios_inactivos = Socio.objects.filter(estado_soc='INACTIVO')
    for socio in socios_inactivos:
        print(f"Socio: {socio.nombres_soc}")
    
    context = {
        'socios_tipo':socios_tipo,
        'medidores': medidores,
        'medidores_estado': medidores_estado,
        'lecturas_anio': lecturas_anio,
        'lecturas_mas_altas_enero_2024': lecturas_mas_altas_enero_2024,
        'medidores_tarifas':medidores_tarifas,
        'rutas_medidores':rutas_medidores,
        'socios_mas_medidores': socios_mas_medidores,
        'socios_inactivos': socios_inactivos        
    }
    
    
    return render(request, 'dashboard.html', context)