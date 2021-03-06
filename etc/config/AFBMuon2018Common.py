#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
samplesDef = {
    'data'   : tnpSamples.AFBMuon['data2018'].clone(),
    'mcNom'  : tnpSamples.AFBMuon['mg2018'].clone(),
    'mcAlt'  : tnpSamples.AFBMuon['amc2018'].clone(),
    'tagSel' : tnpSamples.AFBMuon['mg2018'].clone(),
}

## some sample-based cuts... general cuts defined here after                           
## require mcTruth on MC DY samples and additional cuts                                
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()      
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()                  
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_'+samplesDef['tagSel'].name)
    samplesDef['tagSel'].set_cut('tag_pt > 32')                                                                            

    
## set MC weight, simple way (use tree weight)
weightName = 'pair_genWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
