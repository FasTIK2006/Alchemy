from inventory import Inventory
from ingredients import ingredients
from potions import potions
from crafting import craft
from recipes import recipes

def show_menu():
    print("\n=== АЛХИМИЯ ===")
    print("1. Показать инвентарь")
    print("2. Добавить ингредиент")
    print("3. Сварить зелье")
    print("4. Показать все рецепты")
    print("0. Выход")

def main():
    inventory = Inventory()
    # немного ингредиентов для старта
    inventory.add("mint", 3)
    inventory.add("water", 3)
    inventory.add("fire_flower", 2)

    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            inventory.show(ingredients, potions)

        elif choice == "2":
            add_ingredient(inventory)

        elif choice == "3":
            brew_potion(inventory)

        elif choice == "4":
            show_recipes()

        elif choice == "0":
            print("До встречи!")
            break

        else:
            print("❌ Нет такого пункта")


def add_ingredient(inventory):
    print("\nДоступные ингредиенты:")
    for i, (ingredient_id, ingredient) in enumerate(ingredients.items(), 1):
        print(f"  {i}. {ingredient.name} (id: {ingredient_id})")

    ingredient_id = input("Введите id ингредиента: ").strip()

    if ingredient_id not in ingredients:
        print("❌ Такого ингредиента нет")
        return

    try:
        amount = int(input("Сколько добавить? ").strip())
        if amount <= 0:
            print("❌ Количество должно быть больше 0")
            return
    except ValueError:
        print("❌ Нужно ввести число")
        return

    inventory.add(ingredient_id, amount)
    print(f"✔ Добавлено: {ingredients[ingredient_id].name} x{amount}")


def brew_potion(inventory):
    print("\nВведите id ингредиентов через пробел.")
    print("Например: mint water")

    raw = input("Ингредиенты: ").strip()
    selected = raw.split()

    if not selected:
        print("❌ Ничего не выбрано")
        return

    # проверяем, что все id существуют
    for ingredient_id in selected:
        if ingredient_id not in ingredients:
            print(f"❌ Неизвестный ингредиент: {ingredient_id}")
            return

    craft(inventory, selected)


def show_recipes():

    print("\n=== РЕЦЕПТЫ ===")
    if not recipes:
        print("Рецептов пока нет")
        return

    for combination, recipe in recipes.items():
        names = ", ".join(ingredients[i].name for i in combination)
        potion = potions[recipe["potion_id"]]
        print(f"  {names}  →  {potion.name} (+{recipe['xp']} XP)")


if __name__ == "__main__":
    main()

