import random
import time

def multiplication_trainer():
    N = int(input("Введите количество примеров: "))
    correct = 0
    total_time = 0

    for i in range(1, N + 1):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        while True:
            try:
                print(f"Вопрос {i}/{N}")
                start = time.time()
                answer = int(input(f"{a} × {b} = "))
                elapsed = time.time() - start
                total_time += elapsed
                if answer == a * b:
                    print(f"Верно! (Время: {elapsed:.1f} сек)")
                    correct += 1
                else:
                    print(f"Неверно! Правильно: {a * b} (Время: {elapsed:.1f} сек)")
                break
            except ValueError:
                print("Пожалуйста, введите целое число!")

    print("=" * 50)
    print("СТАТИСТИКА:")
    print("=" * 50)
    print(f"Общее время: {total_time:.1f} секунд")
    print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
    print(f"Правильных ответов: {correct}/{N}")
    print(f"Процент правильных: {correct / N * 100:.1f}%")

multiplication_trainer()
