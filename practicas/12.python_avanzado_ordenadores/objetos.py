class Ordenador:
    def __init__(self, marca:str, cpu:str, ram:int, hd:int) -> None:
        self.marca = marca
        self.cpu = cpu
        self.ram = ram
        self.hd = hd

    def __str__(self) -> str:
        return f"{self.marca} {self.cpu} {self.ram} {self.hd}"

    