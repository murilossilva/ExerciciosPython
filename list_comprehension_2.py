carrinho = []
carrinho.append(('Produto_1', 30))
carrinho.append(('Produto_2', 50))
carrinho.append(('Produto_3', 20))

total = sum([x[1] for x in carrinho])
print(f'A soma total da sua compra foi de R$: {total:.2f}')
