class fabrica:
    def __init__(self, Marca, Color, Almacenamiento, Ram):
        self.Marca = Marca
        self.Color = Color
        self.Almacenamiento =  Almacenamiento
        self.Ram= Ram

    def compra(self):
            print("Necesito un telefono de estas caracteristicas.")
            print("Marca", self.Marca)
            print("Color", self.Color)
            print("Almacenamiento", self.Almacenamiento)
            print("Ram", self.Ram)


celular1 = fabrica("Samsung", "Azul", 128, 16)
celular1.compra()