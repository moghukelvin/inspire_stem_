# Program to calculate hire purchase
# Date : 21/2/2024
# Name : kelvin moghul

cp = float(input("enter cost price"))
deposit1 = float(input("enter deposit percentage"))
monthly_installment = float(input("enter installment periods in months"))
installments = float(input("enter amount paid in each installment"))
deposit2 = deposit1 *0.001
downpayment =deposit2 * cp
hirepurchase = downpayment + installments * monthly_installment

print(hirepurchase)

additionalprice1 = hirepurchase - cp
additionalprice2 = additionalprice1 * 100/cp

print(additionalprice1 ,"is the additional price he is paying")
print(additionalprice2 ,"is the percentage of the additional price he is paying")