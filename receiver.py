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
select = None

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
    global ax, ay, az 
    global gx, gy, gz
    global peak_ax, peak_ay, peak_az, peak_gx, peak_gy, peak_gz
    global rms_a_g
    global fft_ax, fft_ay, fft_az, fft_gx, fft_gy, fft_gz
    global ffti_ax, ffti_ay, ffti_az, ffti_gx, ffti_gy, ffti_gz
    
    raw_arrays    =  []
    rms_array     =  []
    peaks_arrays  =  []
    fft_re_arrays =  []
    fft_im_arrays =  []

    send_message(pack('2s',"1".encode()))
    
    i=0
    while i<6 :
        raw_arrays[i]    = recive_raw()
        rms_array[i]     = recive_rms()
        fft_re_arrays[i] = recive_fft_re()
        fft_im_arrays[i] = recive_fft_im()
        peaks_arrays[i]  = recive_peaks()
        i+=1

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
    return

def cambiar_tamano_ventana(nuevo_t):

    send_message(pack('2s',"2".encode()))

    wSize = nuevo_t
    if nuevo_t < 10:
        nuevo_t = "00" + str(nuevo_t)
    elif nuevo_t < 100:
        nuevo_t = "0" + str(nuevo_t)
    else:
        nuevo_t = str(nuevo_t)
    
    print(wSize)
    #mandamos tamaño de ventana
    send_message(pack('3s',nuevo_t.encode()))

def cortar_comunicacion():
    send_message(pack('2s',"3".encode()))
    ser.close()

def create_time_array():
    global time_array
    measurement_time = window_size/800
    interval = measurement_time/window_size

    time_array = np.arange(0,measurement_time,interval).tolist()

#____________________________________________________________
#   MAIN
#____________________________________________________________
print("<receiver.py> inicio main")

print("<receiver.py> ready main")