#from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'miniAOD_BcToBsPi_v1'
config.General.workArea = 'crab_privateMC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500

config.JobType.psetName = 'miniAOD_crab_fake_cfg.py'


#config.JobType.inputFiles = ['run_crab.sh', 'BPH-RunIIFall18GS-BcToBsPi_cfg.py', 'DR_step1_crab_cfg.py', 'DR_step2_crab_cfg.py', 'pu.py' , 'miniAOD_crab_fake_cfg.py', 'miniAOD_crab_cfg.py']
config.JobType.inputFiles = ['run_crab_TOT_prod_fromLHE.sh', 'LHE_crab_cfg.py', 'BPH-RunIIFall18GS-BcToBsPi_cfg.py', 'DR_step1_crab_cfg_ac.py', 'DR_step2_crab_cfg.py', 'pu.py' , 'miniAOD_crab_fake_cfg.py', 'miniAOD_crab_cfg.py']

config.JobType.scriptExe= 'run_crab_TOT_prod_fromLHE.sh'
config.JobType.numCores=1

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000 #500
#config.JobType.eventsPerLumi = 50000
config.Data.totalUnits = 3500000 #200000
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/moameen/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'BcToBsPi_JPsiPhi_MuMu_KK_13TeV_pythia8'
config.Data.outputDatasetTag ='BcToBsPi-MINIAODSIM'

#config.Site.storageSite = 'T2_CH_CSCS'
config.Site.storageSite = 'T3_CH_CERNBOX'
