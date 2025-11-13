from app.utils import utils
from app.classes.voiture import Voiture

if __name__ == "__main__":
    ma_voiture = Voiture("McLaren", "P1", 2015)
    utils.show(ma_voiture, 'ma_voiture')
    
    print("\nAcces à une prop de la classe")
    print("ma_voiture.roues =", ma_voiture.roues)
    print("Voiture.roues =", Voiture.roues)
