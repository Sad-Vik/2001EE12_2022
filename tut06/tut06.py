# from datetime import datetime
# start_time = datetime.now()
def attendance_report():
    try:
        import pandas as pd
        import os
        import datetime
        import re
        try:
            pd.io.formats.excel.ExcelFormatter.header_style = None
            data = pd.read_csv("input_attendance.csv")
            ip = pd.read_csv("input_registered_students.csv")
            df1 = data['Timestamp'].str.extract(r'(?P<Date>[0-9]{2}/[0-9]{2}/[0-9]{4}) (?P<Time>[0-9]{2}:[0-9]{1,2}:[0-9]{1,2})')
            df2 = data['Attendance'].str.extract(r'(?P<Roll>[0-9]{4}[a-zA-Z]{2}[0-9]{2}) (?P<Name>[a-zA-Z ]*$)')
            df = pd.concat([df1,df2],axis = 1)
            for i in range(len(df)):
                date, time = df.iloc[i, 0], df.iloc[i, 1]
                dd, mm, yy = (int(x) for x in date.split('/'))
                HH, MM, SS = (int(y) for y in time.split(':'))
                df.loc[i,"Day"] = datetime.date(yy, mm, dd).strftime("%A")
                df.loc[i,"OnTime"] = "Yes" if (HH == 14) | (HH == 15 & MM == 00 ) else "No"
            x = df.loc[((df["Day"] =="Thursday")|(df["Day"] =="Monday"))].reset_index(drop=True)
            start_date = datetime.datetime.strptime(x.iloc[0, 0],'%d/%m/%Y')
            end_date = datetime.datetime.strptime(x.iloc[-1, 0],'%d/%m/%Y')
            list = []
            delta = end_date - start_date   # returns timedelta
            for i in range(0,delta.days + 1,7):
                day = start_date + datetime.timedelta(days=i)
                list.append(day)
            if x.iloc[0,4] == "Monday":
                start_date += datetime.timedelta(days=3)
                end_date  -= datetime.timedelta(days=4)
            elif x.iloc[0,4] == "Thursday":
                start_date += datetime.timedelta(days=4)
                end_date -= datetime.timedelta(days=3)
            delta = end_date - start_date   # returns timedelta
            for i in range(0,delta.days + 1,7):
                day = start_date + datetime.timedelta(days=i)
                list.append(day)
            list.sort()    # list containg all working dates.
            Workdays = [x.strftime('%d/%m/%Y') for x in list]
        # All pre-processing has been completed now just feed all the req data to excel.
             ####INDIVIUAL ROLL
            roll_sheet = pd.DataFrame()
            roll_sheet.loc[0, "Date"] = ""
            for i in range(len(Workdays)):
                roll_sheet.loc[i+1, "Date"] = Workdays[i]
            pass_list = []
            def export_roll(sno):
                try:
                    x = os.path.realpath(os.path.dirname(__file__))
                    os.chdir(x+'\output')
                    roll_sheet.to_excel(f'{ip["Roll No"][sno]}.xlsx', index=False)
                except:
                    print("there is problem with path! input manually")
            for sno in range(len(ip)):
                roll_sheet.loc[0,"Roll"] = ip["Roll No"][sno]
                roll_sheet.loc[0,"Name"] = ip["Name"][sno]
                roll_check = df[df['Roll'] == ip["Roll No"][sno]]
                cnt = roll_check['Date'].value_counts()
                cnt_real = roll_check[roll_check['OnTime']=="Yes"]['Date'].value_counts()
            #Total attendance count
                row =1
                for i in Workdays:
                    if (i in cnt)&(i in cnt_real):
                        roll_sheet.loc[row,"Total Attendance Count"] = str(cnt[i])
                        roll_sheet.loc[row,"Real"] = "1"
                        roll_sheet.loc[row,"Absent"] = "0"
                        roll_sheet.loc[row,"Duplicate"] = str(cnt_real[i]-1)
                        roll_sheet.loc[row,"Invalid"] = str(cnt[i]-cnt_real[i])
                    elif (i in cnt)&(i  not in cnt_real):
                        roll_sheet.loc[row,"Total Attendance Count"] = str(cnt[i])
                        roll_sheet.loc[row,"Real"] = "0"
                        roll_sheet.loc[row,"Absent"] = "1"
                        roll_sheet.loc[row,"Duplicate"] = "0"
                        roll_sheet.loc[row,"Invalid"] = str(cnt[i])
                    else:
                        roll_sheet.loc[row,"Total Attendance Count"] = "0"
                        roll_sheet.loc[row,"Real"] = "0"
                        roll_sheet.loc[row,"Absent"] = "1"
                        roll_sheet.loc[row,"Duplicate"] = "0"
                        roll_sheet.loc[row,"Invalid"] = "0"
                    row +=1
                pass_list.append(roll_sheet["Real"].tolist())
                export_roll(sno)
            ###### CONSOLIDATED
            console = pd.DataFrame()
            console.loc[0,"Roll"] = "Sorted by roll no"
            for list in pass_list:
                del list[0]
            for i in range(len(ip)):
                console.loc[i+1,"Roll"] = ip.loc[i,"Roll No"]
                console.loc[i+1,"Name"] = ip.loc[i,"Name"]
                for day in range(len(Workdays)):
                    console.loc[i+1,f'{Workdays[day]}'] = 'P' if pass_list[i][day] == "1" else 'A'
                console.loc[i+1,'Actual Lecture Taken'] = len(Workdays)
                console.loc[i+1,'Total Real'] = pass_list[i].count("1")
                #directly applying % instead of applying formula by openpyxl
                console.loc[i+1,'% Attendance'] = round((pass_list[i].count("1"))/len(Workdays), 2)
            console.loc[0,'Actual Lecture Taken'] = '(=Total Mon+Thru dynamic count)'
            console.loc[0,'% Attendance'] = "Real/Actual Lecture Taken (Keep two digits decimal precision e.g., 90.58, round off )"
            x = os.path.realpath(os.path.dirname(__file__))
            os.chdir(x+'\output')
            console.to_excel("attendance_report_consolidated.xlsx",sheet_name='Consolidated Report',index=False)

        except:
            print("Provide correct path for input and output and start again.")
    except:
        print("Error in importing packages please pip install if not done.")
# from platform import python_version
# ver = python_version()
# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


attendance_report()
#This shall be the last lines of the code.
# end_time = datetime.now()
# print('Duration of Program Execution: {}'.format(end_time - start_time))
