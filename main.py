import matplotlib.pyplot as plt


def plot_graph(d, n, title, currency, period):
	t = [t for t in range(1,n+1)]
	for key in d.keys():
		plt.plot(t, d[key], label=key)
	plt.grid()
	plt.xlabel(f"Período em {period}")
	plt.ylabel(f"Valor em {currency}")
	plt.xticks(t)
	plt.title(title)
	plt.legend()	
	plt.show()

currency = input("Entre o nome da moeda: ")
P = float(input(f"Entre o valor a ser financiado em {currency}: "))
period = input("Entre como o período está discretizado (anos, por exemplo): ")
n = int(input(f"Entre o período, em {period}: "))
i = float(input("Entre a taxa de juros, em decimais (0.10, por exemplo): "))

# SAF
A = (P*i*(1+i)**n)/((1+i)**n-1)
S_0 = P
J_1 = S_0 * i
a_1 = A - J_1

A_t = [A for t in range(1,n+1)]
a_t = [0 for t in range(1,n+1)]
a_t[0] = a_1
J_t = [0 for t in range(1,n+1)]
J_t[0] = J_1
S_t = [0 for t in range(1,n+1)]
S_t[0] = P - a_1

SAF = {"Parcela": A_t, "Juros": J_t, "Amortização": a_t, "Saldo devetor": S_t}

for t in range(1,n):
	J_t[t] = S_t[t-1] * i
	a_t[t] = A - J_t[t]
	S_t[t] = S_t[t-1] - a_t[t]
plot_graph(SAF, n, f"Sistema de Amortização Francês para {P} {currency} \n ao longo de {n} {period} com juros de {i*100}% por {period}", currency, period)


# SAC
a_t = [P/n for t in range(1,n+1)]
S_t = [P - P/n * t for t in range(1,n+1)]
J_t = [P * i for t in range(1,n+1)]

for t in range(1,n):
	J_t[t] = S_t[t-1] * i

A_t = [a_t[t] + J_t[t] for t in range(0,n)]

SAC = {"Parcela": A_t, "Juros": J_t, "Amortização": a_t, "Saldo devetor": S_t}

plot_graph(SAC, n, f"Sistema de Amortização Constante para {P} {currency} \n ao longo de {n} {period} com juros de {i*100}% por {period}", currency, period)

for key in SAF.keys():
	plot_graph({"SAC": SAC[key], "SAF": SAF[key]}, n,
	           f"Comparativo de {key} entre SAF e SAC para {P} reais \n ao longo de {n} {period} com juros de {i*100}% por {period}", currency, period)
