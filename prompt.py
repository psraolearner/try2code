from sys import argv
script ,user_name =argv
prompt = "Ans:"
print "Hi %s,I'm the %s script." %(user_name, script)
print "I'd like to ask you few questions."
print "Do you like me %s?" %user_name
likes = raw_input( prompt)
print "Where do you live %s?" %user_name
lives = raw_input( prompt)
print "What is your lovable pet %s?" %user_name
loves  = raw_input( prompt)
print "What kind of computer do you have?"
computer = raw_input( prompt)
print """
Alright, so you said %s about liking me.
You live in %s.Not sure where that is.
And your lovable pet is %s.That's my favorite too.
And you have a %s computer.That's very nice.
""" % (likes,lives,loves, computer)
