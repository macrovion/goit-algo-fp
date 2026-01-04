# жадібний алгоритм: вибирає страви, максимізуючи співвідношення калорій до вартості
def greedy_algorithm(items, budget):
    # створюємо список (назва, вартість, калорії, співвідношення)
    item_list = []
    for name, data in items.items():
        cost = data['cost']
        calories = data['calories']
        ratio = calories / cost if cost > 0 else 0
        item_list.append((name, cost, calories, ratio))

    # сортуємо за спаданням співвідношення калорій до вартості
    item_list.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for name, cost, calories, ratio in item_list:
        if cost <= remaining_budget:
            chosen_items.append(name)
            total_calories += calories
            remaining_budget -= cost

    return chosen_items, total_calories, budget - remaining_budget

# динамічне програмування: знаходить оптимальний набір страв для максимізації калорійності
def dynamic_programming(items, budget):
   # перетворюємо дані у списки для легшого доступу за індексом
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(items)

    # створюємо таблицю DP, де K[i][w] - макс. калорій для перших i страв при бюджеті w
    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    # заповнюємо таблицю знизу вгору
    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost_i = costs[i - 1]
            cal_i = calories[i - 1]

            if cost_i <= w:
                # вибираємо максимум: брати страву або не брати
                K[i][w] = max(cal_i + K[i - 1][w - cost_i], K[i - 1][w])
            else:
                # страва занадто дорога для поточного ліміту w
                K[i][w] = K[i - 1][w]

    # відновлення обраних страв
    selected_items = []
    w = budget
    total_cal = K[n][budget]
    
    # йдемо у зворотному порядку, щоб визначити, які елементи були додані
    for i in range(n, 0, -1):
        if total_cal <= 0:
            break
        
        if total_cal != K[i - 1][w]:
            selected_items.append(names[i - 1])
            total_cal -= calories[i - 1]
            w -= costs[i - 1]

    # перерахуємо фінальну вартість для виводу
    final_cost = sum(items[item]['cost'] for item in selected_items)
    
    return selected_items, K[n][budget], final_cost


# вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# тестування
budget = 100 # можна змінити бюджет для перевірки різних сценаріїв

print(f"Бюджет: {budget}\n")

# виклик жадібного алгоритму
greedy_items, greedy_cal, greedy_cost = greedy_algorithm(items, budget)
print("--- Жадібний алгоритм ---")
print(f"Обрані страви: {greedy_items}")
print(f"Сумарна калорійність: {greedy_cal}")
print(f"Витрачено коштів: {greedy_cost}")

print("\n")

# виклик динамічного програмування
dp_items, dp_cal, dp_cost = dynamic_programming(items, budget)
print("--- Динамічне програмування ---")
print(f"Обрані страви: {dp_items}")
print(f"Сумарна калорійність: {dp_cal}")
print(f"Витрачено коштів: {dp_cost}")
