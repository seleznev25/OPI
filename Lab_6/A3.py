import matplotlib.pyplot as plt

def plot_workout_types(workouts):
    types = Counter([w['type'] for w in workouts])
    plt.pie(types.values(), labels=types.keys(), autopct='%1.1f%%')
    plt.title("Круговая диаграмма типов тренировок")
    plt.show()

def plot_user_activity(users, workouts):
    names = [u['name'] for u in users]
    counts = [len([w for w in workouts if w['user_id']==u['user_id']]) for u in users]
    plt.bar(names, counts)
    plt.title("Активность пользователей")
    plt.show()

def plot_user_efficiency(users, workouts):
    names = [u['name'] for u in users]
    avg_calories = []
    for u in users:
        ws = [w for w in workouts if w['user_id']==u['user_id']]
        avg_calories.append(sum(w['calories'] for w in ws)/len(ws) if ws else 0)
    plt.bar(names, avg_calories)
    plt.title("Эффективность тренировок (средние калории)")
    plt.show()
