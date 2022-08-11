descontos = 300.00
salario_fixo = 1800.00
vendas_mes = 240
valor_comissao = 0.2
valor_total_vendas = vendas_mes * valor_comissao
valor_salario_liquido = (salario_fixo + valor_total_vendas) - descontos


print(valor_salario_liquido)