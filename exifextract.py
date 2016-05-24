# dit programma maakt gebruik van libimage-exiftool-perl/8.60-2
# laad de libraries
import os
from subprocess import check_output

# variabelen voor de broninstructieregel
broninstructie = "ls"
bronoptie = ""
brondrive = "/"
bronpad = "/home/peter/Afbeeldingen"
bronbestand = "*.svg"

# variablelen voor de doelinstructieregel
doelinstructie = "exiftool -common -csv"
doeloptie = ""
doeldrive = "/"
doelpad = "/home/peter"
doelbestand = "test.csv"

# bouw de broninstructieregel
bronregel = broninstructie + ' ' + brondrive + bronpad + '/' + bronbestand
# pas de broninstructieregel aan aan het os(/ wordt \) en voeg de opties toe(/ moet blijven)
osbronregel = (os.path.normpath(bronregel)) + " " + bronoptie

# controle
#print (bronregel)
print (osbronregel)

# voer de broninstructie uit
result=check_output(osbronregel, shell=True)
# verdeel het resultaat in regels
lines = result.split('\n')
# maak de doelinstructieregel aan per broninstructieregel
for line in lines:
    if len(line) > 0:
        # bouw de doelinstructieregel
        doelregel = doelinstructie + ' ' + line + ' >> ' + doeldrive + doelpad + '/' + doelbestand
        # pas de broninstructieregel aan aan het os(/ wordt \) en voeg de opties toe(/ moet blijven)
        osdoelregel = (os.path.normpath(doelregel)) + " " + doeloptie
        # laat de doelinstructieregel zien
        print (osdoelregel)
        # voer de doelinstructieregel uit
        result2 = check_output(osdoelregel, shell=True)
    
  
