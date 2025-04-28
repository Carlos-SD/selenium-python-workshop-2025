Feature: Articulo en mercadolibre
    Scenario: Buscar “iPhone 13” y verificar que aparecen resultados que contienen el texto “iPhone”.
        Given el usuario se encuentra en la seccion de busqueda de mercadolibre
        When el usuario escribe Iphone 13
        Then aparecen resultados que contienen el texto Iphone