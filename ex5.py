from sys import argv

user_name = argv
prompt = '> '

print "Hi, my name is %s." %(user_name)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives =raw_input(prompt)

print """
Alright, so you said %r about liking me. You live in %r. not sure where that is. And you havea %r computer. Nice """ % (likes, lives, computer)
