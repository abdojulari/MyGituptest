test = raw_input("Enter a number:")
try:
  test = int(test)
except:
  print "Invalid entry."
  quit()
result = test * 2
print result

