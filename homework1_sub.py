'''
Created on Mar 23, 2018

@author: Anthony
exercises for edX that is PyLint clean
'''

# test git


def remaining_balance(periodic_rate, amount, payment, months):
    '''
    This is the f(x) function used by the bounds and bisection search

    Parameters: periodic_rate is APR / 12
                amount = total loan balance
                payment = amount paid each month
                months = length of time
    '''
    for i in range(1, months + 1):
        running_balance = amount
        if running_balance > 0:
            monthly_interest = running_balance * periodic_rate
        else:
            monthly_interest = 0
        running_balance = running_balance + monthly_interest - payment
        print(i, amount, monthly_interest, payment - monthly_interest, running_balance)
        amount = running_balance
    return amount


balance = 999999
annualInterestRate = 0.18
NMAX = 500
TOLERANCE = .01


def main():
    '''
    Main function that implements bounds and bisection search
    '''

    iterations = 1
    monthly_rate = annualInterestRate / 12
    payment_lower_bound = balance / 12
    payment_upper_bound = (balance * (1 + monthly_rate) * 12) / 12
    solution_found = False
    while iterations <= NMAX:
        payment_test = (payment_lower_bound + payment_upper_bound) / 2  # new midpoint
        print(iterations, payment_lower_bound, payment_upper_bound, payment_test)
        test_payment_remaining = remaining_balance(monthly_rate, balance, payment_test, 12)
        # lower_bound_remaining = remaining_balance(monthly_rate,BALANCE,payment_lower_bound,12)
        if(abs(test_payment_remaining) < TOLERANCE
                or (payment_upper_bound - payment_lower_bound) / 2 < TOLERANCE):
            solution_found = True
            print("solution is payment of:", payment_test, " on iteration: ", iterations)
            print("Lowest Payment: %.2f" % payment_test)
            break
        else:
            iterations = iterations + 1
            if test_payment_remaining < 0:
                payment_upper_bound = payment_test
            else:
                payment_lower_bound = payment_test
    if solution_found is False:
        print("No solution found, maximum iterations exceeded")


if __name__ == "__main__":
    main()
