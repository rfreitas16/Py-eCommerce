

def formata_preco(val):
    return f'R${val:.2f}'. replace('.' ,',')

#quantidade de itens no carrinho
def cart_total_qtd(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])

#soma dos valores do carrinho
def cart_totals(carrinho):
    return sum(
            [
                item.get('preco_quantitativo_promocional')
                if item.get('preco_quantitativo_promocional')
                else item.get('preco_quantitativo')
                for item
                in carrinho.values()
            ]
        )