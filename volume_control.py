from os import popen
import sys
print(sys.argv[1]+" "+sys.argv[2])
a = popen("pactl list sink-inputs").read()
a = str(a).split("Sink Input")
for i in a:
    if 'media.name = "'+sys.argv[1]+'"' in i or 'application.process.binary = "'+sys.argv[1]+'"' in i:
        a = i

a = str(a).replace("\t","").split("\n")
sink = a[0].replace("#","").replace(" ","")



popen("pactl set-sink-input-volume "+sink+" "+sys.argv[2]+"%")

