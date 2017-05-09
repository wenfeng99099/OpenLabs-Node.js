#!/usr/bin/python
import websocket
import json
import serial
import thread
import time

def on_message(ws, message):
    connection.write(""+message+"".encode())
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "Socket connection closed"

def on_open(ws):
    data_rw = ["OpenLabsClient","Connect"]
    data_js = json.dumps(data_rw)
    ws.send(data_js)
    #while True:
        # print 'Am in!!'
        # data_log = connection.readline().decode('ascii')
        # print data_log
    def run(*args):
        prevTime = None
        while True:
            data_log = connection.readline()
            if prevTime is None:
                time_delay = 0
            else:
                current_time = int(time.time()*1000)
                time_delay = current_time - prevTime
                prevTime = current_time
            data_log += "T"+str(time_delay)
            print (data_log)
            data_rw = ["OpenLabsHost",data_log]
            data_js = json.dumps(data_rw)
            ws.send(data_js)
            time.sleep(0.5)
            pass
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    connection = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout = 0.5)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://107.170.249.214:3131",
        on_open = on_open,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close
    )
    ws.run_forever()