from decano import Decano
from facultad import Facultad
from universidad import Universidad

decano1 = Decano("Julio", 44556673, "juliochucho@blbl.com")
decano2 = Decano("Soledad", 22233008, "Soledadposta@gmail.com")
facultad1 = Facultad("Ingeniería", decano1)
facultad2 = Facultad("Medicina", decano2)

universidad = Universidad("Tecnológica Nacional")

universidad.agregarFacultad(facultad1)
universidad.mostrarFacultad()

universidad.agregarFacultad(facultad2)
universidad.mostrarFacultad()
