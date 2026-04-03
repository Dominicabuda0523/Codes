# Write code below 💖

c_pesos = int(input("How much do you have left in Colombian Pesos: "))
p_soles = int(input("How much do you have left in Peruvian Soles: "))
b_reais = int(input("How much do you have left in Brazilian Reais: "))

pesos_cnvrt = c_pesos * 0.00027
soles_cnvrt = p_soles * 0.29
reais_cnvrt = b_reais * 0.19

total_usd = pesos_cnvrt + soles_cnvrt + reais_cnvrt
print(f"Your total in US Dollars is ${total_usd}.")