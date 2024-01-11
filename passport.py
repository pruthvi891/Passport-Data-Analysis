import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import csv

df =pd.DataFrame()
csv_file = r'D:\python\PassportSeva_1_1'

def introduction():
    msg='''
           Passport is one of the most basic requirement if you want to travel outside of India. In order to
           support the needs of passport of its citizen, Government of India has established regional passport
           offices across the India in different cities.

           The dataset contains the data generated in this regional passport seva kendra and the data is categorised
           in the different categories.

           In this project we are going to analyse the same dataset using Python Pandas on windows machine but the
           project can be run on any machine support Python and Pandas. Besides pandas we also used matplotlib python

           module for visualization of this dataset.

           The whole project is divided into four major parts ie reading, analysis, visualization and export. all these
           part are further divided into menus for easy navigation

           Passport Project made by    : Pruthviraj Patole
           Roll No                     : 2VX21MC067
           School Name                 : VTU, Belagavi
           session                     : 2020-22

           '''
    for x in msg:
        print(x,end ='')


def read_csv_file():
    df =pd.read_csv("E:\downloads\PassportSeva_1_1.csv")
    print(df)

# name of function      : clear
# purpose               : clear output screen
def clear():
    for x in range(10):
               print()



def data_analysis_menu():
        df = pd.read_csv("E:\downloads\PassportSeva_1_1.csv")
        while True:
            clear()
            print('\n\nData Analysis MENU ')

            print('1.  Show Whole DataFrame\n')
            print('2.  Show Columns\n')
            print('3.  Show Top Rows\n')
            print('4.  Row Bottom Rows\n')
            print('5.  Show Specific Column\n')
            print('6.  Add a New Record\n')
            print('7.  Add a New Column\n')
            print('8.  Delete a Column\n')
            print('9.  Delete a Record\n')
            print('10.  Update a Record\n')
            print('11.  RPO Report \n')
            print('12.  Scheme Type Report \n')
            print('13.  Data Summery\n')
            print('14.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            if ch == 1:
                print(df)
                wait = input()
            if ch == 2:
                print(df.columns)
                wait = input()
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input()
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input()
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input()
            if ch==6:
                a = input('Enter service Name :')
                b = input('Enter New Rpo Name :')
                c = input(' Enter New Scheme Type :')
                d= int(input('Enter Total LastWeekCount :'))
                e = int(input('Enter LastMonthCount :'))
                f = int(input('Enter YearTillDate :'))
                g = input('Enter Date of Entry')
                data={'ServiceName':a,'RpoName':b,'SchemeType':c,'LastWeekCount':d,'LastMonthCount':e,'YearTillDate':f,'Date':g}
                df = df.append(data,ignore_index=True)
                print(df)
                wait=input()
            if ch==7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name]=col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()

            if ch==8:
                col_name =input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait=input()

            if ch==9:
                index_no =int(input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch==11:
                print(df.columns)
                print(df['RpoName'].unique())
                rp= input('Enter Rpo Name ')
                g = df.groupby('RpoName')
                print('Rpo Name ', rp)
                print(g['YearTillDate'].sum())
                print('\n\n\n Press any key to continue....')
                wait=input()

            if ch==12:
                df1=df.SchemeType.unique()
                print('Available Schemes :',df1)
                print('\n\n')
                schName =input('Enter Scheme Type :')
                df1=df[df.SchemeType==schName]
                print(df1)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch==13:
                print(df.describe())
                print("\n\n\nPress any key to continue....")
            if ch == 14:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv('E:\downloads\PassportSeva_1_1.csv')
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  Whole Data LINE Graph\n')
        print('2.  Whole Data Bar Graph\n')
        print('3.  Whole Data Scatter Graph\n')
        print('4.  Whole Data Pie Chart\n')
        print('5.  Bar Graph By User Condition\n')
        print('6.  Bar Graph Scheme Type\n')
        print('7.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:' ))

        if ch==1:
            g = df.groupby('RpoName')
            x = df['RpoName'].unique()
            y = g['YearTillDate'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('Regional Offices')
            plt.ylabel('Total Passport served')
            plt.title('Passport served')
            plt.grid(True)
            plt.plot(x, y)
            plt.show()

        if ch==2:
            g = df.groupby('RpoName')
            x = df['RpoName'].unique()
            y = g['YearTillDate'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('Regional Offices')
            plt.ylabel('Total Passport served')
            plt.title('Passport served')
            plt.bar(x, y)
            plt.grid(True)
            plt.show()
            wait = input()

        if ch==3:
            g = df.groupby('RpoName')
            x = df['RpoName'].unique()
            y = g['YearTillDate'].sum()
            plt.xticks(rotation='vertical')
            plt.xlabel('Regional Offices')
            plt.ylabel('Total Passport served')
            plt.title('Passport served')
            plt.grid(True)
            plt.scatter(x, y)
            plt.show()
            wait = input()

        if ch==4:
            g = df.groupby("SchemeType")
            x = df['SchemeType'].unique()
            y = g['YearTillDate'].sum()
            plt.pie(y, labels=x, autopct='% .2f', startangle=90)
            plt.xticks(rotation='vertical')
            plt.show()

        if ch==5:
            rponames=df['RpoName'].unique()
            print(rponames)
            rpo=input('Enter RpoName as shown It is Case Sensitive : ')
            x = df[df.RpoName==rpo].SchemeType
            y = df[df.RpoName==rpo].LastWeekCount
            plt.bar(x,y)
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(rpo)
            plt.xlabel('Scheme Types')
            plt.show()
            wait= input()

        if ch==6:
            schemes = df.SchemeType.unique()
            print('Available Schemes :',schemes)
            print('\n')
            schName = input('Enter Scheme Type Name :')
            names = df[df.SchemeType==schName].RpoName
            counting = df[df.SchemeType==schName].LastMonthCount
            plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title(schName)
            plt.xlabel('Regional Passport Office')
            plt.ylabel('No. Of applications')
            plt.bar(names,counting)
            plt.show()

        if ch==7:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv("E:\downloads\PassportSeva_1_1.csv")
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print()
        print('1.  CSV File\n')
        print('2.  Excel File\n')
        print('3.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch==1:
            df.to_csv(r'E:\pydb\excelexport.csv', index = True)
            print('\n\nCheck your new file "excelexport.csv"  on E: Drive.....')
            wait = input()

        if ch == 2:
            df.to_excel(r'E:\pydb\PANDASEXPORT.xlsx', index = True)
            print('\n\nCheck your new file "excelexport.xlsx"  on E: Drive.....')
            wait = input()

        if ch == 3:
            break

def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice==1:
                                 print('We need to add two number')
                                 read_csv_file()
                                 wait=input("Enter any key")

                      if choice==2:
                                 print('We need to subtract two number')
                                 data_analysis_menu()
                                 wait=input()

                      if choice==3:
                                 graph()
                                 wait=input()

                      if choice==4:
                                 export_menu()
                                 wait=input()

                      if choice==5:
                                 break
           clear()


# call your main menu
main_menu()
