####################################################################################################################
##
## This code will generate a consensus tree for a number of MrBayes output tree files
## As an example, you can pass it a list of output files for a number of genes, it will take in the MrBayes ouput
## of those files and generate a consensus tree for each gene from the MrBayes runs. 
## It is just a simple wraper around sumtrees.py. 
##
####################################################################################################################
import os
import glob


## this function accepts the parameters needed for sumtrees and loops through all tree sets constructing the consensus trees
def conTree(treeFiles, conThreshold, burnIn, outputPath, numProcs) :

	for treeSet in treeFiles :
		
		outTreeName = outputPath + "/" + treeSet[0].split(".run")[0].split("/")[1] + "_" + str(conThreshold*100).split(".0")[0] + "_con.tree"
		treeNames = " ".join(treeSet)
		print(outTreeName)
		cmd = "sumtrees.py -m %s --min-clade-freq=%s --burnin=%s --output-tree-filepath=%s %s" %(str(numProcs), conThreshold, burnIn, outTreeName, treeNames)
		os.system(cmd)


## this function just collects the names of all of the tree files as a list of lists
def collectTreeFiles(baseInputDir, numRuns) :

	allFiles = glob.glob(baseInputDir + "/*.t")
	
	uniqueFileNames = []
	for a in allFiles :
		name = a.split(".run")[0]
		uniqueFileNames.append(name)

	treeFiles = []
	for name in set(uniqueFileNames) :

		treeFileSet = []
		n = 1
		while n <= numRuns :
			treeFile = name + ".run" + str(n) + ".t"
			treeFileSet.append(treeFile)
			n += 1

		treeFiles.append(treeFileSet)

	return treeFiles


def main() :

	treeFiles = collectTreeFiles(baseInputDir, numRuns)
	
	conTree(treeFiles, conThreshold, burnIn, outputPath, numProcs)


if __name__ == "__main__":
    
	conThreshold = .50 # min. % support required (i.e. .50 for a majority rule consensus, .95 for a 95% con. tree)
	numRuns = 4 # num. of individual runs for each analyses. 
	baseInputDir = "" # main directory where .t files live
	outputPath = "contrees" # folder where you want consensus trees saved
	burnIn = 200 # num. of trees to discard before constructing consensus trees
	numProcs = 4 # use this if you are using the cluster or multi-core machine. it will speed it up. Number of processors to use.

	# start it all
	main()
