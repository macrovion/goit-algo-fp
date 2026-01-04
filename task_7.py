import random
import matplotlib.pyplot as plt

# функція симулює кидки двох кубиків задану кількість разів
def dice_simulation(num_simulations):
    
    # словник для збереження кількості випадінь кожної суми (від 2 до 12)
    sum_counts = {i: 0 for i in range(2, 13)}

    # створення симуляції
    for _ in range(num_simulations):
        # кидаємо два кубики
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        # визначаємо суму
        total_sum = die1 + die2
        
        # підраховуємо кількість
        sum_counts[total_sum] += 1
        
    return sum_counts

# параметри симуляції
TOTAL_ROLLS = 1_000_000  # велика кількість кидків (1 мільйон) для точності

print(f"Запуск симуляції {TOTAL_ROLLS} кидків...\n")
results = dice_simulation(TOTAL_ROLLS)

# підготовка даних для відображення
sums = list(range(2, 13))
probabilities = []

# створення таблиці
print(f"{'Сума':<6} | {'Кількість випадінь':<20} | {'Імовірність (Монте-Карло)':<25}")
print("-" * 60)

for s in sums:
    count = results[s]
    # обчислення ймовірності у відсотках
    prob_percent = (count / TOTAL_ROLLS) * 100
    probabilities.append(prob_percent)
    
    # вивід рядка таблиці
    print(f"{s:<6} | {count:<20} | {prob_percent:.2f}%")

# створення графіку
plt.figure(figsize=(10, 6))
bars = plt.bar(sums, probabilities, color='skyblue', edgecolor='black')

# налаштування графіку
plt.title(f'Розподіл ймовірностей суми двох кубиків\n(на основі {TOTAL_ROLLS} симуляцій)', fontsize=14)
plt.xlabel('Сума', fontsize=12)
plt.ylabel('Ймовірність (%)', fontsize=12)
plt.xticks(sums)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# додаємо підписи відсотків над стовпчиками
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval:.1f}%', ha='center', va='bottom')

# показати графік
plt.show()
