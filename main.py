from machine import Pin
import time, network, os, machine, dht, sys

def blink():
    for i in range(0,20):
        Pin(2, Pin.OUT).off()
        #print("on")
        time.sleep(0.05)
        Pin(2, Pin.OUT).on()
        #print("off")
        time.sleep(0.05)

def info():
    print("Es gibt folgende Dateien:\n")
    print(os.listdir())
    print("\n")
    print("Verbunden mit Netzwerk:")
    print(network.WLAN(network.STA_IF).isconnected())
    print("\n")
    print("IP-address, netmask, gateway, DNS\n")
    print(network.WLAN(network.STA_IF).ifconfig())


def restart():
    print("Das Gerät wird neugestartet\n")
    Pin(2, Pin.OUT).off()
    time.sleep(2)
    machine.reset()

def allDPinsOFF():
    #Pin(16, Pin.OUT).off()
    Pin(5, Pin.OUT).off()
    Pin(4, Pin.OUT).off()
    #Pin(0, Pin.OUT).off()
    #Pin(2, Pin.OUT).off()
    Pin(14, Pin.OUT).off()
    Pin(12, Pin.OUT).off()
    Pin(13, Pin.OUT).off()
    Pin(15, Pin.OUT).off
    print("complete\n")

def getPinBelegung():
    print("\n"
    "DO - 16 (-USER--WAKE)\n"
    "D1 - 05\n"
    "D2 - 04\n"
    "D3 - 00 (-FLASH)\n"
    "D4 - 02 (-TXD1) = LED??\n"
    "D5 - 14 (-HSCLK)\n"
    "D6 - 12 (-HMSISO)\n"
    "D7 - 13 (-RXD2--HMOSI)\n"
    "D8 - 15 (-TXD2--HCS)\n"
    )

def onPin(pin):
    Pin(pin, Pin.OUT).on()

def offPin(pin):
    Pin(pin, Pin.OUT).off()

def ente():
    dh = dht.DHT22(machine.Pin(4))
    while True:
        try:
            time.sleep(1)
            dh.measure()
            time.sleep(2)
            t = dh.temperature()
            h = dh.humidity()
            print('Temp: ', t, 'C\Humidity: ', h, '%')
            time.sleep(1)
        except OSError as e:
            print("Cant read:", e)
            sys.print_exception(e)

def helpme():
    print("Functions:\n info()\n blink()\n"
    " restart()\n allDPinsOFF()\n getPinBelegung()\n"
    " onPin()\n offPin()\n ente()\n startWebserver()\n deleteFile(input)\n getTempHum():\n")

blink()

def dino():
    print("Starting DHT22.")
    d = dht.DHT11(machine.Pin(14, machine.Pin.PULL_UP))
    while True:
        print("Measuring.")
        retry = 0
        while retry < 3:
            try:
                d.measure()
                break
            except:
                retry = retry + 1
                print(".", end = "")
        print("")
        if retry < 3:
            print("Temperature: %3.1f °C" % d.temperature())
            print("Humidity: %3.1f %% RH" % d.humidity())
        time.sleep(5)

def getTempHum():
    d = dht.DHT11(machine.Pin(14, machine.Pin.PULL_UP))
    try:
        d.measure()
    except:
        return("No Data")
    s = (str(d.temperature()) + "°C" + "bei " + str(d.humidity()) +"% Luftfeuchtigkeit")
    return s

def deleteFile(input):
    import os
    os.remove(input)
    print(os.listdir())

def startWebserver():
    try:
        import usocket as socket
    except:
        import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
  <p>GPIO state: <strong>""" + getTempHum() + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""

    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        led_on = request.find('/?led=on')
        led_off = request.find('/?led=off')
        if led_on == 6:
            print('LED ON')
            blink()
        if led_off == 6:
            print('LED OFF')
            blink()
        response = html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
