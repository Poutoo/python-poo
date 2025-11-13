class Ma_classe:
    def __new__(cls, *args, **kwargs):
        print("Création d'une nouvelle instance de Ma_classe")
        instance = super(Ma_classe, cls).__new__(cls)
        return instance
    
    def __init__(self, *args, **kwargs):
        print("Initialisation de l'instance de Ma_classe")
        self.props = args[0]
        
    def __del__ (self) -> None:
        print("Destruction de l'instance de Ma_classe")
        