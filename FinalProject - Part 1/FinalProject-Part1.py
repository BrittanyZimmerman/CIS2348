# Brittany Zimmerman
# 2219602

from datetime import datetime       # needed to read and compare dates


class item:     # initiates item class for all inventory elements

    def __init__(self, itemID=0, manuF='none', itemT='none', itemP=0.0, serv=datetime.today(), dmg='False'):
        self.itemID = itemID
        self.manuF = manuF
        self.itemT = itemT
        self.itemP = itemP
        self.serv = serv
        self.dmg = dmg


if __name__ == "__main__":
    full_table = {}     # Dictionary to hold all inventory elements for retrieval
    item_type = []
    itemID_List = []
    dmg_inv = []        # Lists for sorting
    manuF_list = []
    date_list = []
    price_list = []

    import csv      # Needed for csv manipulation

    with open('ManufacturerList.csv', 'r') as csvfile:      # Opens/reads manufacturer list
        list_reader = csv.reader(csvfile)
        for row in list_reader:     # Takes rows from csv and adds them to line
            line = item()           # Classifies line as an item
            line.itemID = row[0]
            line.manuF = row[1]     # Places elements in required organizational structure in line
            line.itemT = row[2]
            line.dmg = row[3]
            full_table[line.itemID] = line  # Defines ItemID as key and adds line items to Full Table dictionary

    with open('PriceList.csv', 'r') as csvfile:     # Opens/reads price list and add missing elements to Full table dictionary
        list_reader = csv.reader(csvfile)
        for row in list_reader:                     # Adds any missing elements
            full_table[row[0]].itemP = row[1]

    with open('ServiceDatesList.csv','r') as csvfile:       # Opens/reads service list and adds missing elements
        list_reader = csv.reader(csvfile)
        date_format = '%m/%d/%Y'    # Format for datetime
        for row in list_reader:
            new_date = datetime.strptime(row[1], date_format).date()    # strips dates
            full_table[row[0]].serv = new_date                          # adds elements to table

    for i in full_table:    # creates a list of just manufacturers
        manuF_list.append(full_table[i].manuF)
    manuF_list.sort()       # sorts manufacturer list
    manuF = {}              # placed in dictionary

    for i in manuF_list:    # specified key to ensure unique values
        manuF[i] = i
    with open('FullInventory.csv', 'w', newline='') as csvfile:     # opens for writing
        line_writer = csv.writer(csvfile)
        for i in manuF:                                            # iterates and adds sorted elements to csv
            for j in full_table:
                if full_table[j].manuF == i:
                    line_writer.writerow([full_table[j].itemID, full_table[j].manuF,
                                            full_table[j].itemT, full_table[j].itemP,
                                            full_table[j].serv, full_table[j].dmg])

    for i in full_table:                        # creates list for item type
        item_type.append(full_table[i].itemT)
    item_type.sort()                            # sorts item types
    itemT = {}
    for i in item_type:                         # ensures unique values
        itemT[i] = i
    for i in full_table:                        # creates list for ItemID
        itemID_List.append(full_table[i].itemID)
    itemID_List.sort()                          # sorts item ID
    for i in itemT:
        with open(f'{i.capitalize()}Inventory.csv', 'w', newline='') as csvfile:  # opens capitalized variable named csv for writing
            line_writer = csv.writer(csvfile)
            for j in itemID_List:
                for k in full_table:
                    if full_table[k].itemID == j:   # iterates and writes needed elements to file
                        line_writer.writerow([full_table[k].itemID, full_table[k].manuF,
                                              full_table[k].itemP, full_table[k].serv,
                                              full_table[k].dmg])

    for i in full_table:                       # creation of date list table
        date_list.append(full_table[i].serv)
    date_list.sort()
    dates = {}
    for i in date_list:                        # ensure unique values
        dates[i] = i

    with open('PastServiceDateInventory.csv', 'w', newline='') as csvfile:  # opens past service csv for writing
        line_writer = csv.writer(csvfile)
        for i in dates:
            for j in full_table:
                if datetime.today().date() > full_table[j].serv and full_table[j].serv == i:    #compared today's date with the service due date
                    line_writer.writerow([full_table[j].itemID, full_table[j].manuF,
                                          full_table[j].itemT, full_table[j].itemP,
                                          full_table[j].serv, full_table[j].dmg],)

    for i in full_table:        # adds prices to list
        price_list.append(full_table[i].itemP)

    price_list.sort()           # sorts prices
    prices = {}
    for i in price_list:        # ensures unique price values
        prices[i] = i

    with open('DamagedInventory.csv','w', newline='') as csvfile:   # opens csv to write damaged inventory
        line_writer = csv.writer(csvfile)
        for i in prices:
            for j in full_table:
                if full_table[j].dmg == 'damaged' and full_table[j].itemP == i:     # checks if item flagged as damaged
                    line_writer.writerow([full_table[j].itemID, full_table[j].manuF,    # writes rows with relevant information
                                          full_table[j].itemT, full_table[j].itemP,
                                          full_table[j].serv])
    print('Reports generated.')







