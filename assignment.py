import random

CreditScore = random.randrange(400,850)

#Enter the price of the House you wish to Buy
price = int(input("Enter the house price: "))

#Enter the first name
first_name = input("Enter the first name: ")

#Enter the last name
last_name = input("Enter the last name: ")

fullname = first_name + " " + last_name

#Enter the email
email = input("Enter the email address: ")

#Enter the phone number
phone = input("Enter the phone number: ")

#Enter the mailing
address = input("Enter the mailing address: ")

#Enter the mailing
city = input("Enter the City: ")

#Enter the mailing
zipcode = input("Enter the zip code: ")
downPayment = 0

if CreditScore >= 780:
    status = ("Excellent Credit")
    #print("Zero Down Payment")
    downPayment = (0.10 * price)
    #print ('DownPayment: ' + downPayment)

elif CreditScore >= 740:
    status = ("Very Good")
    downPayment = (0.11 * price)
   # print ('DownPayment: ' + downPayment)

elif CreditScore >= 720:
    status = ("Above Average")
    downPayment = (0.13 * price)
    #print ('DownPayment: ' + downPayment)

elif CreditScore >= 680:
    status = ("Average")
    downPayment = (0.16 * price)
    #print ('DownPayment: ' + downPayment)

elif CreditScore >= 620:
    status = ("Below Average")
    downPayment = (0.18 * price)
    #print ('DownPayment: ' + downPayment)

elif CreditScore >= 580:
    status = ("Poor Credit Score")
    downPayment = (0.20 * price)
  #print ('DownPayment: ' + downPayment)

elif CreditScore < 520:
    status = ("Poor Credit Score")
    downPayment = (0.25 * price)
    #print ('DownPayment: ' + downPayment)
print('Fullname:' + fullname)
print('Email:' + email)
print('Physical Address:' + address )
print('City:' + city)
print('House Price:' + str(price))
print('Down Payment:' + str(downPayment))
print('Credit Score:' + str(CreditScore))
print('Credit Status:' + status)

print("CONGRATULATIONS - YOU NOW OWN YOUR DREAM HOUSE- {}".format(fullname))