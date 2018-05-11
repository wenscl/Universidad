rubros = [
    (1, 'Dulce de Leche'),
    (2, 'Leche'),
    (3, 'Mantecas'),
    (4, 'Yogures'),
    (5, 'Crema de leche'),
    (6, 'Quesos'),
    (7, 'Kids'),
]

subrubros = [
    (1, 1, 'Clásico', 'Pote'),
    (2, 1, 'Repostero', 'Pote'),
    (3, 2, 'Leche en Polvo', 'Caja'),
    (4, 2, 'Entera', 'Caja'),
    (5, 2, 'Descremada', 'Caja'),
    (6, 2, 'Chocolatada', 'Caja'),
    (7, 3, 'Pan de manteca', 'Papel Aluminio'),
    (8, 3, 'Porción desayuno', 'Pote pequeño'),
    (9, 4, 'Bebibles', 'Sachet'),
    (10, 4, 'Batidos', 'Pote'),
    (11, 4, 'Con Cereales', 'Pote'),
    (12, 4, 'Con Colchón de Frutas', 'Pote'),
    (13, 4, 'Firme', 'Pote'),
    (14, 5, 'Clásica', 'Pote'),
    (15, 5, 'Doble', 'Pote'),
    (16, 6, 'Untables', 'Pote'),
    (17, 6, 'Pasta Blanda', 'Envoltorio plástico'),
    (18, 6, 'Pasta Dura', 'Envoltorio plástico'),
    (19, 6, 'Pasta Semidura', 'Envoltorio plástico'),
    (20, 6, 'Queso Crema', 'Pote'),
    (21, 6, 'Rallados', 'Bolsa'),
    (22, 7, 'Con top', 'Pote'),
    (23, 7, 'Flanes', 'Pote'),
    (24, 7, 'Leche Larga Vida', 'Caja'),
    (25, 7, 'Postres', 'Pote'),
]

resultado = [(index + 1, "Producto {} - Ilolay".format(index + 1), subrubro[3], rnombre, subrubro[2]) for index, subrubro in enumerate(subrubros) for rid, rnombre in rubros if subrubro[1] == rid]

for x in resultado:
    print('{},'.format(x))
