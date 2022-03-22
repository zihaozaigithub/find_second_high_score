def find_second_score(students):
	if len(students) <= 1:
		return print('not a list') #check if a list
	else:
		scores = []
		for student in students:
			scores.append(student[1]) # put only scores in a list
		print(scores)
		uni_scores = sorted(set(scores))
		second_high_score = uni_scores[-2] # set uniq number list and sort
		print(second_high_score)
		for student in students:           # find second high students name 
			if student[1] == second_high_score:
				print(student[0])


students = [['Jerry', 88], ['Justin', 90], ['Tom', 90]]
find_second_score(students)
