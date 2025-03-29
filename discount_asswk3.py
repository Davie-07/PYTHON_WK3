def calculate_discount(price, discount_percent):

    if discount_percent >= 20:                              # specified condition of 20% to be checked
     discount_amount = (discount_percent / 100) * price    #calculates discounts
     final_price = price - discount_amount                 # then calculates the final amount after discount has been applied
 
    else :
       final_price = price                         # if the condition is not met, then the else condition is executed

    return final_price

item_price = float(input("Enter the original price of the item: "))   #prompts for user input for item price
discount_percent = float(input("Enter the discount percent: "))      #Specifies what percent discount is to be applied

final_price = calculate_discount(item_price, discount_percent)   
print("Item amount after discount is $", final_price)         #prints the final result to the user

