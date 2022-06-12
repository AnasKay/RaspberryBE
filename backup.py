from wsgiref.simple_server import make_server
import falcon
import serial

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

ser2 = serial.Serial(
    port='/dev/ttyAMA1',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )


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


class SendUart:

    def on_post(self, req, resp):
        message = req.media.get("message")
        print('I was called on ser with \"'+message+'\" in the req!\n')
        if(not ser.is_open):
            ser.open()
        ser.write(message.encode())
        print("ser write done")
        ser.close()
        resp.media = {
            "message": message
        }
        resp.status = falcon.HTTP_200


class SendUart2:

    def on_post(self, req, resp):
        message = req.media.get("message")
        print('I was called on ser2 with \"'+message+'\" in the req!\n')
        if(not ser2.is_open):
            ser2.open()
        ser2.write(message.encode())
        print("ser2 write done")
        ser2.close()
        resp.media = {
            "message": message
        }
        resp.status = falcon.HTTP_200





app = falcon.App()
help_page = helpPage()
send_uart = SendUart()
send_uart2 = SendUart2()

app.add_route('/', help_page)
app.add_route('/uart', send_uart)
app.add_route('/uart2', send_uart2)

if __name__ == '__main__':
    with make_server('', 80, app) as httpd:
        print('Server is listening on Port 80 ...')
        httpd.serve_forever()

