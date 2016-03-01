from Bio import AlignIO
import glob


##########################################################################################
##   Converts a directory of sequence alignment files into another file format.
##
##
##   Requirements: 
##   1. Python 2.7
##   2. Biopython
##
##########################################################################################

outputDir = '' ## where output alignments should be located.
inputDir = '' ## where input alignments are located.
outputFormat = 'nexus' ## format of output alignments
inputFormat = 'fasta' ## format on input alignments
outputSuffix = '.nex' ## ending for each output file



alignmentFiles = glob.glob(inputDir + "*")
for f in alignmentFiles:
    align = AlignIO.read(f, inputFormat)
    print "Converting file %s..." % f
    AlignIO.convert(f, inputFormat, outputDir + file_name[:-3] + outputSuffix, outputFormat, alphabet=None)