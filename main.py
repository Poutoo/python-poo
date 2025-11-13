from app.utils import utils
from app.classes.voiture import Voiture

if __name__ == "__main__":
    ma_voiture = Voiture("McLaren", "P1", 2015)
    utils.show(ma_voiture, 'ma_voiture')
    
    print("\nAcces à une prop de la classe")
    print("ma_voiture.roues =", ma_voiture.roues)
    print("Voiture.roues =", Voiture.roues)
    
    ma_voiture.afficher_details()
    ma_voiture.accelerer(50)
    ma_voiture.freiner(20)
    ma_voiture.afficher_details()
    
    print("Roue :", ma_voiture.getRoues())
    ma_voiture.setRoues(5)
    print("Roue modifiée :", ma_voiture.roues)
    Voiture.setRoues(6)
    print("Roue modifiée via la classe :", Voiture.roues)
    
    