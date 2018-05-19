from django.contrib import admin
from .models import (Tecnica,Estudiante,Profesor,EstadoInstrumento,
                    EstadoPago,EstadoAsistencia,Inventario,
                    PagoEstudiante,asistencia,Sexo,
                    Grado,Enfermedad,conceptoPago,mes,
                    PagoProfesor)

class PagoEstudianteAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'concepto', 'mes','estado','cantidadPago','fecha_pago')
    list_filter = ('estudiante', 'concepto','mes')
    ordering = ('-fecha_pago',)
    search_fields = ('estudiante',)
        

admin.site.register(Tecnica)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(EstadoInstrumento)
admin.site.register(EstadoPago)
admin.site.register(EstadoAsistencia)
admin.site.register(Inventario)
admin.site.register(PagoEstudiante,PagoEstudianteAdmin)
admin.site.register(asistencia)
admin.site.register(Sexo)
admin.site.register(Grado)
admin.site.register(Enfermedad)
admin.site.register(conceptoPago)
admin.site.register(mes)
admin.site.register(PagoProfesor)


