blue = int(input("Enter the number of blue shirts  "))
white = int(input("Enter the number of white shirts  "))
red = int(input("Enter the number of red shirts  "))
total = blue+white+red

prob_b = blue/total
prob_r = red/total
prob_bga = prob_b

probb_r = prob_r*prob_b

print("The probabilty of getting a blue shirt first and red shirt second is   ", round(prob_b,3) )
print("The probabilty of bothe venets occuring tgt is    ", round(prob_r,3) )