
def sum_negative_between_extremes(values: list[float]) -> float:
    if not values:
        raise ValueError("Массив не должен быть пустым.")
    min_index = values.index(min(values))
    max_index = values.index(max(values))

    left = min(min_index, max_index) + 1
    right = max(min_index, max_index)

    return sum(value for value in values[left:right] if value < 0)


def read_array() -> list[float]:
    while True:
        try:
            size = int(input("Введите количество элементов N: "))
            if size <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка: N должно быть целым положительным числом.")

    while True:
        try:
            values = [
                float(item.replace(",", "."))
                for item in input(f"Введите {size} чисел через пробел: ").split()
            ]
            if len(values) != size:
                print(f"Ошибка: требуется ввести ровно {size} чисел.")
                continue
            return values
        except ValueError:
            print("Ошибка: все элементы должны быть числами.")


def format_number(value: float) -> str:
    return str(int(value)) if float(value).is_integer() else str(value)


def run_self_tests() -> None:
    assert sum_negative_between_extremes([5, -2, 4, -3, -7, 1]) == -5
    assert sum_negative_between_extremes([-10, -2, 0, 8]) == -2
    assert sum_negative_between_extremes([1, 9, -4, -6, -10]) == -10
    assert sum_negative_between_extremes([3, -1]) == 0


def main() -> None:
    run_self_tests()
    values = read_array()
    result = sum_negative_between_extremes(values)
    print("Сумма отрицательных элементов между минимумом и максимумом:",
          format_number(result))

if __name__ == "__main__":
    main()
