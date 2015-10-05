def accruable(basic, allowance):
    print "The Basic: %d" % basic
    print "The Allowance: %d" %allowance
    
def deduction(tax, payee):
    print "The tax: %d" % tax
    print "The Paye: %d" %payee
    
print "We will like to calculate accruable"
my_basic= int(raw_input("Enter the value for Basic: "))
my_allowance =int(raw_input("Enter the value for Allowance: "))
accruable(my_basic, my_allowance)
salary = my_basic + my_allowance
print "The Salary is ", salary

print "We will to calculate deductions"
deduction(10000, 7500)
ded = 10000 + 7500
print "The deduction is ", ded

print "The salary for this month is calculated as follows"
net_pay = salary - ded
print net_pay
