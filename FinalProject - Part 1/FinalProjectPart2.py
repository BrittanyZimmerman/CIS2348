#   Brittany Zimmerman
#   2219602

from datetime import datetime
import csv


class item:
    # initiates item class for all inventory elements
    def __init__(self, itemID=0, manuF='none', itemT='none', itemP=0.0, serv=datetime.today(), dmg='False'):
        self.itemID = itemID
        self.manuF = manuF
        self.itemT = itemT
        self.itemP = itemP
        self.serv = serv
        self.dmg = dmg


if __name__ == "__main__":
    # Dictionary to hold all inventory elements for retrieval
    full_table = {}
    item_type = []
    itemID_List = []
    # Lists for sorting
    dmg_inv = []
    manuF_list = []
    date_list = []
    price_list = []

    # Opens/reads manufacturer list
    with open('ManufacturerList.csv', 'r') as csvfile:
        list_reader = csv.reader(csvfile)
        # Takes rows from csv, initialized as item class, adds formatted versions to line.
        for row in list_reader:
            line = item()
            line.itemID = row[0]
            line.manuF = row[1].lower().replace(" ", "")
            line.itemT = row[2].lower()
            line.dmg = row[3]
            # ItemID defined as key, lines added to full_table.
            full_table[line.itemID] = line

            # Opens/reads price list and adds pricing as itemP.
        with open('PriceList.csv', 'r') as csvfile:
            list_reader = csv.reader(csvfile)
            for row in list_reader:
                # Defined float itemP.
                full_table[row[0]].itemP = float(row[1])

        # Opens/reads service list and adds service dates to full_table as serv.
        with open('ServiceDatesList.csv', 'r') as csvfile:
            list_reader = csv.reader(csvfile)
            # datetime formatting
            date_format = '%m/%d/%Y'
            for row in list_reader:
                # strips dates and adds to full_table as serv.
                new_date = datetime.strptime(row[1], date_format).date()
                full_table[row[0]].serv = new_date

    # appends full_table.itemT to itemT list for sorting.
    for i in full_table:
        item_type.append(full_table[i].itemT)
    item_type.sort()
    itemT = {}
    # adds itemT table values to dictionary to ensure unique values.
    for i in item_type:
        itemT[i] = i

    # Manufacturers appended to list and sorted.
    for i in full_table:
        manuF_list.append(full_table[i].manuF)
    manuF_list.sort()
    manuF = {}
    # Manufacturers added to dictionary as key to ensure unique values.
    for i in manuF_list:
        manuF[i] = i

    # input initialized as string r for input validation.
    inp_str = 'r'

    # loops while input not q or Q
    while inp_str != 'q' and inp_str != 'Q':
        # input variables initialized as string 'r' for input validation at beginning of each loop.
        inp_manu = 'r'
        inp_itemT = 'r'
        # asks for input and converts to lower case to ignore case sensitivity.
        inp_str = str(input(f'Please enter item type and manufacturer.')).lower()
        # check to break explicitly if q detected, stops any subsequent print statements.
        if inp_str == 'q' or inp_str == 'Q':
            break

        # searches user input for manufacturer and item type, setting variables equal if found.
        for i in manuF:
            if i in inp_str:
                inp_manu = i
        for i in itemT:
            if i in inp_str:
                inp_itemT = i

        # if variables unassigned to new values, print inventory message.
        if inp_manu == 'r' or inp_itemT == 'r':
            print('No such item in inventory')

        #   initialized search list with like types and user calculation checks.
        else:
            user_search = [0, '', '', 0]
            user_calc = []

            # iterates through full table, checks that manufacturer and item type match.
            # appends to user_search if not damaged, current date is before service date,
            # and ensures check at each iteration that all prices are added from low to high.
            for i in full_table:
                if full_table[i].manuF == inp_manu and full_table[i].itemT == inp_itemT:
                    if full_table[i].dmg != 'damaged' and datetime.today().date() < full_table[i].serv:
                        if user_search[3] < full_table[i].itemP:
                            user_search[0] = full_table[i].itemID
                            user_search[1] = full_table[i].manuF
                            user_search[2] = full_table[i].itemT
                            user_search[3] = full_table[i].itemP

            # adds all found values to user_calc to narrow down to max price.
            for j in user_search:
                user_calc.append(user_search)

            # iterates through found prices, replacing user_max value until final max line found.
            # this is then added to user_final for printing.
            user_max = 0
            user_final = []
            for j in user_calc:
                if j[3] > user_max:
                    user_max = j[3]
                    user_final = j

            # prints formatted values only if checks successful.
            if len(user_final) > 0:
                print(f'Your item is: {user_final[0]},'
                      f' {user_final[1].capitalize().replace(" ", "")}, '
                      f'{user_final[2]},'
                      f' ${user_final[3]}')
            else:
                print('No such item in inventory')

            # adds formatted values to client recommendation list
            # if an item of the same item type, but not manufacturer, found and also not damaged or past service date.
            client_rec = []
            for i in full_table:
                if full_table[i].manuF != inp_manu and full_table[i].itemT == inp_itemT:
                    if full_table[i].dmg != 'damaged' and datetime.today().date() < full_table[i].serv:
                        client_rec.append(full_table[i])

                        # checks on loop, if previous checks yield an item, that the absolute value of the subtraction
                        # of recommended item from original item yields a lower number than previously assigned,
                        # assigning new value if found.
                        rec_dif = 1000000000000
                        final_rec = []
                        if len(user_final) > 0:
                            for j in client_rec:
                                if abs(user_final[3] - j.itemP) < rec_dif:
                                    rec_dif = abs(user_final[3]-j.itemP)
                                    final_rec = j

                            # formatted values are printed if found.
                            print(f'You may, also, consider: {final_rec.itemID}, '
                                  f'{final_rec.manuF.capitalize().replace(" ","")}, '
                                  f'{final_rec.itemT}, '
                                  f'${final_rec.itemP}')
