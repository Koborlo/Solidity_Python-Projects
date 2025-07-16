inp =input('EXAM SCORE: ')
score = int(inp)
if score >= 90:
    print('GRADE A')
elif score >= 80:
    print('GRADE B')
elif score >= 70:
    print('GRADE C')
elif score >= 60:
    print('GRADE D')
elif score == 50:
    print('PASS')
else:
    print('FAIL!TRY AGAIN LATER')