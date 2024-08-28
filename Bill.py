#  Write a Python program to calculate electricity bill based on following parameters.
unit = int(input("Enter The Your Units for calculate :"))
def bill():
    if(1<unit<=150):
        print("Your Bill is : ", unit * 2.40, "Bill/Unit .")
    elif(151<=unit<=300):
        total = unit-150
        price = total*3.00
        final_total = 150*2.40+price
        print("Your Bill is : ",final_total, "Bill/Unit .")
    elif(300<unit):
        total = unit-150
        total2 = unit-300
        total3 = total - total2
        price = total3*3.00
        price1 = total2*3.20
        price2 = 150*2.40
        final_total = price1+price+price2
        print("Your Bill is : ",final_total," Bill/Unit .")
    else:
        print("You Enter Wrong Value .")
    
bill()