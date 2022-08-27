#Title: getUtilBills.py
#Author: cwilliams
#Date: 06/28/2022
#Purpose: Read through my check book register and get the latest amount for the 4 utilies
#1. Water: Water ePays
#2. Electricity: 4ChangeEnergy
#3. Natural Gas: Atmos
#4. Internet: AT&T
#Caveats:
#1. Can mix and match month's utility bills if they have not all come in for the current month
#2. Requires editing of bank transaction log to remove multiple header records
#3. Manual retrieval of BofA checking account transactions log
#4. Manual delivery of summary to payee.
#5. AT&T has two bills and the internet bill is usually $55.29. The other bill is hundreds more and incorrect for reimbursement.

#Changes
# 08/27/22 Checking in code to version control

#!\C:\Users\chuck\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts
import os
import csv
#test
import sys
import datetime
#Variables
l_bank_trans_file = "C:\\Users\\chuck\\Documents\\Python\\Data\\bofachkstmt08012022-08232022-edit.csv"
#why are some "global" variables accessible in main and others do not appear to be?
l_water_name = "Water ePays"
l_water_name = l_water_name.upper()
l_elec_name = "4Change Energy"
l_elec_name = l_elec_name.upper()
l_gas_name = "Atmos"
l_gas_name = l_gas_name.upper()
l_inet_name = "ATT*BILL PAYMENT"
l_inet_name = l_inet_name.upper()
l_test = True

def main():
    print('Scanning checking account activity for latest utility bills.')
    print('Utilities include:', l_water_name,',', l_elec_name,',', l_gas_name,',', l_inet_name)
    print(' ')
    #Note that \U is a special character sequence and therefore we have escaped it with an additional slash
    #print('Is C:\\Users\chuck\Documents\Python\Data\bofachkstmt05012022-06282022-edit.csv the most recent transactions file? Y/N')
    #li_recent = input('Is C:\\Users\chuck\Documents\Python\Data\bofachkstmt08012022-08122022-edit.csv the most recent transactions file? Y/N ')
    li_recent = input('Is '+ l_bank_trans_file + ' the most recent transactions file? Y/N ')

    if li_recent == 'N':
        sys.exit('Please retrieve and place the latest transactions file.')

    #forward declaration, did not work as global
    l_max_water_date = datetime.datetime(1970, 1, 1)
    l_water_util_amt = 0
    l_max_elec_date = datetime.datetime(1970, 1, 1)
    l_elec_util_amt = 0
    l_max_gas_date = datetime.datetime(1970, 1, 1)
    l_gas_util_amt = 0
    l_max_inet_date = datetime.datetime(1970, 1, 1)
    l_inet_util_amt = 0

    #with open(r"C:\Users\chuck\Documents\Python\Data\bofachkstmt08012022-08122022-edit.csv", mode="r", encoding="utf8") as i_file:
    with open(l_bank_trans_file, mode="r", encoding="utf8") as i_file:

        dictreader = csv.DictReader(i_file, skipinitialspace=True)

        for line in dictreader:
            #calc most recent water utility bill amount
            if l_water_name in line['Description']:
                l_max_water_date = line['Date']
                l_water_util_amt = line['Amount']
                if l_max_water_date < line['Date']:
                    l_max_water_date == line['Date']
                    
                    if l_test:
                        print ("New water date", l_max_water_date)

                    l_water_util_amt == line['Amount']
                if l_test:
                    print("Water", l_water_name, ":", line['Date'],line['Amount'])
 #           else:
 #               l_max_water_date = '?'
 #               l_water_util_amt = 0

            #calc most recent elec utility bill amount
            if l_elec_name in line['Description']:
                l_max_elec_date = line['Date']
                l_elec_util_amt = line['Amount']
                if l_max_elec_date < line['Date']:
                    l_max_elec_date == line['Date']

                    if l_test:
                        print ("New elec date", l_max_elec_date)

                    l_elec_util_amt == line['Amount']
                if l_test:
                    print("Electricity", l_elec_name,":", line['Date'], line['Amount'])
#            else:
#                l_max_elec_date = '?'
#                l_elec_util_amt = 0

            #calc most recent gas utility bill amount
            if l_gas_name in line['Description']:
                l_max_gas_date = line['Date']
                l_gas_util_amt = line['Amount']
                if l_max_gas_date < line['Date']:
                    l_max_gas_date == line['Date']
                    
                    if l_test:
                        print ("New gas date", l_max_gas_date)

                    l_gas_util_amt == line['Amount']
                if l_test:
                    print("Natural Gas aka", l_gas_name, ":", line['Date'], line['Amount'])
 #           else:
 #               l_max_gas_date = '?'
 #               l_gas_util_amt = 0

            #calc most recent internet access bill amount
            if l_inet_name in line['Description']:
                l_max_inet_date = line['Date']
                l_inet_util_amt = line['Amount']
                if l_max_inet_date < line['Date']:
                    l_max_inet_date == line['Date']

                    if l_test:
                        print ("New inet date", l_max_inet_date)

                    l_inet_util_amt == line['Amount']
                if l_test:
                    print("Internet", l_inet_name, ":", line['Date'], line['Amount'])
 #           else:
 #               l_max_inet_date = ''
 #               l_inet_util_amt = 0

    print("Summary:")
    #print(l_max_water_date,l_water_name,l_water_util_amt)
    print(l_max_elec_date,l_elec_name,l_elec_util_amt)
    print(l_max_gas_date,l_gas_name,l_gas_util_amt)
    print(l_max_inet_date,l_inet_name,l_inet_util_amt)

    if l_water_util_amt == 0:
        print("Missing water utility amount in the transaction file.")
    if l_elec_util_amt == 0:
        print("Missing electric utility amount in the transaction file.")
    if l_gas_util_amt == 0:
        print("Missing gas utility amount in the transaction file.")
    if l_inet_util_amt == 0:
        print("Missing internet utility amount in the transaction file.")
    
    l_util_amt = abs(float(l_water_util_amt)) + abs(float(l_elec_util_amt)) + abs(float(l_gas_util_amt)) + abs(float(l_inet_util_amt))

    print("Current total is ${:.2f}".format(float(l_util_amt)))
    print("Total no. of searched transactions: %d"%(dictreader.line_num))

    #test, show system arguments
    if l_test:
        print (sys.argv)

    i_file.close

if __name__ == "__main__":
    main()