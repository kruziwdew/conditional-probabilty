def prob_a_b(pink,blue,total):
    prob_p = pink/total
    prob_bl = blue/(total -1)
    prob_p_bl = prob_p*prob_bl
    return round(prob_p_bl, 3)
pink = int(input("Number of pink balls : "))
blue = int(input("Number of blue balls : "))
total = pink+blue

print("Probabilty of pink ball first  and blue as second ball is  ", prob_a_b(pink,blue,total))

