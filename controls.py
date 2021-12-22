
import time
from datetime import datetime

schwellwertLuftfeuchtigkeit = 75    #Schwellenwert der Luftfeuchtigkeit. Bei weniger = Mistmaker an
uvLamp01_start = 6                   #Startzeit 01 der UV-Lampe 6Uhr = 6*60*60
uvLamp01_stop = 8                   #Stopzeit 01 der UV-Lampe
uvLamp02_start = 16                  #Startzeit 02 der UV-Lampe
uvLamp02_stop = 18                   #Stopzeit 02 der UV-Lampe
ventilator_interval = 2             #bspw.: Alle 2 Stunden
ventilator_duration = 10            #sei 10 Minuten an
stdMult = 60*60                     #Stunden Multiplikator

uvLst1 = uvLamp01_start * stdMult
uvLsp1 = uvLamp01_stop * stdMult
uvLst2 = uvLamp02_start * stdMult
uvLsp2 = uvLamp02_stop * stdMult

i = uvLamp01_start * stdMult
start = int(time.time())-1
now = 0
count_sec = 0
count_days = 0

while now <= 24*stdMult:
    now +=100
    #print("now: ", now)
    if (now == uvLst1):
        print("on_1 @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " +  str(round(time.time())) +  " | Uptime_Days: " +  str(count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLsp1):
        print("off_1 @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " +  str(round(time.time())) +  " | Uptime_Days: " +  str(count_days) + " | Uptime_Hours: " + str(round(now/ stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLst2):
        print("on_2 @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " +  str(round(time.time())) +  " | Uptime_Days: " +  str(count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLsp2):
        print("off_2 @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " +  str(round(time.time())) +  " | Uptime_Days: " +  str(count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == 24*stdMult):
        print("Es ist ", now/stdMult, " Uhr. Der Timer wird zurückgesetzt\n\n")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " +  str(round(time.time())) +  " | Uptime_Days: " +  str(count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n\n"
        f.write(string)
        f.close()
        count_days = count_days + 1

        now = 0
    time.sleep(0.001)
print (count_sec)
