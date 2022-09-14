'''
def octact_identification(mod=5000):
  ###Code

  mod = 5000
  octact_identification(mod)
'''
import pandas as pd
import math as math
ip = pd.read_csv("octant_input.csv")
ip.loc[0, "U_avg"] = ip["U"].mean()
ip.loc[0, "V_avg"] = ip["V"].mean()
ip.loc[0, "W_avg"] = ip["W"].mean()
ip["U1"] = ip["U"] - ip["U"].mean()
ip["V1"] = ip["V"] - ip["V"].mean()
ip["W1"] = ip["W"] - ip["W"].mean()

'''
for x, y, z in ip["U1"], ip["V1"], ip["W1"]:
    if x > 0 and y > 0:
        octant = 1
        if z < 0:
            octant = -1 * octant
    elif x < 0 and y > 0:
        octant = 2
        if z < 0:
            octant = -1 * octant
    elif x < 0 and y < 0:
        octant = 3
        if z < 0:
            octant = -1 * octant
    elif x > 0 and y < 0:
        octant = 4
        if z < 0:
            octant = -1 * octant
    octant.append(ip["Octant"])

'''
mod = 5000
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
'''
for A in [1, -1, 2, -2, 3, -3, 4, -4]:
    ip.loc[0, A] = len(ip.Octant == A)
'''
ip.loc[0, "+1"] = len(ip.Octant == +1)
ip.loc[0, "-1"] = len(ip.Octant == -1)
ip.loc[0, "+2"] = len(ip.Octant == +2)
ip.loc[0, "-2"] = len(ip.Octant == -2)
ip.loc[0, "+3"] = len(ip.Octant == +3)
ip.loc[0, "-3"] = len(ip.Octant == -3)
ip.loc[0, "+4"] = len(ip.Octant == +4)
ip.loc[0, "-4"] = len(ip.Octant == -4)
'''
ip.loc[0, ["+1", "-1", "+2", "-2", "+3", "-3", "+4", "-4"]] = [len(ip.Octant == +1), len(ip.Octant == -1), len(
    ip.Octant == +2), len(ip.Octant == -2), len(ip.Octant == +3), len(ip.Octant == -3), len(ip.Octant == +4), len(ip.Octant == -4)]
ip.loc[i+2,"OctantID"]
x = ip['Octant'].value_counts()
print(x)
y = ip['Octant'].value_counts(bins=5000)
'''
value = math.ceil((len(ip.Octant)/mod))
for i in range(value):
    if mod*(i+1) < len(ip.Octant):
        ip.OctantID[i+2] = str(mod*i)+"-"+str(mod*(i+1) - 1)
    else:
        ip.OctantID[i+2] = str(mod*i)+"-"+str(len(ip.Octant)-1)
#    for B in [1, -1, 2, -2, 3, -3, 4, -4]:
#        ip.loc[i+2, B] = len(ip.Octant == B)
    ip.loc[i+2, "+1"] = len(ip.Octant == +1)
    ip.loc[i+2, "-1"] = len(ip.Octant == -1)
    ip.loc[i+2, "+2"] = len(ip.Octant == +2)
    ip.loc[i+2, "-2"] = len(ip.Octant == -2)
    ip.loc[i+2, "+3"] = len(ip.Octant == +3)
    ip.loc[i+2, "-3"] = len(ip.Octant == -3)
    ip.loc[i+2, "+4"] = len(ip.Octant == +4)
    ip.loc[i+2, "-4"] = len(ip.Octant == -4)
ip.to_csv("octant_output1.csv", index=False)
