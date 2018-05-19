from django.urls import path

from .import views

app_name = 'financiero'
urlpatterns = [
	path('',views.IndexView.as_view(), name='index'),
	path('reporte-estudiantes/',views.Reporteestudiantes.as_view(), name='reporte-estudiantes'),

]