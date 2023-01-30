from Openclassroom.Hammer import Hammer
from Openclassroom.Nail import Nail
from Openclassroom.Screw import Screw
from Openclassroom.Tools import Tools
from Openclassroom.Tournevis import Tournevis
if __name__ == '__main__':
 tools = Tools()
 tourn = Tournevis()
 ham = Hammer()

 tools.ajouter(tourn)
 tools.ajouter(ham)
 tools.display()

vis = Screw()
print(vis.__str__())
tourn.serrer(vis)
print(vis.__str__())

clou = Nail()
print(clou.__str__())
ham.planter(clou)
print(clou.__str__())
