#This program simulates a 6/49 lotto, notifying wins for 5/6 (5% payout) and 6/6 (Jackpot) payouts. 
#Credit to the office pool for the idea -- I'm still not buying any lottery tickets. No bonus numbers

import random
random.seed()
numbers = [i for i in range(1, 49)]

#Winning ticket number, no different than the quickpick function currently, may change to include chooses 6 + 1 Bonus number
def pickWinner():
	return sorted(random.sample(numbers, 6))

#Quickpick Ticket generator
def quickPick():
	return sorted(random.sample(numbers, 6))

#Generates pre-defined number of tickets
def generateTickets(num):
	tickets = {}
	tickets_per_week = num		#unecessary
	for i in range(1, tickets_per_week+1):
		tickets[i] = quickPick()
	return tickets	

#Calculates total ticket cost
def costOfTickets(cost, weeks, tickets_per_week):
	return cost * tickets_per_week * weeks

#Unused function that prints a set of tickets	
def printTickets(tickets):
	for i in tickets:
		print "Ticket " +  str(i) + " : " + str(tickets[i])
	return None

#Reads an set of tickets, the week number, and the winning ticket. Checks if a ticket has >=5 matching numbers or is a winner prints some message and returns a jackpot winner boolean. 	
def compareTickets(tickets, winner, week):
	jackpot  = False
	for i in tickets:
		NumCount = 0		#number of wining numbers in each ticket, actually, this doesn't need to exist. just do len(winningNumbers)
		winningNumbers = []	#array that holds the numbers
		for j in tickets[i]:
			if j in winner:
				NumCount += 1
				winningNumbers.append(j)
		# if NumCount > 0:
			# print "Ticket " + str(i) + " has " + str(NumCount) + " winning numbers: " + str(winningNumbers)
		if NumCount >= 5:
			print "Ticket " + str(i) + " in week " + str(week) + " has " + str(NumCount) + " winning numbers: " + str(winningNumbers)
		if NumCount == 6:
			print "Ticket " + str(i) + " has won the lottery in week " + str(week) + "(" + str(week/52) + " years since playing)"
			jackpot = True
	if jackpot == False:
		return 0
	else:
		return 1

#main program, playing the lottery each week until limit is reached
def playLottery(weeks, tickets_per_week, cost):
	tickets = generateTickets(tickets_per_week)
	winner = []
	week_limit = weeks
	ticket_price = cost
	jackpot = 0
	for i in range(1, week_limit+1):
		week = i
		tickets = generateTickets(tickets_per_week) #generates new tickets per week
		winner = pickWinner()
		#print "The winning numbers in week " + str(week) + " are: " + str(winner)
		if compareTickets(tickets, winner, week):
			jackpot += 1
	print "You paid $" + str(costOfTickets(ticket_price, weeks, tickets_per_week)) + " for " +str(weeks*tickets_per_week) + " tickets over " + str(float(weeks)) + " weeks(" + str(float(weeks/52)) + " years) and won the jackpot " + str(jackpot) + " times"
	return None

#Define number of weeks to play, cost of tickets, and number of tickets per week
weeks = 52000*2
tickets_per_week = 20
cost = 3

playLottery(weeks, tickets_per_week, cost)