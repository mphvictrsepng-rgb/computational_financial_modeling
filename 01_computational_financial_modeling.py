# ID_01 Simple Interest
def calculate_si(P, r, t):
    I = P*r*t
    return print(f'ID_1: R{I:.2f}')
calculate_si(4500, 0.07, 5)

# ID_02 Compound Interest
def compound_ann(P, i, n):
    A = P*(1+i)**n
    return print(f'ID_2: R{A:.2f}')                     
compound_ann(12000, 0.065, 8)          #This calculation doesn't give me the exact decimal figures, I'll try sorting it because I understand that numbers need to be accurate in finance.

# ID_03 Hire Purchase   
def hp_monthly(P, depo, r, t):
    A = (P*(1+ r*t)) / 36
    return print(f'ID_3: R{A:.2f}')
hp_monthly(18700, 0.15, 0.11, 3)  #also not giving accurate decimals.

# The above is my first attempt where I calculated the principal balance separately (I didn't include that part in my code above)
# Here is anothere code where I calculate the principle balance included in the code, but it's a longer approach, and looks a bit messy. And still, I can't get the exact decimal figure (.03)

# A = ?
P = 22000
deposit = 22000*0.15
P_bal = P - deposit       # to determine the principle balance.
r = 0.11
t = 3
A = P_bal*(1 + r * t) // 36
print(f'ID_3: R{A:.2f}')

# ID_04 Inflation Analysis
def inflation(P, i, n):
    A = P*(1 + i)**n
    return print(f'ID_4: R{A:.2f}')
inflation(1550, 0.055, 12)              #I still get inaccurate decimal numbers, I'll google how to round up, or maybe I could've missed something.

# ID_05 Reducing Depreciation
def depreciate(P, i, n):
    A = P*(1 - i)**n
    return print(f'ID_5: R{A:.2f}')
depreciate(480000, 0.18, 6)

# ID_06 Quarterly Compounding
def comp_q(P, r, t):                # I was thinking of doing this one the same way I did ID_3, but it's going to look like a longer code.
    A = P*(1 + r/4)**(4 * t)        # I also preder to leave space in between my parameters, makes it look better and it's easy for the eyes to track
    return print(f'ID_6: R{A:.2f}')
comp_q(95000, 0.09, 4)

# ID_07 Loan Accrual
def loan_acc(P, r, t):
    I = (P*(1 + r/12)**12) - P
    return print(f'ID_7: R{I:.2f}')
loan_acc(30000, 0.14, 1)            

# ID_08 Capital Doubling Time
def double_time(I, P, r):
    t = I//(P * r)                             # P and I must be equal, accroding to google. And I used // since I'm working with a years, which need to be whole numbers, unless I start comsidering months as well.
    return print(f'ID_8: {t:.0f} years')
double_time(15000, 15000, 0.125)

# ID_09 Effective Annual Rate
def get_ear(nominal, m):
    Effective_ann = (1 + nominal/m)**m - 1
    return print(f'ID_9: {Effective_ann:.2f}%')
get_ear(0.132, 12)                                   # I'm wrong here

# ID_10 Fund Growth
def zaio_growth(P, r, t):
    A = P*(1 + r/2)**(2*t)
    return print(f'ID_10: R{A:.2f}')
zaio_growth(2500000, 0.15, 10)

# Another attempt
"""
# A = ?
P = 2500000
r = 0.15
t = 10
x = r/2
z = 2 * t

A = P*(1 + x)**z
print(f'ID_10: R{A:.2f}')       # Still getting inaccurate numbers.

"""
