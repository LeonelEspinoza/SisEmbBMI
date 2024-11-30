import serial
from struct import pack, unpack
import time
import numpy as np

# Se configura el puerto y el BAUD_Rate
PORT = 'COM3'  # Esto depende del sistema operativo
BAUD_RATE = 115200  # Debe coincidir con la configuracion de la ESP32

# Se abre la conexion serial
ser = serial.Serial(PORT, BAUD_RATE, timeout = 1)

#variable para manejar los casos
window_size = 0

#listas con datos
ax = []
ay = []
az = []

gx = []
gy = []
gz = []

peak_ax = []
peak_ay = []
peak_az = []
peak_gx = []
peak_gy = []
peak_gz = []

rms_a_g = []

fft_ax = []
fft_ay = []
fft_az = []
fft_gx = []
fft_gy = []
fft_gz = []

ffti_ax = []
ffti_ay = []
ffti_az = []
ffti_gx = []
ffti_gy = []
ffti_gz = []

time_array = []

# Funciones
def send_message(message):
    """ Funcion para enviar un mensaje a la ESP32 """
    ser.write(message)

def receive_response():
    """ Funcion para recibir un mensaje de la ESP32 """
    response = ser.readline()
    return response

def receive_data(msg_size):
    """ Funcion que lee {msg_size} floats de la ESP32 """
    data = ser.read(4*msg_size)
    data = unpack(f"{msg_size}f", data)
    return data

def send_end_message():
    """ Funcion para enviar un mensaje de finalizacion a la ESP32 """
    end_message = pack('4s', 'END\0'.encode())
    ser.write(end_message)

def make_f(size):
    strf = "f" * size
    return strf

def recive_raw():
    while True:
        if ser.in_waiting > 0:
            try:
                raw_array = receive_data(window_size)
            except:
                continue
            finally:
                return raw_array

def recive_rms():
    while True:
        if ser.in_waiting > 0:
            try:
                rms = receive_data(1)
            except:
                continue
            finally:
                return rms

def recive_peaks():
    while True:
        if ser.in_waiting > 0:
            try:
                peaks = receive_data(5)
            except:
                continue
            finally:
                return peaks

def recive_fft_re():
    while True:
        if ser.in_waiting > 0:
            try:
                fft_re = receive_data(window_size)
            except:
                continue
            finally:
                return fft_re

def recive_fft_im():
    while True:
        if ser.in_waiting > 0:
            try:
                fft_im = receive_data(window_size)
            except:
                continue
            finally:
                return fft_im
    
def solicitar_ventana():
    print("<receiver.solicitar_ventana()> start")
    global ax, ay, az 
    global gx, gy, gz
    global peak_ax, peak_ay, peak_az, peak_gx, peak_gy, peak_gz
    global rms_a_g
    global fft_ax, fft_ay, fft_az, fft_gx, fft_gy, fft_gz
    global ffti_ax, ffti_ay, ffti_az, ffti_gx, ffti_gy, ffti_gz
    
    raw_arrays    =  [0 for i in range(6)]
    rms_array     =  [0 for i in range(6)]
    peaks_arrays  =  [0 for i in range(6)]
    fft_re_arrays =  [0 for i in range(6)]
    fft_im_arrays =  [0 for i in range(6)]

    send_message(pack('2s',"1".encode()))
    print("<receiver.solicitar_ventana()> selection sent")
    
    print("<receiver.solicitar_ventana()> receiving data")
    i=0
    while i<6 :
        raw_arrays[i]    = recive_raw()
        print(f"raw_arrays[{i}]: {raw_arrays[i]}")
        
        rms_array[i]     = recive_rms()
        print(f"rms_array[{i}]: {rms_array[i]}")
        
        fft_re_arrays[i] = recive_fft_re()
        print(f"fft_re[{i}]: {fft_re_arrays[i]}")
        
        fft_im_arrays[i] = recive_fft_im()
        print(f"fft_im_arrays[{i}]: {fft_im_arrays[i]}")
        
        peaks_arrays[i]  = recive_peaks()
        print(f"peaks_arrays[{i}]: {peaks_arrays[i]}")
        i+=1
        print("\n")

    print("<receiver.solicitar_ventana()> assigning results")
    
    rms_a_g = rms_array

    gx      = raw_arrays[0]
    fft_gx  = fft_re_arrays[0]
    ffti_gx = fft_im_arrays[0]
    peak_gx = peaks_arrays[0]
    
    gy      = raw_arrays[1]
    fft_gy  = fft_re_arrays[1]
    ffti_gy = fft_im_arrays[1]
    peak_gy = peaks_arrays[1]
    
    gz      = raw_arrays[2]
    fft_gz  = fft_re_arrays[2]
    ffti_gz = fft_im_arrays[2]
    peak_gz = peaks_arrays[2]
    
    ax      = raw_arrays[3]
    fft_ax  = fft_re_arrays[3]
    ffti_ax = fft_im_arrays[3]
    peak_ax = peaks_arrays[3]
    
    ay      = raw_arrays[4]
    fft_ay  = fft_re_arrays[4]
    ffti_ay = fft_im_arrays[4]
    peak_ay = peaks_arrays[4]
    
    az      = raw_arrays[5]
    fft_az  = fft_re_arrays[5]
    ffti_az = fft_im_arrays[5]
    peak_az = peaks_arrays[5]

    create_time_array()
    create_5peak_str()
    print("<receiver.solicitar_ventana()> finish")
    return

def cambiar_tamano_ventana(nuevo_t):
    global window_size
    send_message(pack('2s',"2".encode()))

    window_size = nuevo_t
    if nuevo_t < 10:
        nuevo_t = "00" + str(nuevo_t)
    elif nuevo_t < 100:
        nuevo_t = "0" + str(nuevo_t)
    else:
        nuevo_t = str(nuevo_t)
    
    #mandamos tamaño de ventana
    send_message(pack('3s',nuevo_t.encode()))

    print(f"<receiver.cambiar_tamano_ventana({nuevo_t})> window_size = {window_size}")

def cortar_comunicacion():
    send_message(pack('2s',"3".encode()))
    ser.close()

def create_time_array():
    global time_array
    measurement_time = window_size/800
    interval = measurement_time/window_size

    time_array = np.arange(0,measurement_time,interval).tolist()

def create_5peak_str():
    global peak_ax, peak_ay, peak_az, peak_gx, peak_gy, peak_gz

    peak_ax = ', '.join(map(str,peak_ax))
    peak_ay = ', '.join(map(str,peak_ay))
    peak_az = ', '.join(map(str,peak_az))
    peak_gx = ', '.join(map(str,peak_gx))
    peak_gy = ', '.join(map(str,peak_gy))
    peak_gz = ', '.join(map(str,peak_gz))



#____________________________________________________________
#   MAIN
#____________________________________________________________
print("<receiver.py> inicio main")
#wait for OK_setup

#Enviar mensaje 'BEGIN'
message = pack('6s','BEGIN\0'.encode())
send_message(message)
print("<receiver.py> 'BEGIN' sended")

print("<receiver.py> wating 'OK setup'")
c = 0
while True:
    if c>100000:
        print("<receiver.py> 'BEGIN' resended")
        message = pack('6s','BEGIN\0'.encode())
        send_message(message)
        c=0
    if ser.in_waiting > 0:
        try:
            response = ser.readline()
            response = unpack("s", response)
        except:
            continue
        finally:
            if str(response).rfind('OK setup') == -1:
                continue
            break
    c+=1

print("<receiver.py> waiting for window size")
#wait for window size in NVS
while True:
    if ser.in_waiting > 0:
        try:
            window_size_bytes = ser.read(4)
            print("<receiver.py> serial readed")
            window_size_bytes = unpack("i", window_size_bytes)
            print("<receiver.py> unpacked: "+ str(window_size_bytes))
            window_size = int.from_bytes(window_size_bytes)
            print("<receiver.py> window size: "+str(window_size))
        except:
            continue
        finally:
            if window_size < 1:
                print("<receiver.py> Error! window size < 1")
                continue
            message = pack("3s", 'OK\0'.encode())
            send_message(message)
            print("<receiver.py> 'OK' sent")
            break
print("<receiver.py> ready main")