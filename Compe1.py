# Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

monto = float(input(""))

print ("NOTAS:")
billete100 = monto // 100
monto = monto % 100
print (int(billete100), "nota(s) de R$ 100.00")

billete50 = monto // 50
monto = monto % 50
print (int(billete50), "nota(s) de R$ 50.00")

billete20 = monto // 20
monto = monto % 20
print (int(billete20),  "nota(s) de R$ 20.00")

billete10 = monto // 10
monto = monto % 10
print (int(billete10), "nota(s) de R$ 10.00")

billete5 = monto // 5
monto = monto % 5
print (int(billete5), "nota(s) de R$ 5.00")

billete2 = monto // 2
monto = monto % 2
print (int(billete2), "nota(s) de R$ 2.00")

print ("MOEDAS:")
moneda1 = monto // 1
monto = monto % 1
print (int(moneda1), "moeda(s) de R$ 1.00")

moneda050 = monto // 0.50
monto = monto % 0.50
print (int(moneda050), "moeda(s) de R$ 0.50")

moneda025 = monto // 0.25
monto = monto % 0.25
print (int(moneda025), "moeda(s) de R$ 0.25")

moneda010 = monto // 0.10
monto = monto % 0.10
print (int(moneda010), "moeda(s) de R$ 0.10")

moneda005 = monto // 0.05
monto = monto % 0.05
print (int(moneda005), "moeda(s) de R$ 0.05")

moneda001 = monto // 0.01
monto = monto % 0.01
print (int(moneda001), "moeda(s) de R$ 0.01")