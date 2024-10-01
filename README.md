### Завдання 1:

Кількість вершин: 7

Кількість ребер: 9

Ступінь кожної вершини:

    Station A: 3
    Station B: 2
    Station C: 4
    Station D: 2
    Station E: 2
    Station F: 3
    Station G: 2

### Завдання 2:

DFS шлях: ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']

BFS шлях: ['Station A', 'Station C', 'Station F']

BFS знаходить коротший шлях, тому що він першочергово обирає найближчі вершини, тоді як DFS намагається дослідити всі можливі шляхи, що часто призводить до довшого шляху.

### Завдання 3:

Найкоротші шляхи:

    Station A:
        Station A: 0
        Station C: 1
        Station B: 2
        Station F: 4
        Station G: 6
        Station E: 6
        Station D: 8
    Station B:
        Station B: 0
        Station A: 2
        Station C: 3
        Station F: 6
        Station G: 8
        Station E: 8
        Station D: 10
    Station C:
        Station C: 0
        Station A: 1
        Station F: 3
        Station B: 3
        Station E: 5
        Station D: 7
        Station G: 7
    Station D:
        Station D: 0
        Station E: 3
        Station F: 5
        Station C: 7
        Station A: 8
        Station G: 10
        Station B: 10
    Station E:
        Station E: 0
        Station F: 2
        Station D: 3
        Station C: 5
        Station A: 6
        Station G: 7
        Station B: 8
    Station F:
        Station F: 0
        Station E: 2
        Station C: 3
        Station A: 4
        Station G: 5
        Station D: 5
        Station B: 6
    Station G:
        Station G: 0
        Station F: 5
        Station A: 6
        Station E: 7
        Station C: 7
        Station B: 8
        Station D: 10
