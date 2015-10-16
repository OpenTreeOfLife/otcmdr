import sys
from subprocess import Popen

import general_utils

################ config #####################
javapre = "java -XX:+UseConcMarkSweepGC -Xmx32g -server -jar"
treemloc = "/home/josephwb/Work/OToL/treemachine/target/treemachine-0.0.1-SNAPSHOT-jar-with-dependencies.jar"
basedir = "/home/josephwb/Desktop/python_synth/"
otloc = basedir + "ott2.9draft12/" # where is ott?
otceteraloc = "/home/josephwb/Work/OToL/otcetera/supertree/" # supertree dir

synthottid = "93302" # cellular organisms
dbname = basedir + "Life_ottv2.9draft12.db"
synthtree = basedir + "Life_ottv2.9draft12_synth.tre"

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

#############################################

# the following will all be created (or overwritten)
subsettax = basedir + "subset_taxonomy-ott" + synthottid + ".tsv"
subsettaxtree = basedir + "subset_taxonomy-ott" + synthottid + ".tre"
studyloc = basedir + "Source_nexsons/" # only overwritten if download = true
trloc = basedir + "Processed_newicks/"
ranklist = basedir + "tree-ranking.txt"
subprobs = basedir + "subprobs"
processedsubprobs = basedir + "Processed_subprobs"

print "loading synthottid:",synthottid
print "loading " + str(len(studytreelist)) + " studies:", studytreelist


## phase 1: get data, initialize db, format newicks for otcetera decomposition
# get nexsons
download = True # set to False if you already have a set of nexsons and do not want fresher copies
if download:
    general_utils.get_all_studies_opentreeapi(studytreelist, studyloc)
else:
    print "\nAssuming all studies have already been downloaded to:", studyloc

# subset taxonomy
general_utils.subset_taxonomy(synthottid, otloc, subsettax)

# generate taxonomy newick (used by otcetera below)
general_utils.get_taxonomy_newick(treemloc, javapre, subsettax, subsettaxtree)

# initialize db
general_utils.init_taxonomy_db(treemloc, javapre, dbname, subsettax, otloc, basedir)

# process nexsons
general_utils.process_nexsons(studytreelist, studyloc, javapre, treemloc, dbname, trloc)

## phase 2: decomposition
general_utils.generate_tree_ranking(studytreelist, trloc, ranklist)
general_utils.set_symlinks(otceteraloc, ranklist, trloc, subsettaxtree, basedir)
general_utils.run_decomposition(basedir, otceteraloc, subprobs)

## phase 3: load, synthesis, extract
# put subprobs into format expected by treemachine
general_utils.format_subprobs(treemloc, javapre, subprobs, processedsubprobs)
general_utils.load_subprobs(treemloc, javapre, dbname, processedsubprobs, basedir)

# do it already!
general_utils.run_synth(treemloc, javapre, dbname, processedsubprobs, synthottid, basedir)
general_utils.extract_tree(treemloc, javapre, dbname, synthottid, basedir, synthtree)

## other commands: make archive, send to dev, etc. not necessary here