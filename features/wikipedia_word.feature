Feature: Titulo de articulo correcto
    Scenario: Buscar el término "Python (lenguaje de programación)" y verificar que el título del artículo mostrado sea correcto.
        Given el usuario se encuentra en la seccion de busqueda de wikipedia
        When el usuario escribe Python 
        Then aparece un articulo con el titulo Python