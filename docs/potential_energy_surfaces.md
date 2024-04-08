# Potential Energy Surfaces


### 3.1. Overview

The concept of a molecular potential energy surface (PES) is fundamental to practical models of molecular structure and dynamics. The PES describes the potential energy in terms of the molecular geometry, which in turn is defined by the positions of the atomic nuclei. In the classical approximation, molecular motions are determined by forces (and hence accelerations) corresponding to gradients of the PES, and equilibrium molecular structures correspond to minima of the PES. The term potential energy surface stems from a visualization in which a potential energy function in $N$ dimensions (that is, in configuration space) is described as a surface in $N+1$ dimensions, with energy corresponding to height. (When $N>2$, the visualization is necessarily somewhat nonvisual.)

The significant features of a PES are its ${ }^{\circ}$ potential wells and the passes (termed ${ }^{\circ} \mathrm{cols}$ ) between them. A point representing the state of a stiff, ${ }^{\circ}$ stable structure resides in a well with steep walls (i.e., with a large second derivative of the energy, the basis of stiffness, for all displacements) and no low, accessible cols leading to alternative wells (i.e., no low-energy routes to other structures, the basis of stability). A point representing the initial state of a chemically reactive structure, in contrast, resides in a well linked to another well by a col of accessible height. A point representing a mobile nanomechanical component commonly moves in a well with a long, level floor. Molecular systems in which all transitions occur between distinct potential wells resemble transistor systems in which all transitions occur between distinct logic states: in both instances, the application of correct design principles can yield reliable behavior even though other systems subject to the same physical principles behave erratically.

Physicists and chemists describe molecular behavior using a hierarchy of approximations of varying accuracy; the PES concept itself is one such approximation. The following sections move from extremely accurate but impractical theories to less accurate but more useful approximations. Section 3.2 discusses both exact quantum mechanical theories and chemically useful approximations to them. Section 3.3 discusses molecular mechanics methods at some length: for nanomechanical engineering, approaches like those described in Sections 3.3 to 3.5 often provide the most useful approximations to the PES, from the standpoint both of accuracy and of computational feasibility. (A discussion of the accuracy of these methods relative to different requirements appears in Section 4.4.) Section 3.4 discusses specialized potential energy functions describing chemical reactions, and Section 3.5 discusses models of the interaction energy of large objects, neglecting atomic detail. Most of the topics introduced in this chapter are discussed at length in the literature; suggestions for further reading are appended.

### 3.2. Quantum theory and approximations

The analysis of nanomechanical systems requires models describing the behavior of molecular scale systems. The appropriate models more closely resemble those used in chemistry and materials science than (for example) those used in particle physics. For perspective, however, it may be useful to view the hierarchy of approximations from the heights of modern physical theory before moving into the domain of practical calculation. Note that the following overview of quantum mechanics is offered chiefly for perspective; although some analytical models in this volume describe quantum mechanical effects, none makes direct use of wave equations or of the mathematical apparatus of quantum mechanics itself.

### 3.2.1. Overview of quantum mechanics

a. Relativistic theories. In the 1940s, Feynman, Schwinger, and Tomonaga each independently developed formulations of the theory of quantum electrodynamics (QED), which describes electromagnetic fields and electrons in a unified way. Where the mathematics of QED can be manipulated to yield precise predictions, its predictions (e.g., of the magnetic properties of free electrons and the spectrum of the hydrogen atom) have been confirmed to the last measurable detail. It correctly predicts that the electron $g$-factor is $\sim 2.002319304$ rather than 2 as expected from previous theory, and it predicts the Lamb shift in the hydrogen spectrum (which changes an energy level by less than one part in $10^{6}$ ) to an accuracy of many decimal places. There is every reason to think that the theory would be equally precise in other areas, if it could be applied. In practice, owing to the difficulty of calculations, chemists and material scientists do not use QED. Its great contributions have been in high-energy physics and in its use as a prototype for other physical theories, such as quantum chromodynamics.

Earlier, in 1931, Dirac had developed a fully relativistic quantum mechanics which predicted electron spin (with a g-factor of 2) and provided a correct explanation for the splitting of certain spectral lines in hydrogen, reflecting shifts in energy levels by about one part in $10^{4}$. Relativistic effects are large in the inner electron shells of heavy elements, but these shells are so tightly bound to the nucleus that they are chemically inert; most relativistic effects on ${ }^{\circ}$ valence electrons (especially those of light elements) are chemically negligible.[^4] Since Dirac's theory is difficult to apply and describes effects that can often be neglected, it is not used in standard quantum mechanical calculations in chemistry and materials science.

b. Schrödinger's theory. Earlier still, in 1926, Schrödinger had developed a formulation of nonrelativistic quantum mechanics that remains the basis for calculations in quantum chemistry. Schrödinger described matter in terms of a wave equation (here shown with a scalar potential),

$$
\begin{equation*}
-\frac{\hbar^{2}}{2} \sum_{j} \frac{1}{m_{j}} \frac{\partial^{2}}{\partial r_{j}^{2}} \psi(\mathbf{r}, t)+\mathscr{V}(\mathbf{r}, t) \psi(\mathbf{r}, t)=i \hbar \frac{\partial}{\partial t} \psi(\mathbf{r}, t) \tag{3.1}
\end{equation*}
$$

in which a system of $N$ particles with masses $m_{0}, m_{1}, m_{2}, \ldots, m_{N-1}$ is described (neglecting spins) by the coordinate vector $\mathbf{r}$ with components $r_{0}, r_{1}, r_{2}, \ldots, r_{3(N-1)}$ equaling $x_{0}, y_{0}, z_{0}, x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}, \ldots, z_{(N-1)}$, and a potential energy function $\mathcal{V}(\mathbf{r}, t)$. This is a partial differential equation in a $3 N$-dimensional configuration space, and physically valid solutions, $\psi(\mathbf{r}, t)$, are subject to a set of boundary, continuity, normalization, and particle-exchange symmetry conditions. Molecular structure calculations seek solutions describing bound, time-invariant systems, but this problem cannot be solved exactly even for a molecule as simple as $\mathbf{H}_{2}$. Nonetheless, because no simpler theory provides an acceptable description of the quantum mechanical behavior of molecular matter, the Schrödinger equation has become the basis of a host of approximation schemes. These approximations represent steps backward in fundamental physical theory, but steps forward in understanding real physical systems.

c. Schrödinger's theory applied to molecules. In order to understand the general nature of these approximation schemes, it is necessary to say a little more about Schrödinger's theory as applied to molecules.[^5] In calculating the structure of isolated systems, the potential energy function $\mathcal{V}(\mathbf{r}, t)$ is time independent, and is simply the total Coulomb energy for the interaction of each pair of charged particles

$$
\begin{equation*}
\mathcal{V}(\mathbf{r})=\sum_{i<j} \frac{q_{i} q_{j}}{4 \pi \varepsilon_{0} d_{i j}} \tag{3.2}
\end{equation*}
$$

where $d_{i j}$ is the distance between particles $i$ and $j, q_{i}$ and $q_{j}$ are their charges, and $\varepsilon_{0}$ is the permittivity of free space. The potential energy function is thus based on a picture of particles with precise positions in ordinary space. The ${ }^{\circ}$ wave function determines the ${ }^{\circ}$ probability density function

$$
\begin{equation*}
f_{\mathbf{r}, t}(\mathbf{r}, t)=\psi^{*}(\mathbf{r}, t) \psi(\mathbf{r}, t) \tag{3.3}
\end{equation*}
$$

This expression is defined over the $3 N$ dimensional configuration space, hence it yields not only the particle density (and hence the charge density) at each point in 3-dimensional space, but also the probability density associated with each spatial configuration of particles. Owing to particle-exchange symmetry conditions and electrostatic repulsion, electron positions are not independent, but correlated. This precludes solving the $3 N$ dimensional problem as a set of $N$ coupled problems in three dimensions. (In the steady-state solutions of greatest chemical interest, this correlation of particle positions and motions is described by a wave function that is time independent, save for a time-varying phase factor.)

### 3.2.2. The Born-Oppenheimer PES

In chemistry and nanomechanical engineering, the full wave function gives more information than is necessary; indeed, the wave function per se is of little interest. Approximations and partial solutions can accordingly be of great value. Because each particle adds three dimensions and disproportionate computational cost, it is useful to partition problems into simpler subproblems when the resulting inaccuracies are not too severe.

Most computational techniques exploit the Born-Oppenheimer approximation, which treats the motion of electrons and nuclei separately. Even the lightest nucleus has $\sim 1836$ times the inertia of an electron. The characteristic speeds and frequencies of nuclear motion are accordingly much lower than those of electronic motion. The Born-Oppenheimer approximation treats nuclei as motionless and computes the wave function and energy for a system of electrons in the presence of a fixed nuclear configuration. In this approximation, each nuclear configuration corresponds to a single electronic ground-state energy. This defines the ground-state Born-Oppenheimer potential energy function $\mathscr{V}\left(\mathbf{r}_{\mathrm{n}}\right)$, where the vector $\mathbf{r}_{n}$ specifies only nuclear coordinates and $\mathscr{V}\left(\mathbf{r}_{n}\right)$ is quite unlike the simple Coulomb potential. In analyzing nuclear motions using this potential function, electronic motions are implicitly assumed to adjust without a time lag. The Born-Oppenheimer approximation breaks down when nuclear motions are fast enough (e.g., in high-energy collisions), when excited states occur at very low energies (this is rare in stable molecules), and when small changes in nuclear coordinates cause large changes in the electron wave function (for example in nearly degenerate states where the Jahn-Teller effect becomes important, as occurs in some symmetrical transition-metal complexes). Under ordinary conditions in which nuclear kinetic energies are less than electronic kinetic energies (and nuclear speeds are accordingly much smaller), the Born-Oppenheimer approximation usually gives an excellent account of molecular behavior.

In most nanomechanical systems, as in most chemical reactions, electron wave functions change smoothly with changes in molecular geometry. Under these conditions, there are no abrupt changes in electron distribution and energy, that is, no electronic transitions. In the absence of electronic transitions, and within the Born-Oppenheimer approximation, molecular dynamics depends only on the Born-Oppenheimer potential. If one knows this potential, or has an adequate approximation to it, then one can analyze molecular dynamics without reference to electronic behavior. (When electronic transitions occur, they place the system on another Born-Oppenheimer potential surface.) The

Born-Oppenheimer potential defines the potential energy surface, and can be used in both classical and quantum models of dynamics.

### 3.2.3. Molecular orbital methods

Practical calculations require further approximations. The most popular approaches result in a family of techniques known as molecular ${ }^{\circ}$ orbital methods; these make different approximations, yielding computations of widely varying accuracy and cost.

a. The independent-electron approximation. Molecular orbital methods begin with the independent electron approximation, in which each electron is treated as moving in the electrostatic potential that would result from the timeaverage distribution of the other electrons; this neglects the electrostatic electron correlation effects mentioned in Section 3.2.1c. Together with the BornOppenheimer approximation, this approximates the problem of solving a single Schrödinger equation in $3 N$-dimensional configuration space as that of solving $N$ coupled Schrödinger equations in three-dimensional space, where $N$ is the number of electrons. The coupling is treated by the self-consistent field method: conceptually, each newly calculated electron wave function results in a new distribution of charge density, which changes the potential experienced by the other electrons, and so demands a new calculation; the resulting iterative process converges toward a set of single-electron wave functions, each consistent with the electrostatic potential of the rest (in practice, more efficient iterative procedures are employed). Each single-electron wave function corresponds to a molecular orbital having a particular energy and charge distribution. In this process, the overall many-electron wave function is described by a determinant based on these orbitals; this imposes particle-exchange symmetry conditions.

b. Approximate wave functions. In a typical quantum chemistry program, single-electron wave functions are approximated as weighted sums of simple (e.g., "Gaussian type") basis functions, and the programs vary the weighting of each basis function to form a wave function of minimum energy. Increasing the number of basis functions provides increased flexibility in shaping the wave function, enabling the construction of more accurate molecular orbitals; the number of basis functions must equal or (far better) exceed the number of electrons in the molecule. Computations on moderately large molecules are prohibitively expensive and time-consuming, however, because the cost of computing the energy of a single molecular geometry by these methods varies roughly as the fourth power of the number of basis functions.

c. Electron correlation and "levels of theory." Molecular orbital computations can be made more accurate by taking electron correlation into account using configuration interaction (CI) and related perturbation theory methods.[^6] In CI methods, a "configuration" refers not to a spatial configuration of electrons (in the sense of a configuration space) but to a pattern of orbital occupancy: that is, to a wave function formed from a particular set of single-electron wave functions. Judiciously mixing multiple wave functions, some representing excited states and each calculated using the independent-electron approximation, is equivalent to permitting correlated electron motions and hence reduces the errors of the independent-electron approximation. The set of possible configurations is combinatorially large; practical calculations often require selecting the most important configurations from a set of millions. The practical importance of electron correlation varies with the system and the phenomenon considered; it is the source of attractive forces between neutral, nonpolar molecules and is particularly important in calculating the energy of bonds far from ${ }^{\circ}$ equilibrium geometries (i.e., during the transition state of a chemical reaction). Configuration interaction calculations often converge slowly and expensively.

d. Semiempirical methods. The techniques just described (termed ab initio methods) make approximations in determining wave functions, but they use no parameters other than fundamental physical constants. Semiempirical molecular orbital methods (such as MNDO, AM1, and PM3) make further approximations in computing wave functions, but they compensate by introducing parameters for different atom types to fit results to experimental data. These methods neglect certain integrals that arise in more complete calculations and treat the compact, high-energy orbitals of inner-shell electrons as fixed. Semiempirical methods have a far lower computational cost, by a factor of 50 to 500 even for a molecule as small as propane (Clark, 1985), but vary in their accuracy in a complex manner (e.g., having special problems with hydrogen bonds, or with boron). There is considerable room for cleverness in semiempirical methods, which continue to improve (Stewart, 1990).

e. Results and accuracy. Molecular orbital methods can be used to calculate parameters such as charge distribution, polarizability, and ionization energies, but their chief application in the present context is to evaluate the energy as a function of molecular configuration: that is, the Born-Oppenheimer potential. This information suffices to determine equilibrium molecular geometries, corresponding to local or global energy minima, but finding them requires energy evaluations (often augmented by direct calculations of energy gradients) at many points in configuration space. More complex structures require evaluation at more points, hence computational cost scales with size even more adversely than the costs of single-point calculations would suggest.

The challenge of applying molecular orbital methods to chemical reactions is suggested by the great difference between the total molecular binding energy calculated by these methods (the energy required to separate a molecule into isolated electrons and nuclei) and the energy differences of chemical interest. The total binding energy for a small molecule is typically on the order of $10^{-15} \mathrm{~J}$, and the energy of a single chemical bond is on the order of $10^{-18} \mathrm{~J}$, but the energy required to rearrange bonds in a chemical reaction is typically $<10^{-19} \mathrm{~J}$, and the success of a solution-phase chemical process can be critically dependent on energy differences of $<10^{-20} \mathrm{~J}$. Thus, chemists often require that errors be less than $10^{-4}$ or $10^{-5}$ of the total energy, although larger errors in total energy can often be tolerated so long as energy differentials between similar structures are computed accurately enough.

This accuracy can be achieved using molecular orbital methods (for small structures), and such calculations can be used to design chemically-active groups for use in reactive devices in molecular manufacturing systems. Nonetheless, limitations associated with the expense, accuracy, and scalability of molecular orbital methods motivate the continuing popularity of empirically based models of molecules and chemical reactions.

### 3.3. Molecular mechanics

An alternative to performing quantum mechanical calculations of electronic structure is to approximate the Born-Oppenheimer potential directly in terms of the molecular geometry. Molecular mechanics methods (among others) take this approach, which is well suited to most problems of nanomechanical design and modeling.

### 3.3.1. The molecular mechanics approach

a. Overview. Organic chemists traditionally represent molecular structures with ball-and-stick models in which each ball represents an atom and each stick represents a bond. In quantum mechanical calculations, there is no a priori concept of a "chemical bond," and the behavior of bonding emerges afresh in each calculation. Molecular mechanics calculations, in contrast, begin with the concept of bonds, then use them as a basis for modeling the molecular potential energy surface. Molecular mechanics thus builds directly on a familiar and useful visualization of molecular structure.

Molecular mechanics programs use an approximate PES to calculate the properties of equilibrium molecular structures (that is, of local minima on the surface). This PES is developed by choosing functional forms and parameters that yield structures with properties that closely approximate the experimentally measured geometries, energies, and vibrational frequencies of molecules in the laboratory. Structural geometries are determined experimentally by (for example) $x$-ray crystallography, microwave spectroscopy, and gas-phase electron diffraction; heats of formation by calorimetry; and vibrational frequencies by infrared spectroscopy. Molecular mechanics thus builds directly on a large body of experimental results regarding the mechanical properties of molecules.

Burkert and Allinger (1982) provide data on the typical accuracy of calculations performed on hydrocarbons using the MM2 model: estimated bond lengths typically match experimental values to within a few times $10^{-13} \mathrm{~m}(\sim 0.1 \%)$, estimated bond angles typically match within about $0.01 \mathrm{rad}\left(\approx 0.6^{\circ}\right.$, or $\left.0.5 \%\right)$, and energies within a few times $10^{-21} \mathrm{~J}$. These values are comparable in accuracy to the experimental data itself. Accuracies are lower among nonhydrocarbon structures, but are often good by nanomechanical standards (Section 4.4.3).

Burkert and Allinger compare the computational costs of molecular mechanics calculations to those of $a b$ initio quantum mechanical calculations: for a small molecule (propylamine, with 13 atoms) cost favors molecular mechanics by a factor of $10^{3}$. For larger molecules the difference becomes more pronounced: computational costs for molecular mechanics methods increase at between the second and third power of the number of atoms, rather than the higher powers characteristic of molecular orbital methods. As of 1992, molecular mechanics calculations on $10^{5}$ atom systems have become routine, and systems of $10^{2}$ to $10^{3}$ atoms are readily modeled using personal computers.

b. Limitations, content, and applications. Molecular mechanics systems have, however, been successfully applied to only a narrow range of molecular structures in configurations not too far from equilibrium. They use energy functions and parameters tailored to specific, local arrangements of atoms. Fortunately for nanomechanical engineering efforts, the most advanced molecular mechanics methods have been developed to model a class of structures that includes those most suitable for use as nanomechanical components-that is, structures built largely of carbon atoms (often augmented with one or more of the elements $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}, \mathrm{Si}, \mathrm{P}, \mathrm{S}$, and $\mathrm{Cl}$ ) joined by strong, directional, covalent bonds. Structures of this class are the focus of organic chemistry; a subset of these structures comprises most of the molecular machinery of living systems.

Within this set, limitations remain. Aside from the small inaccuracies found in all structures, standard molecular mechanics programs cannot realistically describe certain structures. For example, they can model many stable structures, even when ${ }^{\circ}$ strained, but cannot model chemical transformations or systems on the verge of such transformations. Computational results must be examined with an eye for such invalidating conditions.

Molecular mechanics programs differ in their intended applications, with some designed for speed and others for accuracy, with some intended for broad classes of organic structures and others specialized for biomolecules. In general, systems intended for large biomolecules also place a premium on speed and give poor descriptions of structures with large strain energies; popular examples are AMBER (Weiner et al., 1984; Weiner et al., 1986) and CHARMM (Brooks et al., 1983). A widely used molecular mechanics model intended for a broad range of organic structures (including structures with large strain energies) is MM2 (Allinger, 1977), developed by Norman Allinger and his coworkers. Although in the process of being superseded by the similar, but more complex and accurate MM3 (Allinger et al., 1990; Allinger et al., 1989; Lii and Allinger, 1989a; Lii and Allinger, 1989b; Lii and Allinger, 1991), MM2 gives good results for a broad range of structures and is a standard model in the chemical literature. After evaluation and with some caveats, the MM2 model is used as an engineering approximation in much of the present work. Computations performed by MM2based software are used to characterize the minimum-energy configurations of structures, their stiffness, bearing properties, and the like; MM2 parameters are also used as a basis for several analytical models.

Molecular mechanics programs treat the total potential energy as a sum of terms accounting chiefly for bond stretching, bending, and torsion, and for van der Waals, overlap, and electrostatic interactions among nonbonded atoms. To develop a physical intuition for the mechanical behavior of molecular systems, one needs a feel for the nature and magnitude of these forces. Although physical intuition cannot substitute for a more precise analysis, it can be of great value in shaping designs and choosing what to analyze. The relationships and parameters that follow provide a good basis for physical understanding and also enable pocket-calculator estimates of the stiffness, force, and energy associated with molecular deformations. In the exploratory phase of design, one must test and

Table 3.1. Some atom types used in the MM2 program (Allinger, 1986) along with (rationalized) MM2 nonbonded interaction parameters. Note that the lone pair electrons associated with nitrogen and oxygen atoms are modeled by treating each pair as a pseudoatom. The full set of atom types described by MM2 is roughly twice as large as this list.

| MM2 <br/> code | Symbol | Type | $\varepsilon_{\text {vdw }}$ <br/> $(\mathrm{maJ})$ | $r_{\text {vdw }}$ <br/> $\left(10^{-10} \mathrm{~m}\right)$ | Mass <br/> $(\mathrm{amu})$ | Mass <br/> $\left(10^{-27} \mathrm{~kg}\right)$ |
| :---: | :---: | :---: | :---: | :---: | ---: | :---: |
| 1 | $\mathrm{C}$ | $s p^{3}$ | 0.357 | 1.90 | 12.000 | 19.925 |
| 2 | $\mathrm{C}$ | $s p^{2}$ alkene | 0.357 | 1.94 | 12.000 | 19.925 |
| 3 | $\mathrm{C}$ | $s p^{2}$ carbonyl | 0.357 | 1.94 | 12.000 | 19.925 |
| 4 | $\mathrm{C}$ | $s p$ acetylene | 0.357 | 1.94 | 12.000 | 19.925 |
| 5 | $\mathrm{H}$ | hydrocarbon | $0.382^{\mathrm{a}}$ | $1.50^{\mathrm{a}}$ | 1.008 | 1.674 |
| 6 | $\mathrm{O}$ | $\mathrm{C}-\mathrm{O}-[\mathrm{H}, \mathrm{C}]$ | 0.406 | 1.74 | 15.999 | 26.565 |
| 7 | $\mathrm{O}$ | carbonyl | 0.536 | 1.74 | 15.999 | 26.565 |
| 8 | $\mathrm{~N}$ | sp $^{3}$ | 0.447 | 1.82 | 14.003 | 23.251 |
| 11 | $\mathrm{~F}$ | fluoride | 0.634 | 1.65 | 18.998 | 31.545 |
| 12 | $\mathrm{Cl}$ | chloride | 1.950 | 2.03 | 34.969 | 58.064 |
| 13 | $\mathrm{Br}$ | bromide | 2.599 | 2.18 | 78.918 | 131.038 |
| 14 | $\mathrm{I}$ | iodide | 3.444 | 2.32 | 126.900 | 210.709 |
| 15 | $\mathrm{~S}$ | sulfide | 1.641 | 2.11 | 31.972 | 53.087 |
| 19 | $\mathrm{Si}$ | silane | 1.137 | 2.25 | 27.977 | 46.454 |
| 20 | $\mathrm{LP}$ | lone pair | 0.130 | 1.20 | 0.000 | 0.000 |
| 21 | $\mathrm{H}$ | alcohol | 0.292 | 1.20 | 1.008 | 1.674 |
| 22 | $\mathrm{C}$ | cyclopropane | 0.357 | 1.90 | 12.000 | 19.925 |
| 25 | $\mathrm{P}$ | phosphine | 1.365 | 2.18 | 30.994 | 51.464 |

${ }^{\text {a }}$ See Section 3.3.2e for correction factors.

modify tentative concepts. This requires quick, accessible estimates of energies, forces, and stiffnesses, and of how they vary. For this, experience shows the value of graphs such as Figures 3.3 to 3.9.

### 3.3.2. The MM2 model

In molecular mechanics, bonds are defined by the types of the atoms they join, and these atom types can depend on both atomic number and bonding environment: for example, carbon atoms that participate only in single bonds are classified as a different type from those that participate in double or triple bonds. Table 3.1 lists some of the atom types used by the MM2 program and their nonbonded-interaction parameters (Section 3.3.2e).

a. Bond stretching. Bonds resist stretching and compression, tending toward an equilibrium length. The MM2 expression for the potential energy of bond stretching $\mathscr{V}_{\mathrm{s}}$ includes a cubic term to account for anharmonicity

$$
\begin{equation*}
\mathscr{V}_{\mathrm{s}}=\frac{1}{2} k_{\mathrm{s}}\left(r-r_{0}\right)^{2}\left[1-k_{\text {cubic }}\left(r-r_{0}\right)\right] \tag{3.4}
\end{equation*}
$$

In this expression, $r_{0}$ is the equilibrium bond length, $r$ is the actual bond length, $k_{\mathrm{s}}$ is the stretching stiffness, and $k_{\text {cubic }}$ is the magnitude of a cubic correction, for which the MM2 model uses an invariant value of $2 \times 10^{10} \mathrm{~m}^{-1}$. (For ease of use,

Table 3.2. MM2 bond-stretching parameters (Allinger, 1986) for some common bond types; the full set is roughly six times larger.

| Bond type <br/> $(\mathrm{MM} 2$ codes $)$ | $\boldsymbol{k}_{\mathbf{s}}$ <br/> $(\mathbf{N} / \mathrm{m})$ | $r_{0}$ <br/> $\left(10^{-10} \mathrm{~m}\right)$ | Bond type |
| :---: | :---: | :---: | :--- |
| $1-5$ | 460 | 1.113 | $\mathrm{C}-\mathrm{H}$ |
| $1-1$ | 440 | 1.523 | $\mathrm{C}-\mathrm{C}$ |
| $2-2$ | 960 | 1.337 | $\mathrm{C}=\mathrm{C}$ |
| $4-4$ | 1560 | 1.212 | $\mathrm{C} \equiv \mathrm{C}$ |
| $1-6$ | 536 | 1.402 | $\mathrm{C}-\mathrm{O}$ |
| $1-8$ | 510 | 1.438 | $\mathrm{C}-\mathrm{N}$ |
| $3-7$ | 1080 | 1.208 | $\mathrm{C}=\mathrm{O}$ |
| $1-11$ | 510 | 1.392 | $\mathrm{C}-\mathrm{F}$ |
| $1-12$ | 323 | 1.795 | $\mathrm{C}-\mathrm{Cl}$ |
| $1-13$ | 230 | 1.949 | $\mathrm{C}-\mathrm{Br}$ |
| $1-14$ | 220 | 2.149 | $\mathrm{C}-\mathrm{I}$ |
| $8-20$ | 610 | 0.600 | $\mathrm{~N}-\mathrm{LP}$ |
| $8-8$ | 560 | 1.381 | $\mathrm{~N}-\mathrm{N}$ |
| $6-20$ | 460 | 0.600 | $\mathrm{O}-\mathrm{LP}$ |
| $6-21$ | 460 | 0.942 | $\mathrm{O}-\mathrm{H}$ |
| $6-6$ | 781 | 1.470 | $\mathrm{O}-\mathrm{O}$ |
| $1-19$ | 297 | 1.880 | $\mathrm{C}-\mathrm{Si}$ |
| $1-25$ | 291 | 1.856 | $\mathrm{C}-\mathrm{P}$ |
| $1-15$ | 321.3 | 1.815 | $\mathrm{C}-\mathrm{S}$ |
| $19-19$ | 185 | 2.332 | $\mathrm{Si}-\mathrm{Si}$ |
| $22-22$ | 440 | 1.501 | $\mathrm{C}-\mathrm{C}$ |
| (cyclopropane) |  |  |  |

all MM2 expressions and parameters have been converted into SI units.) Table 3.2 lists some MM2 bond-stretching parameters.

b. Bond angle-bending. Two bonds to a shared atom define a bond angle (four bonds to a shared atom define six such angles). In the structures for which MM2 provides a good approximation, bond angles can be described as having preferred values with displacements countered by restoring forces; this describes amines poorly,[^7] and can describe trivalent but not pentavalent phosphorus (Burkert and Allinger, 1982). In its description of the potential energy $\mathscr{V}_{\theta}$ of

Table 3.3. MM2 bond angle-bending parameters (Allinger, 1986) for some common bond types; the full set is roughly ten times larger.

| Angle type <br/> (MM2 codes) | $k_{\theta}$ <br/> $\left(\mathrm{aJ} / \mathbf{r a d}^{2}\right)$ | $\theta_{0}$ <br/> $(\mathrm{deg})$ | $\theta_{0}$ <br/> $(\mathrm{rad})$ | Angle type |
| :---: | :---: | :---: | :---: | :---: |
| $1-1-1$ | 0.450 | 109.47 | 1.911 | $\mathrm{C}-\mathrm{C}-\mathrm{C}$ |
| $1-1-5$ | 0.360 | 109.39 | 1.909 | $\mathrm{C}-\mathrm{C}-\mathrm{H}$ |
| $5-1-5$ | 0.320 | 109.40 | 1.909 | $\mathrm{H}-\mathrm{C}-\mathrm{H}$ |
| $1-1-11$ | 0.650 | 109.50 | 1.911 | $C-C-F$ |
| $11-1-11$ | 1.070 | 107.10 | 1.869 | $\mathrm{~F}-\mathrm{C}-\mathrm{F}$ |
| $1-2-1$ | 0.450 | 117.20 | 2.046 | $\mathrm{C}-\mathrm{C}\left(s p^{2}\right)-\mathrm{C}$ |
| $2-1-2$ | 0.450 | 109.47 | 1.911 | $\mathrm{C}\left(s p^{2}\right)-\mathrm{C}-\mathrm{C}\left(s p^{2}\right)$ |
| $1-2-2$ | 0.550 | 121.40 | 2.119 | $\mathrm{C}-\mathrm{C}=\mathrm{C}$ |
| $2-2-5$ | 0.360 | 120.00 | 2.094 | $\mathrm{C}=\mathrm{C}-\mathrm{H}$ |
| $2-2-2$ | 0.430 | 120.00 | 2.094 | $\mathrm{C}=\mathrm{C}-\mathrm{C}\left(s p^{2}\right)$ |
| $1-4-4$ | $0.200^{\mathrm{a}}$ | 180.00 | 3.142 | $\mathrm{C}-\mathrm{C} \equiv \mathrm{C}$ |
| $1-3-7$ | 0.460 | 122.50 | 2.138 | $\mathrm{C}-\mathrm{C}=\mathrm{O}$ |
| $1-6-1$ | 0.770 | 106.80 | 1.864 | $\mathrm{C}-\mathrm{O}-\mathrm{C}$ |
| $1-8-1$ | 0.630 | 107.70 | 1.880 | $\mathrm{C}-\mathrm{N}-\mathrm{C}$ |
| $1-1-6$ | 0.700 | 107.50 | 1.876 | $\mathrm{C}-\mathrm{C}-\mathrm{O}$ |
| $1-1-8$ | 0.570 | 109.47 | 1.911 | $\mathrm{C}-\mathrm{C}-\mathrm{N}$ |
| $1-6-20$ | 0.350 | 105.16 | 1.835 | $\mathrm{C}-\mathrm{O}-\mathrm{LP}$ |
| $1-8-20$ | 0.500 | 109.20 | 1.906 | $\mathrm{C}-\mathrm{N}-\mathrm{LP}$ |
| $20-6-20$ | 0.240 | 131.00 | 2.286 | LP-O-LP |
| $19-19-19$ | 0.350 | 111.30 | 1.943 | $\mathrm{Si}-\mathrm{Si}-\mathrm{Si}$ |
| $19-1-19$ | 0.400 | 115.50 | 2.016 | $\mathrm{Si}-\mathrm{C}-\mathrm{Si}$ |
| $1-19-1$ | 0.480 | 110.80 | 1.934 | $\mathrm{C}-\mathrm{Si}-\mathrm{C}$ |
| $12-1-12$ | 1.080 | 111.70 | 1.950 | $\mathrm{Cl}-\mathrm{C}-\mathrm{Cl}$ |
| $1-1-15$ | 0.550 | 109.00 | 1.902 | $\mathrm{C}-\mathrm{C}-\mathrm{S}$ |
| $1-15-1$ | 0.720 | 96.30 | 1.902 | $\mathrm{C}-\mathrm{S}-\mathrm{C}$ |

a Allinger and Pathiaseril (1987).

bond angle-bending, MM2 includes a sextic term

$$
\begin{equation*}
\mathscr{V}_{\theta}=\frac{1}{2} k_{\theta}\left(\theta-\theta_{0}\right)^{2}\left[1+k_{\text {sextic }}\left(\theta-\theta_{0}\right)^{4}\right] \tag{3.5}
\end{equation*}
$$

In this expression, $\theta_{0}$ is the equilibrium bond angle, $\theta$ is the current bond angle, $k_{\theta}$ is the angular spring constant, and $k_{\text {sextic }}$ is the magnitude of a sextic bending constant (taken to be $0.754 \mathrm{rad}^{-4}$ in all cases). Table 3.3 lists some MM2 bond angle-bending parameters.

To compare bond angle-bending to bond stretching, one needs a measure of stiffness in terms of spatial (not angular) displacement. To first order, bond angle-bending can be described by the contribution of the angular stiffness $k_{\theta}$ to an ordinary stiffness $k_{\mathrm{s} \perp}$ characterizing displacements of an atom perpendicular to a chosen bond and in the plane of the corresponding angle:

$$
\begin{equation*}
k_{\mathrm{s} \perp}=k_{\theta} / r_{0}^{2} \tag{3.6}
\end{equation*}
$$

Table 3.4. Some MM2 parameters for out-of-plane bending.

| Angle type <br/> (MM2 code ranges) | $k_{\theta}$ <br/> $\left(\mathrm{aJ} / \mathrm{rad}^{2}\right)$ |
| :---: | :---: |
| $2-(1 \ldots 9)$ | 0.05 |
| $3-(1 \ldots 9)$ | 0.80 |
| $9-(1 \ldots 4)$ | 0.05 |
| $9-(6 \ldots 9)$ | 0.05 |

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-68.jpg?height=213&width=433&top_left_y=658&top_left_x=167)

Figure 3.1. Out-of-plane bending geometry in the MM2 model. In calculating angle-bending energies centered on $s p^{2}$ atoms (such as $\mathrm{C}$ in the diagram at left), each angle (such as ACB) is described in terms of an in-plane component (the angle AEB) and an out-of-plane component (the angle CDE); the line CE is perpendicular to the $\mathrm{ABD}$ plane.

Bond angle-bending stiffnesses are substantially less than bond-stretching stiffnesses. For example, in the bending of a $\mathrm{C}-\mathrm{C}-\mathrm{C}$ bond angle, $k_{\mathrm{s} \perp}=19.4 \mathrm{~N} / \mathrm{m}$, or about $1 / 20$ the stretching stiffness of a $\mathrm{C}-\mathrm{C}$ bond (all carbons ${ }^{\circ} s p^{3}$ ). In an $s p^{3}$ tetrahedral geometry, bending of one bond with respect to the other three is characterized by a stiffness 1.5 times greater than this.

Systems containing $s p^{2}$ atoms have a preferred plane and are subject to a restoring force when bonds are bent away from this plane. Table 3.4 lists some force constants for out-of-plane bending. Figure 3.1 illustrates the definition of the in-plane and out-of-plane bending angles; the three atoms surrounding an $s p^{2}$ carbon (e.g., in formaldehyde) define three angles of each kind.

c. Bond torsion. Rotation about bonds is not free rotation [in the technical sense used by chemists (Mislow, 1989)], but can often permit a freely turning motion in a mechanical engineer's sense. The MM2 potential describes the variation in energy associated with rotation about a bond as a sum of four-atom torsional potentials, in which the torsion angle is defined as shown in Figure 3.2. The six hydrogen atoms in ethane define nine such angles. Each four-atom torsional potential takes the form

$$
\begin{equation*}
V_{\omega}=\frac{1}{2}\left[V_{1}(1+\cos \omega)+V_{2}(1-\cos 2 \omega)+V_{3}(1+\cos 3 \omega)\right] \tag{3.7}
\end{equation*}
$$

Some parameters are listed in Table 3.5.

As with bond angle-bending, torsional restoring forces can be described (to first order, for configurations at the bottom of a potential well) by a stiffness associated with small displacements tangent to the torsional motion. The maximum stiffness contribution from a single torsional term for a set of four $s p^{3}$ carbons (associated with the torsional displacement of one terminal carbon atom) is about $0.36 \mathrm{~N} / \mathrm{m}$. Ordinary torsional stiffness terms (and related forces and energies) are thus about 1/50 the magnitude of bond angle-bending stiffness terms, or about $1 / 1000$ the magnitude of bond-stretching stiffnesses. In nanomechanical structures designed for rigidity, torsional contributions to stiffness are

Table 3.5. MM2 parameters for bond torsion (the full set is roughly 80 times larger).

| Torsion type <br/> (MM2 codes) | $V_{1}$ <br/> $(\mathrm{maJ})$ | $V_{2}$ <br/> $(\mathrm{maJ})$ | $V_{3}$ <br/> $(\mathrm{maJ})$ | Torsion type |
| :---: | :---: | :---: | :---: | :---: |
| $1-1-1-1$ | 1.39 | 1.88 | 0.65 | $\mathrm{C}-\mathrm{C}-\mathrm{C}-\mathrm{C}$ |
| $1-1-1-5$ | 0.00 | 0.00 | 1.85 | $\mathrm{C}-\mathrm{C}-\mathrm{C}-\mathrm{H}$ |
| $5-1-1-5$ | 0.00 | 0.00 | 1.65 | $\mathrm{H}-\mathrm{C}-\mathrm{C}-\mathrm{H}$ |
| $1-1-1-11$ | 0.00 | -0.60 | 6.46 | $\mathrm{C}-\mathrm{C}-\mathrm{C}-\mathrm{F}$ |
| $1-2-2-1$ | -0.69 | 69.47 | 0.00 | $\mathrm{C}-\mathrm{C}=\mathrm{C}-\mathrm{C}$ |
| $2-2-2-2$ | -6.46 | 55.58 | 0.00 | $\mathrm{C}\left(\mathrm{sp}^{2}\right)-\mathrm{C}=\mathrm{C}-\mathrm{C}\left(\mathrm{sp}^{2}\right)$ |
| $5-2-2-5$ | 0.00 | 104.21 | 0.00 | $\mathrm{H}-\mathrm{C}=\mathrm{C}-\mathrm{H}$ |

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-69.jpg?height=227&width=352&top_left_y=697&top_left_x=285)

Figure 3.2. Torsion geometry.

seldom crucial (any structure in which they were a chief source of rigidity would not be very rigid). Double bonds have substantial torsional stiffness, and are an exception to this generalization. The MM2 model includes many torsional energy parameters; MM2/CSC adds additional torsional parameters, and the present work has supplemented this set as needed.

d. Electrostatic interactions. Structures containing atoms of substantially different ${ }^{\circ}$ electronegativity (i.e., most molecules other than hydrocarbons) have significant bond dipole moments, and ionic structures have charge. MM2 describes electrostatic interactions in molecules by summing dipole-dipole interactions (and so forth) in accord with classical electrostatics, assuming a uniform value of the dielectric constant that can be adjusted to reflect the properties of different surroundings. Since the surrounding structures are inhomogeneous on the same scale as the interacting entities, the assumption of a uniform dielectric constant is a relatively crude approximation.

An example of a strongly polarized bond is $\mathrm{C}-\mathrm{F}$, with a dipole moment of $\sim 4.7 \times 10^{-30} \mathrm{C} \cdot \mathrm{m}$. If this dipole is treated as resulting from atom-centered fractional charges, the corresponding charge on the $\mathrm{F}$ atom is about $-0.2 e$. Figures 3.6 and 3.7 include a comparison of the magnitude of electrostatic and nonbonded interactions for $\mathrm{C}-\mathrm{F}, \mathrm{C}-\mathrm{Cl}$, and $\mathrm{C}-\mathrm{Br}$ groups, calculated using atomcentered fractional charges.

e. Nonbonded interactions. Corresponding to each atom type (Table 3.1) is a set of parameters describing the attractive and repulsive forces experienced by pairs of uncharged, nonbonded atoms. Physicists usually apply the term "van der Waals force" to the attractive component alone, that is, to the London dispersion force (along with various polar interactions between molecules). This volume follows a common usage in computational chemistry, treating polar interactions separately but including the ${ }^{\circ}$ overlap repulsion (a.k.a. exchangeforce, hard-core, Born, or steric repulsion) as part of a single nonbonded potential. The MM2 model describes these overall interactions with a Buckingham (or $\exp -6$ ) potential

$$
\begin{equation*}
\mathcal{V}_{\mathrm{vdw}}=\varepsilon_{\mathrm{vdw}}\left[2.48 \times 10^{5} \exp \left(-12.5 \frac{r}{r_{\mathrm{vdw} 0}}\right)-1.924\left(\frac{r}{r_{\mathrm{vdw} 0}}\right)^{-6}\right] \tag{3.8}
\end{equation*}
$$

where $r$ is the distance between the atoms, the parameter $\varepsilon_{\mathrm{vdw}}$ for the interaction between atoms 1 and 2 equals $\left(\varepsilon_{\mathrm{vdw} 1}+\varepsilon_{\mathrm{vdw} 2}\right) / 2$, and $r_{\mathrm{vdw} 0}$ equals $r_{\mathrm{vdw} 1}+r_{\mathrm{vdw} 2}$. This function has a minimum of $-\varepsilon_{\mathrm{vdw}}$ at $r=r_{\mathrm{vdw} 0}$. The forces between atoms bonded to a common atom (i.e., 1-3 interactions) are included not in the nonbonded interaction energy, but in the bond angle-bending energy; all other pairs are included in the sum. (The above expression has been recast to make $\varepsilon_{\mathrm{vdw}}$ equal the binding energy at $r=r_{\text {vdw } 0}$.)

Equilibrium separations between atoms in different molecules (and in larger structures) are usually smaller than the pairwise equilibrium separations defined by the nonbonded interaction parameters: The short-range nature of the exponential component allows only nearest neighbors to make a significant contribution to the repulsive side of the balance, but the $r^{-6}$ forces have a longer range, allowing many atoms to make a significant contribution to the attractive side (Section 3.5). Equilibrium separations shrink accordingly.

The absence of nucleocentric spherical symmetry in bonded atoms leads to certain complications, however. Calculation of nonbonded interactions for $s p^{3}$ nitrogen and oxygen atoms in the MM2 model includes the effects of associated lone-pair pseudoatoms. When hydrogen atoms form bonds, an unusually large fraction of their electron density shifts toward the other atom; in calculating nonbonded interactions, MM2 models this by moving the effective position of the hydrogen atom inward to 0.915 of the full bond length. Describing pairwise interactions using the above mean and sum expressions for $\varepsilon_{\mathrm{vdw}}$ and $r_{\mathrm{vdw} 0}$ is a rough approximation; for the nonbonded interaction between hydrogen and $s p^{3}$ carbon, $r_{\mathrm{vdw} 0}$ is corrected to 0.982 of the summed value, and $\varepsilon_{\mathrm{vdw}}$ is corrected to 1.011 of the mean value.

f. Complications and conjugated systems. The MM2 model includes a number of small corrections and special cases. For example, when bond angles are reduced, equilibrium bond lengths increase. This is described in the MM2 potential by a stretch-bend interaction term; for bonds $\mathrm{A}$ and $\mathrm{B}$ forming an angle $\boldsymbol{\theta}$,

$$
\begin{equation*}
V_{\mathrm{s} \theta}=k_{\mathrm{s} \theta}\left(\theta-\theta_{0}\right)\left[\left(r_{\mathrm{A}}-r_{\mathrm{A} 0}\right)+\left(r_{\mathrm{B}}-r_{\mathrm{B} 0}\right)\right] \tag{3.9}
\end{equation*}
$$

Some parameters are listed in Table 3.6. A reduction in bond angle by $0.1 \mathrm{rad}$ yields a modest $0.00014 \mathrm{~nm}$ change in the equilibrium lengths of the two associated bonds. A larger (but static) correction to equilibrium bond length is applied in the presence of adjacent bonded atoms of differing electronegativity. The extreme case is $\mathrm{F}$, which shortens an adjacent $\mathrm{C}-\mathrm{C}$ bond by $0.0022 \mathrm{~nm}$, or about $1.4 \%$. The MM2 model includes special-case parameters for three- and fourmembered rings, and for ${ }^{\circ}$ hydrogen bond interactions.

Table 3.6. Stretch-bend parameters.

| Angle type $^{\mathrm{a}}$ | $k_{\mathrm{s} \theta}$ <br/> $\left(10^{-9} \mathrm{~N} / \mathrm{rad}\right)$ |
| :---: | :---: |
| X-First-Y | 1.20 |
| $\mathrm{X}-$ Second-Y | 2.50 |
| X-First-H | 0.90 |
| $\mathrm{X}-$ Second-H | -4.00 |
| a $\mathrm{X}, \mathrm{Y}=$ first or second row atoms; First = first row atom; |  |
| Second = second row atom; H = hydrogen. |  |

A major complication arises in ${ }^{\circ}$ conjugated double-bond systems, in which the treatment of bonds as entities with properties depending only on their near neighbors breaks down. Where single and double bonds alternate along a chain or ring, delocalization of ${ }^{\circ} \mathrm{pi}$ electrons can greatly affect the potential energy function; benzene is a classic example. MM2 describes conjugated systems by performing a minimal quantum mechanical analysis of the participating pi electrons; it uses the results to estimate the magnitude of fractional bonding between pairs of atoms, and then adjusts the force field parameters (equilibrium bond lengths, stiffnesses, torsional energies, etc.) accordingly. (Further complications in the MM2 model are omitted from this discussion.)

g. Notes on MM2 in light of MM3. Known shortcomings of MM2 are discussed in a set of papers describing a preliminary version of the MM3 force field (Allinger et al., 1989; Lii and Allinger, 1989a; Lii and Allinger, 1989b). Aside from problems noted in Sections 3.3.1b and 3.3.2b, the greatest shortcoming of MM2 is its inaccurate prediction of molecular vibrational frequencies; accuracy in this was sacrificed to achieve greater accuracy in describing the energy and geometry of equilibrium configurations. Since frequencies depend on molecular stiffnesses, this failure is of significance to the design of molecular machines.

MM3 succeeds in fitting vibrational frequencies while improving accuracy in other areas by virtue of a more complex functional form (e.g., a stretch-torsion interaction, a cubic bending term, a quartic stretching term) and additional parameters. MM3 predicts greater stiffness than MM2, by factors of $\sim 1.5$ or more for angle bending (Table 3.7). Since MM3 is a better model, it is clear that MM2 stiffness values are substantially lower than those of real molecules. Greater stiffness is usually an asset in molecular machinery, hence this defect in MM2 usually provides a conservative bias: it tends to generate false-negative rather than false-positive assessments of device feasibility. An exception to this rule is in structures where angle-bending strain relieves bond stretching: the low anglebending stiffness of the MM2 model may then result in a false-positive assessment of the stability of a stretched bond.

From a nanomechanical perspective, the other major modification in MM3 (again indicating a shortcoming in MM2) is its treatment of nonbonded interactions. MM3 uses an exp-6 potential, but with 12.0 in place of 12.5 in the exponent [see Eq. (3.8)], and a smaller weighting on the exponential term. The atomic parameters developed thus far have larger atomic radii (by a factor of

Table 3.7. Ratios of MM3 and MM2 stiffness parameters.

| Bond-stretching stiffness parameters: |  |
| :---: | :---: |
| $\mathrm{C}-\mathrm{C}$ | 1.02 |
| $\mathrm{C}-\mathrm{H}$ | 1.03 |
| Bond angle-bending stiffness parameters: |  |
| $\mathrm{C}-\mathrm{C}-\mathrm{C}$ | 1.49 |
| $\mathrm{C}-\mathrm{C}-\mathrm{H}$ | 1.64 |
| $\mathrm{H}-\mathrm{C}-\mathrm{H}$ | 1.72 |

$\sim 1.07$ ) and smaller energy scale factors (by $\sim 0.55$ ). The net result is a softer interaction, with lower energies, forces, and stiffnesses in the deep repulsive regime; typical differences are on the order of tens of percent. This difference has mixed effects on nanomechanical systems.

The softer interactions decrease the calculated stiffness of bearings and other devices using nonbonded contacts, but the stiffness of these interactions is sensitive to load and hence is subject to design control. Softer, longer-range interactions both decrease phonon transmission and make surfaces smoother, thereby decreasing several drag mechanisms that occur in bearings (Section 10.4.6). So long as a substantial margin of safety is provided in the design of stiff, nonbonded interfaces, this shortcoming of MM2 should only rarely result in false-positive assessments of the feasibility of a nanomechanical system.

### 3.3.3. Energy, force, and stiffness under large loads

Nanomechanical engineering and conventional chemistry place different demands on potential energy functions and emphasize different properties. Some of these differences are discussed in more detail in Section 4.4.3c, which compares the accuracies demanded by solution-phase and ${ }^{\circ}$ machine-phase chemistry. Other differences result from the nanomechanical emphasis on force as a controllable parameter and on stiffness as a determinant of positioning errors; in conventional chemistry, stiffness is of interest chiefly as a determinant of vibrational frequencies in spectroscopy, and force is rarely mentioned. Further, many nanomechanical systems apply large forces to bonds and to nonbonded interfaces. Although strained organic molecules can experience large bonded and nonbonded forces, potential functions developed for chemistry must be examined for suitability before applying them to problems of nanomechanical design involving large loads.

a. Bonds under large tensile loads. For describing bonds under large tensile loads, the MM2 bond-stretching function is clearly inadequate: the cubic term eventually results in a repulsive force of unbounded magnitude. Higher-order terms, unimportant in most molecules, were omitted to reduce computational expense. Where stresses and separations are larger, the potential energy of stretching in covalent bonds commonly is modeled using the Morse function

$$
\begin{equation*}
\mathscr{V}_{\text {morse }}=D_{\mathrm{e}}\left(\left\{1-\exp \left[-\beta\left(r-r_{0}\right)\right]\right\}^{2}-1\right) \tag{3.10}
\end{equation*}
$$

Table 3.8. Bond dissociation energies, stiffnesses, lengths, and Morse $\beta$ parameters. Values of $r_{0}$ and $k_{\mathrm{s}}$ from Table 3.2.

| Bond | $D_{0}$ <br/> $(\mathrm{aJ})$ | $D_{\mathrm{e}}$ <br/> $(\mathrm{aJ})$ | $k_{\mathrm{s}}$ <br/> $(\mathrm{N} / \mathrm{m})$ | $\beta$ <br/> $\left(10^{10} \mathrm{~m}^{-1}\right)$ | $r_{0}$ <br/> $\left(10^{-10} \mathrm{~m}\right)$ | Compound | ref. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{C}-\mathrm{H}$ | 0.642 | 0.671 | 460 | 1.851 | 1.113 | $\mathrm{H}-\mathrm{C}\left(\mathrm{CH}_{3}\right)_{3}$ | a |
| $\mathrm{C}-\mathrm{C}$ | 0.545 | 0.556 | 440 | 1.989 | 1.523 | $\mathrm{CH}_{3}-\mathrm{C}\left(\mathrm{CH}_{3}\right)_{3}$ | b |
| $\mathrm{C}=\mathrm{C}$ | 1.190 | 1.207 | 960 | 1.994 | 1.337 | $\mathrm{H}_{2} \mathrm{C}=\mathrm{CH}_{2}$ | a |
| $\mathrm{C} \equiv \mathrm{C}$ | 1.594 | 1.614 | 1560 | 2.198 | 1.212 | $\mathrm{HC} \equiv \mathrm{CH}$ | a |
| $\mathrm{C}-\mathrm{N}$ | 0.498 | 0.509 | 510 | 2.238 | 1.438 | $\mathrm{C}_{2} \mathrm{H}_{5}-\mathrm{N}\left(\mathrm{CH}_{3}\right)_{2}$ | b |
| $\mathrm{C}-\mathrm{O}$ | 0.564 | 0.575 | 536 | 2.159 | 1.402 | $\mathrm{C}_{2} \mathrm{H}_{5}-\mathrm{OCH}_{3}$ | b |
| $\mathrm{C}=\mathrm{O}$ | 1.327 | 1.343 | 1080 | 2.005 | 1.208 |  | c |
| $\mathrm{C}-\mathrm{F}$ | 0.876 | 0.887 | 510 | 1.695 | 1.392 | $\mathrm{~F}-\mathrm{C}_{2} \mathrm{H}_{5}$ | $\mathbf{a}$ |
| $\mathrm{N}-\mathrm{H}$ | 0.631 | 0.664 | 610 | 2.143 | 1.020 | $\mathrm{H}-\mathrm{N}\left(\mathrm{CH}_{3}\right)_{2}$ | b |
| $\mathrm{N}-\mathrm{N}$ | 0.405 | 0.417 | 560 | 2.592 | 1.381 | $\mathrm{H}_{2} \mathrm{~N}-\mathrm{N}\left(\mathrm{CH}_{3}\right)_{2}$ | a |
| $\mathrm{O}-\mathrm{H}$ | 0.725 | 0.753 | 460 | 1.747 | 0.942 | $\mathrm{H}-\mathrm{OC}\left(\mathrm{CH}_{3}\right)_{3}$ | b |
| $\mathrm{O}-\mathrm{O}$ | 0.259 | 0.272 | 781 | 3.789 | 1.470 | $\left(\mathrm{CH}_{3}\right)_{3} \mathrm{CO}-\mathrm{OC}\left(\mathrm{CH}_{3}\right)_{3}$ | $3^{a}$ |
| $\mathrm{C}-\mathrm{Si}$ | 0.616 | 0.624 | 297 | 1.543 | 1.880 | $\mathrm{CH}_{3}-\mathrm{Si}\left(\mathrm{CH}_{3}\right)_{3}$ | a |
| $\mathbf{C}-\mathbf{P}$ | 0.439 | 0.446 | 291 | 1.806 | 1.856 |  | c |
| $\mathrm{C}-\mathrm{S}$ | 0.532 | 0.539 | 321 | 1.726 | 1.815 | $\mathrm{CH}_{3}-\mathrm{SCH}_{3}$ | a |
| $\mathrm{C}-\mathrm{Cl}$ | 0.583 | 0.591 | 323 | 1.653 | 1.795 | $\mathrm{Cl}-\mathrm{CH}_{3}$ | b |
| $\mathrm{C}-\mathrm{Br}$ | 0.482 | 0.488 | 230 | 1.536 | 1.949 | $\mathrm{Br}-\mathrm{CH}_{3}$ | a |
| $\mathrm{C}-\mathrm{I}$ | 0.393 | 0.398 | 220 | 1.662 | 2.149 | $\mathrm{I}-\mathrm{CH}_{3}$ | b |
| $\mathrm{Si}-\mathrm{Si}$ | 0.555 | 0.559 | 185 | 1.286 | 2.332 | $\left(\mathrm{CH}_{3}\right)_{3} \mathrm{Si}-\mathrm{Si}\left(\mathrm{CH}_{3}\right)_{3}$ | a |

${ }^{a}$ Kerr, 1990

${ }^{b}$ McMillen and Golden, 1982

${ }^{c}$ Huheey, 1978

with the corresponding forces and stiffnesses

$$
\begin{gather*}
F_{\text {morse }}=-\frac{\partial}{\partial r} \mathscr{V}_{\text {morse }}=2 \beta D_{\mathrm{e}}\left\{\exp \left[-2 \beta\left(r-r_{0}\right)\right]-\exp \left[-\beta\left(r-r_{0}\right)\right]\right\}  \tag{3.11}\\
k_{\mathrm{s}, \text { morse }}=\frac{\partial^{2}}{\partial r^{2}} \mathscr{V}_{\text {morse }}=2 \beta^{2} D_{\mathrm{e}}\left\{2 \exp \left[-2 \beta\left(r-r_{0}\right)\right]-\exp \left[-\beta\left(r-r_{0}\right)\right]\right\} \tag{3.12}
\end{gather*}
$$

In Eqs. (3.10) to (3.12),

$$
\begin{equation*}
\beta=\sqrt{k_{\mathrm{s}} / 2 D_{\mathrm{e}}} \tag{3.13}
\end{equation*}
$$

where the energy $D_{\mathrm{e}}$ represents the depth of the potential well. The value of $D_{\mathrm{e}}$ cannot be directly measured, but is the sum of the energy required to break the bond at zero $\mathrm{K}$, shown as $D_{0}$, and the zero point vibrational energy associated with the bond. It can be approximated as

$$
\begin{equation*}
D_{\mathrm{e}} \approx D_{0}+\frac{\hbar}{2} \sqrt{\frac{k_{\mathrm{s}}}{\mu}}=D_{0}+\frac{\hbar \omega}{2} ; \quad \mu=\frac{m_{1} m_{2}}{m_{1}+m_{2}} \tag{3.14}
\end{equation*}
$$

where $m_{1}$ and $m_{2}$ are the masses of the bonded atoms. The zero-point energy of a harmonic oscillator of frequency $\omega$ is $\hbar \omega / 2$, and Eq. (3.14) treats a bonded pair of atoms as if it were a harmonic oscillator having the frequency of an analogous isolated diatomic molecule. In the case of a $\mathrm{C}-\mathrm{C}$ bond, $D_{\mathrm{e}}$ is about $1.02 D_{0}$. Table 3.8 lists values for $D_{\mathrm{e}}$ based on tabulated values for bond dissociation energies and the bond stiffness values of the MM2 potential, using Eq. (3.14) to approximate the zero-point energy after correction to zero $\mathrm{K}$. These values can be substantially modified by the surrounding molecular structure.

Figure 3.3 plots the $\mathrm{C}-\mathbf{C}$ Morse potential based on the values in Table 3.8, along with the MM2 bonded and nonbonded potentials; Figures 3.4 and 3.5 plot additional Morse potentials for easy reference. Although its form is motivated by quantum mechanical considerations, the Morse function grows increasingly inaccurate far from the equilibrium separation. From a structural perspective,

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-74.jpg?height=1298&width=1119&top_left_y=656&top_left_x=193)

Figure 3.3. Morse and MM2 nonbonded potentials, forces, and stiffnesses for carboncarbon interactions. The Morse curves are based on parameters for $\mathbf{C}-\mathbf{C}$ bonds (Table 3.8); a dotted curve shows the MM2 bond-stretching potential for comparison. The curves for $\mathrm{C} \mid \mathrm{C}$ contacts are based on parameters from Table 3.1 for $s p^{2}$ carbon atoms, which have better-exposed surfaces than do typical $s p^{3}$ atoms. Note the breakdown in the MM2 exp-6 model at distances around $0.15 \mathrm{~nm}$; the dotted extensions of solid curves represent clearly nonphysical regions.

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-75.jpg?height=1309&width=1102&top_left_y=156&top_left_x=308)

Figure 3.4. Morse potentials, forces, and stiffnesses for a representative sample of bond types useful in structural frameworks. Parameters from Table 3.8.

the shape of the Morse function is of interest chiefly within the separation defined by the inflection point, $r=r_{0}+(\ln 2) / \beta$; a Morse bond stretched beyond this length by a position-independent force becomes mechanically unstable (for $\mathrm{C}-\mathrm{C}$, at $\sim 0.187 \mathrm{~nm}$ ). Beyond the inflection point, the stiffness becomes negative, reaching a most-negative value of $-0.125 k_{\mathrm{s}}$.

At larger separations, a more accurate potential is the Lippincott function,

$$
\begin{equation*}
\mathscr{V}_{\text {lippincott }}=D_{\mathrm{e}}\left[1-\exp \left(-\frac{k_{\mathrm{s}} r_{0}\left(r-r_{0}\right)^{2}}{2 D_{\mathrm{e}} r}\right)\right], \quad r \geq r_{0} \tag{3.15}
\end{equation*}
$$

which better fits data from vibrational spectroscopy (Eggers et al., 1964) and accurate $a b$-initio molecular orbital calculations (Brown and Truhlar, 1985), although its accuracy is poor for $r<r_{0}$. In comparison to the Morse function, the Lippincott function commonly predicts a greater magnitude for both the bond breaking force and the most-negative stiffness $\left(<-0.125 k_{\mathrm{s}}\right)$. Chapter 6 examines

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-76.jpg?height=1915&width=1108&top_left_y=181&top_left_x=189)

Figure 3.5. The relationships in Figure 3.4 regraphed on a logarithmic scale to facilitate reading of values. Dashed lines represent negative values.

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-77.jpg?height=1314&width=1110&top_left_y=156&top_left_x=301)

Figure 3.6. MM2 nonbonded potentials, forces, and stiffnesses for a representative sample of pairwise nonbonded interactions (the $\mathrm{C} \mid \mathrm{O}$ curves omit the lone-pair contribution). The solid curves for $\mathrm{F}|\mathrm{F}, \mathrm{Cl}| \mathrm{Cl}$, and $\mathrm{Br} \mid \mathrm{Br}$ nonbonded interactions are accompanied by dotted curves representing combined nonbonded and electrostatic effects for the collinear dipole systems $\mathrm{C}-\mathrm{F}|\mathrm{F}-\mathrm{C}, \mathrm{C}-\mathrm{Cl}| \mathrm{Cl}-\mathrm{C}$, and $\mathrm{C}-\mathrm{Br} \mid \mathrm{Br}-\mathrm{C}$. Also shown are interactions between two isolated electrons (off scale in the upper graph).

bond strengths using Morse potentials (which underestimate strength); Chapter 8 examines bond-breakage processes using Lippincott potentials (which provide more adverse estimates of stiffness).

b. Nonbonded interactions under large compressive loads. Nonbonded interactions (Figures 3.6 and 3.7) can be divided into multiple components, of which the MM2 model takes account of three: electrostatic forces, attractive van der Waals forces, and overlap repulsion forces. The latter two forces are represented by the $r^{-6}$ and exponential terms of the exp-6 potential, both of which have forms motivated by approximate quantum theories. More thorough treatments of these forces include small attractive $r^{-8}, r^{-10}$ (etc.) terms, three-body interactions, induced dipole effects, different rules of combination for estimating

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-78.jpg?height=1913&width=1110&top_left_y=177&top_left_x=188)

Figure 3.7. The relationships in Figure 3.6 regraphed on a logarithmic scale to facilitate reading of values. Dashed lines represent negative values.

the well depths and equilibrium radii of pairwise interactions, and so forth. Modeling interactions within and between molecules in terms of atom-by-atom pairwise potentials of any kind has no basic theoretical justification and guarantees some inaccuracy. Discussions of alternative models may be found in the literature (Maitland et al., 1981; Rigby et al., 1986). Nonetheless, molecular mechanics potentials including the three components just mentioned have proved accurate enough for a wide range of purposes. The additional interaction terms just mentioned are inconsequential when repulsive forces are dominant, as is common at interfaces within nanomechanical devices.

Several well-known potential forms are unsuitable for analyzing nanomechanical systems that involve large repulsive energies. The Lennard-Jones 6-12 potential, although time honored, has a repulsive interaction that lacks theoretical motivation and is unrealistically steep. The Maitland and Smith potential (Maitland et al., 1981), although excellent in the low-energy range, is again too steep in the deep repulsive regime.

The MM2 expression for nonbonded interactions has two parameters: the equilibrium separation of two atoms and the depth of the well at that point. Well depths commonly are on the order of $1 \mathrm{maJ}$, but repulsive interaction energies of nanomechanical interest range upward to $>100 \mathrm{maJ}$. This gap raises questions regarding the realism of the MM2 potential at higher energies, as does the behavior of the MM2 potential at distances below $0.323 r_{\mathrm{vdw} 0}$, where the exponential repulsion is overwhelmed by a nonphysical extension of the $r^{-6}$ attraction. The general realism of the MM2 exp-6 function at intermediate separations and high energies can be tested by comparing its description of noble gas interactions [using well depths and equilibrium separations drawn from Rigby et al. (1986)] to the interactions measured in collision experiments using neutral particle beams (Amdur and Jordan, 1966). This comparison indicates that the MM2 potential approximates the experimentally measured potential reasonably well (within tens of percent) at radii as small as $0.5 r_{\mathrm{vdw} 0}$, and thus at energies $>100 \mathrm{maJ}$. This is an ample range and accuracy for most nanomechanical design work.

As is detailed in Chapter 5, stiff interactions are often necessary in order to minimize quantum and thermal uncertainties in position. Nanomechanical components frequently are constrained not by bonds, but by overlap repulsion. This makes nonbonded forces and stiffnesses important. In the MM2 approximation

$$
\begin{align*}
F_{\mathrm{vdw}} & =-\frac{\partial}{\partial r} \mathscr{V}_{\mathrm{vdw}} \\
& =\varepsilon_{\mathrm{vdw}}\left[\frac{3.1 \times 10^{6}}{r_{\mathrm{vdw} 0}} \exp \left(-12.5 \frac{r}{r_{\mathrm{vdw} 0}}\right)-\frac{11.54}{r}\left(\frac{r}{r_{\mathrm{vdw} 0}}\right)^{-6}\right] \tag{3.16}
\end{align*}
$$

and

$$
\begin{align*}
k_{\mathrm{s}, \mathrm{vdw}} & =\frac{\partial^{2}}{\partial r^{2}} \mathscr{V}_{\mathrm{vdw}} \\
& =\varepsilon_{\mathrm{vdw}}\left[\frac{3.88 \times 10^{7}}{r_{\mathrm{vdw} 0}^{2}} \exp \left(-12.5 \frac{r}{r_{\mathrm{vdw} 0}}\right)-\frac{80.81}{r^{2}}\left(\frac{r}{r_{\mathrm{vdw} 0}}\right)^{-6}\right] \tag{3.17}
\end{align*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-80.jpg?height=1554&width=1095&top_left_y=154&top_left_x=203)

Figure 3.8. MM2 nonbonded potential energies and stiffnesses as a function of the pairwise force for a range of pairwise interactions. The dotted diagonal lines represent Eq. (3.18) (bottom) and Eq. (3.19) (top) for $r_{\text {vdw0 }}=0.36 \mathrm{~nm}$.

Figures 3.6 and 3.7 plot energy, force, and stiffness as functions of distance for various pairwise nonbonded interactions. In the repulsive regime, stiffness increases with decreasing separation and increasing force; the achievable compressive force commonly limits the achievable stiffness. Figure 3.8 plots stiffness and energy as functions of compressive force for a representative set of pairwise interactions. Where the exponential term dominates, stiffness, force, and energy are proportional. For strongly repulsive interactions in the MM2 model

$$
\begin{equation*}
k_{\mathrm{s}, \mathrm{vdw}} \approx \frac{12.5}{r_{\mathrm{vdw} 0}} F_{\mathrm{vdw}} \approx 3.5 \times 10^{10} F_{\mathrm{vdw}} \tag{3.18}
\end{equation*}
$$

A similar expression describes the energy in the strongly repulsive regime:

$$
\begin{equation*}
\mathcal{V}_{\mathrm{vdw}} \approx 0.0 \delta r_{\mathrm{vdw} 0} F_{\mathrm{vdw}} \approx 2.9 \times 10^{-11} F_{\mathrm{vdw}} \tag{3.19}
\end{equation*}
$$

Under these conditions, the wide range of $\varepsilon_{\mathrm{vdw}}$ values (a factor of $\sim 10$ ) is of no significance. Only the smaller range of $r_{\mathrm{vdw} 0}$ values (a factor of $\sim 1.5$, omitting the MM2 lone-pair pseudoatom) affects the stiffness and stored energy resulting from a given compressive load. Note that the form of these relationships makes it a matter of indifference whether a compressive load is concentrated on a single atom or spread over many, so long as each single-atom load is large enough for the approximation to apply.

Chemists define various atomic sizes, including covalent, ionic, and van der Waals radii. These have the property that, under the relevant conditions (covalent bonding, ionic contact, and zero-load nonbonded contact) the distance between atoms of any two types can be approximated as the sum of their separate radii. For nanomechanical work, it is convenient to define analogous summable nonbonded radii for atoms under mechanical load. The following

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-81.jpg?height=984&width=1078&top_left_y=1131&top_left_x=320)

Figure 3.9. Approximate summable nonbonded radii, based on Eq. (3.20): for a given force between two atoms, their separation is approximately the sum of the above radii.

approximate expression defines loaded contact radii as a function of the applied force $F$

$$
\begin{equation*}
r_{\text {loaded }}(F) \approx \frac{r_{\text {vdw }}}{13.6} \ln \left(\frac{2.5 \times 10^{6} \varepsilon_{\mathrm{vdw}}}{r_{\mathrm{vdw}} F}\right) \tag{3.20}
\end{equation*}
$$

In the range $F=0.1$ to $5 \mathrm{nN}$, this approximation yields separations within $4 \%$ of the values implied by the MM2 nonbonded interaction model for all pairs of atoms drawn from the list in Table 3.1 save for those including iodine or the lone-pair pseudoatom. These functions are graphed in Figure 3.9.

### 3.4. Potentials for chemical reactions

### 3.4.1. Relationship to other methods

Because molecular-mechanics methods (Section 3.3) are based on the notion of structures with well-defined bonds, they cannot describe transformations that make or break bonds, and cannot predict chemical instabilities (discussed in Chapter 6). Potential energy functions describing chemical reactions have been the subject of separate study (reviewed in Truhlar and Steckler, 1987). Techniques that combine molecular mechanics potentials for describing large structures with reaction potentials [or with quantum mechanical methods applied to small regions (Singh and Kollman, 1986)] are useful in describing nanomechanisms that make and break bonds.

Bond cleavage and formation present computational challenges for molecular orbital methods. Accurate calculations often require extensive use of CI methods to account for electron correlation effects, raising the cost of computations and preventing computations of useful accuracy on complex systems. Even where computations are feasible at many points on the PES, subsequent analytical studies often demand that the surface be described by some function fitted to those points. Accordingly, studies of molecular reaction dynamics usually rely on approximate potential energy surfaces. These are described either by fitting complicated functions to quantum mechanical calculations, or by adjusting a few parameters in a fixed functional form to make calculated reaction rates (and their temperature dependence) fit experimental data. Only the simplest reactions and PES approximations are described here; a growing literature is concerned with elaborating potentials for polyatomic reaction dynamics (Truhlar and Steckler, 1987).

### 3.4.2. Bond cleavage and radical coupling

The simplest reactions break a single bond and yield two ${ }^{\circ}$ radicals that undergo no subsequent rearrangement. These reactions have potential energy surfaces that are extensions of bond stretching and bond angle-bending. The Morse function, Eq. (3.10), can serve as an approximate potential for homolytic reactions (i.e., bond cleavage yielding a pair of radicals rather than a pair of ions). For the design of reactive nanomechanisms, the important region of the Morse function lies between the bottom of the potential well $\left(r=r_{0}\right)$ and the distance at which the stiffness is most negative [which occurs at $r=r_{0}+(\ln 4) / \beta$ ]. Toward the outer end of this range, however, the Lippincott potential appears to give a more accurate description.

Bond formation by radical coupling (the inverse of homolytic bond cleavage) requires paired, antiparallel electron spins (termed a ${ }^{\circ}$ singlet state, for reasons rooted in spectroscopy). With paired spins, this process follows a Morse potential; systems with parallel, unpaired spins (triplet states) experience a potential approximated by the repulsive, anti-Morse function

$$
\begin{equation*}
\mathcal{V}_{\text {anti-morse }}=\frac{1}{2} D_{\mathrm{e}}\left(\left\{1+\exp \left[-\beta\left(r-r_{0}\right)\right]\right\}^{2}-1\right) \tag{3.21}
\end{equation*}
$$

and form no bond. Energetic considerations favor spin pairing and bond formation, but the pairing of initially unpaired spins (an electronic transition between potential surfaces termed intersystem crossing) can be slow relative to the picosecond time scale of thermal molecular motion (Section 8.4.4b).

### 3.4.3. Abstraction reactions

More complex reactions break and form bonds simultaneously. The most studied class involves the transfer of a single atom from a molecule to a radical, such as the symmetrical hydrogen ${ }^{\circ}$ abstraction reaction

$$
\begin{equation*}
\mathrm{H}_{3} \mathrm{C}+\mathrm{HCH}_{3} \rightarrow \mathrm{H}_{3} \mathrm{CH}+\mathrm{CH}_{3} \tag{3.22}
\end{equation*}
$$

Abstraction reactions often have been modeled using the London-EyringPolanyi-Sato (LEPS) potential (Sato, 1955), or using the related extended$L E P S$ potential (Kuntz et al., 1966). The latter is based on the expression

$$
\begin{align*}
V_{\mathrm{LEPS}} & =\frac{Q_{\mathrm{AB}}}{1+S_{\mathrm{AB}}}+\frac{Q_{\mathrm{BC}}}{1+S_{\mathrm{BC}}}+\frac{Q_{\mathrm{AC}}}{1+S_{\mathrm{AC}}} \\
& -\sqrt{\frac{1}{2}\left[\left(\frac{J_{\mathrm{AB}}}{1+S_{\mathrm{AB}}}-\frac{J_{\mathrm{BC}}}{1+S_{\mathrm{BC}}}\right)^{2}+\left(\frac{J_{\mathrm{BC}}}{1+S_{\mathrm{BC}}}-\frac{J_{\mathrm{AC}}}{1+S_{\mathrm{AC}}}\right)^{2}+\left(\frac{J_{\mathrm{AC}}}{1+S_{\mathrm{AC}}}-\frac{J_{\mathrm{AB}}}{1+S_{\mathrm{AB}}}\right)^{2}\right]} \tag{3.23}
\end{align*}
$$

a function of the interatomic distances $r_{\mathrm{AB}}, r_{\mathrm{BC}}$, and $r_{\mathrm{AC}}$ (see following expressions) which reduces to the LEPS potential when the Sato parameters $S_{\mathrm{AB}}$, $S_{\mathrm{BC}}$, and $S_{\mathrm{AC}}$ are all equal, and further reduces to the London equation when all three equal zero. In this expression, $\mathrm{A}, \mathrm{B}$, and $\mathrm{C}$ represent the three atoms directly participating in bond breaking and formation, and the energies $Q_{\mathrm{XY}}$ and $J_{X Y}$ represent the coulomb and exchange integrals between atoms $X$ and $Y$ (these quantities arise in quantum mechanical descriptions of bonding). In the LEPS model, bonding interactions between atoms $\mathrm{X}$ and $\mathrm{Y}$ are described by the Morse function

$$
\begin{equation*}
\frac{Q_{\mathrm{XY}}+J_{\mathrm{XY}}}{1+S_{\mathrm{XY}}}=D_{\mathrm{eXY}}\left(\left\{1-\exp \left[-\beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{0 \mathrm{XY}}\right)\right]\right\}^{2}-1\right) \tag{3.24}
\end{equation*}
$$

and antibonding interactions are described by the anti-Morse function

$$
\begin{equation*}
\frac{Q_{\mathrm{XY}}-J_{\mathrm{XY}}}{1-S_{\mathrm{XY}}}=\frac{1}{2} D_{\mathrm{eXY}}\left(\left\{1+\exp \left[-\beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{0 \mathrm{XY}}\right)\right]\right\}^{2}-1\right) \tag{3.25}
\end{equation*}
$$

yielding the expressions

$$
\begin{align*}
& Q_{\mathrm{XY}}=\frac{1}{2} D_{\mathrm{eXY}}\left\{\frac{1}{2}\left(S_{\mathrm{XY}}+3\right) \exp \left[-2 \beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{0 \mathrm{XY}}\right)\right]\right.  \tag{3.26}\\
&\left.-\left(3 S_{\mathrm{XY}}+1\right) \exp \left[-\beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{\mathrm{XXY}}\right)\right]\right\}
\end{align*}
$$

and

$$
\begin{align*}
J_{\mathrm{XY}}=\frac{1}{2} D_{\mathrm{eXY}}\left\{\frac{1}{2}\left(3 S_{\mathrm{XY}}+1\right) \exp \left[-2 \beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{\mathrm{XXY}}\right)\right]\right.  \tag{3.27}\\
\left.-\left(S_{\mathrm{XY}}+3\right) \exp \left[-\beta_{\mathrm{XY}}\left(r_{\mathrm{XY}}-r_{0 \mathrm{XY}}\right)\right]\right\}
\end{align*}
$$

The bond properties of isolated molecules define the pairwise Morse parameters. For any given choice of Morse and Sato parameters, the LEPS potential can be expressed as a function of the three interatomic distances, $r_{\mathrm{AB}}, r_{\mathrm{BC}}$, and $r_{\mathrm{AC}}$; for a collinear system, it can be expressed as a function of two such distances. In the limit as one atom is removed to infinity while the other pair remains in close proximity, the LEPS potential reduces to the Morse potential for that pair of atoms.

Despite (and because of) their limited flexibility, LEPS and extended LEPS potentials have been a basis for work in molecular reaction dynamics (Levine and Bernstein, 1987) and transition state theory (Bérces and Márta, 1988). They are used in Section 8.5.4a to examine the effects of mechanical forces on abstraction reactions. A wide range of alternative functional forms has been explored in the literature, but improved fits are usually purchased at the expense of substantially greater mathematical complexity (Bérces and Márta, 1988).

### 3.5. Continuum representations of surfaces

Nanomechanical components often are subject to forces dominated by bonding and overlap repulsion, but van der Waals attractions (London dispersion forces) between nanometer-scale objects can also be substantial. The long-range nature of these forces motivates the use of continuum approximations. At small spacings, surface-surface interactions require a model that separately accounts for the first atomic layer, including overlap forces.

### 3.5.1. Continuum models of van der Waals attraction

a. The Hamaker constant. In terms of the MM2 parameters, the long-range interatomic pairwise potential is

$$
\begin{equation*}
\mathscr{V}_{\mathrm{vdw}}=-\frac{C}{r^{6}} ; \quad C=1.924 \varepsilon_{\mathrm{vdw}} r_{\mathrm{vdw} 0}^{6} \tag{3.28}
\end{equation*}
$$

For interactions involving a pair of solid bodies, the continuum model merges the contributions of the individual atoms and describes them in terms of the Hamaker constant, $\mathscr{A}$. In the simplest description, the interacting materials are assumed to be separated by vacuum, and only nonretarded pairwise interactions are considered.[^8] The Hamaker constant can then be expressed as

$$
\begin{equation*}
\mathscr{A}_{12}=\pi^{2} C n_{\mathrm{v} 1} n_{\mathrm{v} 2} \tag{3.29}
\end{equation*}
$$

where $n_{\mathrm{v} 1}$ and $n_{\mathrm{v} 2}$ are the number densities of atoms in the interacting bodies. (Where a body contains several atom types, it can be treated as the superposition of several bodies each with a single atom type.) This and the more rigorous Lifshitz theory are described in Israelachvili (1992). Values of the Hamaker constant for condensed media are typically in the range of 30 to $500 \mathrm{maJ}$.

For nonpolar insulators of different Hamaker constant interacting across vacuum,

$$
\begin{equation*}
\mathscr{A}_{12} \approx \sqrt{\mathscr{A}_{11} \mathbb{A}_{22}} \tag{3.30}
\end{equation*}
$$

(Note that the MM2 model uses the arithmetic mean for calculating pairwise dispersion interactions between unlike atoms; the geometric mean has better theoretical justification and has been adopted in MM3.) For interactions between nonpolar insulators 1 and 2 across a medium 3 ,

$$
\begin{equation*}
\mathscr{A}_{132} \approx\left(\sqrt{\mathbb{A}_{11}}-\sqrt{\mathbb{A}_{33}}\right)\left(\sqrt{\mathbb{A}_{22}}-\sqrt{\mathbb{A}_{33}}\right) \tag{3.31}
\end{equation*}
$$

When one or more phases are polar (e.g., water), an estimate of the Hamaker constant can be derived from an approximation to the Lifshitz theory (Israelachvili, 1992), which includes contributions from dipole-dipole interactions:

$$
\begin{gather*}
\mathscr{A}_{132} \approx \frac{3 \hbar \omega}{8 \sqrt{2}} \frac{\left(n_{1}^{2}-n_{3}^{2}\right)\left(n_{2}^{2}-n_{3}^{2}\right)}{\left(\sqrt{n_{1}^{2}+n_{3}^{2}}+\sqrt{n_{2}^{2}+n_{3}^{2}}\right) \sqrt{\left(n_{1}^{2}+n_{3}^{2}\right)\left(n_{2}^{2}+n_{3}^{2}\right)}}  \tag{3.32}\\
+\frac{3}{4} k T\left(\frac{\varepsilon_{1}-\varepsilon_{3}}{\varepsilon_{1}+\varepsilon_{3}}\right)\left(\frac{\varepsilon_{2}-\varepsilon_{3}}{\varepsilon_{2}+\varepsilon_{3}}\right)
\end{gather*}
$$

In this expression, $n$ is the optical refractive index, $\varepsilon$ is the zero-frequency dielectric constant, and $\omega$ is the absorption frequency of the medium (or where frequencies differ, the mean). For many materials, $\hbar \omega \approx 2 \mathrm{aJ}$. Table 3.9 lists values of $n$ and $\varepsilon$ for several materials, together with the resulting Hamaker constants for interactions across vacuum between two bodies of identical composition.

b. Interactions between objects. Figure 3.10 presents approximate expressions for the attractive potential between objects of various shapes. Note that the potential energy always diverges as the distance $s \rightarrow 0$; a minimum separation $s_{\text {min }} \approx 0.2 \mathrm{~nm}$ commonly is assumed in the literature. This can be rationalized in terms of a $\sim 0.1 \mathrm{~nm}$ gap between a fictitious Hamaker surface (which bounds the

Table 3.9. Refractive index, zero-frequency dielectric constant, and Hamaker constant [from Eq. (3.32)] for several materials; $\hbar \omega$ taken as $2 \mathrm{aJ}$.

| Material | $\boldsymbol{n}$ | $\boldsymbol{\varepsilon}$ | $\mathscr{A}_{11}(\mathrm{maJ})$ |
| :--- | :---: | :---: | :---: |
| Polytetrafluoroethylene | 1.35 | 2.1 | 38 |
| Polyethylene | 1.52 | 2.3 | 76 |
| Diamond | 2.40 | 5.5 | 340 |
| Fused silica | 1.49 | 3.8 | 69 |
| Water | 1.33 | 78.5 | 37 |
| Glycerol | 1.47 | 42.5 | 66 |
| Metals (Au, Ag, $\mathrm{Cu})$ |  |  | 300 to 500[^61] |

| ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=369&width=552&top_left_y=905&top_left_x=188) | ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=369&width=552&top_left_y=905&top_left_x=767) |
| :---: | :---: |
| ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=366&width=509&top_left_y=1289&top_left_x=188) | ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=369&width=552&top_left_y=1289&top_left_x=767) |
| ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=366&width=509&top_left_y=1673&top_left_x=188) | ![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-02.jpg?height=366&width=552&top_left_y=1673&top_left_x=767) |

Figure 3.10. The potential energy, $\mathscr{V}_{\text {vdw }}$ of the van der Waals attraction in the nonretarded continuum approximation; after Israelachvili (1992). In the two-surface expression, $S=$ area. The more complex expressions for geometries with $r \approx s$ appear in Hiemenz (1986).

region of high polarizability in an object) and an approximate excluded-volume surface (describing the limits of motion imposed by overlap repulsion). The gap occurs because polarizability chiefly arises from regions of high electron density within bonds and atomic core regions, while the overlap repulsion is substantial even outside these regions. Section 3.5.2 describes flat-surface models that include the effects of overlap repulsion.

Taking $\mathscr{A}=400 \mathrm{maJ}$ (a fairly high value) and $s=0.2 \mathrm{~nm}$ (i.e., contact), the attractive dispersion force between two spheres of $r=1 \mathrm{~nm}$ is $\sim 0.83 \mathrm{nN}$. For parallel surfaces at this separation, the force per unit area is $\sim 2.7 \times 10^{9} \mathrm{~N} / \mathrm{m}^{2}$ $\left(=2.7 \mathrm{nN} / \mathrm{nm}^{2}\right.$ ), $\sim 1 / 20$ the tensile strength of diamond. Doubling $s$ (for example, by interposing scattered atomic-scale bumps as spacers) reduces this force to $\sim 3.3 \times 10^{8} \mathrm{~N} / \mathrm{m}^{2}$.

### 3.5.2. Transverse-continuum models of surfaces

Chapters 7 and 10 examine the mechanical properties of sliding, unreactive, atomically precise interfaces in which van der Waals attraction and overlap repulsion are the dominant forces.[^9] This requires a model for the interaction energy of two such surfaces at small separations. In the interfaces of greatest practical interest, the structures of the two surfaces are out of register (owing to differences in lattice spacing or to a relative rotation). Neglecting elastic deformations resulting from interfacial forces, this results in a surface-surface potential that can be approximated in terms of the interactions of layers in which the effects of the constituent atoms have been spread uniformly over a plane. In a further approximation, all but the outermost layers can be spread uniformly in the third dimension and their overlap repulsions (which are subject to rapid exponential decay) can be neglected, yielding the standard Hamaker-constant model for interactions involving the interior regions (Figure 3.11).

With this model, the total surface-interaction energy is the sum of the pairwise interactions of the two explicitly treated planes, of each plane and the opposed continuum, and of the two continua:

$$
\begin{equation*}
\mathscr{V}_{\text {surf }}=\mathscr{V}_{\mathrm{a} 1-\mathrm{a} 2}+\mathscr{V}_{\mathrm{a} 1-\mathrm{v} 2}+\mathscr{V}_{\mathrm{a} 2-\mathrm{v} 1}+\mathscr{V}_{\mathrm{v} 1-\mathrm{v} 2} \tag{3.33}
\end{equation*}
$$

with obvious generalizations when more layers of atoms are treated explicitly.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-03.jpg?height=372&width=474&top_left_y=1710&top_left_x=281)

Figure 3.11. Model of two surfaces, showing the outermost atomic layers described as uniform planes and deeper regions approximated as uniform volumes.

The plane-plane interaction energy can be calculated from integrals describing the point-plane interaction energy, using an exp-6 potential. In terms of the densities $n_{\mathrm{a} 1}$ and $n_{\mathrm{a} 2}$ of atoms in the two planes, the energy per unit area is

$$
\begin{equation*}
\frac{\mathscr{V}_{\mathrm{a}-\mathrm{a}}}{S}=n_{\mathrm{a} 1} n_{\mathrm{a} 2} \pi\left[\frac{2 A}{b^{2}}(b s+1) \exp \left(-b s_{\mathrm{a}-\mathrm{a}}\right)-\frac{C_{\mathrm{a}-\mathrm{a}}}{2 s_{\mathrm{a}-\mathrm{a}}^{4}}\right] \tag{3.34}
\end{equation*}
$$

where $C$ is the same as in Eq. (3.28), and $A$ and $b$ are parameters for the exponential component of the interatomic interaction, when expressed in the form

$$
\begin{equation*}
\mathscr{V}_{\text {rep }}=A \exp (-b s) \tag{3.35}
\end{equation*}
$$

In the MM2 model,

$$
\begin{equation*}
A=2.48 \times 10^{5} \varepsilon_{\mathrm{vdw}} ; \quad b=\frac{12.5}{d_{\mathrm{vdw} 0}} \tag{3.36}
\end{equation*}
$$

For all other interactions, overlap repulsion is neglected. The interaction between atoms in a plane and in a volume [from Eq. (3.29) and the expression in Figure 3.10a] contributes

$$
\begin{equation*}
\frac{\mathcal{V}_{\mathrm{a}-\mathrm{v}}}{S}=-n_{\mathrm{a} 1} n_{\mathrm{v} 2} \frac{\pi C_{\mathrm{a}-\mathrm{v}}}{6 s_{\mathrm{a}-\mathrm{v}}^{3}} \tag{3.37}
\end{equation*}
$$

The interaction between the two continuum regions [from Eq. (3.29) and the expression in Figure 3.10d] contributes

$$
\begin{equation*}
\frac{\mathcal{V}_{\mathrm{v}-\mathrm{v}}}{S}=-n_{\mathrm{v} 1} n_{\mathrm{v} 2} \frac{\pi C_{\mathrm{v}-\mathrm{v}}}{12 s_{\mathrm{v}-\mathrm{v}}^{2}} \tag{3.38}
\end{equation*}
$$

The gap $d_{\mathrm{g}}$ between the plane and the surface of the continuum is chosen so as to count the effects of each atom exactly once, in the long-range attraction limit. Figure 3.12 graphs the energy, force, and stiffness resulting from this model for several sets of parameters.

### 3.5.3. Molecular models and bounded continuum models

Molecular mechanics methods can be used to calculate the mechanical properties of ${ }^{\circ}$ diamondoid bulk materials, and to relate bulk properties (such as elastic ${ }^{\circ}$ modulus) to the properties of nanoscale components of similar structure (Section 9.4). The mechanical behavior of stable diamondoid structures is often well approximated by linear elastic models; the atomic details of their interiors are then irrelevant to their external properties and can be neglected in much of the design process. Note that such approximations are of little use in standard organic chemistry, where large, stiff, regular structures are rare, and likewise in oprotein chemistry, where structures are flexible and highly inhomogeneous.

For irregular surfaces in contact, there often is no substitute for modeling at the level of interatomic potentials. Nonetheless, Eqs. (3.18) and (3.19) provide approximate formulas for the stiffness and energy of repulsive interactions as a function of the applied compressive force. These interactions are relatively insensitive to details of surface structure (within the class of structures of chief

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-05.jpg?height=1298&width=1112&top_left_y=169&top_left_x=303)

Figure 3.12. Interaction of pairs of surfaces according to Eqs. (3.33)-(3.38), with the following parameters (identical for both surfaces):

| Curve | $n_{\mathrm{a}}$ <br/> $\left(10^{19} / \mathrm{m}^{2}\right)$ | Atom type <br/> $(\mathrm{MM} 2)$ | $n_{\mathrm{v}}$ <br/> $\left(10^{29} / \mathrm{m}^{3}\right)$ | Atom type <br/> $(\mathrm{MM} 2)$ | $d_{\mathrm{g}}$ <br/> $\left(10^{-9} \mathrm{~m}\right)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\mathrm{a}$ | 0.9 | $\mathrm{C}(1)$ | 1.50 | $\mathrm{C}(1)$ | 0.09 |
| $\mathrm{~b}$ | 0.9 | $\mathrm{C}(1)$ | 0.75 | $\mathrm{C}(1)$ | 0.09 |
| $\mathrm{c}$ | 1.8 | $\mathrm{C}(1)$ | 1.50 | $\mathrm{C}(1)$ | 0.09 |
| $\mathrm{~d}$ | 1.8 | $\mathrm{C}(1)$ | 0.75 | $\mathrm{C}(1)$ | 0.09 |
| $\mathrm{e}$ | 1.4 | $\mathrm{Si}(19)$ | 1.50 | $\mathrm{C}(1)$ | 0.13 |

interest here). In the attractive regime, the comparatively long-range nature of van der Waals forces motivates the use of a continuum approximation, leading to the formulas presented in Figure 3.10. Based on the these observations, Chapter 9 develops bounded continuum models that permit a limited but atomically motivated return to continuum approximations like those used throughout macromechanical engineering.

### 3.6. Conclusions

The potential energy surface of a ground-state system determines its mechanical properties. Molecular orbital methods familiar in chemistry can provide descriptions of the PES for analyzing mechanochemical processes and small nanomechanical structures, but computational costs grow steeply with system size. For designing nanomechanical components, molecular mechanics models such as MM2 are appropriate, available, and computationally affordable. Molecular mechanics methods and models based on them are used throughout later chapters. Specialized potential energy functions for bond cleavage and abstraction reactions are useful in analyzing some mechanochemical processes, and are applied in Chapter 8. The MM2 potential energy function has here been used to develop a PES for surface-surface interactions that omits atomic detail, providing a basis for continuum models that describe the interaction of adjacent nanoscale components. These models are developed further in Chapters 9 and 10.

### 3.7. Further reading

This chapter and the next outline topics that are foundational not only to molecular nanotechnology, but to conventional chemistry and chemical physics, hence an extensive literature already exists. This section suggests some points of departure for those wishing to explore these topics in more depth.

Molecular quantum mechanics. The foundations of molecular quantum mechanics have not changed in decades, and many textbooks teach the subject. Examples include Atoms and Molecules (Karplus and Porter, 1970) and Molecular Quantum Mechanics (Atkins, 1970). A useful volume for orientation to the subject is Quanta: a handbook of concepts (Atkins, 1974), a cross-referenced, alphabetically organized work containing essays, equations, and diagrams on most quantum mechanical phenomena in molecules.

Computational methods in quantum mechanics have advanced greatly over the decades. An introduction to the subject from a user's perspective is $A$ Handbook of Computational Chemistry (Clark, 1985); this volume includes concrete examples of the use of popular programs along with less perishable information on techniques and pitfalls in the field. The methods of $a b$ initio molecular orbital theory are described in Ab Initio Molecular Orbital Theory (Hehre et al., 1986) together with descriptions of numerous computational results.

Potential energy surfaces. A general introduction to molecular mechanics methods is given by Molecular Mechanics (Burkert and Allinger, 1982). A Handbook of Computational Chemistry (Clark, 1985) includes descriptions of MM2, although its main focus is on quantum chemistry.

Molecular mechanics methods are evolving rapidly. A common operation is to find a local minimum on the PES; so-called Newton methods have usually required storage space proportional to $N^{2}$ (where $N$ is the number of atoms) and a computational time proportional to $N^{3}$, but more recent algorithms have better scaling laws: $N^{1.5}$ and $N^{2}$ respectively (Ponder and Richards, 1987a). For engineering work, fast, rough approximations are of considerable value in the early stages of design and analysis; a method has been reported that gives results similar to MM2 using simpler, faster code based purely on pairwise, interatomic central forces (Saunders and Jarret, 1986). Quantum chemistry methods are being used to improve molecular mechanics models, for example, in work supported by the Consortium for Research and Development of Potential Energy Functions (Hagler et al., 1989).

Intermolecular forces are complex, though most are weak enough to be neglected in nanomechanical engineering. A good introduction is The Forces Between Molecules (Rigby et al., 1986); a more advanced book is Intermolecular Forces: Their Origin and Determination (Maitland et al., 1981). An excellent text that emphasizes interactions between objects and forces in liquids is Intermolecular and Surface Forces (Israelachvili, 1992). The broad literature on surface science and surface chemistry contains much that is relevant, but often focuses on surfaces that are unstable and reactive; these need not be used in nanomechanical devices.

Potential energy surfaces for atom-transfer (abstraction) reactions are discussed in Levine and Bernstein (1987) and at greater length in Bérces and Márta (1988); both include extensive references to the literature. Truhlar and Steckler (1987) review potential energy surfaces for more complex reacting systems.

[^4]: Relativistic effects in heavy atoms cause strong spin-orbit coupling, which can increase the rate of electronic transitions such as the flipping of unpaired electron spins in free radicals, with consequent effects on the rates of chemical reactions (Section 8.4.4b). For typical molecules of interest, however, spin-orbit coupling does not significantly affect structure or dynamics before or after the transition.
[^5]: The basic nature of the equation suggests why calculations are difficult. Using samples at 10 points to approximate the integral of a one-dimensional function is often easy, though not always very accurate. But consider a function in a 126-dimensional space: sampling a $10 \times 10 \times 10 \times 10 \times \ldots$ grid would require an impossible $10^{126}$ function evaluations. Solving a differential equation with boundary conditions is generally more difficult than integration, and finding a wave function for the electrons in benzene, for example, presents a problem of this sort in a 126-dimensional space.
[^6]: Calculations using different basis sets or corrections for electron correlation are described as being at different "levels of theory." They might better be described as different levels of approximation, with the more accurate levels converging on the Born-Oppenheimer approximation to the Schrödinger equation.
[^7]: Modeling of 'lone pairs as pseudoatoms with bond-bending interactions incorrectly prohibits the inversion of ${ }^{\circ}$ amines, a process in which the lone pair smoothly redistributes to the other face of the group. To picture a lone pair, first imagine a methane molecule, tetrahedral $\mathrm{CH}_{4}$. Now imagine that one of the $\mathrm{H}$ nuclei (a proton) is somehow moved to the carbon nucleus: the result is ammonia, $\mathrm{NH}_{3}$. What happens to the two electrons that previously formed a $\mathrm{CH}$ bond? They remain in the same region, but having no proton to attract them, they spread to occupy more space. This bulge of electron density is the nitrogen lone pair, modeled in MM2 by burying an atomlike object in the outer regions of the $\mathbf{N}$ atom. Oxygen is treated as having two lone-pair pseudoatoms, but in fluorine the three lone pairs blend into a distribution treated as symmetric; neon has perfect spherical symmetry.
[^8]: The Schrödinger equation in the form given by Eq. (3.1) assumes electrostatic interactions between all particles everywhere, which cannot be quite right: electrons move, and the speed of light is finite, and so the fields must lag. In a theoretician's world in which fields propagate instantaneously, interactions are termed nonretarded and often have simpler mathematical descriptions. Owing to retardation, London dispersion forces at large separations fall off as $r^{-7}$ rather than the $r^{-6}$ stated by Eq. (3.28); this is described by the Casimir-Polder equation. In solution, retardation effects are important at separations greater than $\sim 5 \mathrm{~nm}$ (Israelachvili, 1992).
[^61]: Hamaker constants for metals from Israelachvili (1992). Values for $n, \varepsilon$ from Gray (1972), Lide (1990).
[^9]: This is not universal: metal surfaces (for example) would undergo bonding rather than repulsion; potential functions are discussed in Israelachvili (1992).