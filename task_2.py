import turtle

def draw_pythagoras_tree(t, branch_len, level):
        
    # базовий випадок рекурсії: якщо рівень 0, зупиняємось
    if level == 0:
        return

    # налаштування вигляду гілки залежно від рівня, чим вищий рівень (ближче до стовбура), тим товстіша лінія
    t.width(level) 
    
    # Змінюємо колір: останні рівні (листя) - зелені, стовбур - коричневий
    if level <= 2:
        t.pencolor("green")
    else:
        t.pencolor("brown")

    # малюємо стовбур
    t.forward(branch_len)

    angle = 30  # кут розгалуження
    t.right(angle)

    # рекурсивний виклик для правої частини
    draw_pythagoras_tree(t, branch_len * 0.75, level - 1)

    # поворот наліво
    t.left(angle * 2)

    # рекурсивний виклики для лівої частини
    draw_pythagoras_tree(t, branch_len * 0.75, level - 1)

    # поворот назад і рух назад
    t.right(angle)
    
    if level > 2:
        t.pencolor("brown") # повертаємо колір стовбура перед відходом назад
    
    t.backward(branch_len)

def main():
    # налаштування екрану
    screen = turtle.Screen()
    screen.title("Фрактал: Дерево Піфагора")
    screen.bgcolor("white")

    # отримання рівня рекурсії від користувача
    try:
        recursion_level = int(screen.numinput("Налаштування", 
                                              "Введіть рівень рекурсії (рекомендовано 5-10):", 
                                              default=7, minval=1, maxval=12))
    except TypeError:
        # скасування, якщо користувач натиснув Cancel
        print("Вхідні дані скасовано.")
        return
    
    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)  
    t.up()
    t.goto(0, -250) 
    t.down()

    print(f"Малюємо дерево з рівнем рекурсії: {recursion_level}")
    
    # запуск малювання 
    draw_pythagoras_tree(t, 100, recursion_level)
    
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
