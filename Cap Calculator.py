#CAP Calculator

grades_cap = {"A+": 5.0 , "A": 5.0, "A-": 4.5, 'B+':4.0, 'B':3.5,'B-': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F':0 }

def freshie():
    freshie_check = input("Is this your first sem? ")
    if freshie_check[0].upper() == "N": # no or n or N or NO
        current_cap = float(input("What is your current cap? "))
        completed_mc = int(input("How many graded Modular Credits have been completed? ")) #does not include SU-ed mods
    else:
        current_cap = 0
        completed_mc = 0
    return current_cap, completed_mc

current_cap, completed_mc = freshie()

def new_sem():
    num_mods = int(input("How many mods did you complete? "))
    sap = 0
    sum_new_mc = 0
    for i in range(1,(num_mods+1)):
        new_mc = int(input("What is the number of MCs for mod",i,"? "))
        new_grade = input("What is the grade? ")
        sap += grades_cap[new_grade.upper()] * new_mc
        sum_new_mc += new_mc
    return sap, sum_new_mc

sap, sum_new_mc = new_sem()

def main():
    updated_cap = (current_cap*completed_mc + sap)/(completed_mc + sum_new_mc)
    print(updated_cap)


if __name__ == '__main__': main()



