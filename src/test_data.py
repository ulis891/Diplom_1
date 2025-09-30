class BunData:
    BUN_NAME = "test"
    BUN_PRICE = 100

    BUN_TEST_DATA = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ]


class IngredientData:
    INGREDIENT_TYPE = "test Ingredient type"
    INGREDIENT_NAME = "test Ingredient name"
    INGREDIENT_PRICE = 150

    INGREDIENTS_TEST_DATA = [
        ("SAUCE", "Соус традиционный", 50),
        ("SAUCE", "Соус spicy", 90),
        ("FILLING", "Биокотлета", 500)
    ]


class BurgerData(BunData, IngredientData):
    TEST_BURGERS = [
        {
            "bun": BunData.BUN_TEST_DATA[0],
            "ingredients": [IngredientData.INGREDIENTS_TEST_DATA[0]],
            "price": 250
        },
        {
            "bun": BunData.BUN_TEST_DATA[1],
            "ingredients": [IngredientData.INGREDIENTS_TEST_DATA[1]],
            "price": 490
        },
        {
            "bun": BunData.BUN_TEST_DATA[2],
            "ingredients": [IngredientData.INGREDIENTS_TEST_DATA[2]],
            "price": 1100
        },
        {
            "bun": BunData.BUN_TEST_DATA[0],
            "ingredients": [IngredientData.INGREDIENTS_TEST_DATA[0], IngredientData.INGREDIENTS_TEST_DATA[1]],
            "price": 340
        }
    ]
