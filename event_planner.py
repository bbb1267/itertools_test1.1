import itertools

def run_event_planner():
    guests = ['Алексей', 'Мария', 'Иван', 'Елена']
    main_dishes = ['Стейк', 'Рыба']
    drinks = ['Вино', 'Сок', 'Вода']
    table_numbers = [1, 1, 2, 2]

    # 1. Все возможные заказы (product)
    menu_options = list(itertools.product(main_dishes, drinks))
    print(f"Вариантов меню: {len(menu_options)}")

    # 2. Рассадка по парам (combinations)
    pairs = list(itertools.combinations(guests, 2))
    print(f"Пар для нетворкинга: {pairs}")

    #3. Дежурство (cycle + islice)
    dj_queue = itertools.cycle(guests)
    first_10_djs = list(itertools.islice(dj_queue, 10))
    print(f"Очередь DJ: {first_10_djs}")

    #4. Группировка по столам(zip_longest)
    seating = list(itertools.zip_longest(guests, table_numbers, fillvalue="Без места"))
    print(f"Рассадка: {seating}")

    #5. HARD(combinations + filters)
    weights = [15, 30, 45, 10, 20]
    target = 60
    valid_combos = []
    for r in range(1, len(weights) + 1):
        for combo in itertools.combinations(weights, r):
            if sum(combo) == target:
                valid_combos.append(combo)
    print(f"Комбинация подарков на {target}кг: {valid_combos}")


if __name__ == "__main__":
    run_event_planner()
    

          
