#  ejemplo con reportlab
#
# pip install reportlab
#

from reportlab.pdfgen import canvas

c = canvas.Canvas("ejemplo.pdf")
c.drawString(100, 750, "Hola desde ReportLab")
c.save()

print("pdf creado")
