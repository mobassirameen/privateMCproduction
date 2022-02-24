cmsrel CMSSW_10_2_9
cd CMSSW_10_2_9/src
cmsenv


git clone git@github.com:mobassirameen/privateMCproduction.git
scram b -j 8

To run the miniAOD production, modify the settings in crab_TOT_prod_fromLHE.py to your needs for the number of events and storage on the T2 where you have writing rights.

cd $CMSSW_BASE/src/privateMCproduction
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
crab submit crab_TOT_prod_fromLHE.py

at this point a CRAB_PROJ_DIR should be created.

check the status submission with : crab status CRAB_PROJ_DIR and resubmit : crab resubmit CRAB_PROJ_DIR
