
import time
#from datetime import datetime



stdMult = 60*60                     #Stunden Multiplikator
humidity_change = True
uvLst1 = 0
uvLsp1 = 0
uvLst2 = 0
uvLsp2 = 0
vent_intrvl = 0
vent_intrvl_min = 0
humidity_in = 0
schwellwertLuftfeuchtigkeit = 0
vent_off = 86401

def getData():
    inputFile = open('in.txt', 'r')
    data = inputFile.readlines()
    humidity_in = int(data[0][:2])

    schwellwertLuftfeuchtigkeit = int(data[1][:2])    #Schwellenwert der Luftfeuchtigkeit. Bei weniger = Mistmaker an
    uvLamp01_start = int(data[2][:2])                  #Startzeit 01 der UV-Lampe 6Uhr = 6*60*60
    uvLamp01_stop = int(data[3][:2])                   #Stopzeit 01 der UV-Lampe
    uvLamp02_start = int(data[4][:2])                 #Startzeit 02 der UV-Lampe
    uvLamp02_stop = int(data[5][:2])                  #Stopzeit 02 der UV-Lampe
    ventilator_interval = int(data[6][:2])             #bspw.: Alle 2 Stunden
    ventilator_duration = int(data[7][:2])            #sei 10 Minuten an
    inputFile.close()

    uvLst1 = uvLamp01_start * stdMult
    uvLsp1 = uvLamp01_stop  * stdMult
    uvLst2 = uvLamp02_start * stdMult
    uvLsp2 = uvLamp02_stop  * stdMult
    vent_intrvl = ventilator_interval * stdMult
    vent_intrvl_min = ventilator_duration * 60
    return uvLst1,uvLsp1,uvLst2,uvLsp2,vent_intrvl,vent_intrvl_min,schwellwertLuftfeuchtigkeit,humidity_in


#i = uvLamp01_start * stdMult
start = int(time.time())-1
now = 0
count_sec = 0
count_days = 0
uvLst1,uvLsp1,uvLst2,uvLsp2,vent_intrvl,vent_intrvl_min,schwellwertLuftfeuchtigkeit,humidity_in = getData()
while now <= 24*stdMult:
    now +=10
    #print("now: ", now)
    if (now == uvLst1):
        #print("on_1_Lamp @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLsp1):
        #print("off_1_Lamp @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now/ stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLst2):
        #print("on_2_Lamp @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (now == uvLsp2):
        #print("off_2_Lamp @", now/stdMult, "Uhr")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()

    if ((now % vent_intrvl) == 0):
        print("on_Ventilator @", round(now / stdMult), "Uhr & now =", now)
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
        vent_off = now + vent_intrvl_min
    if (now == vent_off):
        print("off_Ventilator @", round(now / stdMult), "Uhr & now =", now)
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
        f.write(string)
        f.close()
    if (humidity_change == True):
        if(humidity_in <= 75):
            #print("on_Mistmaker @", round(now / stdMult), "Uhr &", "Luftfeuchtigkeit: ", humidity_in , "%")
            f = open('log.txt', 'a')
            string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
                count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
            f.write(string)
            f.close()
        else:
            #print("off_Mistmaker @", round(now / stdMult), "Uhr &", "Luftfeuchtigkeit: ", humidity_in , "%")
            f = open('log.txt', 'a')
            string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
                count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n"
            f.write(string)
            f.close()
        humidity_change = False
    if (now % 60 == 0): # jede Minute
        f = open('in.txt', 'r')
        t = int(f.readline(2)) #liest die ersten beiden chars ein
        f.close()
        #print(end="\r Luftfeuchtigkeit: " + str(t) + "\t\t")
        if(t != humidity_in):
            humidity_in = t
            humidity_change = True
        #humidity_change = True
    if (now % 3600 == 0): # jede Stunde
        uvLst1, uvLsp1, uvLst2, uvLsp2, vent_intrvl, vent_intrvl_min, schwellwertLuftfeuchtigkeit, humidity_in = getData()

    if (now == 24*stdMult):
        print("Es ist ", now/stdMult, " Uhr. Der Timer wird zurückgesetzt\n\n")
        f = open('log.txt', 'a')
        string = "Uptime_Raw: " + str(round(time.time())) + " | Uptime_Days: " + str(
            count_days) + " | Uptime_Hours: " + str(round(now / stdMult)) + "\n\n"
        f.write(string)
        f.close()
        count_days = count_days + 1
        now = 0
    time.sleep(0.01)
print (count_sec)
