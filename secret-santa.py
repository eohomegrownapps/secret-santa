# -*- coding: utf-8 -*-
import random
import copy
import sendgrid

def secretsanta(families, email):
	pairings = []
	giftablelist = copy.deepcopy(families)
	gid = -1
	for group in families:
		gid += 1
		for person in group:
			gifts = giftable(giftablelist,gid)
			if gifts == False:
				return secretsanta(families, email)
			giftablelist = gifts[1]
			giftee = gifts[0]
			pairings.append([person,giftee])
	mail(pairings, email)
	print "Done"

def sendmail(giver, recipient, giveremail):
	sg = sendgrid.SendGridClient("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")
	message = sendgrid.Mail()

	message.add_to(giveremail)
	message.set_from("add email address here")
	message.set_subject("add email subject here")
	message.set_html("HTML formatted message here. Use vars giver and recipient (strings) in message.")

	sg.send(message)

def mail(pairings,email):
	print "Sending Mail..."
	for i in pairings:
		giveremail = email[i[0]]
		giver = i[0]
		recipient = i[1]
		sendmail(giver, recipient, giveremail)
	
def giftable(giftables,gid):
	giftuntouched = copy.deepcopy(giftables)
	giftables.pop(gid)
	giftlist = []
	for i in giftables:
		for j in i:
			giftlist.append(j)
	if len(giftlist)==0:
		return False
	else:
		index = random.randint(0,len(giftlist)-1)
		giftee = giftlist[index]
		for i in range(0,len(giftuntouched)):
			for j in range(0,len(giftuntouched[i])):
				if giftuntouched[i][j]==giftee:
					giftuntouched[i].pop(j)
					break
		return [giftee, list(giftuntouched)]
	
if __name__ == '__main__':
	#Format families as follows: 
	#Enclose the name of the person in quotation marks
	#Put names of people who are related (i.e. people who can't give gifts to each other) in a sublist together
	#Put it all in one big list
	#e.g. a,b,c are in a family
	#d,e are in a family
	families = [["a","b","c"],["d","e"]]
	#Put name to email in key-value dictionary like below.
	email = {"a":"a@mail.com","b":"b@mail.com","c":"c@mail.com","d":"d@mail.com","e":"e@mail.com",
	print "Choosing Pairings..."
	secretsanta(families, email)