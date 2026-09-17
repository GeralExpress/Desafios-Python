listamercado = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90, 'capinha', 12)

for c in range(0, len(listamercado), 2):
    print(f'{listamercado[c]:.<32}R$ {listamercado[c + 1]:.2f}' )