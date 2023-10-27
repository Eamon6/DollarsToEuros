convert = input("Would you like to convert dollars to euros? ")
while convert == "yes":
    dollars = float(input("Enter dollar amount to be converted: $"))
    euros = dollars * 0.94540
    print("In euros you would have €" + str(euros))
    convert = input("Would you like to convert dollars to euros? ")

    