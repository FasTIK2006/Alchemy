class Potion:
    def __init__(self, name, description, price, effect):
        self.name = name
        self.description = description
        self.price = price
        self.effect = effect

    def __str__(self):
        return self.name



potions = { #зелья для игры
    "healing_potion": Potion(
        "Зелье лечения",
        "Восстанавливает здоровье",
        25,
        "Лечение"
    ),

    "energy_potion": Potion(
        "Зелье энергии",
        "Восстанавливает энергию",
        30,
        "Энергия"
    ),

    "calm_potion": Potion(
        "Зелье спокойствия",
        "Снимает усталость",
        20,
        "Спокойствие"
    ),

    "magic_potion": Potion(
        "Зелье магии",
        "Увеличивает магическую силу",
        40,
        "Магия"
    ),

    "shadow_potion": Potion(
        "Эликсир теней",
        "Позволяет управлять теневой энергией",
        60,
        "Тьма"
    ),

    "dragon_potion": Potion(
        "Эликсир драконьей силы",
        "Увеличивает силу и выносливость",
        100,
        "Сила"
    ),

    "clarity_potion": Potion(
        "Эликсир ясного разума",
        "Улучшает концентрацию и ясность мыслей",
        40,
        "Концентрация"
    ),

    "phoenix_potion": Potion(
        "Эликсир феникса",
        "Дарует энергию возрождения",
        180,
        "Возрождение"
    ),

    "oblivion_potion": Potion(
        "Эликсир забвения",
        "Позволяет на время забыть неприятные воспоминания",
        90,
        "Забвение"
    ),

    "arcane_potion": Potion(
        "Эликсир арканы",
        "Наделяет алхимика древней магической силой",
        200,
        "Древняя магия"
    )
}