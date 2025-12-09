import xml.etree.ElementTree as ET

def load_users_data(filename="users.xml"):
    users_tree = ET.parse(filename)
    users = []
    for user_elem in users_tree.getroot().findall('user'):
        user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': int(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text
        }
        users.append(user)
    return users

def load_workouts_data(filename="workouts.xml"):
    workouts_tree = ET.parse(filename)
    workouts = []
    for w_elem in workouts_tree.getroot().findall('workout'):
        workout = {
            'workout_id': int(w_elem.find('workout_id').text),
            'user_id': int(w_elem.find('user_id').text),
            'date': w_elem.find('date').text,
            'type': w_elem.find('type').text,
            'duration': int(w_elem.find('duration').text),
            'distance': float(w_elem.find('distance').text),
            'calories': int(w_elem.find('calories').text),
            'avg_heart_rate': int(w_elem.find('avg_heart_rate').text),
            'intensity': w_elem.find('intensity').text
        }
        workouts.append(workout)
    return workouts

def get_stats(users, workouts):
    total_workouts = len(workouts)
    total_users = len(users)
    total_calories = sum(w['calories'] for w in workouts)
    total_time_hours = sum(w['duration'] for w in workouts) / 60
    total_distance = sum(w['distance'] for w in workouts)

    print("ОБЩАЯ СТАТИСТИКА")
    print("===========================")
    print(f"Всего тренировок: {total_workouts}")
    print(f"Всего пользователей: {total_users}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time_hours:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
