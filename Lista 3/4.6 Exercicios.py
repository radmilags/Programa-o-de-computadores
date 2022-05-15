# 1. Escreva um programa que leia um número inteiro, que corresponde a um sequencia de chamada em uma fila de espera, 
# e mostre a mensagem Proximo:
# 001, onde o número deve ser mostra com 3 algarismo, preenchendo com zeros
# a esquerda.
# Exemplo de entrada e saída para a execução do programa:
n = int(input())
print("Proximo: {:03d}".format(n))

# 2. Escreva um programa que calcule o valor de um salário após um reajuste. O
# programa deve ler da entrada padrão o valor atual do salário mínimo percentual
# de reajuste, também um número real. O program deve calcular o percentual o
# novo valor do salário e mostrar o valor atual, e o novo valor após o reajuste.
# Exemplo de entrada e saída para a execução do programa:
n = int(input())
p = float(input())
n1 = (p*n/100) + n
print("Atual: ", n)
print("Novo: {:.2f}".format(n1))

# 3. Escreva um programa que leia o raio de um círculo e mostre a área circunferência do mesmo, 
# com exatamente 4 casas decimais.
# Considere o valor de π = 3.14159
# Exemplo de entrada e saída para a execução do programa:
r = float(input())
r = 3.14159 * r * r
print("{:.4f}".format(r))

# 4. Escreva um programa que leia o valor final de venda de um automóvel e calcule
# seu preço sem impostos, os valores pagos para cada tipo de imposto e imprima
# os resultados. Considere que, para automóveis populares, o ICMS (Imposto
# sobre Circulação de Mercadorias e Serviços) é de 18%, o IPI (Imposto sobre
# Produtos Industrializados) é de 13%, o PIS (Programa de Integração Social
# ) é de 1, 4%, e a Cofins (Contribuição para o Financiamento da Seguridade
# Social) é de 7, 6%. Todos os impostos são calculados sobre o valor de custo do
# automóvel. Todos os valors devem ser mostrados com 2 (duas) casas decimais.
# Exemplo de entrada e saída para a execução do programa:
vt = float(input())
vi = vt - (vt*40/140)
icms = (vt*18/140)
ipi = (vt*13/140)
pis = (vt*1.4/140)
cofins = (vt*7.6/140)
print("ICMS: {:.2f}".format(icms))
print("IPI: {:.2f}".format(ipi))
print("PIS: {:.2f}".format(pis))
print("Cofins: {:.2f}".format(cofins))
print("Valor sem impostos: {:.2f}".format(vi))