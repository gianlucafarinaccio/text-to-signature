from PIL import Image, ImageDraw, ImageFont

# Impostazioni immagine
width, height = 512, 200
background_color = "white"
text_color = "black"
text = "Daniele Ferneti"

# Crea un'immagine vuota
image = Image.new("RGB", (width, height), background_color)

# Crea un oggetto per il disegno
draw = ImageDraw.Draw(image)

# Imposta il font (usa un font disponibile nel tuo sistema)
try:
    font = ImageFont.truetype("Bs Signature Demo.ttf", 100)  # Specifica il font e la dimensione
except IOError:
    font = ImageFont.load_default()  # Font di default se quello specificato non è trovato

# Calcola la posizione del testo per centrarlo
text_bbox = draw.textbbox((0, 0), text, font=font)  # Ottieni le coordinate della bounding box
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2

# Disegna il testo sull'immagine
draw.text((x, y), text, fill=text_color, font=font)

# Salva o mostra l'immagine
image.show()  # Mostra l'immagine
image.save("immagine_con_testo2.png")  # Salva l'immagine
