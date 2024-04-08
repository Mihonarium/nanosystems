# Molecular Dynamics


### 4.1. Overview

Molecular dynamics is fundamental to molecular machinery and has received extensive study in physical chemistry and chemical physics. Chapters 5-8 all deal with specific aspects of molecular dynamics; the present chapter provides a brief overview of the topic, examining the applicability of various approaches to nanomechanical problems. Section 4.2 reviews methods used in nonstatistical descriptions of molecular dynamics, considering both quantum mechanical and classical models for the calculation of system trajectories. Section 4.3 reviews statistical descriptions of molecular dynamics (both classical and quantum mechanical), including a discussion of the relationships among entropy, information, and computation. Section 4.4 returns to the issue of PES approximations, using dynamical principles to examine the differing requirements for accuracy that arise in different applications. As in the previous chapter, suggestions for further reading are appended.

### 4.2. Nonstatistical mechanics

This section outlines several nonstatistical descriptions of molecular dynamics used in scientific work, commenting on their applicability to nanomechanical engineering problems.

### 4.2.1. Vibrational motions

Molecular vibrations have been extensively studied in connection with infrared spectroscopy, and observed infrared vibrational frequencies are a major constraint used in determining parameters for molecular mechanics energy functions. Small displacements of a stiff structure from its equilibrium geometry are associated with nearly linear restoring forces. This permits the use of a harmonic approximation, in which the vibrational dynamics can be separated into a set of independent normal modes and the total motion of the system can be treated as a linear superposition of normal-mode displacements. This common approximation is of considerable use in describing nanomechanical systems.

Since both classical and quantum mechanics permit exact solutions for the harmonic oscillator, the time evolution of systems can readily be calculated in the harmonic approximation. In real systems, nonlinear effects permit energy exchange among vibrational modes, causing relaxation to thermal equilibrium. The equilibrium state, in turn, is best described by the methods of statistical mechanics. A nonstatistical description of vibrational motion is of interest chiefly during (or within a few relaxation times of) the excitation of a vibrational mode by a nonthermal energy source.

### 4.2.2. Reactions and transition rates

a. Molecular beam experiments. Vibrations involve motion within a potential well; reactions involve transitions between potential wells. Molecular reaction dynamics has been extensively studied by means of crossed molecular beams, and a major application (and test) of potential energy functions for chemical reactions has been the calculation of vibrational states and angular distributions resulting from reactive scattering.

With high-quality beams of simple molecules, one can observe quantum mechanical oscillations in the angular distribution of scattered trajectories. These result from interference among alternative collision paths that yield indistinguishable outgoing molecular trajectories and states. A broader distribution of initial energies and angles will obliterate these fine features, however, yielding a smooth distribution of product trajectories.

In practice, calculations of molecular reaction dynamics commonly are based on the quasiclassical approximation (Levine and Bernstein, 1987). In this approximation, initial molecular states of vibration and rotation are described classically, but are chosen with initial energies and angular momenta that match quantum constraints. Quantum mechanical uncertainties in position are modeled by calculating many trajectories with randomly chosen vibrational and rotational phase angles. Trajectories are then computed by integrating the classical equations of motion. Finally, quantization of outcomes is modeled by lumping final trajectories into bins in phase space such that each bin corresponds to a permissible quantum state of the product. These calculations cannot yield quantum interference patterns or resonances, but give reasonably accurate descriptions of the coarse dynamical features of a reactive collision, such as the overall distribution of scattering angles and vibrational excitations.

b. Solution and machine phase vs. molecular beams. Coarse features from a reaction dynamics perspective are, however, fine features from the perspective of a chemist or a nanomechanical engineer. Chemical reactions in nanomechanical systems bear little resemblance to reactions in crossed molecular beams. In an extended solid system subject to relatively slow mechanical motions, reactive molecular components do not encounter one another with well-defined energies and momenta; broad, thermal distributions dominate. Likewise, during the course of the encounter, the reactive components do not form an isolated system with locally conserved energy, momentum, and angular momentum; the reactive system remains coupled to a thermal bath. The notion of a scattering angle is meaningless, and reaction-induced vibrational excitations are quickly thermalized.

In these respects, reactions in nanomechanical systems resemble the solution-phase reactions familiar to chemists. In such systems, the chief concern is with overall reaction rates, not with the details of trajectories. As a consequence, the detailed shape of the PES (crucial to the details of reactive scattering) is of reduced importance. Reaction rate data only weakly constrain PES properties. Given a few properties of the PES, thermally activated reaction rates are calculated using classical or quantum mechanical transition state theories based on statistical mechanics; these are discussed in Chapter 6.

### 4.2.3. Generalized trajectories

a. Classical dynamical models. Even in the absence of reactive transformations, the motions of typical nanomechanical systems cannot be completely described in terms of vibrations. Like protein chains or molecules in a liquid, these systems typically permit large displacements subject to complex, interacting constraints. Their motions must be described by more general methods.

It is common practice to model the trajectories of such systems by integrating the classical equations of motion, deriving the forces on each atom from approximate potential functions (e.g., molecular mechanics potentials). Where statistical properties are desired, a common approach is to integrate the equations of motion for a substantial time, taking a time average of the quantities of interest. Time steps are typically $\sim 10^{-15} \mathrm{~s}$, and current computers have been used to follow the dynamics of $\sim 10^{3}$ atom systems for $\sim 10^{-9} \mathrm{~s}$. These techniques are suitable for describing the short-term dynamics of nanomechanical components.

b. Quantum corrections. Quantum effects on molecular trajectories can be approximated by an adaptation of classical molecular mechanics techniques in which each atom is represented by a circular chain of atoms with suitable interactions; this has been applied to large molecules, such as the protein ferrocytochrome $c$ (Zheng et al., 1988). The effects are, as one would expect, largest for high-frequency vibrations, such as bond stretching, bending, and torsional motions involving hydrogen atoms. From a statistical perspective, thermal motions result in a certain probability density function for the positions of atoms with respect to their surroundings, and quantum effects broaden this probability density function.

c. Dynamical regimes and corresponding models. The dynamical behavior of nanomechanical systems can be partitioned into three categories: (1) thermally excited vibrational motions within potential wells, (2) thermally excited transitions between potential wells, and (3) other motions, driven by nonthermal energy sources. Motions in category 1 can be treated either classically or quantum mechanically; Chapter 5 compares the statistical distributions resulting from classical and quantum models. Chapter 6 examines motions in category 2 , again comparing classical and quantum approaches within a statistical framework. Most motions encountered in category 3 are of low frequency and hence little influenced by quantum effects at ordinary temperatures. They can usually be modeled by applying classical dynamics to molecular mechanics potentials, or (on somewhat larger scales) to bounded continuum models (Section 9.3.3).

### 4.3. Statistical mechanics

Statistical mechanics (also known as statistical or molecular thermodynamics) is most commonly applied to relate macroscopic thermodynamic properties to statistical descriptions of the behavior of large numbers of molecules. En route to describing properties of bulk matter, statistical mechanics frequently describes probability distributions for underlying molecular variables, such as position and velocity. In the present context, it is these probabilistic descriptions of the behavior of individual molecular objects that are of primary value.

Statistical mechanics can frequently provide estimates of the statistical behavior of nanomechanical systems without the computational cost of running a detailed dynamical simulation for long periods of time. Today, it is expensive to do a simulation of $10^{3}$ atoms for as long as $10^{-9} \mathrm{~s}$, yet a nanomechanism that fails even once per millisecond may be unacceptable. Estimating failure rates by observing more than $10^{6}$ expensive simulations would be impractical. Statistical mechanics, in contrast, can provide estimates for the frequencies of extremely rare events using efficient analytical methods.

Statistical mechanics is commonly used to calculate quantities such as pressure, entropy, and free energy based on averages taken over many molecules in thermal equilibrium. But can temperature, for example, be used to describe a single molecule? There is no fundamental difference between (1) the statistical distribution of a dynamical quantity computed for many similar molecules at a particular instant (which is the usual concern of statistical mechanics), (2) the statistical distribution computed for a single representative molecule over a long period of time, and (3) the probability distribution for a single molecule at a single time. Accordingly, the concepts of pressure, entropy, free energy, and the like can be used to reason about (for example) the expected mean efficiency of a single nanomachine in a single operational cycle. The only caveat stems from the assumption of equilibrium; this is discussed in Section 4.3.4, and the subtle relationship between measurement and equilibrium is discussed in Section 4.3.5.

### 4.3.1. Detailed dynamics vs. statistical mechanics

By omitting dynamical details, statistical mechanics provides a simplification that can assist both calculation and understanding. In the operation of real nanomechanical systems, the initial conditions are never known with the precision assumed in classical dynamical models, and seldom with the precision assumed in quantum dynamical models. Instead, the motions and displacements resulting from thermal excitation are random variables subject to some distribution. Rather than introducing arbitrary assumptions, statistical mechanics takes these uncertainties as fundamental, yielding inherently probabilistic descriptions of system behavior.

The nanomechanical engineer's task, then, is to devise systems in which all probable behaviors (or all but exceedingly improbable behaviors) are compatible with successful system operation. This typically requires designs that present low energy barriers to desired behaviors, and high energy barriers to undesired behaviors, in which the high energy barriers often are a consequence of the use of stiff components.

Even if one were to assume classical, deterministic behavior and nearly perfect information regarding initial conditions, a typical nanomechanical system would soon require a statistical description. Consider the trajectory of a particle rebounding from an atom: because atoms are not flat, a small perturbation typically causes a particle to rebound at a different angle, leading to a larger perturbation at its next point of impact. In a typical system, trajectories that are initially almost identical will rapidly diverge until they have no similarity. This divergence is characteristic of chaos. Further, real nanomechanical systems are in mechanical or radiative contact with an environment at some nonzero temperature, providing a constant source of unpredictable thermal excitations.

### 4.3.2. Basic results in equilibrium statistical mechanics

Statistical mechanics takes its simplest form for systems at thermodynamic equilibrium. Since this is often a good approximation for real systems, some basic results are worth summarizing. [This discussion largely follows (Knox, 1971).]

a. Quantum statistical mechanics. In quantum statistical mechanics, it is convenient to consider a system that is in thermal equilibrium with a heat bath, yet is assumed to have a set of bath-independent quantum states $i=0,1,2, \ldots$ In equilibrium statistical mechanics, a complete description of a system consists of a specification of the probability, $P(i)$, for each state $i$. This takes the form

$$
\begin{equation*}
P(j)=\frac{\exp [-\mathscr{E}(j) / k T]}{\sum_{i=0}^{\infty} \exp [-\mathscr{E}(i) / k T]} \tag{4.1}
\end{equation*}
$$

where $\mathscr{E}(j)$ represents the energy of state $j$. The probability that the system is in state $i$ is proportional to the Boltzmann factor, $\exp [-\mathscr{E}($ state $) / k T]$, and all states of a given energy are thus equally probable.

A quantity of special importance is the denominator of the above expression,

$$
\begin{equation*}
q=\sum_{i=0}^{\infty} \exp [-\mathscr{E}(i) / k T] \tag{4.2}
\end{equation*}
$$

where $q$ is a temperature-dependent pure number termed the partition function of the system (note that its magnitude depends on the choice of the zero of the energy scale). The partition function can be related to the variables of classical thermodynamics. The mean energy of the system is given by an expression involving a constant-volume derivative of the partition function

$$
\begin{equation*}
\overline{\mathscr{E}}=k T^{2}(\partial \ln q / \partial T)_{V} \tag{4.3}
\end{equation*}
$$

as is the ${ }^{\circ}$ entropy

$$
\begin{equation*}
\mathscr{S}=[\partial(k T \ln q) / \partial T]_{V} \tag{4.4}
\end{equation*}
$$

The ${ }^{\circ} \mathrm{Helmholtz}$ free energy is

$$
\begin{equation*}
\mathscr{F}=-k T \ln q=\mathscr{E}-T \mathscr{S} \tag{4.5}
\end{equation*}
$$

and the pressure is given by a constant-temperature derivative

$$
\begin{equation*}
p=-(\partial \mathscr{F} / \partial V)_{T}=k T(\partial \ln q / \partial V)_{T} \tag{4.6}
\end{equation*}
$$

b. Classical statistical mechanics. Paralleling the quantum case, in classical statistical mechanics it is common to consider a system that is in thermal contact with a heat bath, yet is treated as having a bath-independent energy function, $\mathscr{E}$ (state). For a mechanical system, a state is defined as a point in the phase space defined by the set of position coordinates $q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}$ (the position), and the corresponding momentum coordinates $p_{1}, p_{2}, p_{3}, \ldots, p_{3 N}$ (the momentum), where $N$ is the number of atoms. Here, a complete description consists of a specification of the probability density function (PDF) over phase space. The fundamental result is

$$
\begin{equation*}
f_{\text {state }}(\text { state })=\frac{\exp [-\mathscr{E}(\text { state }) / k T]}{\int_{p, q} \ldots \int \exp [-\mathscr{E}(\text { state }) / k T] d p_{1} d q_{1} d p_{2} d q_{2} \ldots d p_{3 N} d q_{3 N}} \tag{4.7}
\end{equation*}
$$

where the PDF, $f_{\text {state }}$ (state), is the probability of occupancy per unit volume of phase space associated with each point in that space.

The denominator of the above expression (times a factor demanded by the correspondence principle[^10]) defines the classical partition function for a solid

$$
\begin{equation*}
q_{\mathrm{c}}=(2 \pi \hbar)^{-3 N} \int_{p, q}^{\ldots} \int \exp [-\mathscr{E} / k T] d p_{1} d q_{1} d p_{2} d q_{2} \ldots d p_{3 N} d q_{3 N} \tag{4.8}
\end{equation*}
$$

which (in the classical approximation) can be used as the value of the partition function in Eqs. (4.3) through (4.6).

In nanomechanical design, a common concern is the probability that a thermally excited system will be found in a particular configuration at a particular time. Molecular mechanical systems can usually be described in terms of motion on a single potential energy surface, and the total energy can be divided into potential energy and kinetic energy terms

$$
\begin{equation*}
\mathscr{E}(\text { state })=\mathscr{V}(\text { position })+\mathscr{T}(\text { momentum }) \tag{4.9}
\end{equation*}
$$

With this division, Eq. (4.7) can be factored, and by integrating over the momentum coordinates of the phase space, a PDF over the position coordinates alone (the classical equilibrium PDF in configuration space) can be obtained

$$
\begin{equation*}
f_{\text {position }}(\text { position })=\frac{\exp [-\mathscr{V}(\text { position }) / k T]}{\int_{q} \ldots \int \exp [-\mathscr{V}(\text { position }) / k T] d q_{1} d q_{2} \ldots d q_{3 N}} \tag{4.10}
\end{equation*}
$$

Note that the probability density associated with a position in configuration space is (save for a normalization factor) dependent purely on its potential energy. The distribution of momenta and kinetic energies is independent of the configuration, and hence the mean kinetic energy of a classical system at thermal equilibrium remains unchanged in all configurations. (This uniform behavior of the momentum components simplifies the description of nanomechanical systems near thermal equilibrium, making the configuration space picture of Section 4.3.3 more useful.)

Classical statistical mechanics is frequently a useful approximation. At ordinary temperatures its significant failings occur chiefly in stiff, high-frequency modes; these usually have little effect on the dynamics of nanometer-scale diamondoid components (which are by these standards soft, slow, and ponderous). Chapter 5 examines positional PDFs describing various elementary nanomechanical systems, comparing the results of quantum and classical models; its results indicate the limits within which classical statistical mechanics yields accurate results regarding positional uncertainty in nanomechanical engineering systems.

### 4.3.3. The configuration-space picture

Although it yields no new physical information, it can be helpful to regard a classical mechanical system containing $N$ atoms as a single moving point in a configuration space of $3 N$ dimensions, in which each of the three Cartesian coordinates of each atom corresponds to one dimension. Adding a single, orthogonal, "vertical" dimension to represent potential energy yields a potential energy surface in configuration space (Chapter 3). The configuration point can then be imagined as sliding over an undulating, frictionless surface subject to a gravitational force-depending on initial conditions and the shape of the surface, the point may oscillate in a potential well, move along a valley, pass from one well to another through a ${ }^{\circ} \mathrm{col}$ between peaks, and so forth.

To make this dynamical picture work out properly, the configuration-space coordinates corresponding to an atom must vary in proportion to the Cartesian space coordinates of the atom multiplied by $m^{-1 / 2}$, where $m$ is the mass of the atom. The kinetic energy of the coordinate point is then an isotropic function, depending only on the square of the speed.

In configuration space, a linear, elastic system corresponds to a point moving in a single potential well (neglecting translational and rotational degrees of freedom). For a two-atom system (approximating the bond as a linear spring and neglecting rotational degrees of freedom), this is a simple parabola. For a noncolinear $\mathrm{N}$-atom system, the potential well retains a parabolic form along any line through the equilibrium point, and the isopotential surfaces are concentric $3 N-6$ dimensional ellipsoids; each of the $3 N-6$ axes of an ellipsoid represents the line of motion of a normal mode. A nonlinear system might permit (for example) the interchange of two atoms given a sufficiently great thermal excitation; the corresponding region of the potential surface has two wells joined by a pass.

a. Probability gas in configuration space. For a classical system at thermal equilibrium with a heat bath, statistical mechanics asserts that the probability density of the configuration point is an inverse exponential function of the energy, here represented by the height. Thus, the probability density varies across the configuration-space landscape much as the atmospheric density varies across a real landscape (Figure 4.1). The configuration-space point is like a gas consisting of a single molecule, with a well-defined mean density, flux, and so forth, at every point.

As in an equilibrated atmosphere (unlike Earth's convecting atmosphere), the mean kinetic energy, and hence the temperature, is independent of the height of the land. The equilibrium ratio of the total probability in two connected valleys depends on their effective volumes; these depend on size and altitude, which correspond to the entropy and energy of the corresponding states. The rate at which probability diffuses through a col between the valleys depends on the height and width of the pass, and on the mean speed and overall probability density of the configuration point. All of these factors appear in transitionstate theory (Chapter 6).

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-15.jpg?height=323&width=863&top_left_y=174&top_left_x=437)

Figure 4.1. A one-dimensional PES shaded to illustrate the probability gas visualization of the equilibrium distribution in configuration space. The state boundaries are drawn in accord with the rules in Section 4.3.3b, but omitting those that correspond to energy barriers that are small compared to $k T$ (these would otherwise subdivide state 1 into three regions).

In statistical mechanics, the principle of detailed balancing asserts that, at equilibrium, the mean rate of transitions from state 1 to state 2 equals that from state 2 to state 1 for all pairs of states. For states defined as regions in configuration space, this has an intuitive interpretation. At equilibrium, gas molecules cross any arbitrarily defined surface element at equal rates from both sides; this is likewise true for the configuration-point gas, and for each surface element of the boundary separating any two states.

b. States in configuration space. The configuration space picture suggests one natural way to define what is meant by "distinct states" of a solid or liquid system (Stillinger and Weber, 1984).[^55] From each point on the energy landscape, there exists a path of steepest descent, and that path always ends in a point or

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-15.jpg?height=482&width=603&top_left_y=1334&top_left_x=285)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-15.jpg?height=482&width=492&top_left_y=1346&top_left_x=943)

Figure 4.2. Definition of states in terms of potential energy minima. Panel (a) shows a potential energy surface defined over a two-dimensional configuration space; Panel (b) shows the same surface as a contour map partitioned into regions corresponding to local potential energy minima (marked by minus signs).

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-16.jpg?height=663&width=1201&top_left_y=197&top_left_x=171)

Figure 4.3. Molecular dynamics simulation of $n$-octane at $400 \mathrm{~K}$ (MM2/CSC). The upper row illustrates molecular configurations at 10 ps intervals, starting after 10 ps of equilibration at the target energy. Each configuration is labeled with its potential energy relative to the minimum-energy configuration for the molecule, and corresponds to a point on a potential energy surface analogous to that shown in Figure 4.2. Lower row: structures and energies of the corresponding state-defining minima, which in the third state happened to be the global minimum. Note that energy differences between conformers frequently are small. Treating all atoms as distinguishable, the number of distinct conformers for octane is on the order of $3^{7}=2187$ (but this is reduced by excluded-volume effects). ${ }^{\circ}$ Conformationally mobile structures like $n$ octane are unsuitable for most nanomechanical applications.

region of locally minimal energy. Thus, points correspond to minima, and each local energy minimum can be taken to mark a distinct state, as indicated in Figure 4.2. Figure 4.3 illustrates configurations and corresponding state-defining minima for $n$-octane in a molecular dynamics simulation.

Minima separated by barriers small compared to $k T$ can often be regarded as a single minimum, because the barriers are crossed so easily. A system acting as a good rotary bearing (Section 10.4), for example, will exhibit a chain or loop of minima having essentially the same depth and separated by barriers of negligible height. For all practical purposes, a chain or loop of this sort constitutes a single potential well. In a properly designed nanomechanical system, cols between potential wells are either functional parts of the design, or are high enough to block any substantial probability flux.

c. Constraints and thermal excitation. Even without being able to visualize interconnected, approximately ellipsoidal potential wells, or ring-shaped valleys in a high-dimensional space, one can get a sense of the strongly constrained nature of the motion of the configuration point in such systems. A similar description of a chemically reacting solution-phase system lacks such well-defined features. Each possible covalent combination of atoms forms a separate valley, and the valleys intertwine in a manner that brings each into close proximity with many others. Which cols are available-determining which reactions can occur at appreciable rates-depends on the relative heights and widths of the numerous connections between valleys. A chemist attempting to control the pattern of reactions must exploit small differences in the heights and effective volumes (the energies and entropies) of cols and valleys. In a nanomechanical system, in contrast, a reaction might occur between two groups brought together by a gearlike rotary motion. The available configuration space consists of two ringshaped valleys linked by a single col of modest height. Unwanted reactions can be prevented by gross mechanical constraints, rather than by small differences in energy and entropy.

The configuration-space picture is most useful when applied to a subsystem that is coupled to a larger system that acts as a thermal bath. This can be described in terms of the potential surface that would arise if the rest of the system were motionless and fully relaxed for all subsystem configurations, combined with a time-varying perturbing potential representing the effects of thermal vibrations external to the subsystem. In this picture, the landscape vibrates, and total energy of the configuration point is not a constant.

### 4.3.4. Equilibrium vs. nonequilibrium processes

The relationships cited in Section 4.3.2 describe equilibrium systems, but a functioning nanomechanical system, with motions driven by input power, is not at equilibrium. How useful, then, is equilibrium statistical mechanics?

Equilibrium statistical mechanics is seldom applied to a true equilibrium system. Matter under ordinary conditions of temperature and density, for example, has crystalline iron as its equilibrium state-if one allows true equilibration of all the nuclear degrees of freedom. In practice, the necessary reactions (e.g., fusion) proceed so slowly that they can be ignored. States (or dynamical domains) that are sufficiently ${ }^{\circ}$ metastable can be treated as stable in calculating "equilibrium" properties.

In macromechanical systems, mechanical motion and thermal motion are quite distinct. In nanomechanical systems, this distinction usually remains clear. Thermal velocities may exceed the imposed mechanical velocities (which in most instances considered are quite small), but thermal velocities (unlike mechanical) have a mean value of zero and are independent of any driving force.

a. Deviations from equilibrium. In mechanical systems, frictional forces convert mechanical energy into ${ }^{\circ}$ thermal energy in a spatially inhomogeneous fashion, causing thermal gradients. In estimating the fluctuations resulting from thermal motion, small regions of matter in such systems can then be approximated as being at thermal equilibrium save for deviations associated with temperature gradients, heat flows, and changing temperatures. When these deviations are small, equilibrium models give good estimates of the statistics of thermally induced displacements and motions in nanomechanical systems.

A small thermal gradient is one that produces only a small difference in the absolute temperature across the diameter of the system under analysis. For a nanomechanical system with a diameter of $10 \mathrm{~nm}$, a $1 \% \Delta T$ (at $300 \mathrm{~K}$ ) requires a gradient of $3 \times 10^{8} \mathrm{~K} / \mathrm{m}$. Assuming a thermal conductivity of $10 \mathrm{~W} / \mathrm{m} \cdot \mathrm{K}$, this yields a thermal power flux of $3 \times 10^{9} \mathrm{~W} / \mathrm{m}^{2}$. This "small" thermal gradient produces a large (i.e., often unacceptable) temperature difference of $300 \mathrm{~K}$ in a modest $10^{-6} \mathrm{~m}$ distance.

A small thermal flux is one that produces only a small difference in the equilibrium distribution of thermal vibrations. This equilibrium distribution is characterized by large power fluxes (which cancel, at equilibrium) on the order of (speed of sound $) \times($ thermal energy $) /($ volume $)$. For a typical material at ordinary temperatures, this is on the order of $\left(3 \times 10^{8} \mathrm{~J} / \mathrm{m}^{3}\right) \times\left(10^{3} \mathrm{~m} / \mathrm{s}\right)=3 \times 10^{11} \mathrm{~W} / \mathrm{m}^{2}$. One percent of this value again corresponds to a net thermal power flux of $3 \times 10^{9} \mathrm{~W} / \mathrm{m}^{2}$. Since thicker layers result in unacceptable values of $\Delta T$, a "small" power flux of this magnitude would be encountered in a working system only if a $\sim 10^{-6} \mathrm{~m}$ (or less) thick slab were to dissipate power at $\sim 10^{15} \mathrm{~W} / \mathrm{m}^{3}$ (or more). Despite the extraordinarily high power-conversion densities possible in small components (see Section 2.2.2), the power-dissipation densities for most complex, multicomponent systems will be small compared to this value.

A small rate of change of temperature is one that produces only a small $\Delta T$ during the characteristic vibrational relaxation time. In a crystal, a measure of this relaxation time is the phonon mean free path divided by the speed of sound; a typical value might be $\left(10^{-8} \mathrm{~m}\right) /\left(10^{3} \mathrm{~m} / \mathrm{s}\right)=10^{-11} \mathrm{~s}$. In a highly inhomogeneous medium (e.g., a typical nanomechanical system), with highly anharmonic interactions (e.g., van der Waals contacts between moving parts), relaxation times typically are shorter. A $1 \% \Delta T$ (at $300 \mathrm{~K}$ ) during a single relaxation time then corresponds to a rate of temperature change in excess of $3 \times 10^{11} \mathrm{~K} / \mathrm{s}$. For typical volumetric heat capacities $\left(\sim 10^{6} \mathrm{~J} / \mathrm{K} \cdot \mathrm{m}^{3}\right)$, this "small" rate of temperature change requires a large power dissipation (as above, $\sim 10^{15} \mathrm{~W} / \mathrm{m}^{3}$ or more).

b. The process of thermalization. Because these "small" thermal gradients, thermal fluxes, and rates of temperature change are all so large, it is often acceptable to divide motions into mechanical and thermal components, describing the thermal motions in terms of the local temperature and the relationships of equilibrium statistical mechanics. The chief exceptions are in descriptions of the processes that convert mechanical motion into thermal excitation, where nonequilibrium vibrational motions are generated and then thermalized.

A typical nonequilibrium event is a transition from one potential well to another that is forced to occur at a particular time by an input of mechanical energy. In the configuration-space picture, the configuration point representing the subsystem passes through a col owing to an imposed change in the shape of the PES, and is thus injected into the new potential well with an unusually high energy and a somewhat-predictable momentum. Regarding the new well as nearly quadratic, the initial state can be viewed as one with a disequilibrium distribution of excitation of normal modes. Relaxation then involves two processes: a tendency toward equilibration of the distribution of modal excitation via anharmonic interactions (given an unusually high total energy) and a tendency toward equilibration of the expected total energy via interactions with a heat bath. For a general anharmonic system in weak contact with a thermal bath, a short-term description of the motion would describe families of trajectories; an intermediate-term description would treat all states of equal energy as equally probable, but would take account of the slowly decaying excess energy; and the long-term description would be in terms of the statistics of fully equilibrated thermal motion.

### 4.3.5. Entropy and information

a. Entropy and probability. The transition from a detailed dynamical description to a statistical description entails discarding information. State variables that are regarded as having definite values in the dynamical description are regarded as having probability distributions in the statistical description. In quantum statistical mechanics, distinct states can be enumerated, and the entropy, which can be stated as

$$
\begin{equation*}
\mathscr{S}=-k \sum_{\text {states }} P(\text { state }) \ln [P(\text { state })] \tag{4.11}
\end{equation*}
$$

is a weighted measure of the number of possible states. This expression yields the familiar result (the third law of thermodynamics) that a perfect crystal at absolute zero has zero entropy: the structure of the crystal is known and it in the vibrational ${ }^{\circ}$ ground state with unit probability; $1 \times \ln (1)=0$, hence $\mathscr{S}=0$. This result is equally true for any completely specified structure at absolute zero.

b. Information can increase free energy. Probability, however, depends on the information one possesses. If I flip a coin and peek at it, it may be heads with probability one for me, while remaining heads with probability $1 / 2$ for you. This may suggest that the entropy of an irregular solid at absolute zero is positive if these irregularities are unknown, but zero if they are completely described by some algorithm or external record (the complete specification just alluded to). If so, then entropy is not a local property of a physical system.

Studies of entropy and information confirm this view. In concrete terms, a structure (such as a polymer with a seemingly random sequence of monomers) can be made to yield more free energy if it is matched against another polymer with a sequence known to be identical-that is, if one has an external record of the sequence (Bennett, 1982). Information regarding the sequence increases the Helmholtz free energy of the polymer, Eq. (4.5), because it eliminates the possibility of many alternative states, and thus lowers $\mathscr{S}$. The free energy extracted from a system can thus depend on the existence of a record, initially located in the external environment, that is brought in, read, and returned unchanged.[^11] This understanding of entropy, although well established in the literature, contradicts the simple perspective presented in most textbooks. (For further discussion, see entropy in the glossary.)c. Entropy and computation. These issues are intimately related to questions regarding the theoretical energy requirements of computation. In the early 1960s, Landauer observed that compressing the logical state of a computer entails compressing its physical state (Landauer, 1961); for example, erasing or overwriting a one-bit storage device with previously unknown contents entails reducing its possible states (one or zero) to a single state (e.g., zero). Such a transformation dissipates a quantity of free energy $\mathscr{F} \geq \ln (2) k T$ per bit erased (Section 7.6.3).

Theorists have examined devices such as Brownian computers with idealized structures (i.e., hard, perfectly rigid parts of arbitrary shape) but subject to realistic dynamics and thermodynamics, as well as computational devices inspired by the molecular machinery of biological systems (Bennett, 1982), idealized, deterministic mechanical systems (Toffoli, 1981; Fredkin and Toffoli, 1982), and quantum mechanical models (Likharev, 1982; Feynman, 1985). These and related studies indicate that logically reversible computations-those where the output uniquely specifies the input - can be performed in a manner approaching thermodynamic reversibility (that is, the dissipation of free energy per logically reversible operation can be made arbitrarily close to zero). The literature and results in this field have been well reviewed (Bennett, 1982; Landauer, 1988). They provide an improved understanding of the second law of thermodynamics (and the impossibility of a Maxwell's Demon), and are of direct relevance both to mechanical nanocomputers and to many other nanomechanical systems.

### 4.3.6. Uncertainty in nanomechanical systems

In conventional mechanical systems, the positions and shapes of components are never completely known: manufacturing tolerances, measurement inaccuracies, and environmental vibrations ensure this. When systems work despite these uncertainties, it is because the uncertainties are kept within tolerable bounds, either by reducing uncertainty or by expanding the range of tolerance.

In nanomechanical systems, quantum and statistical mechanics place physical limits on the reduction of uncertainties. For a structure of a given mass and stiffness in equilibrium at a given temperature, positional uncertainties are fixed and irreducible (Chapter 5). Depending on the design of the system, these uncertainties can cause errors at a rate ranging from negligibly low to unacceptably high.

a. Quantum and classical parallels. There are strong qualitative parallels between the uncertainties of quantum mechanics and those of classical statistical mechanics. In both quantum and statistical mechanics, one begins with a potential energy function, $\mathscr{V}(\mathbf{r})$. In quantum mechanics, the Schrödinger equation ensures that a particle of a given energy has a nonzero (though often vanishingly small) probability of penetrating a potential barrier of any finite height and thickness, and of being found in any region of space. In classical statistical mechanics at finite temperature, Boltzmann's law yields the same qualitative result by assigning a nonzero (though often vanishingly small) probability to states of arbitrarily high energy. In quantum mechanics, a harmonic oscillator has a positional uncertainty characterized by a Gaussian probability distribution; classical mechanics at a finite temperature yields a result of the same form.

Quantum uncertainties measured as the product of the uncertainties in conjugate variables have an irreducible minimum, [^12] for example,

$$
\begin{equation*}
\Delta x \Delta p \geq \hbar / 2 \tag{4.12}
\end{equation*}
$$

but the uncertainty in either variable can be reduced to an arbitrary degree by a suitable measurement. Classical systems permit similar measurements, but present the illusion that the other variable can simultaneously be specified with arbitrary accuracy as well. This difference in the reducibility of uncertainty is, however, irrelevant in the context of equilibrium statistical mechanics. A measurement that reduces uncertainty also reduces entropy (Section 4.3.5) and hence alters the equilibrium of the system from the perspective of the observer, even if in the absence of a physical disturbance of the system itself. Thus, within the equilibrium statistical-mechanical description, uncertainties are irreducible by definition.

In a nanomechanical system, each component has many vibrational degrees of freedom, each subject to thermal excitation. Any attempt to use nanomechanical components within a system to represent the results of measurements performed on other nanomechanical components within a system can succeed in encoding only a small fraction of the information needed to represent the total vibrational state of the system. While one can imagine a device that uses measurement to reduce the uncertainties associated with one or a few critical components, systems will in general be dominated by components subject to statistical uncertainties that are in practice irreducible and that will (as indicated by Section 4.3.4) usually be well described by equilibrium statistical mechanics.

### 4.3.7. Mean-force potentials

Consider a piston that controls the volume of a cylinder containing an ideal gas. The work done in compressing the gas under isothermal conditions causes no change in the potential energy of the gas or of the piston, and yet so long as the system remains isothermal, the force exerted by the gas on the piston can be treated as the gradient of a potential energy function. This function defines a mean-force potential, since it describes the time-average forces experienced by the piston.

The use of a mean-force potential enables the statistical behavior of a portion of an equilibrium (or near-equilibrium) system to be described without including all the coordinates of the full PES. In the piston-and-gas example, the use of a mean-force potential enables the statistical distribution of piston positions and velocities to be calculated directly, without reference to the motions of each of the gas molecules (Section 5.6.2). In general, the mean-force potential defined over the retained coordinates is affected by the omitted coordinates to the extent that the position of the system with respect to the retained coordinates alters the permitted range of motion in the omitted coordinates. In the piston-and-gas example, the range of motion in the coordinates corresponding to the gas molecules is directly determined by the position of the piston; softer constraints on motion (e.g., time-varying ${ }^{\circ}$ elastic restoring forces) have analogous effects. The use of a mean-force potential treats work of compression, which reduces entropy, as equivalent to work done against elastic forces, which increases potential energy.

In quantitative terms, the work done against a mean-force potential (in the classical model) is just $\Delta \mathcal{V}-T \Delta \mathscr{Y}$; this equals $\Delta \mathscr{F}$, given that under isothermal conditions the change in kinetic energy $\Delta \mathscr{T}=0$. A mean-force potential can be applied where imposed motions are slow (permitting thermal equilibration), or where motions-however fast-are spontaneous and thermal, and hence result from the equilibrium state itself.

### 4.4. PES revisited: accuracy requirements

Both dynamical and statistical mechanical models of molecular behavior rely on potential energy surfaces that are (in all cases of nanomechanical interest) approximations known to deviate from reality. The scientific literature on potential energy surfaces describes efforts to improve the correspondence between experiment and theory, and hence focuses on the imperfections and limitations of existing models. In order to understand the utility of existing models from an engineering perspective, it is useful to consider the sensitivity of different physical phenomena to the existing inaccuracies.

### 4.4.1. Physical accuracy

In chemical physics, experiments are designed to provide stringent tests of theoretical models of molecular systems (including their potential energy surfaces), and the theoretical models attempt to predict everything that can be experimentally observed. As discussed in Chapter 3, physicists have made extensive use of molecular beam experiments in which molecules are prepared with precise momenta (and sometimes with control of vibrational states, rotational states, and polarization); they are then allowed to scatter (sometimes with a reactive exchange of atoms) and outcomes are observed and analyzed in terms of scattering angle (etc.).

The quantum interference effects that can be observed in such experiments provide a delicate test of potential energy surface models. Scattering events that involve bond formation and cleavage can traverse energy barriers of over $100 \mathrm{maJ}$, yet the interference effects are sensitive to much smaller energy differences. A characteristic molecular collision time is $>10^{-13} \mathrm{~s}$ (the time required to travel $10^{-10} \mathrm{~m}$ at $10^{3} \mathrm{~m} / \mathrm{s}$ ); changing the potential energy along one of the interfering paths by $1 \mathrm{maJ}$ or less shifts the phase of that path by a radian and causes a substantial change in the interference pattern. Since different trajectories explore different parts of the configuration space, describing interference effects correctly can require accuracy of this magnitude across the entire dynamically accessible potential energy surface.

### 4.4.2. Chemical accuracy

a. Predicting solution-phase reaction rates and equilibria is hard. In solution chemistry, a standard challenge is to predict chemical equilibria, absolute reaction rates, and the relative rates of competing reactions. Synthetic chemistry can be viewed as an engineering discipline aimed at constructing molecules. In this task, rates and equilibria are of central importance: if a reaction equilibrates several species, then the yield of the desired product will depend on the equilibrium concentration ratios; alternatively, if a reaction can proceed along any of several effectively irreversible paths, then the yield of the desired product will depend on the ratio of the reaction rates. In some reactions, yields are affected by both rates and equilibria.

If entropic factors are equal, then the equilibrium ratio of two species is an exponential (Boltzmann) function of the difference in potential energy between the species. Likewise, if entropic factors (and certain dynamical factors) are equal, then the ratio of the rates of two competing reactions is an exponential function of the difference in potential energy between the two transition states. At $300 \mathrm{~K}$, a difference of $1 \mathrm{maJ}$ changes rates and equilibria by a factor of 1.27 , a $10 \mathrm{maJ}$ difference results in a factor of 11 , and a $100 \mathrm{maJ}$ difference results in a factor of $3.1 \times 10^{10}$. To a practicing chemist, an energy difference of $10 \mathrm{maJ}$ between two competing species or transition states which changes the yield of a reaction from $8 \%$ to $90 \%$ usually matters more than would a $100 \mathrm{maJ}$ shift in all energies (causing no change in the course of the reaction) or a $100 \mathrm{maJ}$ shift in the transition-state energies which slows the reaction-completion time from a microsecond to an hour. In discussions of molecular energies, the term "chemical accuracy" usually implies errors of somewhat less than $10 \mathrm{maJ}$ per molecule in describing the energies of chemical species (corresponding to potential wells) and transition states (corresponding to features of cols). Aside from entropic effects dependent on the breadth of potential wells and cols, reaction rates typically exhibit only modest sensitivity to the shape-as distinct from the well depths and ${ }^{\circ}$ barrier heights-of the potential energy surface.

b. Predicting the geometries of flexible structures is hard. Potential energy functions are also used to predict molecular structures; the MM2 PES has good success for a wide range of small organic molecules. A more challenging test is protein modeling, where the shape and stability of the folded protein molecule depend on a delicate balance of free energy terms in which van der Waals interactions, overlap interactions, hydrogen bonding, torsional strains, and entropic factors all play crucial roles. The net stability of a folded structure typically is $\sim 50$ to $100 \mathrm{maJ}$, or $\sim 0.01 \mathrm{maJ}$ per atom. Although present molecular mechanics potentials are good enough to have found extensive use in protein modeling and design, their errors are large compared to the free energy of folding. Further, energy minimization usually yields structures that differ substantially from those experimentally determined by $x$-ray diffraction, even when the experimental structures are taken as a starting point.

Even for small organic molecules, a slightly inaccurate molecular mechanics model can predict structures that are totally wrong. Most molecules of concern in organic chemistry can exist in any of a number of conformations, differing by rotations about bonds; a simple example is $n$-octane, Figure 4.3. The relative energies of molecular conformations are sensitive to torsional energies (Section 3.3.2c) and to weak, nonbonded interactions (Section 3.3.2e). Conformational equilibria, like other chemical equilibria, are greatly altered by energy differences of $\sim 10 \mathrm{maJ}$. A crystal structure (a common source of geometric data) represents one of many possible molecular packing arrangements, again sensitive to
weak forces. A small modeling error can result in a predicted crystal structure containing the wrong conformation packed in a lattice of the wrong symmetry.

### 4.4.3. Accurate energies and nanomechanical design

Nanomechanical systems of the sort considered here are organic structures that resemble (or exceed) proteins in size, and some are used to perform chemical reactions. It is thus important to consider the sensitivity of nanomechanical designs to errors in potential energy surfaces.

a. Sensitive and insensitive designs. It will be possible to design nanomechanical systems that are exquisitely sensitive to the properties of a potential energy surface. For example, successful operation might be made to depend on a ratio of competing transition rates, as in conventional chemistry, or even on interference phenomena in angle-resolved scattering in crossed molecular beams. In general, any measurable physical property can be made essential to the correct operation of a suitable Rube Goldberg device, and hence any known class of unpredictable discrepancies between model and experiment can be used to design a class of devices that cannot with confidence be predicted to work. The design of such sensitive devices is closely related to good design practice in instrumentation and scientific experimentation, but is the opposite of good design practice in conventional engineering.

The robustness, predictability, durability, and performance of nanomechanical designs is usually maximized by making them from strong, stiff materials. Those considered here resemble diamond, consisting of highly ${ }^{\circ}$ polycyclic, threedimensional networks of atoms linked by covalent bonds. Predictions of the stability and geometry of these diamondoid structures are far less sensitive to small errors in potential energy surfaces than are similar predictions for folded protein structures or conformationally mobile organic molecules. Figure 4.4 illustrates the results of a molecular dynamics simulation of a polycyclic octane structure (cubane) under conditions like those of Figure 4.3: no conformational freedom is available, hence the deformations are purely vibrational.

b. Stiff molecules can resist "perturbing" modeling errors. Increasing structural stiffness tends to reduce errors in predicted geometry caused by inaccuracies in the PES. Consider a multiatom design that, when modeled with a potential $\mathscr{V}_{\text {model }}$, is predicted to have desirable geometrical properties. This function, however, differs from the correct (but unknown) potential, $\mathcal{V}_{\text {correct }}$. The transition from model to reality may now be regarded as adding to the model system the perturbing forces defined by the gradient of the difference potential, $\mathscr{V}_{\text {diff }}=\mathscr{V}_{\text {model }}-\mathcal{V}_{\text {correct }}$. A structure of greater rigidity suffers smaller deformations when subject to these perturbing forces; accordingly, a more rigid molecular design is more likely to survive the transition from model to reality without harmful distortion.

Good design practice can increase tolerance for the errors that remain. Nonetheless, errors in predicting molecular geometry can lead to designs that fail to work, in part because small local discrepancies in the predicted equilibrium geometry can have cumulative effects across large structures. Appendix A discusses how this problem can be accommodated during preliminary design and later overcome through experimentation.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-25.jpg?height=456&width=1182&top_left_y=192&top_left_x=282)

Figure 4.4. Molecular dynamics simulation of pentacyclo[4.2.0.0 $\left.2,5.0^{3,8} \cdot 0^{4,7}\right]$ octane (cubane) at $400 \mathrm{~K}$ (MM2/CSC); conditions as in Figure 4.3. The polycyclic structure of cubane, unlike the open-ended chain of $n$-octane, is representative of structures suitable for nanomechanical systems. It is stiff and lacks alternative conformations, hence its shape is insensitive to small errors in the PES, and thermal excitation results in relatively small deformations. All vibrational states correspond to the same minimum, as shown in the lower row. (The length and opacity of formal IUPAC names for polycyclic structures, like that given above for cubane, grows rapidly with molecular size; no attempt will be made to give formal names to structures like those in Figure 1.1.)

c. Mechanosynthesis is relatively insensitive to modeling errors. Errors in modeling chemical reactions play a different role. If the correct sequence of reactions is performed, then the correct structure will result, regardless of small errors in describing reaction rates or transition-state geometries during the process (Section 6.2). Distinct structures correspond to distinct states on a PES determined by invariant physical constants, and the manner of construction has no effect on the nature of the product. In conventional manufacturing, small variations in fabrication steps can have cumulative effects on properties such as product geometry, but no parallel problem arises in molecular manufacturing. Like switching events in digital logic, reactions either occur or they don't, and the result is either correct, or it isn't: ambiguous situations are unstable and transient.

In comparison to conventional chemical synthesis, molecular manufacturing processes based on positional control of synthetic reactions are less sensitive to small energy differences. Individual reaction steps can be driven to completion either by ensuring that energy differences greatly favor the product state, or by repeating trials until a molecular measurement verifies successful completion. To achieve regio- and stereospecificity, reactions can be guided not by differences in reaction rates and equilibria as in conventional synthesis, but by rigid control of ${ }^{\circ}$ reagent access to different sites. In chemical terms, this can create enormous ratios of effective reagent concentration between molecular sites that might otherwise be equally reactive. With positional control of synthesis, the main issues are achieving a high enough reaction rate (fast reactions best exploit the speed of nanomechanical systems) and avoiding (or being able to reverse) unwanted reactions immediately adjacent to the target site. These and related matters are discussed in more detail in Chapter 8.

d. Designs can eventually be tested and corrected. At present, nanomechanical design must rely on modeling because the tools necessary for construction and testing are unavailable. Note, however, that errors in specific designs (as distinct from systematic errors regarding what sorts of designs are workable) will be of little significance until the systems they describe can be constructed and used. Then, of course, testing will become possible, and errors can be corrected.

### 4.5. Conclusions

Models of molecular dynamics (within the Born-Oppenheimer approximation) begin with a potential energy surface, but differ in their treatment of it. Nonstatistical classical methods proceed by assuming a set of initial conditions and then integrating the classical equations of motion of each atom, subject to the forces implied by the PES; statistical results describing (for example) a thermal distribution can be accumulated by examining long simulations. Statistical mechanics methods compute a statistical distribution, commonly that associated with thermal equilibrium: quantum methods compute a distribution of quantum states; classical methods compute a distribution of positions and velocities. Many nanomechanical systems can be analyzed with good accuracy using relationships based on classical equilibrium statistical mechanics, sometimes with quantum corrections. These relationships can be used to define a mean-force potential (or free-energy potential), enabling systems near equilibrium to be described in terms of fewer coordinates. A consideration of PES accuracy requirements in light of dynamical principles and nanomechanical concerns shows that the mechanical stiffness of diamondoid structures and mechanochemical devices often greatly reduces their sensitivity to PES modeling errors, relative to more familiar molecular systems.

### 4.6. Further reading

Molecular dynamics is a broad field with an enormous literature. Basic statistical mechanics is well described in many textbooks, for example (Knox, 1971). Trajectory-based molecular dynamics, being more model dependent and computation intensive, is in a greater state of ferment. A good overview of the dynamics of reactive molecular collisions is (Levine and Bernstein, 1987), which includes many references. Many studies calculate trajectories by integrating the classical equations of motion subject to a molecular mechanics PES. Mitchell and McCammon (1991) review methods for estimating free energy differences between structures using dynamical methods based on molecular mechanics, and improved techniques are discussed in Straatsma and McCammon (1991). These works focus on calculations of the free energy of flexible biomolecules in water, which present difficulties not found in more rigid structures.

[^10]: Which requires that classical and quantum mechanics give the same answers in the limit of large quantum numbers.
[^55]: State is an overworked word. Here, it refers to a region of configuration space; in Section 4.3.2b, it referred to a single point in phase space (= configuration space $x$ momentum space). When a thermally excited nanomechanical system is described as being in some particular state of practical significance, this cannot refer to a point, and typically refers to a region in configuration space of the sort discussed here.
[^11]: More concretely, consider a system that could be in either of two deep, stable potential wells (e.g., a cylinder divided into two compartments by a piston in the middle, with a gas molecule in one or the other). To convert this into a system with a single well, the two wells can be merged symmetrically by dropping the barrier between them (by removing the piston), or asymmetrically (by moving the piston to one end of the cylinder, then removing it). Relative to symmetrical merging, asymmetrical merging can yield more free energy (the one-molecule gas expands against the moving piston, doing work), but only if some external record indicates which well is occupied (enabling a mechanism to choose the right direction for the motion). Proposals to gain this freeenergy increment by observing an initially unknown state can be made quite confusing but prove futile; if successful, they would enable violations of the second law of thermodynamics. Section 7.6.2 analyzes well-merging processes in more detail.
[^12]: The uncertainty principle stated here is implicit in all the later derivations based on quantum mechanical principles, for example, those of Chapter 5.