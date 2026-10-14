from recipes import recipes
from potions import potions
from ingredients import ingredients


def can_craft(inventory, selected_ingredients):
    """Проверяет, можно ли скрафтить по данному набору."""
    combination = tuple(sorted(selected_ingredients))

    if combination not in recipes:
        return False, "Такого рецепта нет"

    for ingredient_id in selected_ingredients:
        if inventory.get_amount(ingredient_id) < 1:
            name = ingredients[ingredient_id].name
            return False, f"Не хватает: {name}"

    return True, None


def craft(inventory, selected_ingredients):
    """Крафтит зелье: забирает ингредиенты, добавляет зелье, возвращает объект зелья и XP."""
    ok, error = can_craft(inventory, selected_ingredients)
    if not ok:
        print(f"❌ {error}")
        return None, 0

    combination = tuple(sorted(selected_ingredients))
    recipe = recipes[combination]
    potion_id = recipe["potion_id"]
    potion = potions[potion_id]
    xp = recipe["xp"]

    # забираем ингредиенты
    for ingredient_id in selected_ingredients:
        inventory.remove(ingredient_id, 1)

    # добавляем зелье в инвентарь
    inventory.add_potion(potion_id, 1)

    # красивый вывод
    show_craft_result(selected_ingredients, potion, xp)

    return potion, xp


def show_craft_result(selected_ingredients, potion, xp):
    print("\n" + "=" * 40)
    print("        ✨ КРАФТ ЗАВЕРШЁН ✨")
    print("=" * 40)
    names = ", ".join(ingredients[i].name for i in selected_ingredients)
    print(f"  Ингредиенты : {names}")
    print(f"  Результат   : {potion.name}")
    print(f"  Описание    : {potion.description}")
    print(f"  Эффект      : {potion.effect}")
    print(f"  Опыт        : +{xp} XP")
    print("=" * 40 + "\n")