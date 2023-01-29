def moyenne_gen(exam,td):
	total = (exam*0.67) + (td*0.33)
	return total


modules = ["Analyse", "Algebre", "Electronique", "SFSD", "Anglais", "Archi", "Proba", "Eco"]

moyenne = 0

for i in range(8):
	print(f"-------{modules[i]}-------")
	td1 = int(input("TD :"))
	exam1 = int(input("Exam :"))
	semi = moyenne_gen(exam1,td1)
	match i:
		case 0:
			moyenne = moyenne + semi*5
		case 1:
			moyenne = moyenne + semi*3
		case 2:
			moyenne = moyenne + semi*4
		case 3:
			moyenne = moyenne + semi*4
		case 4:
			moyenne = moyenne + semi*2
		case 5:
			moyenne = moyenne + semi*4
		case 6:
			moyenne = moyenne + semi*4
		case 7:
			moyenne = moyenne + semi*2


moyenne = moyenne / 28

print(f"AVG = {moyenne}")