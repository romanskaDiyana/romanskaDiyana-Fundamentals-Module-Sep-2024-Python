# Напишете програма, която чете ъгъл в радиани (десетично число) и го преобразува в градуси.
# Използвайте формулата: градус = радиан * 180 /Числото π в Python може да достъпите чрез модула math.
# За да ползвате функционалността му, първо трябва да включите констатата pi.

from math import pi

radians = float(input())
degrees = (radians * 180) / pi

print(degrees)