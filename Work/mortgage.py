# mortgage.py
#
# Exercise 1.7


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0



current_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    current_month +=1 
    actual_payment = payment
    if extra_payment_start_month <= current_month <= extra_payment_end_month: 
        actual_payment += extra_payment
    principal = principal * (1+rate/12) - actual_payment
    total_paid = total_paid + actual_payment

    if principal < 0: 
        total_paid += abs(principal)
        principal = 0
        print(current_month, total_paid, principal)
        break

    print(current_month, total_paid, principal)


print('Total paid', total_paid, 'Months required: ', current_month)