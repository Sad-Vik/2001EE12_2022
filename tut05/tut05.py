# from platform import python_version
# from datetime import datetime
# start_time = datetime.now()
def octant_range_names(mod=5000):
    import pandas as pd
    octant_name_id_mapping = {"+1": "Internal outward interaction", "-1": "External outward interaction", "+2": "External Ejection",
                              "-2": "Internal Ejection", "+3": "External inward interaction", "-3": "Internal inward interaction", "+4": "Internal sweep", "-4": "External sweep"}
    # Read the input file
    ip = pd.read_excel("octant_input.xlsx")
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
        p1, p2, p3, p4 = 0, 0, 0, 0
        n1, n2, n3, n4 = 0, 0, 0, 0
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

    ceil = i+1
    df = ip.iloc[:ceil+1, [13, 14, 15, 16, 17, 18, 19, 20]].copy()
    Valuecounts = df.to_dict('index')
    y = []
    for i in range(len(Valuecounts)):
        x = Valuecounts[i]
        res = dict(zip(x.keys(), pd.Series(
            x.values()).rank(ascending=False).tolist()))
        y.append(res)

    data = pd.DataFrame(y).rename(columns={'+1': "Rank of +1", '-1': "Rank of -1", '+2': "Rank of +2", "-2": "Rank of -2",
                                           "+3": "Rank of +3", "-3": "Rank of -3", "+4": "Rank of +4", "-4": "Rank of -4"})  # dictionary of rank values
    for col in range(8):
        ip.loc[:, col+21] = data.iloc[:, col]
    x = data.columns
    for i in range(8):
        ip.columns.values[i+21] = "{}".format(x[i])

    ip.loc[:, "Rank1 Octant ID"] = pd.DataFrame(y).idxmin(axis=1)
    rno = 0
    for i in ip.loc[:1+len(data), "Rank1 Octant ID"]:
        if str(i) in octant_name_id_mapping.keys():
            ip.loc[rno, "Rank1 Octant Name"] = octant_name_id_mapping[i]
        rno += 1
    l, rno = ceil+5, 0
    ip.loc[l-1, "+1"], ip.loc[l-1, "-1"] = "Octant ID", "Octant Name"
    cnt = ip["Rank1 Octant ID"].value_counts()
    for i in octant_name_id_mapping.keys():
        ip.loc[l+rno, "+1"] = i
        ip.loc[l+rno, "-1"] = octant_name_id_mapping[i]
        if i in cnt:
            ip.loc[l+rno, "+2"] = cnt[i]
        else:
            ip.loc[l+rno, "+2"] = 0
        rno += 1
    # exporting data frame to excel
    ip.to_excel("octant_output_ranking_excel.xlsx", index=False)


# ver = python_version()
# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
mod = 5000
octant_range_names(mod)
# This shall be the last lines of the code.
# end_time = datetime.now()
# print('Duration of Program Execution: {}'.format(end_time - start_time))
