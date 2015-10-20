(Legacy) Python Synthesis Pipeline
---------------
Yes, you, too, can run synthesis. This pipeline is slated for deprecation, but is 
put here for the time being in case it might be of use.

### What You Need
To carry this out, you will need the following:

**this repo** Really, just the scripts `synth_procedure.py` and `general_utils.py`. 
To do this, get the branch `python_synthesis_pipeline`:

    git clone git@github.com:OpenTreeOfLife/otcmdr.git
    cd otcmdr
    git checkout python_synthesis

**treemachine** Found [here](https://github.com/OpenTreeOfLife/treemachine). This'll do ya:

    git clone git@github.com:OpenTreeOfLife/treemachine.git
    cd treemachine
    ./mvn_cmdline.sh

**otcetera** Found [here](https://github.com/OpenTreeOfLife/otcetera). The `otcetera` README 
gives instructions on how to install and test.

**Ranked study list(s)** Python lists (named `studytreelist`) with entires of the form
 `PREFIX_STUDYID_TREEID`. For example:
```python
studytreelist=[
               "ot_119_1",     # Cracidae. Pereira et al. 2002. Syst. Biol.
               "ot_118_1",     # Megapodidae. Harris et al. 2014. J. Biogeo.
               "pg_2577_5980", # Galliformes. Wang et al. 2013. PLoS ONE
               "pg_2866_6656", # Anseriformes. Gonzalez et al. 2009. J. Zool.
               "pg_2860_6646", # Anatidae. Fulton et al. 2012. Proc. Roy. Soc.
               "ot_116_1",     # Strigiformes. Hugall and Stuart-Fox. 2012. Nature # can fill this out more
               "ot_121_7",     # Cuculiformes. Payne. 2005. Book
               "pg_2876_6670", # Tinamidae. Bertelli et al. 2004. Orn. Neotrop.
               "pg_2926_6757", # Palaeognaths. Mitchell et al. 2014. Science
               ...
               ]
```
See example lists included.

**ott** The OpenTree taxonomy, available [here](http://files.opentreeoflife.org/ott/).

**ottid of focal clade** Determines how to subset the taxonomy, as well as the root of 
the graph. Some popular ones: 805080 = life; 691846 = Metazoa; 81461 = Aves; 244265 = Mammalia;
229562 = Tetrapoda; Amniota = 229560; Archosauria = 335588; 304358 = Eukaryota; Decapoda = 169205;
93302 = cellular organisms; 996421 = Archaea; 225495 = cyanobacteria.

### How to run
The easiest way to perform the analyses is to mirror the Asterales example. The file `conf.py` contains 
some configuration settings that are the same for any analysis, specifically:

1. The location of treemachine.
2. The location of otcetera (specifically the `supertree` directory).
3. The location of ott.

Edit `conf.py` to reflect your own machine.

The file `run_asterales_synthesis.py` contains analysis-specific settings:

1. The location of your 'base directory' where you will store results. This directory must already exist.
2. The ottid of the root node of the clade of interest.
3. The python ranked tree list(s) of which sources to use.
4. Some other file names that you do not need to alter.

Set these, er, settings, and run. Since things can take a while, it might be best to run 
this under screen:

    screen
    python run_asterales_synthesis.py

But the Asterales analysis is quick enough that screen is not necessary.

And that is it. 

**TODO:** Write logs for important/verbose steps (load, synth, etc.)
