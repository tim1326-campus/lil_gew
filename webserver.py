# Complete project details at https://RandomNerdTutorials.com
import socket

ts_hum = '60'


def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1

def web_page():
    f = open("lil_gew_Website/lilgewWebsite.html", "r")
    temp = f.read()
    f.close()
    test='''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Gewächshaussteuerung</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <style>
        body {
            background-color: #157347;
        }

        .container {
            margin-top: 20px;

        }

        .row {
            margin-bottom: 10px;
        }

        div.contentshit {
            /*background: url(bg.jpg) no-repeat center center fixed;*/
            background: url(https://images.pling.com/img/00/00/50/43/77/1277473/81a30426d9fcda245f6267b1e583400f8924.jpg) no-repeat center center fixed;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
        }
    </style>
</head>
<body>
<div class="contentshit" >
<div class="container" style="color: white; font-family: Rockwell; margin-top: 0px;" id="ueberschriftContainer">
    <div class="row" style="padding-top: 20px;">
        <div class="col">
        </div>
        <div class="col">
            <h2>Gewächshaussteuerung</h2>
        </div>
        <div class="col">
               <p class="text" style="font-size: small; vertical-align: top;" align="right">Geräte-Uhrzeit 17:05 Uhr</p>
        </div>
    </div>
    <div class="row justify-content-center" style="">
        <div class="col-2 rounded bg-dark bg-opacity-50" align="center">
            Temperature = 69°C
        </div>
        <div class="col-1"></div>
        <div class="col-2 rounded bg-dark bg-opacity-50" align="center">
            Humidity = 69%
        </div>

    </div>
</div>

    <div class="container bg-light bg-opacity-50 rounded-top border" id="schwellenwert_luftfeutigkeit">
        <div class="row bg-secondary bg-opacity-75">
            <div class="col">
                Schwellenwert der Luftfeuchtigkeit
            </div>
        </div>
        <div class="row">
            <div class="col">
                Aktuell geht der MistMaker bei einer Luftfeuchtigkeit von '''+ ts_hum \
         + '''% an.
                <div class="border-bottom border-secondary "></div>
            </div>
            <div class="col-2 ">
               <form action="/" method="GET">
                    <div class="input-group">
                    <input name="ts_hum" type="number" class="form-control form-control-sm text-center" placeholder="Neuer Wert">
                        <div class="input-group-append">
                         <button class="btn btn-success btn-sm" type="submit" id="ts_hum_btn">submit</button>
                        </div>
                    </div>
               </form>
            </div>

        </div>
    </div>

    <div class="container bg-light bg-opacity-50 rounded-top border" id="lampenzyklus">
        <div class="row bg-secondary bg-opacity-75">
            <div class="col">
                Lampenzyklus
            </div>
        </div>
        <div class="row">
            <div class="col-8 ">
                Die erste Einschaltzeit der UV-Lampe beginnt um 6 Uhr und endet um 8 Uhr.
                <div class="border-bottom border-secondary "></div>
            </div>
            <div class="col-2">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Startzeit min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="lamp1">submit</button>
                    </div>
                </div>

            </div>
            <div class="col-2 ">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Stopzeit min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="lamp2">submit</button>
                    </div>
                </div>

            </div>
        </div>
        <div class="row">
            <div class="col-8 ">
                Die zweite Einschaltzeit der UV-Lampe beginnt um 16 Uhr und endet um 21 Uhr.
                <div class="border-bottom border-secondary "></div>
            </div>
            <div class="col-2">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Startzeit min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="lamp3">submit</button>
                    </div>
                </div>

            </div>
            <div class="col-2 ">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Stopzeit min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="lamp4">submit</button>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div class="container bg-light bg-opacity-50 rounded-top border text-" id="ventilatorzyklus">
        <div class="row bg-secondary bg-opacity-75">
            <div class="col">
                Ventilatorzyklus
            </div>
        </div>
        <div class="row">
            <div class="col">
                Der Ventilator schaltet sich alle 2 Stunden an.
                <div class="border-bottom border-secondary "></div>
            </div>
            <div class="col-2 ">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Startzeit min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="vent">submit</button>
                    </div>
                </div>

            </div>

        </div>
        <div class="row">
            <div class="col">
                Der Ventilator bleibt dann für 25 Minuten angeschaltet.
                <div class="border-bottom border-secondary "></div>
            </div>
            <div class="col-2 ">
                <div class="input-group">
                    <input type="text" class="form-control form-control-sm text-center" placeholder="Dauer min">
                    <div class="input-group-append">
                        <button class="btn btn-success btn-sm" type="button" id="vent_dur">submit</button>
                    </div>
                </div>

            </div>

        </div>
    </div>

    <div class="container rounded-top border" style="max-width: 500px; background: linear-gradient(180deg, rgba(47,143,45,1) 0%, rgba(8,160,172,1) 100%, rgba(3,146,212,0) 100%);" id="manuelleSteuerung">
        <div class="row bg-secondary bg-opacity-75">
            <div class="col">
                Manuelle Steuerung
            </div>
        </div>
        <div class="row">
            <div class="col">
                Licht:
            </div>
            <div class="col">
                Status: TEMP
            </div>
            <div class="col-1">
                <button class="btn btn-success" type="submit">On</button>
            </div>
            <div class="col-2">
                <button class="btn btn-danger" type="submit">Off</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                Ventilator:
            </div>
            <div class="col">
                Status: TEMP
            </div>
            <div class="col-1">
                <button class="btn btn-success" type="submit">On</button>
            </div>
            <div class="col-2">
                <button class="btn btn-danger" type="submit">Off</button>
            </div>
        </div>
        <div class="row">
            <div class="col">
                MistMaker:
            </div>
            <div class="col">
                Status: TEMP
            </div>
            <div class="col-1">
                <button class="btn btn-success" type="submit">On</button>
            </div>
            <div class="col-2">
                <button class="btn btn-danger" type="submit">Off</button>
            </div>
        </div>
    </div>
</div>

<p><a href="/?led=on">
    <button class="button">ON</button>
</a></p>
<p><a href="/?led=off">
    <button class="button button2">OFF</button>
</a></p>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
</body>
</html>'''

    html = ("""<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + '0' + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>""")
    return bytearray(temp, 'utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)


while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    temp = request.find('/?ts_hum=')
    if temp == 6:
        temp = find_str(request,'/?ts_hum=') + 9
        ts_hum = str(request[temp:temp+2])
        print(ts_hum)

    led_off = request.find('/?led=off')
    if led_off == 6:
        print('LED OFF')
        #led.value(0)
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')
    conn.send(b'Content-Type: text/html\n')
    conn.send(b'Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    #exit()

