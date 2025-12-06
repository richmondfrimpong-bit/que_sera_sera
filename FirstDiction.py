Class_score = {'Susan': [92, 85, 100], 'Eduardo': [83, 95, 79],
               'Azizi': [91, 89, 82], 'Pantipa': [97, 91, 92]}
overall = 0
totnumscore = 0
for student, grades in Class_score.items():
    total = sum(grades)
    average = total / len(grades)
    print(f'{student} had an average of {average:.2f}')
    overall += total
    totnumscore += len(grades)
    claver = overall / totnumscore

print(f'The class average is {claver:.2f}')

