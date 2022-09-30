def octant_longest_subsequence_count():
    import pandas as pd

    ip = pd.read_excel("input_octant_longest_subsequence.xlsx")
# Data Pre-processing
    ip.loc[0, "U_avg"] = ip["U"].mean()
    ip.loc[0, "V_avg"] = ip["V"].mean()
    ip.loc[0, "W_avg"] = ip["W"].mean()
    ip["U1"] = ip["U"] - ip["U"].mean()
    ip["V1"] = ip["V"] - ip["V"].mean()
    ip["W1"] = ip["W"] - ip["W"].mean()
    # Making Octant
    ip.loc[((ip.U1 > 0) & (ip.V1 > 0) & (ip.W1 > 0)), "Octant"] = "+1"
    ip.loc[((ip.U1 > 0) & (ip.V1 > 0) & (ip.W1 < 0)), "Octant"] = "-1"
    ip.loc[((ip.U1 < 0) & (ip.V1 > 0) & (ip.W1 > 0)), "Octant"] = "+2"
    ip.loc[((ip.U1 < 0) & (ip.V1 > 0) & (ip.W1 < 0)), "Octant"] = "-2"
    ip.loc[((ip.U1 < 0) & (ip.V1 < 0) & (ip.W1 > 0)), "Octant"] = "+3"
    ip.loc[((ip.U1 < 0) & (ip.V1 < 0) & (ip.W1 < 0)), "Octant"] = "-3"
    ip.loc[((ip.U1 > 0) & (ip.V1 < 0) & (ip.W1 > 0)), "Octant"] = "+4"
    ip.loc[((ip.U1 > 0) & (ip.V1 < 0) & (ip.W1 < 0)), "Octant"] = "-4"
    ip.loc[0, " "] = "   "
# Creating three empty lists
    cnt = [0 for i in range(9)]  # For iterating over range
    max_cnt = [0 for j in range(9)]  # For storing max value of cnt
    num = [0 for k in range(9)]  # For assigning count repetitions

    for i in range(len(ip)-1):
        x = int(ip.loc[i, "Octant"])+4
        y = int(ip.loc[i+1, "Octant"])+4
        cnt[x] += 1
        if cnt[x] != cnt[y]:
            if max_cnt[x] < cnt[x]:
                max_cnt[x] = cnt[x]
                num[x] = 1
                cnt[x] = 0
            else:
                if cnt[x] == max_cnt[x]:
                    num[x] += 1
                    cnt[x] = 0
                if max_cnt[x] > cnt[x]:
                    cnt[x] = 0
# Filling the list values to columns using loc
    ip.loc[0, "Count"] = "+1"
    ip.loc[1, "Count"] = "-1"
    ip.loc[2, "Count"] = "+2"
    ip.loc[3, "Count"] = "-2"
    ip.loc[4, "Count"] = "+3"
    ip.loc[5, "Count"] = "-3"
    ip.loc[6, "Count"] = "+4"
    ip.loc[7, "Count"] = "-4"

    ip.loc[0, "Longest Subsequence Length"] = max_cnt[5]
    ip.loc[1, "Longest Subsequence Length"] = max_cnt[3]
    ip.loc[2, "Longest Subsequence Length"] = max_cnt[6]
    ip.loc[3, "Longest Subsequence Length"] = max_cnt[2]
    ip.loc[4, "Longest Subsequence Length"] = max_cnt[7]
    ip.loc[5, "Longest Subsequence Length"] = max_cnt[1]
    ip.loc[6, "Longest Subsequence Length"] = max_cnt[8]
    ip.loc[7, "Longest Subsequence Length"] = max_cnt[0]

    ip.loc[0, "LS Count"] = num[5]
    ip.loc[1, "LS Count"] = num[3]
    ip.loc[2, "LS Count"] = num[6]
    ip.loc[3, "LS Count"] = num[2]
    ip.loc[4, "LS Count"] = num[7]
    ip.loc[5, "LS Count"] = num[1]
    ip.loc[6, "LS Count"] = num[8]
    ip.loc[7, "LS Count"] = num[0]

    ip.to_excel("output_octant_longest_subsequence.xlsx", index=False)


octant_longest_subsequence_count()
