import numpy as np
import sys, math, random
import time

import addlipid
import options
#import energy

# numpy version 1.7.1

start = time.time()

options.init_options()

n_steps = 1000000
move_type = sys.argv[1]
temperature = 310.15
equilibrate = 100000
kb = 1.38064852E-23 * 6.02214076E23 / 4184

c0l         = addlipid.c0
apl         = addlipid.apl
kc          = addlipid.kc
kg          = addlipid.kg
ka          = addlipid.ka
nlipids     = addlipid.nlipids
name        = addlipid.name
n_liptype   = addlipid.n_liptype
n_regions   = addlipid.n_regions
c_regions   = addlipid.cr
k_regions   = addlipid.kr
a_regions   = addlipid.r_area

#############
# functions #
#############

def energy(cnt): 
    bend = 0
    stretch = 0
    ### a_0 is the equilibrium area of the lipids existing in the region (summation of individual lipid apls) ###
    a_0 = np.zeros(n_regions)
    for i in range(n_liptype):
        for j in range(n_regions):
            # added gaussian
            bend += 0.5 * apl[i] * ( c0l[i]**2 - 2 * c0l[i] * c_regions[j] ) * cnt[i+n_liptype*j][1] * ( 0.5 * kc[i] ) + kg[i] * cnt[i+n_liptype*j][1] * k_regions[j]
            a_0[j] += cnt[i+n_liptype*j][1] * apl[i]
    for i in range(n_regions):
        stretch += 0.5 * ( 0.5 * ka[i] ) * a_0[i] * ( a_regions[i] / a_0[i] - 1 )**2
    fe = bend + stretch
    return fe

def counter(lipids,regions):
    cnt_arr = []
    ind_old = 0
    for i in range(n_regions):
        for j in range(len(nlipids)):
            ind = ind_old + nlipids[j]
            residue = np.array(regions[ind_old:ind])
            temp = np.count_nonzero(residue == i)
            cnt_arr.append(temp)
            ind_old = ind
        ind_old = 0
    tempr = []
    for i in range(len(nlipids)*n_regions):
        tempr.append(i)
    full = np.column_stack((tempr, cnt_arr))
    return full


################
# do the setup #
################

### setup lipids ###
lipids = []
j = 0
for i in range(n_liptype):
    if j == 0:
        lipids = [j for k in range(nlipids[j])]
    else:
        lipids = np.append(lipids, [j for k in range(nlipids[j])])
    j += 1
lipids = list(lipids)

### setup regions ###
regions = np.random.randint(n_regions, size=np.sum(nlipids))
regions = list(regions)

### make the master list of lipids and regions: a [[type,region], [type,region], [type,region], [type,region], ...] ###
master = np.column_stack((lipids, regions))

cnt = counter(lipids,regions)

### make average array ###
t1 = [0] * (n_liptype*n_regions)
t2 = []
for i in range(len(nlipids)*n_regions):
    t2.append(i)
avg_arr = np.column_stack((t2, t1))

### construct an area probability array ###
p_area = np.zeros(n_regions)
ind_area = 0
for i in range(n_regions):
    ind_area += a_regions[i]
    p_area[i] = ind_area / sum(a_regions)

#################
# eval and loop #
#################

n  = 1
na = 1
while ( n <= n_steps ):
    ### evaluate energy ###
    feold = energy(cnt)

    ### make lipid moves ###
    if move_type == "0":
        ### make a random lipid move regions ###
        # np.random.randint(len(master), size=1)
        rsel1 = np.random.randint(len(master))
        rsel2 = np.random.randint(len(master))
        temp = master[rsel2][1]
        master[rsel2][1] = master[rsel1][1]
        master[rsel1][1] = temp
        ### get the selection information ###
        id_rsel1 = master[rsel1][0]
        id_rsel2 = master[rsel2][0]
        r_rsel1  = master[rsel1][1]
        r_rsel2  = master[rsel2][1]
        ### update the count array ###
        cnt[id_rsel1+r_rsel2*n_liptype][1] += 1
        cnt[id_rsel1+r_rsel1*n_liptype][1] -= 1
        cnt[id_rsel2+r_rsel1*n_liptype][1] += 1
        cnt[id_rsel2+r_rsel2*n_liptype][1] -= 1
    else:
        ### make a random lipid move based on area probability ###
        rsel1 = np.random.randint(len(master))
        ### get the selection information ###
        id_rsel1 = master[rsel1][0]
        r_rsel1  = master[rsel1][1]
        ### see where the lipid will move based on area ###
        pa = np.random.uniform(0,1)
        for i in range(n_regions):
            if pa <= p_area[i]:
                r_rsel2 = i
                break
        master[rsel1][1] = r_rsel2
        cnt[id_rsel1+r_rsel1*n_liptype][1] -= 1
        cnt[id_rsel1+r_rsel2*n_liptype][1] += 1

    ### evaluate energy ###
    fenew = energy(cnt)
    ### get the MC probability ###
    p = np.exp(-1/(kb*temperature)*(fenew-feold))
    ### compare, accept / reject ###
    comp = np.random.uniform(0,1)
    if comp < p:
        feold = fenew
    else:
        if move_type == "0":
            temp = master[rsel2][1]
            master[rsel2][1] = master[rsel1][1]
            master[rsel1][1] = temp
            cnt[id_rsel1+r_rsel2*n_liptype][1] -= 1
            cnt[id_rsel1+r_rsel1*n_liptype][1] += 1
            cnt[id_rsel2+r_rsel1*n_liptype][1] -= 1
            cnt[id_rsel2+r_rsel2*n_liptype][1] += 1
	else:
            master[rsel1][1] = r_rsel1
            cnt[id_rsel1+r_rsel2*n_liptype][1] -= 1
            cnt[id_rsel1+r_rsel1*n_liptype][1] += 1

    if ( n < equilibrate ):
        n += 1
        continue

    ### update average array ###
    avg_arr += cnt
    ### final count ###
    print avg_arr[:,1]/float(n)
    final_arr = avg_arr[:,1]/float(n)
    ### increase step ###
    n += 1

area_arr = [0 for i in range(n_liptype*n_regions)]
for i in range(len(final_arr)):
    area_arr[i] = final_arr[i]*apl[i % n_liptype]

print ""
print name
s = 0
for i in range(n_regions):
    print sum(area_arr[s:(s+n_liptype)])
    s += n_liptype

print ""
print name
s = 0
for i in range(n_regions):
    print( ' '.join(map(str, final_arr[s:(s+n_liptype)]/sum(final_arr[s:(s+n_liptype)]))))
#    print final_arr[s:(s+n_liptype)]/sum(final_arr[s:(s+n_liptype)])
    s += n_liptype

print ""
end = time.time()
print end - start
