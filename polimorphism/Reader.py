from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiquadraticEquation import BiquadraticEquation
data_of_equations = []
def read(file_name):

    with open(file_name) as f:
        list_of_solutions =[]

        global data_of_equations
        for line in f:
            data = line.split()

            type = len(data)

            if type == 5:
                a = int(data[0])
                b = int(data[2])
                c = int(data[4])
                eq = BiquadraticEquation(a, b, c)
                solution = eq.solve()
                data_of_equations.append([a, b, c, 0])
                list_of_solutions.append((solution))

            elif type == 3:
                a = int(data[0])
                b = int(data[1])
                c = int(data[2])
                eq = QuadraticEquation(a, b, c)

                solution = eq.solve()
                data_of_equations.append([a, b, c])
                list_of_solutions.append((solution))
            elif type == 2:
                a = int(data[0])
                b = int(data[1])
                eq = Equation(a, b)
                solution = eq.solve()
                data_of_equations.append([a, b])
                list_of_solutions.append((solution))


    return list_of_solutions
our_file = read("input03.txt")
print (our_file)
data_of_equations2 = data_of_equations

print (data_of_equations)

zero_results_linear = []
zero_results_quadratic = []
zero_results_biquadratic = []
one_results_linear = []
one_results_quadratic = []
one_results_biquadratic = []
two_results_quadratic = []
two_results_biquadratic=[]
three_results = []
four_results = []
infinite_results_linear= []
infinite_results_quadratic = []
infinite_results_biquadratic = []
def finder (our_file):
    global data_of_equations2
    global zero_results_linear
    global zero_results_quadratic
    global zero_results_biquadratic
    global one_results_linear
    global one_results_quadratic
    global one_results_biquadratic
    global two_results_quadratic
    global two_results_biquadratic
    global three_results
    global four_results
    global infinite_results_linear
    global infinite_results_quadratic
    global infinite_results_biquadratic
    counter = 0
    for i in our_file:

        if len(i)==0:
            if len(data_of_equations[counter])==2:
                zero_results_linear.append(data_of_equations2[counter])
            elif len(data_of_equations[counter])==3:
                zero_results_quadratic.append(data_of_equations2[counter])
            elif len(data_of_equations[counter])==4:
                zero_results_biquadratic.append(data_of_equations2[counter])
            counter +=1
        elif len(i)==1:
            if len(data_of_equations[counter]) == 2:
                one_results_linear.append(data_of_equations2[counter])
            elif len(data_of_equations[counter]) == 3:
                one_results_quadratic.append(data_of_equations2[counter])
            elif len(data_of_equations[counter]) == 4:
                one_results_biquadratic.append(data_of_equations2[counter])
            counter += 1

        elif len(i)==2:
            if len(data_of_equations[counter]) == 3:
                two_results_quadratic.append(data_of_equations2[counter])
            elif len(data_of_equations[counter]) == 4:
                two_results_biquadratic.append(data_of_equations2[counter])
            counter += 1
        elif len(i)==3:
            three_results.append(data_of_equations2[counter])
            counter += 1
        elif len(i)==4:
            four_results.append(data_of_equations2[counter])
            counter += 1
        else:
            if len(data_of_equations[counter]) == 2:
                infinite_results_linear.append(data_of_equations2[counter])
            elif len(data_of_equations[counter]) == 3:
                infinite_results_quadratic.append(data_of_equations2[counter])
            elif len(data_of_equations[counter]) == 4:
                infinite_results_biquadratic.append(data_of_equations2[counter])
            counter += 1
    return [zero_results_linear,zero_results_quadratic, zero_results_biquadratic, one_results_linear, one_results_quadratic, one_results_biquadratic, two_results_quadratic, two_results_biquadratic, three_results, four_results, infinite_results_linear, infinite_results_quadratic, infinite_results_biquadratic]

our_answers = finder(our_file)
zero_results_length1 = len(our_answers[0])
zero_results_length2 = len(our_answers[1])
zero_results_length3 = len(our_answers[2])

one_results_length1 = len(our_answers[3])
one_results_length2 = len(our_answers[4])
one_results_length3 = len(our_answers[5])

two_results_length1 = len(our_answers[6])
two_results_length2 = len(our_answers[7])

three_results_length = len(our_answers[8])

four_results_length = len(our_answers[9])

infinite_results_length1 = len(our_answers[10])
infinite_results_length2 = len(our_answers[11])
infinite_results_length3 = len(our_answers[12])


for i in range(zero_results_length1):
    print(f" Лінійне рівняння {our_answers[0][i][0]}x + {our_answers[0][i][1]} = 0 не має розв'язків")
for i in range(zero_results_length2):
    print(f" Квадратне рівняння {our_answers[1][i][0]}x^2 + {our_answers[1][i][1]}x + {our_answers[1][i][2]} = 0 не має розв'язків")
for i in range(zero_results_length3):
    print(f" Біквадратне рівняння {our_answers[2][i][0]}x^4 + {our_answers[2][i][1]}x^2 + {our_answers[2][i][2]} = 0 не має розв'язків")

for i in range(one_results_length1):
    print(f" Лінійне рівняння {our_answers[3][i][0]}x + {our_answers[3][i][1]} = 0 має один розв'язок")
for i in range(one_results_length2):
    print(f" Квадратне рівняння {our_answers[4][i][0]}x^2 + {our_answers[4][i][1]}x + {our_answers[4][i][2]} = 0 має один розв'язок")
for i in range(one_results_length3):
    print(f" Біквадратне рівняння {our_answers[5][i][0]}x^4 + {our_answers[5][i][1]}x^2 + {our_answers[5][i][2]} = 0 має один розв'язок")

for i in range(two_results_length1):
    print(f" Квадратне рівняння {our_answers[6][i][0]}x^2 + {our_answers[6][i][1]}x + {our_answers[6][i][2]} = 0 має два розв'язки")
for i in range(two_results_length2):
    print(f" Біквадратне рівняння {our_answers[7][i][0]}x^4 + {our_answers[7][i][1]}x^2 + {our_answers[7][i][2]} = 0 має два розв'язки")

for i in range(three_results_length):
    print(f" Біквадратне рівняння {our_answers[8][i][0]}x^4 + {our_answers[8][i][1]}x^2 + {our_answers[8][i][2]} = 0 має три розв'язки")

for i in range(four_results_length):
    print(f" Біквадратне рівняння {our_answers[9][i][0]}x^4 + {our_answers[9][i][1]}x^2 + {our_answers[9][i][2]} = 0 має чотири розв'язки")

for i in range(infinite_results_length1):
    print(f" Лінійне рівняння {our_answers[10][i][0]}x + {our_answers[10][i][1]} = 0 має безліч розв'язків")
for i in range(infinite_results_length2):
    print(f" Квадратне рівняння {our_answers[11][i][0]}x^2 + {our_answers[11][i][1]}x + {our_answers[11][i][2]} = 0 має безліч розв'язків")
for i in range(infinite_results_length3):
    print(f" Біквадратне рівняння {our_answers[12][i][0]}x^4 + {our_answers[12][i][1]}x^2 + {our_answers[12][i][2]} = 0 має безліч розв'язків")

combined_list = [*one_results_linear, *one_results_quadratic, *one_results_biquadratic]

list_of_solutions2 = []

for i in combined_list:
    if len(i) == 2:

        a = int(i[0])
        b = int(i[1])
        eq = Equation(a, b)
        solution = eq.solve()

        list_of_solutions2.append((solution))

    elif len(i) == 3:
        a = int(i[0])
        b = int(i[1])
        c = int(i[2])
        eq = QuadraticEquation(a, b, c)

        solution = eq.solve()

        list_of_solutions2.append((solution))

    elif len(i) == 4:

        a = int(i[0])
        b = int(i[1])
        c = int(i[2])
        eq = BiquadraticEquation(a, b, c)
        solution = eq.solve()

        list_of_solutions2.append((solution))

absolute_max = [*list_of_solutions2[0]]
absolute_min = [*list_of_solutions2[0]]
counter_for_max = 0
counter_for_min = 0
counter_finder_min =[]
counter_finder_max =[]
for i in list_of_solutions2:
    if i[0]>absolute_max[0]:
        absolute_max.clear()
        absolute_max.append(*i)
        counter_finder_max.clear()
        counter_finder_max.append(counter_for_max)
    counter_for_max +=1
    if i[0]<absolute_min[0]:
        absolute_min.clear()
        absolute_min.append(*i)
        counter_finder_min.clear()
        counter_finder_min.append(counter_for_min)
    counter_for_min += 1

new_counter = 0

for i in combined_list:

    if len(i) == 2:
        if new_counter == counter_finder_max[0]:
            print(f" Лінійне рівняння {combined_list[new_counter][0]}x + {combined_list[new_counter][1]} = 0 має найбільший розв'зок {absolute_max[0]}")
        if new_counter ==counter_finder_min[0]:
            print(f" Лінійне рівняння {combined_list[new_counter][0]}x + {combined_list[new_counter][1]} = 0 має найменший розв'зок {absolute_min[0]}")
    elif len(i)== 3:
        if new_counter == counter_finder_max[0]:
            print(f" Квадратне рівняння {combined_list[new_counter][0]}x^2 + {combined_list[new_counter][1]}x + {combined_list[new_counter][2]} = 0 має найбільший розв'зок {absolute_max[0]}")
        if new_counter == counter_finder_min[0]:
            print(f" Квадратне рівняння {combined_list[new_counter][0]}x^2 + {combined_list[new_counter][1]}x + {combined_list[new_counter][2]} = 0 має найменший розв'зок {absolute_min[0]}")
    elif len(i) == 4:
        if new_counter == counter_finder_max[0]:
            print(f" Біквадратне рівняння {combined_list[new_counter][0]}x^4 + {combined_list[new_counter][1]}x^2 + {combined_list[new_counter][2]} = 0 має найбільший розв'зок {absolute_max[0]}")
        if new_counter == counter_finder_min[0]:
            print(f" Біквадратне рівняння {combined_list[new_counter][0]}x^4 + {combined_list[new_counter][1]}x^2 + {combined_list[new_counter][2]} = 0 має найменший розв'зок {absolute_min[0]}")
    new_counter += 1