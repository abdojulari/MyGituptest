def staff_info (name,sex,level, depart,edu):
    print ("Your name %s, your sex %s, your cadre %s, your department %s, your qualification %s ") %(name, sex, level, depart,edu)

def salary(basic, allow):
    print ("Your basic salary %d, your allow %d") %(basic,allow)
    return basic + allow
def deduction(tax, payee, rent):
    print ("Your tax %d, your payee %d, your rent %d") %(tax,payee,rent)
    return tax + payee + rent
 
print "EMPLOYEE'S DETALS"
my_name= raw_input("Please enter your name: ")
my_sex= raw_input("Please enter your sex: ")
my_level= raw_input("Please enter your level: ")
my_depart= raw_input("Please enter your department: ")
my_edu= raw_input("Please enter your qualification: ")

staff_info(my_name, my_sex,my_level,my_depart,my_edu)

print "SALARY INFORMATION"
print "Monthly Gross"
basics = float(raw_input("Enter your basic salary: "))
allowance= float(raw_input("Enter your allowance: "))
basic_salary = basics + allowance

print "Salary: ", basic_salary
salary(basics, allowance)

print "DEDUCTION"
taxs = float(raw_input("Please enter your tax: "))
pay = float(raw_input("Please enter your PAYEE: "))
rents = float(raw_input("Please enter your rent: "))

deduction(taxs,pay,rents)
ded = taxs + pay + rents
print "The deduction", ded
net = salary - ded 
print net

 

