from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from django.template.loader import get_template
from django.template import Context

def generate_pdf(html_content, output_pdf_path):
    # Créer un objet Canvas pour générer le PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Utiliser un modèle Django pour remplir le HTML
    template = get_template("manager_dashboard/evaluations/bulletin_detail.html")
    context = Context({"content": html_content})
    html_content = template.render(context)

    # Convertir le HTML en PDF en utilisant reportlab
    pdf_content = BytesIO()
    p.drawString(100, 100, "Hello World")
    p.save()

    # Enregistrez le PDF généré
    buffer.seek(0)
    with open(output_pdf_path, 'wb') as f:
        f.write(buffer.read())

# Votre modèle HTML
html_content = """
... (votre modèle HTML ici)
"""

# Emplacement de sortie du fichier PDF
output_pdf_path = "releve_de_notes_reportlab.pdf"

# Appel de la fonction pour générer le PDF
generate_pdf(html_content, output_pdf_path)
