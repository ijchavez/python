from orden import Orden
from monitor import Monitor
from teclado import Teclado
from raton import Raton
from computadora import Computadora

teclado_hp = Teclado("HP", "usb")
raton_logitech = Raton("Logitech", "usb")
monitor_samsung = Monitor("HP", 15)

computadora_oficina = Computadora("Computadora de Oficina:", monitor_samsung, teclado_hp, raton_logitech)

teclado_acer = Teclado("Acer", "usb")
raton_asus = Raton("Asus", "usb")
monitor_noblex = Monitor("Noblex", 24)

computadora_hogar = Computadora("Computadora de Hogar", monitor_noblex, teclado_acer, raton_asus)

teclado_gamer = Teclado("gamer", "bluetooth")
raton_gamer = Raton("gamer", "bluetooth")
monitor_gamer = Monitor("gamer", 49)

computadora_gamer = Computadora("Computadora Gamer", monitor_gamer, teclado_gamer, raton_gamer)

teclado_gamer = Teclado("gamer", "bluetooth")
raton_gamer = Raton("gamer", "bluetooth")
monitor_gamer = Monitor("gamer", 49)

computadora_clon = Computadora("Computadora Armada", monitor_gamer, teclado_acer, raton_logitech)

# print(computadora_oficina)
# print(computadora_hogar)
# print(computadora_gamer)
# print(computadora_clon)

listaComputadoras = [computadora_oficina, computadora_hogar]
listaComputadoras1 = [computadora_gamer, computadora_hogar,computadora_gamer]
listaComputadoras2 = [computadora_gamer, computadora_hogar,computadora_oficina,computadora_clon]

orden1 = Orden(listaComputadoras)
print(orden1)

orden2 = Orden(listaComputadoras1)
print(orden2)

orden3 = Orden(listaComputadoras2)
print(orden3)