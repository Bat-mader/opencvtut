import cv2
import numpy as np

# Bild einlesen
image = cv2.imread('Resources/input.jpg')

# Bild in Graustufen umwandeln
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Schwellenwert festlegen - Pixel unterhalb dieser Helligkeit werden weiß
threshold_value = 200

# Erstellen einer Maske für alle Pixel, die nicht weiß genug sind
_, mask = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Die Maske anwenden, um die nicht weißen Bereiche weiß zu machen
image[mask == 255] = [255, 255, 255]

# Ergebnis speichern
cv2.imwrite('abcd.jpg', image)

# Ergebnis anzeigen (optional)
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()