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

          
