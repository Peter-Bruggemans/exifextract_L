# dit programma maakt gebruik van libimage-exiftool-perl/8.60-2
# laad de libraries
import os
from subprocess import check_output

# variabelen voor de broninstructieregel
bronregel = """ls -R /home/peter/Fotos | awk '/:$/&&f{s=$0;f=0}/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}NF&&f{ print s"/"$0 }'"""
bronpad = '/home/peter/Fotos/'
bronbestand = 'CR2'

# variablelen voor de doelinstructieregel
doelinstructie = "exiftool -T -canon -csv"
doeloptie = ""
doeldrive = "/"
doelpad = "/home/peter"
doelbestand = "test.csv"

# controle
#print (bronregel)

# voer de broninstructie uit
result=check_output(bronregel, shell=True)
# verdeel het resultaat in regels
lines = result.split('\n')
# filter op bronpad en bronbestand en maak de doelinstructieregel aan per broninstructieregel
teller = 0
print('Writing')
for line in lines:
    if len(line) > 0:
        if line[-3:] == bronbestand:
            if line[0:len(bronpad)] == bronpad:
                teller = teller + 1
                # bouw de doelinstructieregel
                doelregel = doelinstructie + ' ' + line + ' >> ' + doeldrive + doelpad + '/' + doelbestand
                # pas de broninstructieregel aan aan het os(/ wordt \) en voeg de opties toe(/ moet blijven)
                osdoelregel = (os.path.normpath(doelregel)) + " " + doeloptie
                # laat de doelinstructieregel zien
                print str(teller) + " row(s) written"
                # voer de doelinstructieregel uit
                result2 = check_output(osdoelregel, shell=True)
                
print('Finished')
