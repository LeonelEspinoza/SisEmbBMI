# (C5328-1): Tarea 4 _BMI270_
_11-2024_  
Tarea 4 del ramo Sistemas Embebidos y Sensores.
Integrantes:  
- Diego Opazo
- Felipe Lemos
- Leonel Espinoza
## Antes de ejecutar
### ESP y BMI-270
Para este proyecto es necesario cargar una ESP con el código en el archivo `main/bmi270.c`.  
El archivo debe ser compilado (_build_), y después cargado (_flash_) a una ESP conectada a un BMI270.

### Ambiente virtual
Para ejecutar la aplicación de python es necesario crear un ambiente virtual y en el mismo instalar las librerías y modulos necesarios.

Para crear un ambiente virtual:

    python -m venv /path/to/new/virtual/environment

Activar el ambiente virtual:

    /{path to virtual environment}/scripts/activate

E instalar requirements.txt

    pip install -r app/requirements.txt

## Ejecución

Una vez la ESP conectada a una BMI 270 ya tiene el codigo `main/bmi270.c` y esta corriendo, se puede ejecutar la aplicación gráfica de python.  

Para ejecutar la aplicación:

    python app/main_app.py

Lo primero que realiza la aplicación es intentar sincronizarse con la ESP, por lo tanto puede demorar un momento.

## Utilizar la aplicación
Dentro de la aplicación habran 9 botones:
- Solicitar ventana  
    - Este boton solicita una ventana de datos de giroscopio y acelerometro a la ESP.
    - Es necesario ejecutar esta opcion antes que cualquier otra para el buen funcionamiento de la aplicación

- Gráfico aceleración
    - Muestra las mediciones obtenidas del acelerometro en la ventana solicitada

- Gráfico giroscopio
    - Muestra las mediciones obtenidas del giroscopio en la ventana solicitada

- Gráfico RMS
    - Muestra el RMS calculado para cada eje de ambos sensores

- Tabla 5-Peaks
    - Muestra los 5 peaks de las mediciones para cada eje de ambos sensores

- Gráfico FFT reales
    - Muestra la parte real del FFT calculado para las mediciones de cada eje para ambos sensores

- Gráfico FFT imaginarios
    - Muestra la parte imaginaria del FFT calculado para las mediciones de cada eje para ambos sensores

- Cambiar tamaño ventana
    - podrá ingresar un nuevo tamaño de ventana de mediciones. Es recomendable no solicitar más de 100 datos, pues más allá la aplicación puede fallar.
    - Al apretar "Cambiar tamaño de ventana" después de haber ingrasado el nuevo tamaño de ventana se realizará el cambio. No hay ningún feedback en la aplicación.

- Cerrar conexión
    - Cierra la conexión con la ESP y solicita a la ESP que se reinicie.

### [Video demostrativo](https://youtu.be/MJW4lkWswok)
El enlace lo llevará a un video demostrativo de las funcionalidades de la aplicación



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

La tarea debe entregarse antes del día _02-12-2024 23:59_ 