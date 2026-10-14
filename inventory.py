class Inventory:  # инвентарь игрока
    def __init__(self):
        self.items = {}       # ингредиенты: {ingredient_id: amount}
        self.potions = {}     # зелья: {potion_id: amount}

    # ---------- ИНГРЕДИЕНТЫ ----------
    def add(self, ingredient_id, amount=1):
        if ingredient_id in self.items:
            self.items[ingredient_id] += amount
        else:
            self.items[ingredient_id] = amount

    def remove(self, ingredient_id, amount=1):
        if ingredient_id not in self.items:
            raise ValueError("Такого ингредиента нет в инвентаре.")

        if self.items[ingredient_id] < amount:
            raise ValueError("Недостаточно ингредиентов для удаления.")

        self.items[ingredient_id] -= amount

        if self.items[ingredient_id] == 0:
            del self.items[ingredient_id]

    def get_amount(self, ingredient_id):
        return self.items.get(ingredient_id, 0)

    # ---------- ЗЕЛЬЯ ----------
    def add_potion(self, potion_id, amount=1):
        if potion_id in self.potions:
            self.potions[potion_id] += amount
        else:
            self.potions[potion_id] = amount

    def remove_potion(self, potion_id, amount=1):
        if potion_id not in self.potions:
            raise ValueError("Такого зелья нет в инвентаре.")

        if self.potions[potion_id] < amount:
            raise ValueError("Недостаточно зелий для удаления.")

        self.potions[potion_id] -= amount

        if self.potions[potion_id] == 0:
            del self.potions[potion_id]

    def get_potion_amount(self, potion_id):
        return self.potions.get(potion_id, 0)

    # ---------- ОТОБРАЖЕНИЕ ----------
    def show(self, ingredients, potions):  # интерфейс для отображения инвентаря игрока через консоль
        print("\n=== ИНВЕНТАРЬ ===")

        if not self.items and not self.potions:
            print("Инвентарь пуст")
            return

        if self.items:
            print("  Ингредиенты:")
            for ingredient_id, amount in self.items.items():
                ingredient = ingredients[ingredient_id]
                print(f"    • {ingredient.name}: {amount} шт.")

        if self.potions:
            print("  Зелья:")
            for potion_id, amount in self.potions.items():
                potion = potions[potion_id]
                print(f"    • {potion.name}: {amount} шт.")