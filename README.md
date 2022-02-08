# pore_mc
Monte Carlo code to simulation lipid redistribution on fusion pores

**options.py:**

Use addlipid.addLipid lines to add a new lipid type. The argument list requires: (1) lipid name; (2) lipid spontaneous curvature (units = Å^{-1}); (3) area per lipid (units = Å^{2}); (4) bilayer bending modulus (units = kcal/mol); (5) bilayer Gaussian bending modulus (units = kcal/mol); (6) bilayer compressibility modulus (kcal/mol/Å^{2}); and (7) number of lipids of this type.

Use addlipid.addRegion lines to add a new pore region. This could be the bulk, rim, and neck, for example. The argument list requires: (1) region name; (2) average mean curvature of the region (units = Å^{-1}); (3) average Gaussian curvature of the region (units = Å^{-2}); and (4) the area of the region (units = Å^{2}).


**addlipid.py:**

Reads the information from options.py and prepares it for intput into monte_carlo_area.py


**monte_carlo_area.py**

User can change n_steps (number of MC steps to run), move_type (either 0 or 1; 0 = MC moves based on random selections and 1 = MC moves based on area-weighted selections), temperature (system temperature in K), and equilibrate (number of MC steps left off the front of the simulation for equilibration).

The energy function (def energy) contains the contributions from the bending (the Helfrich Hamiltonian) and stretching free energies. The bilayer bending modulus, bilayer Gaussian modulus, and bilayer compressibility modulus are all multiplied by 1/2 to get leaflet moduli. The moves are done on a "per leaflet" basis.

The lipids are initially randomly assigned to a region and the energy is evaluated. The bending energy is from the Helfrich Hamiltonian and the stretching energy is dependent on the area difference between randomly assigning lipids to a region and the region's constrained area (definied in options.py). An area mismatch results in a strain ((A_{MC step} – A_{defined in options.py}) / A_{defined in options.py}) that is penalized.

If move_type = 0, two random lipids are chosen and switched. The energy is evaluated and the switch is accepted/rejected based on the Metropolis criterion. If move_type = 1, a lipid is randomly selected and the region which it will move is based on area-weighting. That is, it's more likely to move to a region with larger area than smaller area. The energy is evaluated and the switch is accepted/rejected based on the Metropolis criterion. It is suggested that a user use the "1" argument. Therefore, once options.py and monte_carlo_area.py are edited as desired, the program is executed using (tested using Python 2.7.5 and 2.7.16):

python monte_carlo_area.py 1
