#def octact_identification(mod):

import pandas as pd
mod = 5000

# Read the input file
ip = pd.read_csv("octant_input.csv")
# Creating a coloumn containg average of U,V,W
ip.loc[0, "U_avg"] = ip["U"].mean()
ip.loc[0, "V_avg"] = ip["V"].mean()
ip.loc[0, "W_avg"] = ip["W"].mean()
# Creating a coloumn with new U,V,W values
ip["U1"] = ip["U"] - ip["U"].mean()
ip["V1"] = ip["V"] - ip["V"].mean()
ip["W1"] = ip["W"] - ip["W"].mean()
# Creating a coloumn with Octant using loc which checks the condition
# and assigns the value on right of = to it
ip.loc[((ip.U1 > 0) & (ip.V1 > 0) & (ip.W1 > 0)), "Octant"] = "+1"
ip.loc[((ip.U1 > 0) & (ip.V1 > 0) & (ip.W1 < 0)), "Octant"] = "-1"
ip.loc[((ip.U1 < 0) & (ip.V1 > 0) & (ip.W1 > 0)), "Octant"] = "+2"
ip.loc[((ip.U1 < 0) & (ip.V1 > 0) & (ip.W1 < 0)), "Octant"] = "-2"
ip.loc[((ip.U1 < 0) & (ip.V1 < 0) & (ip.W1 > 0)), "Octant"] = "+3"
ip.loc[((ip.U1 < 0) & (ip.V1 < 0) & (ip.W1 < 0)), "Octant"] = "-3"
ip.loc[((ip.U1 > 0) & (ip.V1 < 0) & (ip.W1 > 0)), "Octant"] = "+4"
ip.loc[((ip.U1 > 0) & (ip.V1 < 0) & (ip.W1 < 0)), "Octant"] = "-4"

ip.loc[1, " "] = "User Input"
ip.loc[[0, 1], "OctantID", ] = ["Overall Count", "Mod ="+str(mod)]

num = ip['Octant'].value_counts()

# assigning count numbers from value count under all octants(+1,-1,+2,-2,+3,-3,+4,-4)
ip.loc[0, "+1"] = num["+1"]
ip.loc[0, "-1"] = num["-1"]
ip.loc[0, "+2"] = num["+2"]
ip.loc[0, "-2"] = num["-2"]
ip.loc[0, "+3"] = num["+3"]
ip.loc[0, "-3"] = num["-3"]
ip.loc[0, "+4"] = num["+4"]
ip.loc[0, "-4"] = num["-4"]
# Assign a variable
low = 0000
m = mod
i = 1
while m <= len(ip):
    ip['OctantID'][i+1] = str(low) + "-" + str(m-1)
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0
    for j in range(low, m):
        if ip['Octant'][j] == "+1":
            p1 = p1+1
        elif ip['Octant'][j] == "-1":
            n1 = n1+1
        elif ip['Octant'][j] == "+2":
            p2 = p2+1
        elif ip['Octant'][j] == "+2":
            n2 = n2+1
        elif ip['Octant'][j] == "+3":
            p3 = p3+1
        elif ip['Octant'][j] == "-3":
            n3 = n3+1
        elif ip['Octant'][j] == "+4":
            p4 = p4+1
        elif ip['Octant'][j] == "-4":
            n4 = n4+1
    ip.loc[i+1, "+1"] = p1
    ip.loc[i+1, "-1"] = n1
    ip.loc[i+1, "+2"] = p2
    ip.loc[i+1, "-2"] = n2
    ip.loc[i+1, "+3"] = p3
    ip.loc[i+1, "-3"] = n3
    ip.loc[i+1, "+4"] = p4
    ip.loc[i+1, "-4"] = n4
    low = m
    i = i+1
    m = mod*i
    if m > len(ip):
        m = len(ip)
ip.to_csv("octant_output.csv")


mod = 5000
#octact_identification(mod)
