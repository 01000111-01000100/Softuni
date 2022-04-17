jury_number = int(input())
command = input()
average_score_all_presentations = 0
counter = 0
while command != 'Finish':
    presentation_name = command
    average_score_per_assignment = 0
    for member in range(1, jury_number + 1):
        counter += 1
        score = float(input())
        average_score_per_assignment += score

    average_assignment = (average_score_per_assignment / jury_number)
    print(f'{presentation_name} - {average_assignment:.2f}.')
    average_score_all_presentations += average_score_per_assignment
    command = input()
else:
    average = average_score_all_presentations / counter
    print(f"Student's final assessment is {average:.2f}.")