from collections import Counter

def analyze_user_activity(users, workouts):
    stats = []
    for user in users:
        user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]
        total_calories = sum(w['calories'] for w in user_workouts)
        total_time = sum(w['duration'] for w in user_workouts) / 60
        stats.append({
            'name': user['name'],
            'fitness_level': user['fitness_level'],
            'workouts': len(user_workouts),
            'calories': total_calories,
            'time': total_time
        })
    stats.sort(key=lambda x: x['workouts'], reverse=True)
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for i, s in enumerate(stats[:3], 1):
        print(f"{i}. {s['name']} ({s['fitness_level']}):")
        print(f"   Тренировок: {s['workouts']}")
        print(f"   Калорий: {s['calories']}")
        print(f"   Время: {s['time']:.1f} часов")

def analyze_workout_types(workouts):
    types = {}
    for w in workouts:
        t = w['type']
        if t not in types:
            types[t] = []
        types[t].append(w)

    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for t, ws in types.items():
        avg_dur = sum(w['duration'] for w in ws) / len(ws)
        avg_cal = sum(w['calories'] for w in ws) / len(ws)
        print(f" {t}: {len(ws)} тренировок ({len(ws)/len(workouts)*100:.1f}%)")
        print(f"   Средняя длительность: {avg_dur:.0f} мин")
        print(f"   Средние калории: {avg_cal:.0f} ккал")

def find_user_workouts(users, workouts, user_name):
    user = next((u for u in users if u['name'].lower() == user_name.lower()), None)
    if user:
        return [w for w in workouts if w['user_id'] == user['user_id']]
    return []

def analyze_user(user, workouts):
    user_workouts = find_user_workouts([user], workouts, user['name'])
    total_calories = sum(w['calories'] for w in user_workouts)
    total_time = sum(w['duration'] for w in user_workouts) / 60
    total_distance = sum(w['distance'] for w in user_workouts)
    fav_type = Counter([w['type'] for w in user_workouts]).most_common(1)[0][0]

    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}")
    print("===========================================")
    print(f"Возраст: {user['age']} лет, Вес: {user['weight']} кг")
    print(f"Уровень: {user['fitness_level']}")
    print(f"Тренировок: {len(user_workouts)}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {total_calories/len(user_workouts):.0f}")
    print(f"Любимый тип тренировки: {fav_type}")
