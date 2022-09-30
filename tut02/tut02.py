def octant_transition_count(mod):
    import pandas as pd
    import math
    ip = pd.read_excel("input_octant_transition_identify.xlsx")
    ip.loc[0, "U_avg"] = ip["U"].mean()
    ip.loc[0, "V_avg"] = ip["V"].mean()
    ip.loc[0, "W_avg"] = ip["W"].mean()
    ip["U1"] = ip["U"] - ip["U"].mean()
    ip["V1"] = ip["V"] - ip["V"].mean()
    ip["W1"] = ip["W"] - ip["W"].mean()
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

    ip.loc[0, "+1"] = num["+1"]
    ip.loc[0, "-1"] = num["-1"]
    ip.loc[0, "+2"] = num["+2"]
    ip.loc[0, "-2"] = num["-2"]
    ip.loc[0, "+3"] = num["+3"]
    ip.loc[0, "-3"] = num["-3"]
    ip.loc[0, "+4"] = num["+4"]
    ip.loc[0, "-4"] = num["-4"]
    low = 0000
    m = mod
    i = 1
    d = math.ceil(29745/mod)
    while m <= len(ip):
        ip.loc[i+1, 'OctantID'] = str(low) + "-" + str(m-1)
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
            elif ip['Octant'][j] == "-2":
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
        if m == len(ip):
            break
        else:
            low = m
            i = i+1
            m = mod*i
            if m > len(ip):
                m = len(ip)  # previously done in tut01
# start of tut02
    start = d + 6
    end = 12 + (d+1)*14
    # Creating empty transition count tables
    for i in range(start, end, 14):
        ip.loc[i, "+1"] = "To"
        ip.loc[i+2, " "] = "From"
        ip.loc[i+1, "OctantID"] = "Count"
        ip.loc[i+1, "+1"] = "+1"
        ip.loc[i+1, "-1"] = "-1"
        ip.loc[i+1, "+2"] = "+2"
        ip.loc[i+1, "-2"] = "-2"
        ip.loc[i+1, "+3"] = "+3"
        ip.loc[i+1, "-3"] = "-3"
        ip.loc[i+1, "+4"] = "+4"
        ip.loc[i+1, "-4"] = "-4"
        ip.loc[i+2, "OctantID"] = "-4"
        ip.loc[i+3, "OctantID"] = "-3"
        ip.loc[i+4, "OctantID"] = "-2"
        ip.loc[i+5, "OctantID"] = "-1"
        ip.loc[i+6, "OctantID"] = "+1"
        ip.loc[i+7, "OctantID"] = "+2"
        ip.loc[i+8, "OctantID"] = "+3"
        ip.loc[i+9, "OctantID"] = "+4"
    low = 0000
    m = mod - 1
    for j in range(d+1):
        if not j:
            p = d+5
            ip.loc[p, "OctantID"] = "Overall Transition Count"
        else:
            p = 11+(j)*14
            ip.loc[p, "OctantID"] = "Mod Transition Count"
            if True:
                ip.loc[p+1, "OctantID"] = str(low) + "-" + str(m)
                low = m + 1
                m = m + mod
                if m > len(ip):
                    m = len(ip)-1
    # making empty List Of Lists(LOL) to store values
    lol = [[0 for i in range(9)] for j in range(9)]
    # A for loop that runs all the values in Octant and count+1 in lol
    for num in range(29744):
        x = int(ip.loc[num, "Octant"])+4
        y = int(ip.loc[num+1, "Octant"])+4
        lol[x][y] = lol[x][y] + 1
    # removing those zero values caused due to assuming octants as 0 to 8
    for i in range(9):
        lol[i].pop(4)
    lol.pop(4)
    # assigning the values in lol to empty overall transition table created
    for i in range(8):
        ip.loc[d+8+i, "+1"] = lol[i][4]
        ip.loc[d+8+i, "-1"] = lol[i][3]
        ip.loc[d+8+i, "+2"] = lol[i][5]
        ip.loc[d+8+i, "-2"] = lol[i][2]
        ip.loc[d+8+i, "+3"] = lol[i][6]
        ip.loc[d+8+i, "-3"] = lol[i][1]
        ip.loc[d+8+i, "+4"] = lol[i][7]
        ip.loc[d+8+i, "-4"] = lol[i][0]
    # Repeating the same of what we did for overall transition to mod values
    low = 0000
    high = mod
    for r in range(d):
        lol = [[0 for i in range(9)] for j in range(9)]
        # here we are counting the transition of mod value also
        for num in range(low, high):
            x = int(ip.loc[num, "Octant"])+4
            y = int(ip.loc[num+1, "Octant"])+4
            lol[x][y] = lol[x][y] + 1
        for i in range(9):
            lol[i].pop(4)
        lol.pop(4)
        place = d+8+14*(r+1)
        for i in range(8):
            ip.loc[place+i, "+1"] = lol[i][4]
            ip.loc[place+i, "-1"] = lol[i][3]
            ip.loc[place+i, "+2"] = lol[i][5]
            ip.loc[place+i, "-2"] = lol[i][2]
            ip.loc[place+i, "+3"] = lol[i][6]
            ip.loc[place+i, "-3"] = lol[i][1]
            ip.loc[place+i, "+4"] = lol[i][7]
            ip.loc[place+i, "-4"] = lol[i][0]
        low = high
        high += mod
        if high > len(ip):
            high = 29744

    ip.to_excel("output_octant_transition_identify.xlsx", index=False)


mod = 5000
octant_transition_count(mod)
