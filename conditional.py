def prob_a_b(a,b):
    if a=="1":
        prob_s=0.3
        if b=="1":
            prob_dining=0.75
        else:
            prob_dining=0.25
    else:
        prob_s = 0.7
        if b=="1":
            prob_dining=0.6
        else:
            prob_dining=0.4
    print("probabilty of a given that b has occured  :  ", prob_dining)
    return round(prob_s*prob_dining,3)



print("Enter your choices:  ")
a = input("Is he a fresher \n 1. YES \n 2. NO\n")
b = input ("Is he sitting in the dining hall \n 1. YES \n 2. NO\n")
print(prob_a_b(a,b))