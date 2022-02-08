
import addlipid

def init_options():
	# Lipid name, J0, APL, kc_bilayer, kg_bilayer, ka_bilayer, number of lipids, number of regions
	addlipid.addLipid( "GM3", 0.009259, 55.1, 20.0, 0, 0.4462, 186 )
	addlipid.addLipid( "CHOL", -0.033, 45.0, 20.0, 0, 1.0, 621 )
	addlipid.addLipid( "PAPC", -0.008130, 70.8, 20.0, 0, 0.3742, 109 )
	addlipid.addLipid( "PLPC", -0.003175, 65.9, 20.0, 0, 0.4030, 434 )
	addlipid.addLipid( "PSM", 0.009259, 55.1, 20.0, 0, 0.4462, 545 )
	addlipid.addLipid( "SAPE", -0.025, 69.3, 20.0, 0, 0.4318, 0 )
	addlipid.addLipid( "SAPS", -0.020, 69.3, 20.0, 0, 0.4318, 0 )
        # Region name, j_region, k_region, a_region
        # OUTER RIM NECK
        addlipid.addRegion( "1", 0.007714664, -0.000034, 55335.87698 ) 
        addlipid.addRegion( "2", 0.007294147, -0.000277, 17771.50762 )
        addlipid.addRegion( "3", 0.003312803, -0.000612, 11414.58396 ) 
