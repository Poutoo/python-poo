class Voiture:
    # Props de CLASSE
    # Déclaration + Initialisation
    roues = 4  # Toutes les voitures ont 4 roues

    # Initialisation des props d'INSTANCE
    # on ne peut y acceder qu'à partir de l'instance
    # et non de la classe
    def __init__(self, marque: str, modele: str, annee: int):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.__vitesse = 0  # Vitesse initiale de la voiture

    # Méthodes d'INSTANCE
    # self est une refernce vers l'objet qui sera créé à partir de cette classe
    def accelerer(self, increment: int):
        """Augmente la vitesse de la voiture."""
        self.__vitesse += increment
        print(f"La voiture accélère de {increment} km/h. Vitesse actuelle: {self.__vitesse} km/h")
    
    def freiner(self, decrement: int):
        """Diminue la vitesse de la voiture."""
        self.__vitesse = max(0, self.__vitesse - decrement)
        print(f"La voiture freine de {decrement} km/h. Vitesse actuelle: {self.__vitesse} km/h")  

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Vitesse: {self.__vitesse} km/h")

    def getRoues(self):
        """Retourne le nombre de roues de la voiture."""
        return Voiture.roues
    

    # Méthode de CLASSE
    @classmethod
    def nombre_de_roues(cls):
        """Retourne le nombre de roues des voitures."""
        return cls.roues
    
    @classmethod
    def setRoues(cls, nombre: int):
        """Modifie le nombre de roues des voitures."""
        cls.roues = nombre
        
    # Methode spéciale __str__
    def __str__(self) -> str:
        return f"Voiture(marque={self.marque}, modele={self.modele}, annee={self.annee}, vitesse={self.__vitesse} km/h)"
    
    def __repr__(self) -> str:
        return f"Voiture('{self.marque}', '{self.modele}', {self.annee})"