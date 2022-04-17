unsatisfactory_number = int(input())
solved_tasks = 0
unsolved_tasks = 0
total_evaluation = 0
last_problem = ''
has_failed = True
while unsolved_tasks < unsatisfactory_number:
    tasks_name = input()
    if tasks_name == 'Enough':
        has_failed = False
        break

    evaluation = int(input())
    if evaluation <= 4:
        unsolved_tasks += 1
    total_evaluation += evaluation
    solved_tasks += 1
    last_problem = tasks_name
if has_failed:
    print(f'You need a break, {unsolved_tasks} poor grades.')
else:
    print(f'Average score: {total_evaluation / solved_tasks:.2f}')
    print(f'Number of problems: {solved_tasks}')
    print(f'Last problem: {last_problem}')