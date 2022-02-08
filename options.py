
import addlipid

def init_options():
	# Lipid name, c0, APL, kc_bilayer, kg_bilayer, ka_bilayer, number of lipids, number of regions
        # ka... 250.*6.022E23/(1000*4184*1E20) = 0.3598
        # ka... multiply by 0.0014392925430210324
        # https://reader.elsevier.com/reader/sd/pii/S0009308415300190?token=2C7326623784F813BB56969E335502DAAA96E9EB6DF708AE08C4F4E5DC2808BDA68F4D226B0E25AA3F3F7CFA576E1CF8&originRegion=us-east-1&originCreation=20210806220728
        # small pore (out) is = 148, 521, 107, 388, 464, 0, 0
        # small pore (in) is = 0, 409, 0, 227, 0, 426, 291
        # GM3 is using PSM values
	addlipid.addLipid( "GM3", 0.009259, 55.1, 20.0, 0, 0.4462, 186 )
        # CHOL is using guesses
	addlipid.addLipid( "CHOL", -0.033, 45.0, 20.0, 0, 1.0, 621 )
        # PAPC is using PDPC values
	addlipid.addLipid( "PAPC", -0.008130, 70.8, 20.0, 0, 0.3742, 109 )
        # PLPC is using POPC values
	addlipid.addLipid( "PLPC", -0.003175, 65.9, 20.0, 0, 0.4030, 434 )
        # PSM is PSM
	addlipid.addLipid( "PSM", 0.009259, 55.1, 20.0, 0, 0.4462, 545 )
        # SAPE is using SDPE values
	addlipid.addLipid( "SAPE", -0.025, 69.3, 20.0, 0, 0.4318, 0 )
        # SAPS is using guesses
	addlipid.addLipid( "SAPS", -0.020, 69.3, 20.0, 0, 0.4318, 0 )
        # Region name, c_region, a_region
        # OUTER RIM NECK
        addlipid.addRegion( "1", 0.007714664, -0.000034, 55335.87698 ) 
        addlipid.addRegion( "2", 0.007294147, -0.000277, 17771.50762 )
        addlipid.addRegion( "3", 0.003312803, -0.000612, 11414.58396 ) 
