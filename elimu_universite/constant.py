import os
import qrcode
from io import BytesIO
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from elimu_universite import settings

def generate_qr_code_and_save(data, filename):
    # Créer un objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Ajouter les données (texte) au code QR
    qr.add_data(data)
    qr.make(fit=True)
    # Créer une image PIL (Pillow)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir l'image PIL en octets
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    # Enregistrer l'image dans le dossier media
    file_path = default_storage.path(os.path.join(settings.MEDIA_ROOT, 'qr_codes', filename))
    with open(file_path, 'wb') as f:
        f.write(buffer.getvalue())
    
    # Retourner le chemin de l'image enregistrée (relatif au dossier media)
    return os.path.relpath(file_path, settings.MEDIA_ROOT)

days_of_the_weeks = [
    ('lundi', 'Lundi'),
    ('mardi', 'Mardi'),
    ('mercredi', 'Mercredi'),
    ('jeudi', 'Jeudi'),
    ('vendredi', 'Vendredi'),
    ('samedi', 'Samedi'),
    ('dimanche', 'Dimanche'),
]

hours_of_the_day = [
    ('07h', '07h'),
    ('08h', '08h'),
    ('09h', '09h'),
    ('10h', '10h'),
    ('11h', '11h'),
    ('12h', '12h'),
    ('13h', '13h'),
    ('14h', '14h'),
    ('15h', '15h'),
    ('16h', '16h'),
    ('17h', '17h'),
]

currencies = [
    ('F CFA', 'F CFA')
]

systemes = [
    ('Congolais', 'Congolais')
]

statues = [
    ('Activé', 'Activé'),
    ('Desactivé', 'Desactivé')
]