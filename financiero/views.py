from django.conf import settings
from io import BytesIO
from django.views import generic
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from django.views.generic import View
from .models import Estudiante,PagoEstudiante,conceptoPago
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib.styles import ParagraphStyle

class IndexView(generic.ListView):
	template_name = 'estudiantes/index.html'
	context_object_name = 'estudiantes_list'
	def get_queryset(self):
		return {'Pagos':PagoEstudiante.objects.all().order_by("-fecha_pago"),'estudiantes':Estudiante.objects.all()}
		#list_not = Noticias.objects.filter(fecha_publicacion__lte=timezone.now(),tipo_noticia=1).order_by('-fecha_publicacion')[:10]
		#return {'noticias':list_not,'eventos':Noticias.objects.filter(fecha_publicacion__lte=timezone.now(),tipo_noticia=2).order_by('-fecha_publicacion')[:10]}


class Reporteestudiantes(View):

        def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            archivo_imagen = settings.MEDIA_ROOT+'/imagenes/logo2.jpg'
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
            pdf.drawImage(archivo_imagen, 40, 600, 120, 90,preserveAspectRatio=True)

        def tabla(self,pdf,y,nropago,identificacion):
                pago = PagoEstudiante.objects.get(id=nropago)
                est = Estudiante.objects.get(identificacion = identificacion )
                #Creamos una lista de tuplas que van a contener a las personas
                style = ParagraphStyle(
                        name='Normal'
                        )
                p=Paragraph(est.nombre, style)
                detalles = [["Nro de pago", pago.id],["Fecha",pago.fecha_pago.strftime("%d-%m-%Y")],
                ["Identificación",identificacion],["Nombre",p],["Concepto",pago.concepto],["Pago",pago.cantidadPago]]
                #Establecemos el tamaño de cada una de las columnas de la tabla
                if(pago.concepto == conceptoPago.objects.get(id=2)):
                        detalles = detalles+[("Mes",pago.mes)]
                        y=390

                detalle_orden =  Table(detalles, colWidths=[80, 115])
                #Aplicamos estilos a las celdas de la tabla
                """detalle_orden.setStyle(TableStyle(
                [
                        #La primera fila(encabezados) va a estar centrada
                        ('ALIGN',(0,0),(3,0),'CENTER'),
                        #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                        ('GRID', (0, 0), (-1, -1), 0, 0),
                        #El tamaño de las letras de cada una de las celdas será de 10
                        ('FONTSIZE', (0, 0), (-1, -1), 12),
                        ]
                ))"""
                #Establecemos el tamaño de la hoja que ocupará la tabla
                detalle_orden.wrapOn(pdf,195, 400)
                #Definimos la coordenada donde se dibujará la tabla
                detalle_orden.drawOn(pdf, 10,y)
                return y

        def get(self, request):
                params = request.GET
                nropago = params.get('pago')
                identificacion = params.get('estudiante',0)
                #Indicamos el tipo de contenido a devolver, en este caso un pdf
                response = HttpResponse(content_type='application/pdf')
                #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
                buffer = BytesIO()
                #Canvas nos permite hacer el reporte con coordenadas X y Y
                pdf = canvas.Canvas(buffer)
                #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
                self.cabecera(pdf)
                pdf.setPageSize((200, 700)) 
                #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
                pdf.setFont("Helvetica", 12)
                #Dibujamos una cadena en la ubicación X,Y especificada
                pdf.drawString(40, 580, u"ESCUELA DIOCESANA")
                pdf.drawString(70, 565, u"DE ARTE") 
                
                pdf.setFont("Helvetica", 12)
                pdf.drawString(20, 550, u"Casa Valorart cra 21 #22-44")
                pdf.drawString(50, 537, u"Barrio alto Jardin")
                pdf.drawString(5, 525, u"-----------------------------------------------") 
                y = 410
                y = self.tabla(pdf, y,nropago,identificacion)
                pdf.drawString(5, y-10, u"-----------------------------------------------") 
                pdf.setFont("Helvetica", 10)
                pdf.drawString(40,y-25, u'"La santidad consiste en') 
                pdf.drawString(50,y-40, u'estar siempre alegres"') 
                pdf.drawString(50,y-55, u"Santo Domingo Savio") 
                pdf.drawString(50,y-65, u" ") 
                #Con show page hacemos un corte de página para pasar a la siguiente
                pdf.showPage()
                pdf.save()
                pdf = buffer.getvalue()
                buffer.close()
                response.write(pdf)
                return response
