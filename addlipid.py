
n_liptype = 0
c0        = []
apl       = []
kc        = []
kg        = []
ka        = []
nlipids   = []
name      = []
def addLipid( lipidName, c0in, APLin, kcin, kgin, kain, nlip ):
	global n_liptype, c0, apl, kc, kg, ka, nlipids, name
	name.append(lipidName)
	c0.append(c0in)
	apl.append(APLin)
        kc.append(kcin)
        kg.append(kgin)
        ka.append(kain)
        nlipids.append(nlip)
        n_liptype += 1


n_regions = 0
r_name    = []
r_area    = []
cr        = []
kr        = []
def addRegion( regionName, crin, krin, areain ):
        global n_regions, r_name, r_area, cr, kr
        r_name.append(regionName)
        cr.append(crin)
        kr.append(krin)
        r_area.append(areain)
        n_regions += 1
