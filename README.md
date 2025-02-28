# IoT

Monitoreo de Temperatura con Raspberry Pi Pico W y ThingSpeak

Este proyecto permite medir la temperatura usando el sensor interno de la Raspberry Pi Pico W y enviar los datos a ThingSpeak. Además, MATLAB se usa para calcular el promedio de las últimas 10 lecturas y enviarlo a otro canal en ThingSpeak.

## Requisitos

-Raspberry Pi Pico W

-Sensor LM35

-Breadboard

-Cables

-MicroPython instalado en la Pico W

-Cuenta en ThingSpeak

-MATLAB (para calcular el promedio)

## Instalación de MicroPython en la Raspberry Pi Pico W

Descarga el firmware de MicroPython desde: https://micropython.org/download/rp2-pico-w

Conecta la Raspberry Pi Pico W al PC mientras mantienes presionado el botón BOOTSEL.

La Pico W aparecerá como una unidad USB (RPI-RP2).

Copia el archivo .uf2 descargado y pégalo en la unidad RPI-RP2.

La Pico W se reiniciará con MicroPython instalado.

## Empezar a leer la temperatura 

Toma el archivo main.py que se encuentra en el repositorio y guardalo dentro de la Raspberry Pi Pico W

## Alimentar la Raspberry Pi Pico W sin Computadora

Puedes conectar la Pico W a:

Cargador USB (5V, 500mA mínimo)

Power Bank (batería externa)
