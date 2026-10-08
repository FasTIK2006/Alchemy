class Ingredient:
    def __init__(self, name, price, rarity, effect):
        self.name = name
        self.price = price
        self.rarity = rarity
        self.effect = effect

    def __str__(self):
        return f"{self.name} {self.price} {self.rarity} {self.effect}"

ingredients = {
    "mint": Ingredient(
        "Мята",
        5,
        "Обычная",
        "Лечение"
    ),

    "water": Ingredient(
        "Капля росы",
        7,
        "Обычная",
        "Очищение"
    ),

    "fire_flower": Ingredient(
        "Огненный цветок",
        10,
        "Обычная",
        "Энергия"
    ),

    "moon_dust": Ingredient(
        "Лунная пыль",
        20,
        "Редкая",
        "Магия"
    ),

    "mushroom": Ingredient(
        "Светящийся гриб",
        12,
        "Необычная",
        "Магия"
    ),

    "lavender": Ingredient(
        "Лаванда",
        8,
        "Обычная",
        "Спокойствие"
    ),

    "dragon_scale": Ingredient(
        "Чешуя дракона",
        50,
        "Легендарная",
        "Сила"
    ),

    "shadow_herb": Ingredient(
        "Теневая трава",
        25,
        "Редкая",
        "Тьма"
    )
}
print(ingredients["mint"])  # Output: Мята 5 Обычная Лечение