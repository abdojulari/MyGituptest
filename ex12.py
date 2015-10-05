def accruable(basic, allowance):
    print "The Basic: %d" % basic
    print "The Allowance: %d" %allowance
    
def deduction(tax, payee):
    print "The tax: %d" % tax
    print "The Paye: %d" %payee
    
print "We will like to calculate accruable"
accruable(45000, 50100)
salary = 45000 + 50100
print "The Salary is ", salary

print "We will to calculate deductions"
deduction(10000, 7500)
ded = 10000 + 7500
print "The deduction is ", ded

print "The salary for this month is calculated as follows"
net_pay = salary - ded
print net_pay
