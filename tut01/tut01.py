def octact_identification(mod):
    import pandas as pd

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

    # assigning octant count numbers from value_count under all octants(+1,-1,+2,-2,+3,-3,+4,-4)
    ip.loc[0, "+1"] = num["+1"]
    ip.loc[0, "-1"] = num["-1"]
    ip.loc[0, "+2"] = num["+2"]
    ip.loc[0, "-2"] = num["-2"]
    ip.loc[0, "+3"] = num["+3"]
    ip.loc[0, "-3"] = num["-3"]
    ip.loc[0, "+4"] = num["+4"]
    ip.loc[0, "-4"] = num["-4"]
    # defining a lower and higher boundaries
    low = 0000
    m = mod
    i = 1
    # making loop that runs for as long as m is less than total value count
    while m <= len(ip):
        # ip.loc[i+1, 'OctantID'] = str(low) + "-" + str(m-1)
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        for j in range(low, m):  # for loop that runs for say 0-4999 and if-loops count octant count
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
            # appending those values from the loop to i+1 th row of +1th coloumn
        ip.loc[i+1, "+1"] = p1
        ip.loc[i+1, "-1"] = n1
        ip.loc[i+1, "+2"] = p2
        ip.loc[i+1, "-2"] = n2
        ip.loc[i+1, "+3"] = p3
        ip.loc[i+1, "-3"] = n3
        ip.loc[i+1, "+4"] = p4
        ip.loc[i+1, "-4"] = n4
        # created a if statement to end the continous while loop created
        if m == len(ip):
            ip.loc[i+1, 'OctantID'] = str(low) + "-" + str(m)
            break
        else:
            ip.loc[i+1, 'OctantID'] = str(low) + "-" + str(m-1)
            low = m  # exchanging upper limit to lower so as to run again
            i = i+1
            m = mod*i  # modifying upper limit
            if m > len(ip):  # to check if the upper limit is excceding the total value
                m = len(ip)
    ip.to_csv("octant_output.csv")  # exporting data frame to csv


mod = 5000
octact_identification(mod)
