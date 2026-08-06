print('subject marks')
phy=50
chem= 60
maths= 70
print("physics={} chemistry={} maths={}" .format(phy,chem,maths))  #physics50 chemistry60 maths70
print("physics{0} chemistry{1} maths{2}" .format(phy,chem,maths))  #physics50 chemistry60 maths70
print("physics={x} chemistry={y} maths={z}" .format(x=phy, y=chem, z=maths))  
#physics50 chemistry60 maths70
total= phy+chem+maths
print("total marks",f"{total}")  #total marks 180
print("roll no=","7".zfill(4))  #roll no= 0007
