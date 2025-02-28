import network
import urequests
import time
import machine

# Configura tu red Wi-Fi
SSID = "Tu_Red_WiFi"
PASSWORD = "Tu_Contraseña"

# Configura tu clave de API de ThingSpeak
THINGSPEAK_API_KEY = "TU_API_KEY"

# Conectar a Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Conectando a Wi-Fi...")
    time.sleep(1)

print("Conectado a Wi-Fi!")

# Función para leer la temperatura interna
def leer_temperatura():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    lectura = sensor_temp.read_u16() * conversion_factor
    temperatura = 27 - (lectura - 0.706) / 0.001721  # Fórmula del RP2040
    return temperatura

# Enviar datos a ThingSpeak cada 15 segundos
while True:
    temp = leer_temperatura()
    print(f"Temperatura: {temp:.2f} °C")

    url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={temp}"
    respuesta = urequests.get(url)
    respuesta.close()

    print("Dato enviado a ThingSpeak!")
    time.sleep(180)  # Esperar 180 segundos antes de enviar otro dato
