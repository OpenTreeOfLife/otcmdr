import sys

# config file, specifying where tools can be found, etc.
from conf import *

from subprocess import Popen
import general_utils

###
# NOTE: this replicates the PNAS synthesis analysis. Possibly with an updated taxonomy.
###


################ analysis settings #####################

# where should all results go? this needs to exist before analysis
basedir = "/home/josephwb/Desktop/python_synth/Life/"
# what is the ott id of the root node of the clade of interest?
synthottid = "93302" # cellular organisms
# name of DB
dbname = basedir + "Life_ottv2.9draft12_21Oct2015_BTTF-day.db"
# name of synth tree newick file
synthtree = basedir + "Life_ottv2.9draft12_synth_21Oct2015_BTTF-day.tre"
# where are ranked study lists located? assume here to use dir Study_lists in this repo
listdir = "Study_lists"
sys.path.insert(0, listdir)

## ranked study lists:
from plants import studytreelist as plantslist
from metazoa import studytreelist as metalist
from fungi import studytreelist as fungilist
from safe_microbes import studytreelist as microbelist

studytreelist = []
studytreelist.extend(plantslist)
studytreelist.extend(metalist)
studytreelist.extend(fungilist)
studytreelist.extend(microbelist)

########################################################

# the following will all be created (or overwritten). probably just leave as is
subsettax = basedir + "subset_taxonomy-ott" + synthottid + ".tsv"
subsettaxtree = basedir + "subset_taxonomy-ott" + synthottid + ".tre"
studyloc = basedir + "Source_nexsons/" # will not be overwritten if it exists
trloc = basedir + "Processed_newicks/"
subprobs = basedir + "subprobs"

########################################################

## here we go...

print "loading synthottid:",synthottid
print "loading " + str(len(studytreelist)) + " studies:", studytreelist


## phase 1: get data, initialize db, format newicks for otcetera decomposition
# get nexsons
download = False # set to False if you already have a set of nexsons and do not want fresher copies
if download:
    general_utils.get_all_studies_opentreeapi(studytreelist, studyloc)
else:
    print "\nAssuming all studies have already been downloaded to:", studyloc

## phase 1: prepare db, as well as files for decomposition
general_utils.prepare_for_decomposition(javapre, treemloc, basedir, dbname, otloc, synthottid, subsettax, subsettaxtree,
    studytreelist, studyloc, trloc)

## phase 2: decomposition
general_utils.perform_decomposition(basedir, studytreelist, trloc, otceteraloc, subsettaxtree, subprobs)

## phase 3: load, synthesis, extract
general_utils.run_synthesis(javapre, treemloc, basedir, dbname, synthottid, subprobs, synthtree)

