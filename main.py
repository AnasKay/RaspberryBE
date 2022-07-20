import random
from wsgiref.simple_server import make_server
import falcon
#import serial

#ser = serial.Serial(
#    port='/dev/ttyS0',
#    baudrate=115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
#    )

#ser2 = serial.Serial(
#    port='/dev/ttyAMA1',
#    baudrate=115200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
#    )

def randomSensorData(min, max):
    n = random.randint(min, max)
    return  n



class helpPage:

    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = ('Hello! Following endpoints are avalialbe:\n\n' +
                     req.url + '<path>\n\n'
                               'Available paths:\n'
                               '    /uart, /second\n'
                               'Available POST req Body keys:\n'
                               '   "message"'
                     )


#class SendUart:

#    def on_post(self, req, resp):
#        message = req.media.get("message")
#        print('I was called on ser with \"'+message+'\" in the req!\n')
#        ser.start()
#        ser.write(message.encode())
#        print("ser write done")
#        ser.stop()
#        resp.media = {
#            "message": message
#        }
#        resp.status = falcon.HTTP_200


#class SendUart2:

#    def on_post(self, req, resp):
#        message = req.media.get("message")
#        print('I was called on ser2 with \"'+message+'\" in the req!\n')
#        ser2.start()
#        ser2.write(message.encode())
#        print("ser2 write done")
#        ser2.stop()
#        resp.media = {
#            "message": message
#        }
#        resp.status = falcon.HTTP_200


class getTemperature:

    def on_get(self, req, resp):
        #message = req.media.get("message")
        print('I was called on getTemp\n')
        currentTemp = {
            'Temp': (randomSensorData(0,35))
        }
        # TODO: send data to DB
        resp.media = currentTemp
        resp.status = falcon.HTTP_200

class getBatteryLevel:

    def on_get(self, req, resp):
        print('I was called on getBatteryLevel\n')
        currentBatteryLvl = {
           'Battery': (randomSensorData(0, 100))
        }
        # TODO: send data to DB
        resp.media = currentBatteryLvl
        resp.status = falcon.HTTP_200

class getSpeed:

    def on_get(self, req, resp):
        print('I was called on getSpeed\n')
        currentSpeed = {
           'Speed': (randomSensorData(0, 10))
        }
        # TODO: send data to DB
        resp.media = currentSpeed
        resp.status = falcon.HTTP_200


class getGyrosensor:

    def on_get(self, req, resp):
        print('I was called on getGyro\n')
        currentGyro = {
           'Gyro': ({
               'x': randomSensorData(-10, 10),
               'y': randomSensorData(-10, 10),
               'z': randomSensorData(-10, 10)
               })
        }
        #TODO: send data to DB
        resp.media = currentGyro
        resp.status = falcon.HTTP_200


app = falcon.App(middleware=falcon.CORSMiddleware(allow_origins='*', allow_credentials='*'))
help_page = helpPage()
#send_uart = SendUart()
#send_uart2 = SendUart2()
getTemp = getTemperature()
getBat = getBatteryLevel()
getSpd = getSpeed()
getGyro = getGyrosensor()

app.add_route('/', help_page)
#app.add_route('/uart', send_uart)
#app.add_route('/uart2', send_uart2)
app.add_route('/temp', getTemp)
app.add_route('/bat', getBat)
app.add_route('/speed', getSpd)
app.add_route('/gyro', getGyro)

if __name__ == '__main__':
    with make_server('', 80, app) as httpd:
        print('Server is listening on Port 80 ...')
        httpd.serve_forever()