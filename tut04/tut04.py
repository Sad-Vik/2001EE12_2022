def octant_longest_subsequence_count_with_range():
    try:
        import pandas as pd
        try:
            ip = pd.read_excel(
                "input_octant_longest_subsequence_with_range.xlsx")
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
            To = [[0] for m in range(9)]  # Creating a List of lists (LOL)

            for i in range(len(ip)-1):
                x = int(ip.loc[i, "Octant"])+4
                y = int(ip.loc[i+1, "Octant"])+4
                cnt[x] += 1
                if cnt[x] != cnt[y]:
                    if max_cnt[x] < cnt[x]:
                        To[x].pop()
                        # poping those end values when max_cnt is not maximum
                        max_cnt[x] = cnt[x]
                        num[x] = 1
                        To[x] = [ip.loc[i, "Time"]]
                        cnt[x] = 0
                    else:
                        if cnt[x] == max_cnt[x]:
                            To[x].append(ip.loc[i, "Time"])
# Since a LOL is made to append value. If maximum isnt reached it will be poped
                            num[x] += 1
                            cnt[x] = 0
                        elif max_cnt[x] > cnt[x]:
                            cnt[x] = 0

    # Manually creating columns and filling them with values same as tut 3
            ip.loc[0, "Octants"] = "+1"
            ip.loc[1, "Octants"] = "-1"
            ip.loc[2, "Octants"] = "+2"
            ip.loc[3, "Octants"] = "-2"
            ip.loc[4, "Octants"] = "+3"
            ip.loc[5, "Octants"] = "-3"
            ip.loc[6, "Octants"] = "+4"
            ip.loc[7, "Octants"] = "-4"

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
            ip.loc[0, "   "] = "   "
# creating a new columns to use for tut 4
            ip.loc[0, "Octants."] = "+1"
            ip.loc[2+num[5], "Octants."] = "-1"
            ip.loc[4+num[5]+num[3], "Octants."] = "+2"
            ip.loc[6+num[5]+num[3]+num[6], "Octants."] = "-2"
            ip.loc[8+num[5]+num[3]+num[6]+num[2], "Octants."] = "+3"
            ip.loc[10+num[5]+num[3]+num[6]+num[2]+num[7], "Octants."] = "-3"
            ip.loc[12+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1], "Octants."] = "+4"
            ip.loc[14+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1]+num[8], "Octants."] = "-4"

            ip.loc[0, "Longest Subsequence Length."] = max_cnt[5]
            ip.loc[2+num[5], "Longest Subsequence Length."] = max_cnt[3]
            ip.loc[4+num[5]+num[3], "Longest Subsequence Length."] = max_cnt[6]
            ip.loc[6+num[5]+num[3]+num[6],
                   "Longest Subsequence Length."] = max_cnt[2]
            ip.loc[8+num[5]+num[3]+num[6]+num[2],
                   "Longest Subsequence Length."] = max_cnt[7]
            ip.loc[10+num[5]+num[3]+num[6]+num[2]+num[7],
                   "Longest Subsequence Length."] = max_cnt[1]
            ip.loc[12+num[5]+num[3]+num[6]+num[2]+num[7]+num[1],
                   "Longest Subsequence Length."] = max_cnt[8]
            ip.loc[14+num[5]+num[3]+num[6]+num[2]+num[7]+num[1]
                   + num[8], "Longest Subsequence Length."] = max_cnt[0]

            ip.loc[0, "LS Count."] = num[5]
            ip.loc[2+num[5], "LS Count."] = num[3]
            ip.loc[4+num[5]+num[3], "LS Count."] = num[6]
            ip.loc[6+num[5]+num[3]+num[6], "LS Count."] = num[2]
            ip.loc[8+num[5]+num[3]+num[6]+num[2], "LS Count."] = num[7]
            ip.loc[10+num[5]+num[3]+num[6]+num[2]+num[7], "LS Count."] = num[1]
            ip.loc[12+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1], "LS Count."] = num[8]
            ip.loc[14+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1]+num[8], "LS Count."] = num[0]
# Creating new rows for adding "To" and "From" values Manually

            ip.loc[1, "Octants."] = "Time"
            ip.loc[3+num[5], "Octants."] = "Time"
            ip.loc[5+num[5]+num[3], "Octants."] = "Time"
            ip.loc[7+num[5]+num[3]+num[6], "Octants."] = "Time"
            ip.loc[9+num[5]+num[3]+num[6]+num[2], "Octants."] = "Time"
            ip.loc[11+num[5]+num[3]+num[6]+num[2]+num[7], "Octants."] = "Time"
            ip.loc[13+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1], "Octants."] = "Time"
            ip.loc[15+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1]+num[8], "Octants."] = "Time"

            ip.loc[1, "Longest Subsequence Length."] = "From"
            ip.loc[3+num[5], "Longest Subsequence Length."] = "From"
            ip.loc[5+num[5]+num[3], "Longest Subsequence Length."] = "From"
            ip.loc[7+num[5]+num[3]+num[6],
                   "Longest Subsequence Length."] = "From"
            ip.loc[9+num[5]+num[3]+num[6]+num[2],
                   "Longest Subsequence Length."] = "From"
            ip.loc[11+num[5]+num[3]+num[6]+num[2]+num[7],
                   "Longest Subsequence Length."] = "From"
            ip.loc[13+num[5]+num[3]+num[6]+num[2]+num[7]
                   + num[1], "Longest Subsequence Length."] = "From"
            ip.loc[15+num[5]+num[3]+num[6]+num[2]+num[7]+num[1]
                   + num[8], "Longest Subsequence Length."] = "From"

            ip.loc[1, "LS Count."] = "To"
            ip.loc[3+num[5], "LS Count."] = "To"
            ip.loc[5+num[5]+num[3], "LS Count."] = "To"
            ip.loc[7+num[5]+num[3]+num[6], "LS Count."] = "To"
            ip.loc[9+num[5]+num[3]+num[6]+num[2], "LS Count."] = "To"
            ip.loc[11+num[5]+num[3]+num[6]+num[2]+num[7], "LS Count."] = "To"
            ip.loc[13+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1], "LS Count."] = "To"
            ip.loc[15+num[5]+num[3]+num[6]+num[2]
                   + num[7]+num[1]+num[8], "LS Count."] = "To"

# Since the table has been already created manually just inserting the values
            ip.loc[2, "LS Count."] = To[5][0]
            ip.loc[5, "LS Count."] = To[3][0]
            ip.loc[10, "LS Count."] = To[6][0]
            ip.loc[13, "LS Count."] = To[2][0]
            ip.loc[16, "LS Count."] = To[7][0]
            ip.loc[19, "LS Count."] = To[1][0]
            ip.loc[22, "LS Count."] = To[8][0]
            ip.loc[25, "LS Count."] = To[0][0]

            ip.loc[2, "Longest Subsequence Length."] = (
                To[5][0])-(max_cnt[5]-1)/100
            ip.loc[5, "Longest Subsequence Length."] = (
                To[3][0])-(max_cnt[3]-1)/100
            ip.loc[10, "Longest Subsequence Length."] = (
                To[6][0])-(max_cnt[6]-1)/100
            ip.loc[13, "Longest Subsequence Length."] = (
                To[2][0])-(max_cnt[2]-1)/100
            ip.loc[16, "Longest Subsequence Length."] = (
                To[7][0])-(max_cnt[7]-1)/100
            ip.loc[19, "Longest Subsequence Length."] = (
                To[1][0])-(max_cnt[1]-1)/100
            ip.loc[22, "Longest Subsequence Length."] = (
                To[8][0])-(max_cnt[8]-1)/100
            ip.loc[25, "Longest Subsequence Length."] = (
                To[0][0])-(max_cnt[0]-1)/100

            # since there are repetions for "-1"
            ip.loc[6, "LS Count."] = To[3][1]
            ip.loc[6, "Longest Subsequence Length."] = (
                To[3][1])-(max_cnt[3]-1)/100
            ip.loc[7, "LS Count."] = To[3][2]
            ip.loc[7, "Longest Subsequence Length."] = (
                To[3][2])-(max_cnt[3]-1)/100

            ip.to_excel(
                "output_octant_longest_subsequence_with_range.xlsx", index=False)
        except:
            print("Please provide correct input file!")
    except:
        print("Install pandas and openpyxl before running the code.")


octant_longest_subsequence_count_with_range()
