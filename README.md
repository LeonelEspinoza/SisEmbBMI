# (C5328-1): Tarea 4 _BMI270_
_11-2024_  
Tarea 4 del ramo Sistemas Embebidos y Sensores.
Integrantes:  
- Diego Opazo
- Felipe Lemos
- Leonel Espinoza

## Descripción
El proyecto será una aplicación simple con _Python_ encargada de recibir datos desde la _ESP32_. La _ESP32_ recibirá a su vez datos crudos desde el _BMI270_.  
Estos datos son:
- Aceleracion en los ejes x,y,z
- Giroscopio en los ejes x,y,z

La _ESP_ recibirá los datos del _BMI270_ de manera constante a intervalos definidos por nosostros. Esta recepción se dará por una comunicación _I2C_. Debemos definir el tamaño que condormará nuestras ventanas de datos. Una vez recibida dicha cantidad de datos (la misma cantidad para cada variable) deberán procesarlos y generar métricas a partir de cada ventana. estas métricas serán:
- 5 peaks (datos mayores) de cada ventana.
- RMS de cada ventana. Esto se calcula como: $$\sqrt{\frac{\sum_{i=1}^{n}a^{2}_{i}}{n}}$$
- FFT de cada ventana.  

La _ESP32_ entonces mandará (por una comunicación _UART_) al computador estas métricas junto con las ventanas originales de datos.  

El computador deberá graficar todos los datos que reciba en una interfaz gráfica hecha con _PyQt5_, y deberá permitir interactuar con la _ESP_ mediante inputs para decir cuándo recibir nuevos datos (después de recibir las ventanas completas y las métricas ña _ESP_ debe esperar las instrucciones de la aplicación de _Python_). Queda a su criterio si quieren hacer que la _ESP_ mande todos los datos en un sólo envio o si los va a mandar continuamente, simulando mediciones en tiempo real.

El comportamiento esperado es el siguiente:  
1. Ejecutan la app de _Pyhton_. El menú principal de la app debe darlse la opcion de, por lo menos:

    - Solicitar una ventana de datos
        1. Solicitan una ventana de datos
        2. La ESP comienza a obtener los datos del sensor.
        3. La ESP manda los datos a su computador.
        4. La ESP queda esperando instrucciones.
        5. Python recibe los datos y los muestra.
        6. Vuelven al menu principal.

    - Cambiar el tamaño de la ventana de datos
        1. Solicitan el cambio de tamaño
        2. la ESP cambia el tamaño de la ventana y lo guarda en la _NVS_
        3. Vuelven al menú principal

    - Cerrar la conexión (esto debe reiniciar la _ESP_)
        1. Anuncian el cierre
        2. La _ESP_ se reinicia
        3. La aplicación termina

## Entrega
Se debe entregar:
- Su código funcionando, ya sea en un .zip (sin build) o un link a su repo de GitHub (sin build).
- Un video demostrando el funcionamiento del código con lo solicitado en la descripción. El video debe mostrar:  
    1. Obtención de una primera ventana
    2. Solicitud de una segunda ventana
    3. Cambio de tamaño de ventana
    4. Solicitud de una tercera ventana (con el nuevo tamaño)
    5. Reinicio de la _ESP_ (corte de comunicación)
    6. Obtencion de una cuarta ventana luego del corte de comunicación (deberán ejecutar su app nuevamente). Esta ventana debe ser el del nuevo tamaño que difinieron en el paso 3.

La tarea debe entregarse antes del día _29-11-2024 23:59_ 

## To do
 [X] Lograr imprimir los tres ejes de aceleración  
 [X] Lograr imprimir los tres ejes de giroscopio  
 [ ] Lograr comunicación Python-C  
 [ ] ...  
 [ ] ...  