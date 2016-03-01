###########################################################################################################
##	RandTree version 0.2.5
##	Lyndon Coghill - 2013
##	lcoghill@uno.edu
##	This script is released under GPL version 3. Use it however you want, but its at your own risk.
###########################################################################################################

###########################################################################################################
##	RandTree is a script designed to accept a BEAST generated .TREES file as input.
##
##	It will then parse that file, and retreive a user-specified number of random trees from that file.
##	RandTree will discard a user specified number of trees as a burn-in value.
##	The sampling occurs without replacement, meaning that as a random tree is chosen it is removed from
##	the original tree file so it is impossible to randomly choose the same tree twice. In future versions
## 	I hope to add an option that will let you sample with replacement as well.
##
##	Those trees are then saved in the file "output" file generated in the same directory. 
##
##	The output file is in plain text format with just the trees. In future versions I will attempt to
##	add in the choice to save as plain text or as a new BEAST formatted .trees file.
###########################################################################################################
from sys import stdout
from time import sleep
import os
import re
import random
os.system('cls')
os.system('clear')
print ("		\n")
print ("		RandTree v0.2.5, 2013")
print ("			by")
print ("		 Lyndon M. Coghill")
print ("			 &")
print ("		Trent Santonastaso")
print ("		\n")
print ("	     lcoghill@fieldmuseum.org")
print ("\n\n\n\n")
file_name = input('.TREES File Name: ')# assigns the variable <file_name> to whatever the user enters - this is facilitated by the function <input> and prompted by the text in parentheses
print ("Checking file compatibility. If the tree file is large, this may take a little time...")
print ("\n")
print ("Scanning Line:")
splitTaxaString = ""
taxaNumber = 0
nonTreeLines = 0
totalLines = 0
linecount = 0
time = 0
trees = 0
treesleft = 0
treecount = 1
randomtrees = 0
burnin = 0
percentage = 0
kepttrees = 0
datafile = open(file_name)#we are creating a new variable called <datafile> - by simply evoking its name, we call it into existence, and give it the same contents as the file <file_name> which we open and pass to datafile
for line in datafile: #we are setting up a little module here for every line in this new file, 1 line at a time, we will...
	totalLines = totalLines + 1 # add a line to our tally of the total number of lines.  the variable <totalLines> was created early in the program when many workhorse variables were defined. totalLines started at 0 and after every line we will be keeping count
	stdout.write("\r%d" % totalLines)
	stdout.flush()
	#sleep(0.25)
datafile.close ()


datafile = open(file_name) #we are creating and opening a new variable called datafile and passing the data from the variable called file_name
for line in datafile: #we are opening a module where in for each line in the variable <datafile> we will...
	if "Dimensions ntax=" in line:# look for the character string "Dimensions ntax=", if that characterstring is there then...
		splitTaxaString = line.split("Dimensions ntax=") 
		str1 = ''.join(splitTaxaString)
		str1 = re.sub('[;\n\t]', '', str1)
		taxaNumber = int(str1)
		nonTreeLines = (taxaNumber * 2) + 13

datafile.close()
		
datafile = open(file_name) #file is a function from 2.6 that means the same thing as open in 3.0
for line in datafile:
	if "tree STATE_" in line:
		linecount = linecount + 1

datafile.close()

trees = linecount - 1
## Some heads up to the user
print ("\n")
print ("The file you have chosen contains: ")
print ("\n")
print (totalLines,'total lines with',trees,'individual trees.')	
print ("\n\n")
print ("1. This file is correct, please proceed.")
print ("2. This file is not correct, please cancel the process.")

proceed = input('Proceed?:')
print ("Generating All Trees file...\n")

############################### ACTUAL PROGRAM CODE HERE###############################

if proceed == "1":
### Pull all trees out of original file and place in output tree file
	datafile = open(file_name)
	for line in datafile:
		#print ("Gathering all trees:"
		if "tree STATE_" in line:
			f = open('alltrees.randtree','a')
			f.write(line) # python will convert \n to os.linesep

		#else:
		#	print ("No Line Matches"
	f.close()

### Toss a number of trees equal to the desired burn in value in a percentage. (IE: 10,000 trees with a burnin of 10% means to toss the first 1000 trees and place the rest in the new tree file


percentage = input('Burnin value (% of total trees):')#enter burnin as % of total trees 
percentage = float(percentage) #float is a function that converts the value of a variable to a floating point number - this allows python to use decimals it converts integers to decimals
burnin = percentage / 100 # now percentage as a variable is converted to a decimal number in the float operation and here we divide it by 100 effectively giving it 2 decimal points
burnin = burnin * trees # here burnin has been defined earlier, and we have given it the value of the % trees input divided by 100.  Now we are multiplying that by trees variable
burnin =float(burnin) # here we are converting the variable burnin back to a float.  usually multiplying int by float equals float but Lyndon thinks that doesn't work out so we convert burnin to float again
print (burnin," trees will be discarded.\n") #this line prints the variable burnin plus the bit in quates
f = open('alltrees.randtree') #f is a new variable that we're using to point to the contents of the specific file -alltrees.randtree- in this case we are opening the file with the open function and assigning that open file to the variable f
fo = open('burnin.randtree','w') #same thing here for fo in this case there is a ,w which means read write as opposed to the f variable the file is read only

line_count = 0 # here we are defining 2 more variables
savetree = 1
print ("\nSaving Tree: ") # now we print on the screen that we are saving the trees
while line_count <= trees: # as long as the line count is less than or equal to the trees variable which is 30,000 in this case if you remember do the following
	line = f.readline() # line is a variable which is telling the compy to goto the f address where our 30,000 trees are and perform the function readline which tells the compy to read the first line the empty parenthetical is telling it it's a basic function
	if line_count > burnin: # if the line count is less than the user defined burnin, the rest of this object will not take effect
			stdout.write("\r%d" % savetree) #this code prints the value of savetree on the same line over and over
			stdout.flush()
			fo.write(line) #this is using the write function to write our tree to the fo file it will only do this if the count is greater than burnin
			savetree = savetree + 1 #savetree is a variable that keeps track of the number of trees we are putting into the file
	line_count = line_count + 1 #this is a tabulation that adds one to our variable line_count
f.close()# closes the f file - very important to close the files we opened
fo.close()# same as above


### Ask how many random trees the user would like to pull out
randomtrees = input('\nHow Many Random Trees Do You Want To Retreive?:')
randomtrees = int(randomtrees) ### Generate a random number between 1 and total number of trees remaining in the tree file
treesleft = int(trees - burnin) #set number of trees remaining in alltrees file to the number of trees present originally. a starting point.
if randomtrees > 0:
		while treecount <= randomtrees:
			randomseed = random.randint(1, treesleft)
			alltreesfile = open('burnin.randtree') #in this case we are assigning the alltreesfile variable to the burnin variable because we are using the truncated burnin or burnout trees
			lines= alltreesfile.readlines()
			alltreesfile.close()
			f = open("burnin.randtree","w")
			for line in lines:
				if line == lines[randomseed]: ### Write the file back without the random tree
					outputfile = open('output.randtree','a') ### Put that tree in a new file
					outputfile.write(lines[randomseed])
					outputfile.close()
				else:
					f.write(line) #if the line doesn't match the random seed value, print it back to the original file.
					
			f.close()
			print ("Random Tree", treecount,"/",randomtrees,"saved. This was tree",randomseed,"from the original BEAST analysis.")
			treecount = treecount + 1
			treesleft = treesleft - 1
	
	
	##NEXUS FORMAT CODE HERE - COPY ATTRIBUTES FROM ORIGINAL FILE AND PLACE INTO NEW FILE
		print ("\nNow formating output file to Nexus format...")
		print ("\n")
		line_state = 0 #we are setting an new variable 'line_state' and setting it to 0 - 0 is a variable, and we can call it anything...like 'zero'
		nonTreeLines = nonTreeLines - 1
		original_file = open(file_name) # opens the original tree file in read/write format
		output_file = open('output.trees', 'a') #a means open the file with the condition of append -as opposed to read only or read/write
		trees_file=open('output.randtree')
		while line_state <= nonTreeLines:# != means does not equal. so this line says while the line
			nexus_line = original_file.readline()#this is a new variable
			if "tree STATE_" in nexus_line: #we are looking for the specific text in each line <tree STATE> because when we find that we will perform a function
				line_state = line_state + 1
			else:
				output_file.write(nexus_line)
				line_state = line_state + 1

		
		original_file.close()
		
		for line in trees_file:
			output_file.write(line)
		
		trees_file.close()
		
		output_file.write("End;")
		output_file.close()

		
		#### STILL NEED TO DO THIS!!!!!
		print ("Now removing temporary files to clear disk space...\n")
		
		
		print ("Process complete.")
		print ("RandTree will now exit.")
elif randomtrees == 0:
		print ("I'm sorry. You must select more than 0 random trees. Please try again.")
		print ("RandTree will now exit.")




### Print status on progress
### Print final status message and exit program


##### EXIT PROGRAM IF USER CHOOSES NOT TO proceed
else:
	print ("\n")
	print ("Thank you, please try again. \n")
	print ("RandTree will now exit.\n")
	print ("\n")



