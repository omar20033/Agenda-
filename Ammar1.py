import numpy as np
import matplotlib.pyplot as plt

def durkin_model(distance, frequency, urban_density):
    # Constantes du modèle
    a = 0.3  # coefficient d'absorption urbain
    b = 0.7  # coefficient de diffraction
    c = 1.5  # coefficient de réflexion
    
    # Calcul de l'atténuation
    attenuation = a * urban_density * np.log10(distance) + b * np.sqrt(distance) + c * np.log10(frequency)
    
    return attenuation

# Exemple d'utilisation
distance = np.linspace(1, 50, 100)  # distances de 1 à 50 km
frequency = 1800  # fréquence de 1800 MHz
urban_density = 0.8  # densité urbaine (échelle de 0 à 1)

attenuation = durkin_model(distance, frequency, urban_density)

# Tracer les résultats
plt.plot(distance, attenuation)
plt.xlabel('Distance (km)')
plt.ylabel('Atténuation (dB)')
plt.title('Modèle Durkin')
plt.grid(True)
plt.show()