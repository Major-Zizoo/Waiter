def hotel(bill,tip):
    res = bill+tip
    print("Total amount to be paid is:",res,"$")

bill = int(input("Enter bill amount"))
tip=int(input("Enter tip amount"))
hotel(bill,tip)