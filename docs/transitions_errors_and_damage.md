# Transitions, Errors, and Damage


### 6.1. Overview

In the configuration-space picture, a transition in a nanomechanical system corresponds to a motion of the ${ }^{\circ}$ representative point from one potential well to another. Errors occur when a system executing a pattern of motion transiently enters an undesired potential well; damage occurs when a system permanently exits the set of desired potential wells. Section 6.2 describes standard models used to describe transitions in molecular systems; these are used in later sections to analyze errors and thermomechanical damage. Section 6.3 describes methods for modeling subsystems within machines in terms of time-dependent potential energy surfaces, then uses this approach to model error rates in placing molecular objects into potential wells.

The balance of the chapter examines damage mechanisms. These can be categorized by the energy source that enables the system to surmount the energy barrier that separates working from damaged states. The two broad categories are:

- Internal energy sources, including thermal excitation, mechanical stress, and electromagnetic fields
- External energy sources, including electromagnetic fields and energetic photons and charged particles

Section 6.4 examines the effects of thermal excitation and mechanical stress, drawing on theoretical models of bond cleavage and experimental models of chemical reactivity. Section 6.5 examines photochemical damage and conditions for avoiding it by means of opaque shielding; Section 6.6 examines ionizing radiation damage, presenting models based on experimental studies of damage to biological molecular machines. Section 6.7 summarizes the engineering consequences of these damage mechanisms for the reliability of nanomechanical systems, given the assumption that single-point damage always causes component failure.

Owing to scaling laws (Chapter 2), the magnetic fields that can be generated within nanoscale systems are modest. Where chemical transitions are concerned, these will (at most) influence rates and equilibria in electronic phenomena such
as ${ }^{\circ}$ triplet-singlet intersystem crossing. In typical molecular structures, even the most intense magnetic fields generated in terrestrial physics laboratories cause no damaging transitions; further discussion of chemical effects of magnetic fields is accordingly omitted here. Electric fields, in contrast, can cause electrical breakdown, charge transfer, and molecular damage; Sections 6.4.7 and 11.6.2 touch on these topics.

### 6.2. Transitions between potential wells

### 6.2.1. Transition state theories

The previous chapter examined the effects of thermal excitation and quantum uncertainty in systems that can be described as points oscillating in a single potential well. This section examines thermal and quantum effects in systems characterized by a PES having two or more potential wells. Within each potential well, the location of the state point can be described by a PDF resembling those derived in the previous chapter. This PDF differs, however, in extending over a col that leads to another potential well; as a consequence a system in one well has a finite probability per unit time of moving to another. Transition state theories (TSTs) use a set of approximations to compute these transition rates.

Transition state theories find extensive use in studies of chemical kinetics. They are of little value where conditions are far from microscopic equilibrium (for example, during the first vibration-cycle after a molecule has been photochemically excited) but are not impaired by macroscopic disequilibrium (for example, during the first seconds or nanoseconds after two reagents have been mixed). The discussion in Section 4.3.4 of the utility of equilibrium statistical mechanics in nonequilibrium systems is applicable here.

Classical and quantum mechanical TSTs of varying complexity and accuracy have been developed. In the present context, there is little incentive to seek moderate improvements in accuracy at the cost of great increases in complexity. In evaluating transitions in nanomechanical designs, it usually suffices to establish either (1) that an undesirable transition does (or does not) occur at a sufficiently low rate in a given structure, or (2) that a desirable transition does (or does not) occur at a sufficiently high rate with a given reagent or other molecular device. Since transition rates at $300 \mathrm{~K}$ commonly vary from $>10^{12} \mathrm{~s}^{-1}$ to $<10^{-50} \mathrm{~s}^{-1}$, an approximate value frequently suffices to distinguish a workable from an unworkable design. The solution-chemist's concern with 10 -fold differences in the rates of competing reactions seldom arises.

### 6.2.2. Classical transition state theories

Transition state theories (both classical and quantum mechanical) start with a description of the col surrounding the transition state of a PES. Within the col between the wells is a saddle point; the surrounding region is locally describable by a quadratic function. With a suitable choice of coordinate axes, the curvature of the surface is negative along one axis (which defines the direction of the reaction coordinate) and positive along the other axes. In the most common definition, the transition state corresponds to a surface perpendicular to the reaction coordinate, which passes through the saddle point and divides points corresponding to one well from those corresponding to the other. Some versions of
transition state theory define different transition surfaces. (Note that this surface has one fewer spatial dimension than the potential energy surface; the next section speaks of volumes that correspond to regions of the PES and transition surfaces that separate those regions.)

In solution- and gas-phase chemistry, molecules are free to translate and rotate, and molecular number-densities are important variables. In nanomechanical systems, mechanical constraints can eliminate both translational and rotational degrees of freedom, and most processes are effectively intramolecular, making number densities irrelevant to transition rates. Accordingly, the following treatment is restricted to systems in which the potential wells are localized and distinctly bounded, permitting only vibrational motions within (and transitions between) wells.

a. Standard classical TST. Elementary transition state theory expresses the transition rate, $k_{12}\left(\mathrm{~s}^{-1}\right)$, as

$$
\begin{equation*}
k_{12}=\frac{k T}{2 \pi \hbar} \frac{q^{\ddagger}}{q_{1}} \exp \left(-\Delta \mathscr{V}^{\ddagger} / k T\right) \tag{6.1}
\end{equation*}
$$

In the classical theory, $q_{1}$ is the classical ${ }^{\circ}$ partition function (Section 4.3.2) describing the system when confined to the region of potential well 1 , and $q^{\ddagger}$ is the classical partition function describing a hypothetical system constrained to move along the transition surface. In calculating the transition-state partition function, the position and momentum coordinates corresponding to motion along the reaction coordinate are dropped from the integral in Eq. (4.8). The quantity $\Delta^{\ddagger}$ represents the barrier height, that is, the potential energy difference between the bottom of well 1 and the saddle point of the col (the superscript $\ddagger$ denotes a variable describing a transition state).

Although correct within the classical approximation, Eq. (6.1) does not directly suggest a physical visualization that can aid engineering design. Clear expositions of transition state theory can be found (e.g., Knox, 1971). Other standard expositions, however, speak in terms of fictitious concentrations of fleeting, arbitrarily defined "activated complexes"; these seem more confusing than enlightening. Finally, the presence of $\hbar$ in a classical theory suggests that a detour has been taken somewhere along the path from classical concepts to classical consequences. An alternative approach may help to build a more intuitive understanding, at least of the classical model.

b. The probability-gas visualization. In a purely classical model, the physics behind transition state theory can be visualized in terms of the diffusion of a probability gas (as introduced in Section 4.3.3). When the state of a system is uncertain (e.g., at equilibrium), motion of the representative point must be treated statistically. Rather than thinking in terms of the behavior of a single point over an indefinitely long period of time, one can instead think in terms of the positions and velocities of an indefinitely large number of independently moving points at a single instant. In mass-weighted coordinates (Section 4.3.3), these points behave like an ideal gas of uniform molecular weight and zero collision cross section: they move with the familiar isotropic Gaussian velocity distribution at every point in the space, and their density at every point varies in proportion to the Boltzmann factor, $\exp [-\mathscr{V}($ position $) / k T]$. With a single "gas
molecule," the density of the gas corresponds to the probability density. The diffusion of the gas through a col corresponds to the dynamics described by transition-state theory.

Figure 6.1(a) shows a top view of a two-dimensional square-well potential like that shown in 6.1(b). Since $\exp (-\mathscr{V} / k T)$ is a constant within the enclosed region, the distribution of the probability gas is uniform at equilibrium. Although there are no subsidiary wells, no proper col, and hence no transition state as ordinarily defined, one can divide the region into two nearly circular wells by defining a suitable transition surface, shown as the dotted line in 6.1(a). At equilibrium, the region on the right (state 2 ) contains more probability gas than the region on the left (state 1): in a chemical system, state 2 would be described as "having a lower free energy owing to entropic effects."

The rate of transitions from 1 to 2 (given initial occupancy of 1 ) is easy to calculate. State 1 has a certain volume (area, in two dimensions) and the surface between the states has a certain area (width, in two dimensions). The transition rate is simply the volumetric rate at which probability gas exits the region of state 1 through the available patch of transition surface divided by the total volume of gas in state 1 :

$$
\begin{equation*}
k_{12}=v_{\text {mean }} S_{\text {trans }} / V_{1} \tag{6.2}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-60.jpg?height=1092&width=874&top_left_y=1090&top_left_x=344)

Figure 6.1. Potential energy surfaces illustrating concepts in transition state theory.

where $v_{\text {mean }}$ is the mean speed of particles of probability gas along a given direction (that is, the average of the absolute value of the velocity along that direction, divided by two to discount particles traveling in the wrong direction). This expression generalizes to any number of dimensions: An $N$ dimensional volume is always bounded by an $N-1$ dimensional surface; each patch of surface transmits gas at a rate equaling its area times the mean speed perpendicular to its surface, and the mean speed (in the above sense) is independent of the number of dimensions. In mass-weighted coordinates,

$$
\begin{equation*}
v_{\text {mean }}=\int_{0}^{\infty} \frac{v}{\sqrt{2 \pi k T}} \exp \left(-v^{2} / 2 k T\right)=\sqrt{k T / 2 \pi} \tag{6.3}
\end{equation*}
$$

In a slightly more complicated model, Figure 6.1(c), one region has a lower potential energy than the other. At equilibrium, the distribution of gas between states 1 and 2 is determined by the product of their volumes and the Boltzmann factor $\exp (-\mathscr{V} / k T)$ for each region: this product defines a density-weighted volume, or effective volume. For suitable choices of $V_{1} / V_{2}, \Delta \mathcal{V}$, and $T$, state 1 will be favored and would be described as "having a lower free energy, despite its lower entropy." The calculation of transition rates from 1 to 2 proceeds as before, but with a Boltzmann factor to account for the lower gas density at the "altitude" of the transition surface between the regions:

$$
\begin{equation*}
k_{12}=\frac{v_{\text {mean }}}{V_{\text {state } 1}} S_{\text {col }} \exp \left(-\Delta V^{\ddagger} \neq k T\right) \tag{6.4}
\end{equation*}
$$

This factor reduces the effective area of the transition surface relative to the volume of the well. Note that in this example there is no barrier in the reverse direction, hence the effective area of the transition surface relative to well 2 is unchanged.

Figure 6.1(d) represents a smoother and more realistic PES to which quadratic approximations and classical transition state theory can be applied. In the probability-gas model, the effective volume of each well now must reflect the integral of a Boltzmann weighting over the varying floor height, and the effective area of the transition surface (with respect to a well) must likewise be weighted to account for its varying height.

In a general harmonic well, the stiffness $k_{\mathrm{s}}$ may differ for each coordinate.[^13] Along any given coordinate, the effective width of the well is (without mass weighting)

$$
\begin{equation*}
w_{\text {effective }}=\sqrt{2 \pi} \sigma=\sqrt{2 \pi k T / k_{\mathrm{s}}} \tag{6.5}
\end{equation*}
$$

or, with mass weighting as elsewhere in this section,

$$
\begin{equation*}
w_{\text {effective }}=\sqrt{2 \pi m k T / k_{\mathrm{s}}}=\sqrt{2 \pi k T} \frac{1}{\omega}=\sqrt{k T / 2 \pi} \frac{1}{f} \tag{6.6}
\end{equation*}
$$

allowing expression in terms of the weighting-independent frequency $f$. The effective volume of a well is the product of the effective widths in each of the $N$ dimensions

$$
\begin{equation*}
V_{\text {effective }}=\prod_{i=1}^{N} \sqrt{k T / 2 \pi} \frac{1}{f_{i}}=(k T / 2 \pi)^{N / 2} \prod_{i=1}^{N} \frac{1}{f_{i}} \tag{6.7}
\end{equation*}
$$

and a similar expression of lower dimensionality yields the effective area of the transition surface. Combining these, the transition rate expression becomes

$$
\begin{align*}
k_{12} & =v_{\text {mean }} \frac{S_{\text {col }}}{V_{\text {state } 1}} \exp \left(-\frac{\Delta \mathcal{V}^{\ddagger}}{k T}\right) \\
& =\sqrt{\frac{k T}{2 \pi}} \frac{\left(\frac{k T}{2 \pi}\right)^{\frac{N-1}{2}} \prod_{i=1}^{N-1} \frac{1}{f_{i}^{\ddagger}}}{\left(\frac{k T}{2 \pi}\right)^{\frac{N}{2}} \prod_{i=1}^{N} \frac{1}{f_{i}}} \exp \left(-\frac{\Delta \mathcal{V}^{\ddagger}}{k T}\right) \\
& =\frac{\prod_{i=1}^{N-1} f_{i}}{\prod_{i=1}^{N-1} f_{i}^{\ddagger}} \exp \left(-\frac{\Delta \mathscr{V}^{\ddagger}}{k T}\right) \tag{6.8}
\end{align*}
$$

By applying the expression for the classical partition function of a harmonic oscillator,

$$
\begin{equation*}
q_{\text {class }}=k T / \hbar \omega \tag{6.9}
\end{equation*}
$$

and the observation that the partition function for a linear elastic system is the product of the partition functions for each of its normal modes, an expression identical to Eq. (6.1) can be derived from Eq. (6.8). This illustrates the equivalence between the probability-gas model (with its geometric visualization) and the more abstract formalism of classical transition state theory.

Equation (6.8) has a simple interpretation in the special case where the reaction coordinate leading over the col is an extension of one of the normal modes of the well (of frequency $f_{\text {rc }}$ ) and the other modal frequencies are identical in both the well and transition state. A system of this sort is effectively one dimensional, and the ratio of products in Eq. (6.8) reduces to $f_{\mathrm{rc}}$. The representative point can then be described as striking the barrier $f_{\mathrm{rc}}$ times per second, with a success rate in surmounting the barrier of $\exp \left(-\Delta^{\mathscr{V}} \ddagger / k T\right)$. Where the other modal frequencies are not identical, they can be viewed as affecting the entropy (and thus the free energy) as a function of the reaction coordinate; this coordinate-dependent entropy can be used to define a mean-force potential (Section 4.3.7) for motion along the reaction coordinate. A one-dimensional TST expression in terms of this potential is identical to Eq. (6.8).

c. Shortcomings and variational theories. Within the classical, equilibrium approximation, the TST described above is exact if the relevant integrals are done with an exact potential energy surface, and if transitions are defined simply as motions that cross the transition surface separating the states. On some PESs, however, a large fraction of the trajectories that lead from a low energy in one well to a low energy in another (assuming, as always, coupling to a heat
bath) oscillate across the transition surface several times. Other trajectories may cross the surface and be promptly reflected back into the originating well. These crossings are transitions according to the above definition, but not in any practical chemical sense. Accordingly, classical TSTs provide only an upper bound to the (classical) transition rate of practical interest. The difference is sometimes accommodated by an ad hoc "transmission factor."

Variational transition state theories (which lack ad hoc factors) adjust the geometry of the transition surface to minimize the transition rate. The more sophisticated forms adopt different transition surfaces for trajectories of different energies. These methods yield lower transition rates that are still upper bounds on the rate of practical interest. A review of TSTs, including variational TSTs, can be found in Bérces and Márta (1988). Standard transition state theory usually fits exact classical calculations with reasonable accuracy.

### 6.2.3. Quantum transition state theories

Quantum mechanical corrections to classical transition state theory take three forms: (1) use of a barrier height that accounts for the zero-point energies of the well and transition state, (2) replacement of classical with quantum mechanical partition functions, and (3) use of a correction to account for tunneling through the barrier in the region of the transition state (Bérces and Márta, 1988). These are addressed separately.

It is common to correct barrier heights by adding a zero-point energy term to the energy of the well minimum. The zero-point energy of a linear elastic system is the sum of the zero-point energies of its (real-valued) normal modes; the effective minimum energy of a state is then

$$
\begin{equation*}
\mathcal{V}^{\prime}=\mathscr{V}+\sum_{i=1}^{N} \frac{1}{2} \hbar \omega_{i} \tag{6.10}
\end{equation*}
$$

Application of Eq. (4.2) to the harmonic oscillator yields a standard form for the quantum-mechanical partition function,

$$
\begin{equation*}
q_{\text {quant,zpe }}=[1-\exp (-\hbar \omega / k T)]^{-1} \tag{6.11}
\end{equation*}
$$

which takes the vibrational ground state as the zero of energy and is compatible with corrected barrier heights. Alternatively, one can omit the zero-point energy correction from the barrier height, and instead use a partition function

$$
\begin{equation*}
q_{\text {quant }}=\exp (-\hbar \omega / 2 k T)[1-\exp (-\hbar \omega / k T)]^{-1} \tag{6.12}
\end{equation*}
$$

which takes the well minimum as the zero of energy. The choice is a matter of notational convenience, and expressions using this form more closely correspond to the classical equations.

The partition function for a linear system having $N$ normal modes is the product of the partition functions of the modes; using Eq. (6.12),

$$
\begin{equation*}
q_{\text {quant }}=\prod_{i=1}^{N} \exp (-\hbar \omega / 2 k T)[1-\exp (-\hbar \omega / k T)]^{-1} \tag{6.13}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-64.jpg?height=887&width=1119&top_left_y=162&top_left_x=212)

Figure 6.2. Ratios of quantum mechanical to classical partition functions for harmonic oscillators, [Eq. (6.11)]/[Eq. (6.9)], as a function of temperature and effective stiffness for two values of the effective mass at the well minimum. Since the TST expression contains one more modal factor in the denominator than in the numerator, decreases in the above quantum-to-classical ratios tend to increase transition rates.

As in the classical theory, transition state partition functions are computed by omitting factors associated with motion along the reaction coordinate. Figure 6.2 shows how the ratio of classical and quantum-mechanical partition functions varies with temperature and stiffness.

The standard Wigner approximation to the tunneling correction factor is

$$
\begin{equation*}
\Gamma^{*}=1+\frac{1}{24}\left|\hbar \omega_{\mathrm{rc}} / k T\right|^{2} \tag{6.14}
\end{equation*}
$$

where

$$
\begin{equation*}
\omega_{\mathrm{rc}}=\sqrt{k_{\mathrm{s}, \mathrm{rc}} / m_{\mathrm{eff}, \mathrm{rc}}} \tag{6.15}
\end{equation*}
$$

is an imaginary frequency associated with motion along the reaction coordinate [ $m_{\text {eff }}$ is the effective mass along this coordinate, and the stiffness along the reaction coordinate $k_{\mathrm{s}, \mathrm{rc}}$ is negative (Bell, 1959; Bigeleisen, 1949)]. Figure 6.3 shows how $\Gamma^{*}$ varies with temperature and stiffness. (Section $6.4 .4 \mathrm{~b}$ notes the inapplicability of $\Gamma^{*}$ at low temperatures.)

Combining the preceding substitutions and corrections yields the approximate quantum-mechanical TST expression

$$
\begin{equation*}
k_{12}=\Gamma^{*} \frac{k T}{2 \pi \hbar} \frac{q_{\text {quant }}^{\ddagger}}{q_{\text {quant }, 1}} \exp \left(-\Delta \mathcal{V}^{\ddagger} / k T\right) \tag{6.16}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-65.jpg?height=755&width=1085&top_left_y=52&top_left_x=309)

Figure 6.3. The Wigner tunneling correction factor, Eq. (6.14), as a function of temperature and effective stiffness for two values of the effective mass for motion along the reaction coordinate.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-65.jpg?height=888&width=1093&top_left_y=1131&top_left_x=300)

Figure 6.4. The ratio of quantum to classical transition rates, assuming a one-dimensional model with the stated ratios of stiffnesses along the reaction coordinate. The stiffness at the well minimum is $500 \mathrm{~N} / \mathrm{m}$ (typical of the stretching stiffness of a covalent bond). Note that a stiffness ratio of zero implies an infinitely thick barrier and an absence of tunneling.

The ratio of this quantum mechanical rate constant to the classical rate constant is plotted in Figure 6.4 for examples involving the motion of $\mathrm{H}$ and $\mathrm{C}$ atoms. More sophisticated quantum-mechanical TSTs are reviewed in Bérces and Márta (1988).

### 6.2.4. Tunneling

Tunneling processes dominate the transition rate in all systems at sufficiently low temperatures and in many electronic systems at room temperature. When this occurs, transition state theories based on the Wigner tunneling correction can radically underestimate the transition rate. A different model must be used.

Estimates of tunneling transition rates for a particle in a well bounded by a barrier are derived by multiplying the barrier transmittance $T$ by a suitable frequency factor, such as $\omega / 2 \pi$ (for a harmonic well) or the round-trip traversal time (for a square well). In the classical picture, the particle strikes the barrier with a certain frequency and probability of penetration.

Quantum theory yields exact expressions for $T$ for various cases (such as rectangular barriers) but real systems seldom correspond to one of these. Nanomechanical and electromechanical designs of the sort described in this volume require approximations of broader utility. As with transition state theory, the typical objective is to discriminate between those systems that do and do not have tunneling rates low enough to be acceptable (e.g., low enough for an insulator to transmit little current or for a stressed bond to have a long expected lifetime). A standard method applicable to many systems of low $T$ exploits the WKB (Wentzel-Kramers-Brillouin) approximation.

a. The WKB tunneling approximation. A useful approximation to the transmittance of a potential barrier $\mathscr{V}(x)$ for a normally incident particle of energy $\mathscr{E}$ and effective mass $m_{\text {eff }}$ is

$$
\begin{equation*}
T \approx \exp \left[-2 \int_{x_{0}}^{x_{1}} \sqrt{\frac{2 m_{\mathrm{eff}}}{\hbar^{2}}[\mathscr{V}(x)-\mathscr{E}]} d x\right] \tag{6.17}
\end{equation*}
$$

where the limits of integration define the region in which $\mathscr{V}(x)>\mathscr{E}$ (Figure 6.5). The approximation requires that the exponential decay of the wave function in the region of negative energy be the dominant phenomenon, making $T \ll 1$; it can be applied when tunneling occurs into a continuum of energy states, such as that characterized by free motion of a particle. Where several potential barriers occur in close succession, resonance effects can yield more complex relationships between energies and transmittances.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-66.jpg?height=323&width=446&top_left_y=1927&top_left_x=192)

Figure 6.5. Total energy and potential energy of a tunneling particle, showing the limits of integration used in the WKB approximation.

### 6.3. Placement errors

### 6.3.1. Time-dependent PES models

Section 6.2 implicitly assumes that the PES is unchanging. From a perspective that includes all particles, this is always correct; yet it frequently is convenient to consider mechanical subsystems separately, accounting for the effects of other subsystems by imposing changing boundary conditions on the subsystem under analysis. These boundary conditions involve changes in the PES as a function of time. Detailed dynamical simulations (e.g., Landman et al., 1990) sometimes model the mechanical motion of an adjacent structure by imposing definite trajectories on boundary atoms, and model thermal equilibration by adjusting the mean kinetic energies of a subset of the atoms in thermal contact with the rest. The more abstract models discussed in this section describe a time-dependent PES directly; like standard TSTs, they introduce a thermal-equilibrium assumption by means of a basically statistical description.

Various processes in nanomechanical systems can be described as attempts to place something in the proper potential well. In systems that perform measurement (Chapter 11), the proper potential well corresponds to an accurate measurement of a physical parameter; in nanomechanical computer systems (Chapter 12), the proper potential well corresponds to the correct state of a logic device; in molecular manufacturing (Chapters 13 and 14), the proper potential well corresponds to the desired result of an assembly step. The potential wells and trajectories that specify the process of placement will in the general case involve motions describable only in terms of a PES of high dimensionality; in practice, typical examples of each of the above cases can be described rather well in terms of thermal displacements of an atom (or small group of atoms) in one or two dimensions, subject to an increasing constraint imposed by a mechanical motion in a second or third dimension.

For a concreteness, picture a probe atom at the tip of an elastic beam descending through vacuum toward a surface (Figure 6.6), described by the coordinates $x, y, z$, and $z^{\prime}$. In this model, $z^{\prime}$ is the equilibrium value of $z$ in the absence of thermal excitation and perturbing forces from the surface, or alternatively, the limit of $z$ as the stiffness components $k_{\mathrm{sx}}=k_{\mathrm{sy}}=k_{\mathrm{sz}} \rightarrow \infty$. In a nanomechanical system, the value of $z^{\prime}$ is determined by the mechanical configuration of the rest of the system. The potential $\mathscr{V}(x, y, z)_{z=z^{\prime}}$, can be regarded as a $z^{\prime}$-dependent two-dimensional potential $\mathscr{V}(x, y)$.
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-67.jpg?height=424&width=562&top_left_y=1780&top_left_x=269)

Figure 6.6. Model system consisting of a probe atom positioned by an elastic beam and subject to perturbations both from thermal excitation and from interactions as it encounters the surface below.

This potential is harmonic at large distances from the surface, owing to the beam stiffness; as the probe approaches the surface, corrugations are superimposed on the harmonic potential, growing in magnitude as it grows closer. (At contact, the probe may be forced into a hole by pressure from the arm, or attracted to a site by electrostatic interactions, or bonded to a reactive group.) We seek a potential of the form $\mathcal{V}^{\dagger}\left(x, y, z^{\prime}\right)$ in order to describe time-dependent twodimensional systems $\mathscr{V}^{\dagger}\left[x, y, z^{\prime}(t)\right]$. This is possible if we assume that the probe is mechanically stable in $z$ (i.e., that the $z$ stiffness, summing the beam stiffness and the probe-surface interaction stiffness, remains positive); without this assumption, transitions involving $z$ excitations in a time-dependent three-dimensional potential must be considered explicitly.

How does $\mathscr{V}^{\dagger}$ differ from $\mathscr{V}$ ? At zero $\mathrm{K}$, it equals

$$
\begin{equation*}
\mathscr{V}_{0}^{\dagger}\left(x, y, z^{\prime}\right)=\mathscr{V}\left(x, y, z_{\mathrm{e}}\right)+\frac{1}{2} k_{\mathrm{sz}}\left(z^{\prime}-z_{\mathrm{e}}\right)^{2} \tag{6.18}
\end{equation*}
$$

where $z_{\mathrm{e}}$ is the equilibrium value of $z$ for the given value of $x, y$, and $z^{\prime}$. More generally, one can apply a mean-force potential in which an entropic term accounts for variations in the compression of vibrations in the $z$ direction. Making the harmonic approximation for vibrations about $z_{\mathrm{e}}$ and applying the classical vibrational partition function, the potential at finite temperatures is

$$
\begin{equation*}
\mathscr{V}^{\dagger}\left(x, y, z^{\prime}\right)=\mathscr{V}\left(x, y, z_{\mathrm{e}}\right)+\frac{1}{2} k_{\mathrm{sz}}\left(z^{\prime}-z_{\mathrm{e}}\right)^{2}-k T[1+\ln (k T / \hbar \omega)] \tag{6.19}
\end{equation*}
$$

### 6.3.2. Error models

A detailed model would use Monte Carlo methods to estimate probabilities, integrating the equations of motion for a system. This method could take account of complex potentials and rapid motions in systems far from thermal equilibration, but would be computationally expensive and would offer little general insight.

Transition-state theories can provide a basis for a relatively detailed model of placement errors. In this approach, one would define regions corresponding to growing potential wells, and moving transition surfaces corresponding to growing barriers. Initial assignments of probabilities to wells would follow the Boltzmann distribution, and integration of transition rates would trace the evolution of those probabilities over time. To each transition rate predicted by a fixed-potential TST would be added a rate corresponding to the product of the probability density along each transition coordinate and the rate of motion of the associated transition surface in the time-dependent potential. This approach would be tractable for many problems.

A simpler model can be constructed starting with the observation that, in most systems of engineering interest, barriers between states are initially absent and eventually so high as to preclude significant transition rates. This leads to consideration of models in which equilibration among regions of configuration space switches from complete to nonexistent, omitting consideration of the narrow range of barrier heights in which transition rates are neither fast nor negligible compared to the characteristic time scale of the placement process. As usual, the goal is not to make a perfect prediction of physical behavior, but to
distinguish workable systems, identifying them with a methodology that yields a low rate of false positives without an overwhelming rate of false negatives.

### 6.3.3. Switched-coupling error models

The probability of a state (or set of states) is effectively frozen[^14] when the lowest barrier between it and other states meets the approximate condition

$$
\begin{equation*}
f_{\mathrm{TST}} \exp \left[-\Delta \mathscr{V}^{\dagger}(t) / k T\right] \approx \frac{1}{k T} \frac{\partial}{\partial t} \Delta \mathscr{V}^{\dagger}(t) \tag{6.20}
\end{equation*}
$$

assuming that the barrier height $\Delta \mathcal{V}^{\dagger}(t)$ and the equilibrium ratio of probabilities are both smoothly increasing. (In this expression, $f_{\text {TST }}$ is a frequency factor taken from transition state theory.) This can be termed the time of kinetic decoupling for the two wells; one useful approximation treats this as a discrete time at which equilibration is switched off. A one-dimensional classical model illustrates the consequences of switching equilibration off at different times.

a. The sinusoidal-well model. The simplest time-dependent PES for modeling placement errors combines a fixed, one-dimensional harmonic potential with a time-varying sinusoidal potential

$$
\begin{equation*}
\mathscr{V}^{\dagger}(t)=\frac{1}{2} k_{\mathrm{s}} x^{2}+\left[1-\cos \left(2 \pi x / d_{\mathrm{err}}\right)\right] A t \tag{6.21}
\end{equation*}
$$

This model captures several basic features of placement errors in nanomechanical systems: the harmonic well is aligned to maximize the probability of
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-69.jpg?height=576&width=1010&top_left_y=1194&top_left_x=358)

Figure 6.7. The lower panels illustrate time-dependent potentials described by Eq. (6.21), with higher curves representing later times; the upper panels illustrate the corresponding Boltzmann probability density functions at a particular temperature. In both panels, the dotted curves correspond to the potential at $t_{\text {crit }}$ (Section 6.3.3d); other curves are at $0.5,1.5$ and 10 times $t_{\text {crit }}$. Note the decrease in probability mass in the outlying peaks as the well spacing increases.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-70.jpg?height=682&width=1107&top_left_y=180&top_left_x=223)

Figure 6.8. Error rates per placement operation resulting from the application of different equilibration assumptions to the sinusoidal-well model.

finding the system in the target potential well in the center; other wells, corresponding to error states, appear at some distance $d_{\text {err }}$ from the target well; well depths grow over time at a controlled rate. The bottom panel of Figure 6.7 illustrates the shape of this potential at varying times for two values of $d_{\mathrm{err}}$.

b. The total-equilibrium limit. If equilibration continues until the wells that will eventually hold significant probability are all sharp compared to the initial harmonic well, then the probability mass associated with each is determined only by its depth, which is the height of the harmonic well at a minimum of the sinusoid. In this model, the probability of error is given by the ratio of sums

$$
\begin{equation*}
P_{\mathrm{err}}=2 \sum_{1}^{\infty} \exp \left(-k_{\mathrm{s}}\left(n d_{\mathrm{err}}\right)^{2} / 2 k T\right) / \sum_{-\infty}^{\infty} \exp \left(-k_{\mathrm{s}}\left(n d_{\mathrm{err}}\right)^{2} / 2 k T\right) \tag{6.22}
\end{equation*}
$$

Figure 6.8 shows the probability of error in the total equilibrium limit, as a function of $\mathscr{V}_{1}$. The generalization of this model is standard chemical equilibrium, in which wells can have varying free energies (that is, depths and effective volumes) and have the corresponding Boltzmann-weighted probabilities of occupancy.

c. The instantaneous-onset limit. If the rate parameter $A$ is sufficiently large, the barriers imposed by the sinusoidal potential become large in a time that is short compared to the transit time of a single well, and probabilities are frozen in their prebarrier distribution. The probability of an error is the integral

$$
\begin{equation*}
P_{\mathrm{err}}=2 \int_{d_{\mathrm{err}} / 2}^{\infty} \sqrt{k T / 2 \pi k_{\mathrm{s}}} \exp \left(-k_{\mathrm{s}} x^{2} / 2 k T\right) d x \tag{6.23}
\end{equation*}
$$

of the initial harmonic Boltzmann distribution in the regions beyond the eventual location of the peaks that will bound the target well. The upper curve in Figure 6.8 illustrates how this probability varies as a function of $\mathscr{V}_{1}$, the energy
difference between the target state and the lowest-energy error state. The generalization of this instantaneous limit in a multidimensional system would start with an ellipsoidal Gaussian distribution and impose on this the state boundaries of the final potential surface (Section 4.3.3b), taking the integrated probability outside the boundaries of the correct state as the probability of error.

For a nanomechanical system to be well-approximated by the instantaneous limit, its mechanical speeds must be large compared to its thermal speeds. For combinations of sufficiently large effective masses and sufficiently high mechanical speeds, this may hold true, yet it is unlikely to be a common case. The instantaneous limit maximizes error rates, hence high speeds (which also increase energy dissipation) are usually best avoided.

d. The worst-case decoupling model. Within the bounds of the kineticdecoupling model (allowing free equilibration until some time after energy barriers appear), there exists a decoupling time that maximizes the error rate. In the sinusoidal-well model, the first barriers appear at a time

$$
\begin{equation*}
t_{\text {crit }}=0.2332 d_{\mathrm{err}}^{2} / A \tag{6.24}
\end{equation*}
$$

then grow in height and move inward toward the origin. Figure 6.7 illustrates two time-varying potentials and their corresponding PDFs, showing $t_{\text {crit }}$. Dividing the PDF at the time and position of the initial barrier appearance yields the dashed curve in Figure 6.8; varying the time (and resulting PDF and barrier position) to maximize the error probability yields the solid curve slightly above it.

This model, which permits barrier crossing only so long as it increases errors, yet gives error rates lower than in the instantaneous-onset model, seems a good choice for making conservative estimates of error rates in many circumstances. The conservatism breaks down when error rates are large, that is, when $d_{\text {err }}<\sim 2\left(k T / k_{\mathrm{s}}\right)^{1 / 2}$, but this is outside the usual range of interest. A more common failure is excessive conservatism in systems where a large well may appear after being cut off by a high barrier: this model will then assign an unrealistically high probability to that well. With the notion of state boundaries that change over time, the worst-case switching model readily generalizes to multidimensional systems.

### 6.4. Thermomechanical damage

### 6.4.1. Overview

Thermal excitation, sometimes aided by mechanical stress, can cause permanent damage to devices built with molecular precision. Damaged states (as distinct from transiently disturbed states) occur when a transition occurs into a stable potential well corresponding to a nonfunctional device structure. Causes of damage include:

- Reactions like those between small molecules
- Rearrangements like those within small molecules
- Reactions like those at solid surfaces
- Rearrangements like those within solid objects
- Bond cleavage accelerated by mechanical stress

The first four points can be approached via analogies to known chemical systems. Several of the following sections follow this strategy, building on empirical knowledge and theoretical scaling relationships that describe how transition rates vary with temperature. Here (as in Chapter 8 ) it seems wise to begin by comparing the general conditions of solution-phase and ${ }^{\circ}$ machine-phase chemical processes, as an aid to forming the proper generalizations from present chemical experience.

As shown in Section 6.6, damage caused by a process with a transition lifetime $\geq 10^{20} \mathrm{~s}\left(\approx 3 \times 10^{12}\right.$ years) is small compared to that caused by ionizing radiation under typical conditions (assuming, as usual, that complete device failure will result from a single damaging transition). This rate can accordingly be regarded as small in practical terms, and is used here as a standard of comparison.

It can be useful to draw a distinction between two classes of reactions: those that begin with the breakage of a bond (and may then move on to further transformations), and those that proceed with simultaneous bond breakage and bond formation, permitting lower transition-state energies. In processing metals, ceramics, and semiconductors, temperatures high enough to promote rapid bond breakage are commonplace. In solution chemistry, however, and in nanomachines operating at room temperature, only low-energy (or highly strained) bonds can break at high rates (Sections 6.4.3 and 6.4.4), and the dominant chemical processes therefore involve simultaneous bond breakage and formation. Many organic molecules have no available reaction pathways that permit this; they can accordingly be quite stable at ordinary temperatures when surrounded by similarly stable structures or vacuum.

### 6.4.2. Machine- vs. solution-phase stability

Machine-phase chemistry comprises systems in which all potentially reactive moieties follow controlled trajectories (Section 1.2.2a). Although borderline cases can be imagined, the contrast is clear between systems of small, diffusing molecules in the liquid phase and ${ }^{\circ}$ eutactic systems of molecular machinery as envisioned here. In solution-phase chemistry, potentially reactive moieties encounter each other in relative positions and orientations constrained by only local molecular geometry, not by control of molecular trajectories. In the solution phase, access to a reactive site may be blocked (e.g., by attached hydrocarbon chains); in the machine phase, even an exposed reactive site may never encounter another molecule.

a. Examples. The stability of a structure often depends on its physical environment. For example, a molecular structure including the fragment:

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-72.jpg?height=260&width=352&top_left_y=1954&top_left_x=598)
would be unstable in solution, readily forming dimeric products such as:

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-73.jpg?height=323&width=471&top_left_y=229&top_left_x=628)

among others. The formation of dimers, however, requires that two molecules of the same kind encounter one another; this is inevitable in solution, but not in molecular machines.[^15] Structure $\mathbf{6 . 1}$ has been proposed for a role in a nanomechanical computer (Drexler, 1988b) in which such encounters would not occur.

In that design, however, 6.1 would encounter other structures including the fragment 6.3, which in solution might yield the Diels-Alder adduct 6.4:
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-73.jpg?height=376&width=880&top_left_y=856&top_left_x=419)

and various other products. To approach the Diels-Alder transition state, the rings would have to encounter one another in a nearly parallel orientation, as in 6.5. In the application proposed, however, a surrounding matrix would mechanically constrain the rings, forcing them to approach in a perpendicular orientation, as in 6.6, thereby precluding this reaction.
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-73.jpg?height=578&width=952&top_left_y=1486&top_left_x=384)

b. Machine-phase damage mechanisms. To generalize from these examples:
- Structures that are unstable in solution environments owing to intermolecular reactions between identical molecules can be stable in eutactic systems because collisions do not occur.
- Structures that react on collision in solution environments can fail to react on collision in eutactic systems owing to constraints on orientation.

In solution chemistry, exposed moieties always encounter solvent molecules and often encounter dissolved oxygen, dissolved water, trace contaminants, and container materials, each potentially reactive. In machine-phase chemistry, potentially reactive moieties are constrained, encountering other structures only by design (Chapters 11, 13, and 14 discuss maintenance of controlled environments). In some nanosystems (discussed in Chapters 8, 13, and 14), certain structures and encounter conditions are designed to foster reactions; ${ }^{\circ}$ reagent devices of this sort are considered elsewhere. Other structures and encounter conditions, however, are designed to discourage reactions, and reactions then constitute damage.

In nonreagent nanomechanical systems, contacts between structures serve mechanical functions: bearing surfaces, ${ }^{\circ} \mathrm{cam}$ riders, gear teeth and the like are typical examples. Chapter 11 addresses the stability of the resulting interfaces. Where no mechanical function is served, no contact is necessary, and intermolecular reactions can be excluded from possibility.

Nanomechanical systems are, however, subject to increased reactivity owing to mechanical stresses not found in solution chemistry. These stresses can be used to facilitate desired reactions (Sections 8.3.3c and 8.5) but can also facilitate damage. Stresses are subject to engineering control, and estimation of their chemical effects is important to engineering design. These stress-induced reactions, however, are special cases of intramolecular damage processes involving intramolecular reactions of sorts familiar in conventional chemistry. These reactions are little affected by control of trajectories.

c. Design and intramolecular stability. To provide a thorough discussion of intramolecular reactions would require a thorough discussion of much of chemistry: this is impossible in a single volume, and still further from possibility in a section of a chapter. Even a discussion of organic intramolecular reactions would include nearly the whole of organic chemistry, since the ends of long, flexible molecules can react with each other essentially like separate molecules.

The pursuit of engineering objectives, however, greatly restricts the range of structures to be considered. For example, these objectives usually favor designs in which structures are either intrinsically stiff or held in an extended conformation by tension or by a surrounding matrix. Designs with these characteristics can exclude this class of reactions.

Likewise, the pursuit of engineering objectives often favors the selection of structures with strong, stable patterns of bonding. Errors in discriminating between stable and unstable structures during the preliminary phases of nanomechanical engineering will later be eliminated by more thorough analysis and (eventually) experimental testing. The aim of the present discussion of thermomechanical damage is to outline some principles of importance in (1) generating
reasonable designs and (2) using the chemical literature and computational experiments to evaluate specific designs in more detail.

With regard to reading the chemical literature, a possible source of cognitive bias is worth noting: In studying solution chemistry, one tends to focus on the active reagent molecules, not on the comparatively inert solvent molecules. Indeed, in a typical textbook of organic chemistry, roughly half the chemical species appear to the left of an arrow representing a transformation to another species, $A \rightarrow B$; if $A$ were stable under the specified reaction conditions, it would rarely appear in the equation, save as a notation of reaction conditions. A superficial reading of the chemical literature can thus foster the illusion that almost any set of molecules is likely to react at an appreciable rate. In nanomechanical systems, however, many structures play roles more like those of solvents: these structures can move with respect to one another (and transport reagents) without reacting. If need be, the interactions between nanomechanical surfaces can be made to resemble those among, for example, hexane, benzene, and methyl ether more closely than those among, for example, sodium hydroxide, bromoethane, hydrochloric acid, and cyclopentadiene. Reactivity depends on surface structure and interaction geometry, and will be subject to engineering control guided by experimentation.

### 6.4.3. Thermal bond cleavage

Direct cleavage of a bond by thermal excitation, forming a pair of ${ }^{\circ}$ radicals, is usually slow at ordinary temperatures. Among the major exceptions are organic peroxides, diacyl peroxides, and azo compounds, which find use as initiators of radical reactions:

$$
\begin{aligned}
& \mathrm{R}^{\prime}{ }^{\mathrm{O}-\mathrm{O}_{\mathrm{R}^{\prime}}} \longrightarrow \mathrm{R}^{\prime}{ }^{\mathrm{O} \bullet}+{ }^{\bullet \mathrm{O}_{\mathrm{R}^{\prime}}}
\end{aligned}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-75.jpg?height=108&width=560&top_left_y=1415&top_left_x=579)

$$
\begin{aligned}
& \mathbf{R}^{\prime} \mathbf{N}=\mathrm{N}_{\mathbf{R}^{\prime}} \longrightarrow \mathrm{R} \bullet+\mathrm{N}_{2}+\cdot \mathrm{R}^{\prime}
\end{aligned}
$$

a. Thermal bond cleavage rates. The rate of bond cleavage $k_{\mathrm{cl}}$ cannot be estimated using standard transition state theory when molecules separate into gas-phase radicals: the effective transition state is at infinity, and the transitionstate frequencies are zero. Variational theories can give sensible answers, but a rough approximation, good in a wide range of circumstances (and low by a small factor in this instance), is provided by a one-dimensional theory. In this,

$$
\begin{equation*}
k_{\mathrm{cl}}=\frac{k T}{2 \pi \hbar} \frac{1}{q_{\text {long }}} \exp (-\Delta \mathscr{V} / k T) \tag{6.28}
\end{equation*}
$$

where $q_{\text {long }}$ is the partition function for longitudinal vibrations of the bond,

$$
\begin{equation*}
q_{\text {long }}=\exp \left(-\frac{\hbar}{k T} \sqrt{\frac{k_{\mathrm{s}}}{\mu}}\right)\left[1-\exp \left(-\frac{\hbar}{k T} \sqrt{\frac{k_{\mathrm{s}}}{\mu}}\right)\right]^{-1} \tag{6.29}
\end{equation*}
$$

approximating the effective mass of the system as the ${ }^{\circ}$ reduced mass

$$
\begin{equation*}
\mu=\frac{m_{1} m_{2}}{m_{1}+m_{2}} \tag{6.30}
\end{equation*}
$$

and the effective stiffness as the bond stiffness, $k_{\mathrm{s}}$. The tunneling correction $\Gamma^{*}$ is unity owing to the effectively infinite barrier thickness. Rate increases owing to the increasing effective area of the escape channel with increasing bond length are neglected. Figure 6.9 shows values for the characteristic bond-cleavage time, $\tau_{\mathrm{cl}}=k_{\mathrm{cl}}{ }^{-1}$, based on Eq. (6.28). As shown in Section 6.7, there is seldom reason to seek bond lifetimes $>10^{20} \mathrm{~s}$; of the bonds selected for listing in Table 3.8, only the $\mathrm{O}-\mathrm{O}$ bond of organic peroxides falls short of this lifetime without ${ }^{\circ}$ strain or other adverse influences on bond stability.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-76.jpg?height=1202&width=1181&top_left_y=769&top_left_x=191)

Figure 6.9. Values of the characteristic time for bond breakage, $\tau_{\mathrm{cl}}$, as a function of temperature and the bond energy $\Delta \mathcal{V}$, as given by Eq. (6.28). The solid and dashed lines represent systems in which the partition function $q_{\text {long }}$ is unity (corresponding to the high-frequency limit); the dotted lines just above the solid lines represent systems in which this partition function is calculated for $\omega=7 \times 10^{13} \mathrm{rad} / \mathrm{s}$, a relatively low frequency like that of a $\mathrm{Si}-\mathrm{Si}$ bond.

b. Rate modifications in liquid and solid media. In liquids, the observed rate of thermal bond cleavage is substantially reduced by the dynamic cage effect: radicals surrounded by solvent molecules are confined for several molecular vibration times, permitting opportunities for immediate (geminate) recombination. In solids, geminate recombination is often far more probable than in liquids owing to the near absence of diffusion: the radicals are trapped in solid cages. In the interior of a stiff diamondoid solid, and in the absence of intense stress, separation of radicals commonly requires the simultaneous cleavage of additional bonds, multiplying the effective magnitude of the barrier height and drastically reducing failure rates; this can be termed a solid-cage effect.

Attachment to a ${ }^{\circ}$ rigid structure can have dramatic effects even for surface moieties. For example, while an ordinary organic peroxide, Eq. (6.31), is subject to irreversible cleavage in solution (once separated, the two radicals are unlikely to recombine), an analogous peroxide structure attached to a rigid structure will (in the absence of neighboring reactive moieties) reliably recombine on a $10^{-13} \mathrm{~s}$ time scale Eq. (6.32).

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-77.jpg?height=330&width=729&top_left_y=901&top_left_x=494)

At interior sites, a physical model for thermally activated structural damage is self-diffusion in diamondlike crystals of germanium and silicon, believed to occur largely through a vacancy-hopping mechanism (Reiss and Fuller, 1959). This process requires bond cleavage, as would a damage mechanism in a diamondoid solid; unlike an atom in the interior of a well-designed diamondoid solid, however, an atom adjacent to a vacancy has available to it both room into which to move and unsatisfied valencies with which to bond. Despite these facilitating structural features, the activation energies (which approximate the barrier energies discussed above) for vacancy diffusion in germanium and silicon (Lide, 1990) have been estimated to be 503 and 745 maJ, about 1.6 and 2.0 times their respective bond energies.

A better physical model for thermal damage in the interior of a stable diamondoid solid might be the creation of a new vacancy within a covalent crystal. For this, activation energies are far greater.

### 6.4.4. Thermomechanical bond cleavage

Tensile stress destabilizes bonds, increasing the rate of thermal cleavage and sometimes opening a tunneling path to cleavage. Large angular strains are common in organic chemistry, for example, in small rings. Substantial tensile strains are less common in organic chemistry but frequently are important in nanomechanical systems, where engineering performance often depends on the imposed stress, providing an incentive to push toward the allowable limits of stress.

a. Thermomechanical bond cleavage rates. Cleavage rates for bonds under simple tensile stress at ordinary temperatures can be approximated with a onedimensional quantum TST like that in Section 6.2.3, but with frequencies and barrier heights calculated with the aid of a potential energy function describing bond extension. Combining the Morse function Eq. (3.10) with the potential energy resulting from an applied force $F$ yields

$$
\begin{equation*}
\mathscr{V}_{\text {stressed }}=D_{\mathrm{e}}\left(\left\{1-\exp \left[-\beta\left(\ell-\ell_{0}\right)\right]\right\}^{2}-1\right)-F\left(\ell-\ell_{0}\right) \tag{6.33}
\end{equation*}
$$

Some examples are plotted in Figure 6.10.

The Morse function overestimates the bonding energy in the high extension region, underestimating the energy gradient and the tensile strength of the bond (Section 3.3.3a); it is thus conservative for engineering analyses where bond stability is required for a workable design. Equation (6.33) assumes that the applied force is independent of the displacement. Where applied forces are associated with large positive stiffnesses (e.g., for bonds in diamondoid structures) this analysis, by ignoring the solid-cage effect, grossly overestimates cleavage rates.

Manipulating the Eq. (6.33) yields the classical barrier height (Kauzman and Eyring, 1940)

$$
\begin{equation*}
\Delta \mathscr{V}=D_{\mathrm{e}} \sqrt{1-2 F / \beta D_{\mathrm{e}}}+\frac{F}{\beta} \ln \left(\frac{1-\sqrt{1-2 F / \beta D_{\mathrm{e}}}}{1+\sqrt{1-2 F / \beta D_{\mathrm{e}}}}\right) \tag{6.34}
\end{equation*}
$$

and frequencies at the well minimum and barrier maximum that yield both a one-dimensional partition function (making the conservative approximation of

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-78.jpg?height=793&width=856&top_left_y=1345&top_left_x=346)

Figure 6.10. Morse curves modified by tensile stresses ranging from 0.0 to 1.0 times the critical stress for barrier elimination.

a parabolic well),

$$
\begin{equation*}
q_{\text {quant }}=\exp (-\hbar \omega / k T)[1-\exp (-\hbar \omega / k T)]^{-1} \tag{6.35}
\end{equation*}
$$

where the frequency

$$
\begin{equation*}
\omega=\sqrt{\frac{D_{\mathrm{e}} \beta}{\mu}\left(\beta-2 F / D_{\mathrm{e}}+\sqrt{\beta^{2}-2 \beta F / D_{\mathrm{e}}}\right)} \tag{6.36}
\end{equation*}
$$

and an imaginary frequency that can be used to calculate the Wigner tunneling correction [Eq. (6.14)] is

$$
\begin{equation*}
\omega_{\mathrm{rc}}^{\ddagger}=\sqrt{\frac{D_{\mathrm{e}} \beta}{\mu}\left(\beta-2 F / D_{\mathrm{e}}-\sqrt{\beta^{2}-2 \beta F / D_{\mathrm{e}}}\right)} \tag{6.37}
\end{equation*}
$$

The zero-point energy estimate uses the harmonic approximation, yielding a (conservative) underestimate of the barrier height. All factors incorporating bond frequencies neglect the increase in effective mass and effective stiffness resulting from atoms not directly participating in the bond.

b. Tunneling cleavage rates. At sufficiently low temperatures, the Wigner tunneling correction becomes inadequate and methods like those discussed in Section 6.2.4 must be applied. At zero K, only an estimate of tunneling from the ground state is necessary; the model used here makes the preceding assumptions regarding the potential energy function and effective mass, approximating the transition rate as the product of the vibrational frequency in the well and the WKB transmission probability, Eq. (6.17). Intermediate cryogenic temperatures would require a more complex treatment, giving intermediate values of the bond lifetime.

c. Allowable stresses in covalent bonds. Figure 6.11 graphs the characteristic bond cleavage time $\tau_{\mathrm{cl}}$ vs. applied stress for various bond types at 0,300 , and $500 \mathrm{~K}$, with bond stiffnesses and dissociation energies from Table 3.8. It shows that the criterion $\tau_{\mathrm{cl}}>10^{20} \mathrm{~s}$ is met for a $\mathrm{C}-\mathrm{C}$ bond at $300 \mathrm{~K}$ if the stress is $\leq \sim 1.2 \mathrm{nN} /$ bond. Replacing each stressed $\mathrm{C}-\mathrm{C}$ bond by a pair of $\mathrm{C}-\mathrm{C}$ bonds (modeled by doubling the mass, energy, and stiffness) yields the second curve from the right; note that the threshold stress for this system is $\sim 6 \mathrm{nN}$, substantially more than twice the single-bond threshold stress. This is a consequence of the additivity of the barrier energies for individual bonds combined with the exponential dependence of the cleavage rate on the total barrier. In diamondoid structures, failure commonly requires the simultaneous cleavage of several bonds, hence the acceptable working stress per bond can be substantially higher than for a structure relying on just one bond.

Allowable stresses are strongly temperature dependent: Although this volume is concerned with systems at room temperature, a wider range of structures and stresses can be used at cryogenic temperatures. Conversely, as temperatures increase, workable designs become increasingly constrained, ultimately dwindling to none.

These calculations can be compared to the theoretical tensile strength of diamond estimated by Lawn as $\sim 1.9 \times 10^{11} \mathrm{~N} / \mathrm{m}^{2}$ (Field, 1979). Diamond normally cleaves along a (111) plane, which has $1.8 \times 10^{19}$ bonds $/ \mathrm{m}^{2}$; the strength just
cited corresponds to $\sim 10.6 \mathrm{nN} /$ bond, roughly twice the theoretical limiting strength implied by the more conservative calculations of this section. Lawn also calculates a shear strength of $\sim 1.2 \times 10^{11} \mathrm{~N} / \mathrm{m}^{2}$ (Field, 1979), or $6.7 \mathrm{nN} /$ bond. At $\sim 1300 \mathrm{~K}$, diamond undergoes plastic flow under mean shear stresses as low as $0.18 \mathrm{nN} /$ bond (Brookes et al., 1988), but this process depends on the breakage of bonds in dislocations (where stresses are far higher than the mean) and occurs at temperatures that rapidly cleave $\mathrm{C}-\mathrm{C}$ bonds in normal hydrocarbons.

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-80.jpg?height=1491&width=1091&top_left_y=533&top_left_x=224)

Figure 6.11. Characteristic bond cleavage time vs. applied stress at 0,300 , and $500 \mathrm{~K}$. Calculations at 300 and $500 \mathrm{~K}$ are based on quantum transition state theory (Section 6.2.3); those at zero $\mathrm{K}$ are based on the WKB tunneling approximation (Section 6.2.4). The second curve from the right represents a pair of single $\mathrm{C}-\mathrm{C}$ bonds mechanically constrained to cleave in a concerted process.

### 6.4.5. Other chemical damage mechanisms

a. Elementary, nonelementary, and solvent-dependent reactions. As suggested by Section 6.4.2c, intramolecular reactions provide important models for damage mechanisms of significance in nanomechanical systems. Common intramolecular reactions include elimination (loss of part of a molecule) and rearrangements (structural transformations that leave overall composition unchanged). Often, however, such transformations occur by intermolecular processes, or by intramolecular processes that are solvent dependent.

A simple example is an elimination reaction sometimes written as

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-81.jpg?height=136&width=884&top_left_y=590&top_left_x=580)

This does not occur at an appreciable rate among molecules isolated in vacuum, because the reaction does not occur as shown. The above equation represents a reaction (or compound reaction), but not an elementary reaction, which is to say a single molecular transformation. Not all reactions are elementary, and mistaking a compound reaction for an elementary reaction can lead to mistaken conclusions.

The steps yielding ethylene in Eq. (6.38) can proceed by at least two distinct mechanisms comprising three elementary reactions. The first mechanism is a single-step E2 process, such as:

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-81.jpg?height=306&width=1045&top_left_y=1140&top_left_x=423)

The second is a two-step E1 process, such as:
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-81.jpg?height=250&width=960&top_left_y=1538&top_left_x=516)

Neither reaction mechanism actually yields an $\mathrm{HBr}$ molecule as shown in Eq. (6.38), and both require the participation of other molecules. The 2 in E2 refers to the requirement for participation of two molecules in the slow, ratelimiting step; the 1 in E1 indicates that the rate-limiting step is unimolecular. Even the first step of the E1 reaction is solvent dependent: the separation of a positive and negative ion from $0.3 \mathrm{~nm}$ to $3 \mathrm{~nm}$ in vacuum requires $\sim 700 \mathrm{maJ}$ of energy, but in a medium with the dielectric constant of water, only $\sim 9$ maJ. For similar reasons, $\mathrm{Na}^{+}$and $\mathrm{Cl}^{-}$ions readily leave a salt crystal in water, causing swift dissolution despite the lack of any significant tendency for salt to evaporate

Table 6.1. Temperatures for 30 -minute volatilization half-lives in the absence of air (Schnabel, 1981).

| Polymer | $T_{\text {vol }}(\mathrm{C})$ | $T_{\text {vol }}(\mathrm{K})$ |
| :--- | :---: | :---: |
| Polytetrafluoroethylene | 510 | $\sim 780$ |
| Polybutadiene | 410 | $\sim 680$ |
| Polypropylene | 400 | $\sim 670$ |
| Polyacrylonitrile | 390 | $\sim 660$ |
| Polystyrene | 360 | $\sim 630$ |
| Polyisobutene | 350 | $\sim 620$ |
| Poly(ethylene oxide) | 350 | $\sim 620$ |
| Polymethylacrylate | 330 | $\sim 600$ |
| Polymethylmethacrylate | 330 | $\sim 600$ |
| Polyvinylacetate | 270 | $\sim 540$ |
| Polyvinylchloride | 260 | $\sim 530$ |

into the vacuumlike emptiness of air. In general, processes generating free ions are unusual in vacuum at $300 \mathrm{~K}$.

b. Evidence from pyrolysis. The one-dimensional TST-derived relationships described in Section 6.4.3 can be used to estimate intramolecular reaction rates at $300 \mathrm{~K}$ from reaction rates at higher temperatures (the ratio of partition functions is constant in the classical harmonic approximation, and is treated as constant here). If rates scale as in Eq. (6.28), then a species requiring $\geq 1 \mathrm{~s}$ at $\geq 750 \mathrm{~K}\left(\approx 480^{\circ} \mathrm{C}\right.$ ) to undergo thorough pyrolysis has a transformation lifetime $\tau_{\text {trans }} \geq 10^{20} \mathrm{~s} /$ molecule at $300 \mathrm{~K}$. Thermal exposure times of 1 to $100 \mathrm{~s}$ are common in pyrolysis experiments in organic chemistry (Brown, 1980).

These experiments (discussed in Section 6.4.5d), like the polymer degradation experiments discussed in the next section, give evidence regarding the suitability of various classes of structures for use as major components of longlifetime nanomechanical systems. As should be expected, some are adequate and others are too unstable.

c. Polymer pyrolysis. In the pyrolysis of polymers, $50 \%$ weight loss during $30 \mathrm{~min}$ at $610 \mathrm{~K}\left(\approx 340^{\circ} \mathrm{C}\right.$; centigrade is temporarily adopted here in reporting results from the chemical literature) suggests a rate for fragmentation reactions of $\leq 10^{-20} \mathrm{~s}^{-1}$ per monomer at $300 \mathrm{~K}$. Table 6.1 lists the characteristic temperatures for various polymers; data regarding heat resistant polymers can be found in Critchley et al. (1983). Note that many exceed $610 \mathrm{~K}$ despite the availability of intermolecular processes for degradation; polyvinylchloride, for example, is thought to undergo elimination of $\mathrm{HCl}$ via a radical chain reaction mechanism. In estimating the failure rate of nanomechanical systems, most analyses in this volume assume that the first chemical transformation is sufficient to cause failure (Section 6.7.1a), making chain reactions irrelevant. Polymer degradation studies are accordingly better for establishing lower bounds on achievable stability than they are at establishing upper bounds.

These empirical observations can also be criticized for being sensitive to the cleavage of polymer backbones, but perhaps not to rearrangements of side chains. Rearrangements are better examined in small molecules.

d. Unimolecular elimination, fragmentation, and rearrangement. The rapid pyrolysis of small organic molecules in the gas phase provides a useful model for long-term damage to machine-phase systems at room temperature. These processes can provide a guide to the relationship between stability and local molecular structure. This section offers examples of reactions and sketches some imperfect generalizations regarding molecular stability.

Many structures suffer elimination reactions that proceed at unacceptably high rates at room temperature. In reactions such as
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-83.jpg?height=310&width=824&top_left_y=696&top_left_x=434)

bonds rearrange to make the extremely stable $\mathrm{N}_{2}$ molecule. Reaction (6.42) proceeds quickly at $200 \mathrm{~K}$, but reaction (6.43) does so only at $\geq 370 \mathrm{~K}$ (Carey and Sundberg, 1983b); the difference in reaction mechanism stems from differences in orbital symmetry. Other processes of this sort yield $\mathrm{CO}, \mathrm{CO}_{2}$ and $\mathrm{H}_{2}$. Under pyrolytic conditions, hydrogen halides can be eliminated from alkyl halides [possibly as shown in Eq. (6.44), or in a surface reaction].
![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-83.jpg?height=444&width=812&top_left_y=1324&top_left_x=440)

An extensive review of eliminations under gas-phase pyrolytic conditions appears in Brown (1980), from which reactions (6.44) through (6.46) are taken. Chapter 7 of Carey and Sundberg (1983b) provides a brief overview of elimination reactions and discusses some classes of unimolecular rearrangements of chemical interest. Examples include Cope rearrangements

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-83.jpg?height=152&width=743&top_left_y=2047&top_left_x=492)
and unimolecular ene reactions

![](https://nanosystems.contact.ms/cropped/2024_03_29_6d376e07030ca6d2df72g-84.jpg?height=193&width=697&top_left_y=234&top_left_x=423)

Brown (1980) surveys reactions occurring during gas-phase pyrolysis, describing hundreds of examples of reactions from numerous classes. It is possible to draw some conclusions from this body of data (though without formulating generalizations that neatly categorize molecules according to stability). Brown's stated selection criteria favor the inclusion of reactions that are (1) useful in organic synthesis and (2) proceed at temperatures $>350^{\circ} \mathrm{C}$. The criterion of usefulness favors the inclusion of molecules having a specific reactivity, that is, a specific weakness relative to more inert molecular structures (such as aliphatic hydrocarbons of low strain). Further, the objective of maximizing reaction specificity tends to favor use of the lowest temperatures at which reaction rates are adequate for practical work. Of the structures in Brown (1980), selected for exhibiting useful pyrolytic reactions, the fraction having listed reaction temperatures $>500{ }^{\circ} \mathrm{C}$ (suggesting adequate stability for nanomechanical use at room temperature) is roughly half.

For pyrolytic reactions in general, the structural characteristics favoring reaction temperatures $\leq 480^{\circ} \mathrm{C}$ are too complex to enumerate, but include inherently weak covalent bonds, resonant stabilization of reaction products, high strain, and others. A generalization does hold for the set of unimolecular rearrangements reviewed in Brown (1980): listed reaction temperatures are $>480^{\circ} \mathrm{C}$ unless the molecule either (1) contains two or more pi bonds, or (2) contains both a strained, three-membered ring and one or more pi bonds, or (3) contains a strained, four-membered ring that includes a single pi bond (many molecules with one or more of these features nonetheless have listed reaction temperatures $>480^{\circ} \mathrm{C}$ ). Exceptions to this generalization (including any number of compounds with inherently weak bonds) can be found elsewhere in the literature.

It should be noted that surface-catalyzed and intermolecular gas-phase reaction pathways may occur in some of the systems reviewed in Brown (1980). Removing these pathways can only improve stability. (Rearrangements occurring under various conditions are reviewed in the volumes of Thyagarajan, 1968-1971.)

The thermal rearrangement of hydrocarbons, which has been practiced on a large scale in the petroleum industry to increase the octane rating of gasoline, is relevant to estimating the failure rates of molecules having no special destabilizing characteristics. The temperatures applied are in the 780 to $840 \mathrm{~K}$ range $(\sim 500$ to $570^{\circ} \mathrm{C}$ ), with exposure times of many seconds; this implies $\tau_{\text {trans }}>10^{20} \mathrm{~s}$ at $300 \mathrm{~K}$.

The study of pyrolytic reactions in small molecules provides useful indications of stability in nanomechanical systems at $300 \mathrm{~K}$, but fails to account for two expected differences. The first is the presence of mechanically imposed tensile and shear stresses: these are destabilizing and are, at best, only partially modeled by the methods of Section 6.4.4. Since activation energies for rearrangements frequently fall within the range of activation energies for the cleavage of structurally useful bonds, it seem safe to assume that failure from rearrangement under moderate applied stresses will in these instances meet the $\tau_{\text {trans }}>10^{20} \mathrm{~s}$ at $300 \mathrm{~K}$ criterion.

The second difference is that potentially unstable substructures found in nanomechanical systems commonly are constrained by diamondoid matrices. As we have seen, thermal bond cleavage can be strongly inhibited by the solidcage effect. Likewise, many rearrangements involve atomic displacements that are feasible in flexible structures, but not in more diamondlike structures. An example is the conrotary thermal ring opening of cyclobutene, Eq. (6.49) [with orbitals and transition geometry shown in Eq. (6.50)] contrasted with the expected behavior of a constrained analogue, Eq. (6.51).

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-01.jpg?height=562&width=794&top_left_y=747&top_left_x=457)

A useful exercise is to examine a list of rearrangement reactions and observe how few could occur if most bonds to hydrogen atoms on a molecular surface were instead bonds to carbon atoms in a surrounding matrix of diamondlike rigidity. Diamond itself is stable to $1800 \mathrm{~K}$ in an inert atmosphere $\left(\tau_{\text {trans }}>10^{85} \mathrm{~s}\right.$ at $300 \mathrm{~K}$ ), despite the well-known energetic advantage of rearrangement to graphite.

For the nanomechanical design process, it would be useful to develop an automated classification system capable of reliably labeling structures as adequately stable, inadequately stable, or of unknown adequacy, with the set of structures labeled as adequately stable being large enough to permit effective nanomechanical design. Such a design tool could in substantial measure be validated using the existing data on small-molecule pyrolysis. Lacking a tool of this sort, one must proceed using informal chemical reasoning (drawing on the accumulated generalizations of organic chemistry) and analogy based on model compounds (drawing on the yet more massive accumulation of data in organic chemistry), supplemented by computational methods. The strategy pursued in the present work is to favor structures in which strong bonds form frameworks of diamondlike rigidity that lack substructures of known instability. This strategy is more likely to exclude workable designs (yielding false negatives) than to include unworkable designs (yielding false positives). As development progresses, both classes of error will be reduced.

e. Stability of reagent devices. Molecular manufacturing systems include devices containing moieties that play the role of reagents in organic synthesis. These evidently cannot be designed for high stability in a general sense, hence their stability against unwanted chemical transformations must in practice be examined on a case-by-case basis.

Some broad observations can be made: Reagent moieties make up only a small fraction $\left(10^{-3}\right.$ to $\left.10^{-6}\right)$ of the mass of a molecular manufacturing system as presently conceived; this somewhat reduces their quantitative significance as targets for damage. Further, they are subject to rapid cycles of synthesis and use, rather than serving as structural elements that must be stable for the life of the system; this can reduce their significance as targets for damage. Finally, the reagent devices used in a molecular manufacturing system can be selected from a wide range of candidate structures, including analogues of familiar reagents, catalysts, and reactive intermediates; this generates a large set of options with varying stability characteristics.

The stability of a reagent device depends on its design, which depends in part on its application. Chapter 8 discusses reagent devices in the context of mechanochemical operations, giving special attention to the stability and use of structures that would in solution chemistry be regarded as nonisolable reactive intermediates.

### 6.4.6. The stability of surfaces

Surfaces present special problems only if one regards a bulk phase as the norm. The present work, however, relies chiefly on concepts and models based on the chemistry of small molecules. These molecules are, in effect, all surface. Accordingly, the concepts and models need no modification to make them applicable to surfaces of the sort contemplated here. From this perspective, surfaces are the norm, and it is (for example) the special stability of the diamond interior relative to small, surface-dominated hydrocarbons that has been worthy of remark.

It is well known in materials science that surface diffusion occurs more readily than diffusion in bulk materials, that surfaces frequently undergo spontaneous ${ }^{\circ}$ reconstruction to form arrangements unlike those in the interior, that surfaces are associated with modified electronic properties in semiconductors, and so forth. In judging the significance of these concerns in a particular instance, the nature of the material is crucial.

Metals, for example, frequently exhibit high surface reactivity, diffusion, or both. Nanometer-scale pits made on gold surfaces have been observed to refill through surface diffusion in minutes to hours at room temperature (Emch et al., 1988), but the surface atomic layer of gold is unusual: it has a slightly different lattice spacing from that of the bulk material, presumably facilitating motion. Although some metals and metal surfaces have adequate stability for use in eutactic nanosystems, this volume does not propose using metals in structural roles in nanomechanical components. Section 6.5 discusses the use of aluminum films for photochemical shielding, but films of the sort required are familiar in present technology and can tolerate atomic rearrangements. Section 11.6.1 discusses metals as conductors in electromechanical systems, but even here, alternative conductors are feasible.

Unlike metals, semiconductors are covalently bonded solids somewhat resembling the diamondoid components discussed in Part II. Clean semiconductor surfaces in vacuum consistently exhibit high reactivity and often undergo reconstruction. This unstable behavior, however, disrupts surfaces that a chemist would regard as dense arrays of free radicals or highly strained bonds. Nanomachines need not have such surfaces. Polished, hydrogenated diamond surfaces, in contrast, do not undergo surface reconstruction until heating (at $\geq 1275 \mathrm{~K}$ ) has removed the hydrogen (Hamza et al., 1988). Until then, diamond is an unusually stable hydrocarbon. A wide range of other diamondoid structures with chemically reasonable surfaces should likewise exhibit excellent stability.

### 6.4.7. Thermal ionization and charge separation

The production of an unwanted ion pair in a nanomechanical system could easily disrupt its function; the threshold energies for ionization are therefore of interest. Ionization of a typical organic molecule in vacuum requires $>1.3 \mathrm{aJ}$, and producing an electron-hole pair within diamond requires $\sim 0.864 \mathrm{aJ}$. Structures of this sort undergo thermal ionization at negligible rates at ordinary temperatures, owing to the large energy required to produce charge separation. Mechanical energy applied to moving nanomechanical parts can do charge-separation work, but only if initial charge separation has occurred, placing opposite charges on adjacent moving surfaces.[^16] The ease of producing ions by thermal processes in polar solvents, however, shows that ionization can readily occur in some structures. Indeed, with a suitable arrangement of polar groups around a pair of sites, one of low ionization energy and the other of high electron affinity, ionization can be spontaneous and stable. Ensuring a stable charge distribution will preclude the use of certain structures, but alternatives will usually be feasible. For example, if bearing interfaces with facing arrays of polar groups [e.g., Figure 10.15(d)] were to pose a problem, redesigned bearings with less-polar surfaces [e.g., Figure 10.15(a)] could in most instances be substituted with little loss of system-level performance. Unwanted thermomechanical ionization can be limited to negligible rates in well-designed nanomechanical systems at $300 \mathrm{~K}$.

### 6.5. Photochemical damage

### 6.5.1. Energetic photons

Photochemical processes can excite molecules to energies that are effectively unavailable in equilibrium systems at ambient temperatures. Photons at visible and ultraviolet wavelengths (for example, in sunlight) have energies that are

Table 6.2. Wavelengths, frequencies, and energies

| Band name | Wavelength range <br/> $(\mathrm{nm})$ | Maximum frequency <br/> $(\mathrm{Hz})$ | Maximum energy <br/> $(\mathrm{aJ})$ |
| :---: | :---: | :---: | :---: |
| Visible | $700-400$ | $7.5 \times 10^{14}$ | 0.50 |
| UV-A | $400-320$ | $9.4 \times 10^{14}$ | 0.62 |
| UV-B | $320-280$ | $1.1 \times 10^{15}$ | 0.71 |
| UV-C | $280-200$ | $1.5 \times 10^{15}$ | 1.00 |

characteristic of far higher temperatures (for example, the $\sim 5800 \mathrm{~K}$ of the solar photosphere) and they can deliver that energy to a single molecular site.

Where photochemical damage in the ambient terrestrial environment is concerned, the electromagnetic spectrum has traditionally been divided as shown in Table 6.2. Ultraviolet exposure is limited by atmospheric opacity: From the visible to the UV-B, the atmosphere transmits solar radiation; within the UV-C, absorption by oxygen and ozone effectively blocks solar radiation; at energies beyond the UV-C (the vacuum ultraviolet range), air is opaque. Consequently, both solar and local radiation sources are hazardous in the visible to UV-B range, only local sources are hazardous in the UV-C, and exposure in the vacuum ultraviolet is (within the atmosphere) usually negligible. At yet higher energies, the UV spectrum merges into the $x$-ray spectrum and photons become both penetrating and ionizing; the resulting damage is discussed in Section 6.6.

### 6.5.2. Overview of photochemical processes

Photochemical processes at a given wavelength begin with the absorption of a photon, which requires a chemical species able to absorb at that wavelength. Ordinary ${ }^{\circ}$ alkanes, alcohols, ${ }^{\circ}$ ethers, and ${ }^{\circ}$ amines absorb at wavelengths $<230 \mathrm{~nm}$ (Robinson, 1974), deep in the UV-C. In the absence of oxygen and other photochemically sensitive molecules, lack of absorption renders these substances photochemically stable (by ordinary standards) under ambient UV conditions. Systems of pi electrons characteristically absorb at longer wavelengths (organic dyes, which absorb at visible wavelengths, contain large ${ }^{\circ}$ conjugated pi systems). Quantum mechanical selection rules constrain electronic transitions and absorption cross sections. Multiphoton absorption processes relax constraints on photon energies but require intensities seldom encountered in the absence of lasers.

For a process to do permanent damage to a nanomachine, bonds must be rearranged or cleaved, or a charge must be displaced and trapped. For a given molecular structure, each process has an energy threshold. Energy thresholds for ionization have been discussed in Section 6.4.7; typical energies for molecular ionization are in the vacuum ultraviolet range, and the production of an electron-hole pair in diamond requires a photon of $\lambda<230 \mathrm{~nm}$. Energy thresholds for rearrangements vary greatly with molecular structure and can be quite low. In laboratory photochemistry, rearrangements often involve conjugated pi systems. Broad classes of structures resist low-energy rearrangement.

Bond cleavage requires an energy equal to or greater than the dissociation energy of the bond; in practice, it often requires significantly more energy, since the photochemical process that overcomes the negative potential energy of the
bond also deposits energy in vibrational and electronic excitations. Many bonds of interest in constructing nanomechanical systems-including carbon-carbon bonds-are subject to cleavage at UV-A and UV-B energies.

Photochemical bond cleavage is more common in low-pressure gases than in condensed matter, where competing processes more efficiently dissipate excitation energy. Further, in condensed matter, photochemical (like thermal) bond cleavage frequently is reversed by geminate recombination. Bond cleavage can be characterized by quantum yield, the ratio of bonds cleaved to photons absorbed. For ${ }^{\circ}$ carbonyl-rich polymers, such as poly(methyl-isopropyl ketone), quantum yields are as high as 0.22 at $\lambda=253.7 \mathrm{~nm}$; for polystyrene, the quantum yield is $9 \times 10^{-5}$ (Ranby and Rabek, 1975).

In diffusive chemistry, the consequences of photochemical reactions can be complex. Free radicals can initiate chain reactions involving various reactive species, and all species have unconstrained opportunities for collision. In a structured solid phase, the opportunity to build more constrained systems enables the construction of systems with simpler behavior, including reduced sensitivity to photochemical damage.

### 6.5.3. Design for photochemical stability

In designing nanomechanical systems, photochemical damage can be limited or avoided in three alternative ways:

1. by keeping the entire system away from UV light,
2. by providing the system with a UV-opaque surface layer, or
3. by requiring that all components be photochemically stable.

Approach (1) is simple and workable for many purposes, but limits the nature of operating environments. Approach (2) is analyzed in the next section. Approach (3) would be preferable for some applications, but adding the constraint of photochemical stability would substantially increase the complexity of molecular systems design and eliminate device designs that would otherwise be attractive. The discussion in the present work assumes the use of approach (1) or (2), thereby avoiding photochemical stability constraints in device structures.

It is nonetheless worth briefly considering how one might design systems within the constraints of approach (3). One methodology would focus on absorption processes, attempting to avoid all use of structures that absorb in the UV-A and UV-B bands, but this may not prove practical. An alternative methodology would examine all potential modes of absorption and attempt to ensure that the absorbing structures can tolerate the resulting photochemical excitation. Tolerance for excitation is more achievable in a structured solid phase than in a liquid phase, owing to greater control of reaction opportunities and radical recombination processes. One approach would be to seek structures in which mechanical constraints force swift recombination of any cleaved bond: complications include photoexcitation to triplet states (delaying recombination in a manner that is rare in thermal processes) and rearrangements that trap the system in a ground-state potential well other than that desired. In summary, it may prove possible to develop a library of nanomechanical components that meet the stringent conditions required for UV-B exposure tolerance, but for the present it is easier to assume the use of shielding.

Table 6.3. UV optical properties of aluminum (Gray, 1972).

| Wavelength <br/> (nm) | $n$ | $k$ |
| :---: | :---: | :---: |
| 120 | 0.057 | 1.15 |
| 160 | 0.080 | 1.73 |
| 200 | 0.110 | 2.20 |
| 320 | 0.280 | 3.56 |
| 400 | 0.400 | 4.45 |

### 6.5.4. Photochemical shielding

Most metals block UV radiation of ordinary wavelengths, and aluminum is among the most opaque in thin-film form. The optical transmittance of a metal layer is determined (Gray, 1972) by its index of refraction, $n$, its extinction coefficient, $k$, and (secondarily) by the indexes of refraction of the adjacent media, $n_{1}$ and $n_{2}$. Table 6.3 lists values of $n$ and $k$ for aluminum at UV wavelengths. When an absorbing layer is thick enough, one can neglect interference among reflected waves within the layer. In this single-path approximation, appropriate for shielding calculations, the transmittance is given by:

$$
\begin{equation*}
T=\frac{16 n_{1} n_{2}\left(n^{2}+k^{2}\right)}{\left[\left(n+n_{1}\right)^{2}+k^{2}\right]\left[\left(n+n_{2}\right)^{2}+k^{2}\right]} \exp (-4 \pi k d / \lambda) \tag{6.52}
\end{equation*}
$$

where $d$ is the thickness of the metal layer. Figure 6.12 graphs the transmittance of aluminum layers as a function of their thickness, at several UV wavelengths.

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-06.jpg?height=757&width=1107&top_left_y=1368&top_left_x=223)

Figure 6.12. Transmittance (fraction of optical power transmitted) vs. thickness of aluminum for various wavelengths, $n_{1}=n_{2}=1.5$. Values computed from Eq. (6.52) and Table 6.3.

Note that transmittance is nearly independent of wavelength from the UV-A to the edge of the vacuum ultraviolet.

A typical shield thickness is readily estimated. Assume that the mean time between (photochemical) failures is required to be 30 years $\left(\approx 10^{9} \mathrm{~s}\right)$ for a system with an area of one square micron exposed to terrestrial sunlight. Assume that the mean power density at effective wavelengths is $5 \mathrm{~W} / \mathrm{m}^{2}$, that all shieldpenetrating photons are absorbed in the system, that cleavage of one bond causes the system to fail, and that the quantum efficiency of bond cleavage is $10^{-2}$. With these assumptions, the mean photon flux is $\sim 10^{19} \mathrm{~m}^{-2} \mathrm{~s}^{-2}$, the $30-$ year dose to the system surface is $10^{16}$ photons, and the transmittance must be limited to $10^{-14}$ or less, which can be achieved with a shield thickness of just under $250 \mathrm{~nm}$. Including a shield of this thickness imposes a large volumetric penalty on a system with an overall diameter of $2 \mu$, but only a modest penalty on a system with a diameter of $10 \mu$.

### 6.6. Radiation damage

### 6.6.1. Radiation and radiation dosage

Forms of ionizing radiation include high-energy photons and charged particles. At a nanometer scale, most of the damage done by these forms of radiation is mediated by high-energy secondary electrons. Experiments show that the energy carried by charged particles (including secondary electrons) is chiefly deposited in chains of excitation events with spacings ranging from a several hundred nanometers at $\mathrm{MeV}$ energies, to $\sim 10 \mathrm{~nm}$ at $5 \mathrm{keV}$, to a virtual continuum at low energies; the local chemical effects are like those of UV radiation in the 10 to $30 \mathrm{eV}$ range (Williams, 1972).

Ionizing radiation is measured both in rads ( $1 \mathrm{rad}=100$ ergs absorbed per gram $=10^{-2} \mathrm{~J} / \mathrm{kg}$ ) and in roentgens (defined in terms of ionization produced in air by $x$-ray and gamma radiation; 1 roentgen deposits $\sim 87$ ergs in a gram of air). For many forms of ionizing radiation impinging upon light-element targets, the quantity of energy absorbed by a small volume of matter is roughly proportional to its mass. Background radiation in the terrestrial environment seldom exceeds $0.5 \mathrm{rad} / \mathrm{year}$.

### 6.6.2. Classical radiation target theory

Existing experimental evidence relates radiation dosage to damage in molecular machinery, where that molecular machinery takes the form of proteins serving as enzymes. Classical radiation target theory (Lea,1946) is a standard technique for estimating the molecular mass of enzymes from the loss of enzymatic activity as a function of radiation dose applied to dried enzyme in vacuum (Beauregard and Potier, 1985; Kepner and Macey, 1968). In the target-theory model, a single hit suffices to inactivate an enzyme molecule, and the probability that a molecule will be hit is proportional to its mass (for radiation doses small enough to make multiple hits improbable). Studies of the inactivation of enzymes of known molecular weight indicate that roughly $10.6 \mathrm{aJ}$ of absorbed radiation is required to produce one inactivating hit (Kepner and Macey, 1968), yielding $\sim 10^{15} \mathrm{hits} / \mathrm{kg} \cdot \mathrm{rad}$.

How good is this relationship for estimating the rate of destruction of nanomechanical systems owing to radiation damage? As a rough guide, it should be fairly reliable because it rests directly on experimental evidence. It must, however, be somewhat inaccurate owing to the physical differences between the targets. Proteins can tolerate small changes in side-chain structure at many sites without loss of function, as shown by protein engineering experience (Ponder and Richards, 1987b; Bowie et al., 1990); this suggests a significant ability to absorb structure-altering events while remaining active, which in turn suggests that nanomachines of more tightly constrained design tend to be more sensitive to radiation damage. Weighing on the other side, however, is the greater radiation tolerance of diamondoid structures: where geminate recombination of radicals is strongly favored by mechanical constraints, only a small fraction of excitation events cause a permanent change. This suggests that typical nanomachines tend to be less sensitive to radiation damage than are proteins, which readily undergo backbone cleavage. In summary, nanomachines have a greater fraction of sites at which excitations of bond-cleaving magnitude cause no permanent alteration, and proteins have a greater fraction of sites at which permanent alterations can be tolerated. On the whole, it seems reasonable to assume that diamondoid nanomachines, like proteins, suffer $\sim 10^{15}$ inactivating hits per kilogram per rad. For this estimate to err by being substantially too low would require that enzymes have an implausibly large probability of surviving random structural damage. In this model, the probability that an initially functional component has not been destroyed by radiation damage is

$$
\begin{equation*}
P_{\text {func }} \approx \exp \left(-10^{15} D m\right) \tag{6.53}
\end{equation*}
$$

where $D$ is the dose in rads and $m$ the component mass in kilograms.

### 6.6.3. Effects of track structure

Aside from structural differences, typical nanomechanical systems are far larger than typical enzymes. This affects scaling relationships because radiation hits are distributed not at random, but along particle tracks. In the range of sizes for which the diameter of a mechanism is large compared to the spacing of excitation events along a typical particle track (while remaining small compared to the length of the track), damage becomes proportional not to mass but to area, and hence scales not as $m$ but as $m^{2 / 3}$. In typical radiation environments, components of ordinary density with a diameter of $100 \mathrm{~nm}$ or greater should benefit from this favorable breakdown in linearity. A rough model representing this shift from $m$ to $m^{2 / 3}$ scaling in the vicinity of $100 \mathrm{~nm}$ diameters is

$$
\begin{equation*}
P_{\text {func }} \approx \exp \left(\left\{-\left(10^{15} D m\right)^{-1}-\left[10^{11} D(m / \rho)^{2 / 3}\right]^{-1}\right\}^{-1}\right) \tag{6.54}
\end{equation*}
$$

where $\rho$ is the density of the component in $\mathrm{kg} / \mathrm{m}^{3}$. This model (graphed in Figure 6.13) neglects various factors affecting track structure (though ionizing-event spacing is taken to scale inversely with density). It uses an arbitrary functional form to represent the transition between regimes, and should be taken as only a rough guide to damage rates for large components.

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-09.jpg?height=758&width=1073&top_left_y=159&top_left_x=322)

Figure 6.13. Probability of component failure owing to ionizing radiation damage vs. radiation dose, according to Eq. (6.54), for components of differing masses; assumes failure after a single hit and a component density equaling that of water. Background radiation in the terrestrial environment seldom delivers more than $0.5 \mathrm{rad} /$ year, marked as "typical annual dose." Note that at the assumed density, the graphed curves correspond to component volumes ranging from $1 \mathrm{~nm}^{3}$ to $10^{12} \mathrm{~nm}^{3}=(10 \mu)^{3}$.

### 6.6.4. Radiation shielding

To shield against ionizing radiation usually requires macroscopic thicknesses of dense material, ranging from a fraction of a millimeter for medium-energy alpha particles to meters for gamma and cosmic rays. Earth's atmosphere has an areal mass density of $\sim 10^{4} \mathrm{~kg} / \mathrm{m}^{2}$, yet showers of secondary particles from cosmic rays deliver a significant annual dose at sea level.

Any nonzero exposure to ionizing radiation adversely affects either the reliability or the feasible performance of nanoscale systems, yet even with extensive macroscale engineering, radiation exposure seems inescapable. Thick layers of nonradioactive shielding materials, although able to reduce radiation exposure by large factors, cannot prevent sporadic showers of secondary particles resulting from high-energy cosmic-ray neutrinos. These particles can penetrate planetary thicknesses of rock, and the resulting showers of secondaries have been observed in deep mines, moving upward (Hendricks et al., 1969; Krishnaswamy et al., 1969).

### 6.7. Component and system lifetimes

### 6.7.1. Component lifetimes

a. The single-point failure assumption. Under the conditions of machinephase chemistry, some sources of molecular damage (e.g., reactions with water and free oxygen) are excluded, and most others are subject to control during the design phase. Damage rates can accordingly be quite low. A single chemical
transformation, however, can cause failure. Since a typical system may consist of $10^{6}$ to $10^{12}$ atoms, damage sensitivity can be quite high.

Components of sufficient size can avoid this sensitivity: macroscale machines are proof of this. The exclusive use of large-scale components, however, would sacrifice many of the scaling-law advantages of systems of minimal size. Accordingly, to simplify analysis and ensure conservatism, the present work in most instances assumes that components fail if they experience a single chemical transformation anywhere in their structures. This is the single-point failure assumption. (Chapter 14 discusses larger, damage-tolerant structures.)

In macroscale systems, cumulative wear and fatigue often determine component lifetimes. Wear involves removal of material from a surface, which requires chemical transformations. Fatigue is more subtle, but entails changes in chemical bonding associated with displacements of atoms (e.g., the motion of dislocations). Note, however, that cumulative wear and fatigue play no role in the component lifetimes when the single-point failure assumption is applied: the first chemical transformation step is regarded as fatal, making cumulative processes irrelevant. The elementary mechanisms responsible for cumulative wear and fatigue in macroscale systems can cause damage in nanomechanical systems, but in diamondoid structures they are mostly subsumed by the thermomechanical damage mechanisms discussed in Section 6.4. If damage is avoided, cumulative effects do not occur, and so wear and fatigue as such are absent. Failure rates in as-yet undamaged components are accordingly independent of age.

b. Choosing reliability criteria. What will be the main causes of chemical transformation and resulting failure? By a suitable choice of design, almost any mechanism could be made dominant. By permitting exposure to photochemically active UV wavelengths, photochemical damage could be made dominant; by using organic peroxides or highly strained bonds as structural elements, bond cleavage could be made dominant; other choices could make rearrangements or interfacial reactions dominant. All of these damage mechanisms, however, are subject to rate laws that are exponentially dependent on parameters that are subject to engineering control. Under ambient terrestrial conditions, all can be reduced to low levels by careful design, augmented by experimental testing and redesign if necessary.

Ionizing radiation is less subject to control. Although (imperfect) shielding is possible, it would often be awkward: major reductions in radiation exposure require shielding thicknesses measured in meters, in contrast to the hundreds of nanometers that suffice at UV-A, -B, and -C wavelengths. The present work assumes that ambient terrestrial radiation sets a practical lower bound on molecular damage rates.

This practical lower bound can be used to choose design criteria for other damage rates. Various engineering objectives can be served by using structures of marginal stability; examples include high mechanical speeds (associated with high bond stresses), compact designs (associated with exploitation of relaxed design rules on bond types and geometries), and so forth. Reliability, however, is itself a major engineering objective. Given the assumption of a fixed, structureindependent failure rate resulting from ionizing radiation, it is reasonable to constrain the controllable damage mechanisms to be comparatively small. This is the radiation-damage dominance criterion.

In the terrestrial environment, the level of background radiation rarely exceeds $\sim 0.5 \mathrm{rad} /$ year, which corresponds to $\sim 1.5 \times 10^{7} \mathrm{hits} / \mathrm{kg} \cdot \mathrm{s}$ (Section 6.6). The single-point failure assumption implies that a hit may be equated to a cleaved bond or any other damaging transition. If we demand that all other damage rates be an order of magnitude lower than radiation damage rates, then an acceptable mean failure rate per bond in small structures $(100 \mathrm{~nm}$ diameter or less) is $\sim 10^{-20} \mathrm{~s}^{-1}$, given typical numbers of bonds per kilogram. The $250 \mathrm{~nm}$ photochemical shielding thickness calculated in Section 6.5.4 meets this criterion in full sunlight at Earth's surface. For thermally activated processes, Eq. (6.28) (with $\left.q_{\text {long }}=1\right)$ indicates that failure rates remain acceptable so long as all barrier heights ( $\approx$ activation energies) exceed $\sim 313 \mathrm{maJ}$ at $300 \mathrm{~K}$, or $\sim 366 \mathrm{maJ}$ at $350 \mathrm{~K}$.

In the absence of strong stresses or other destabilizing influences, most covalent bonds of interest (in particular, those between $\mathrm{C}$ and $\mathrm{H}, \mathrm{N}, \mathrm{O}, \mathrm{F}, \mathrm{Si}, \mathrm{P}, \mathrm{S}$, and $\mathrm{Cl})$ substantially exceed these thresholds (Table 3.8); all of those mentioned yield cleavage rates below $10^{-33} \mathrm{~s}^{-1}$. If most bonds in a system have failure rates this low, then a smaller population can have higher failure rates while still meeting the $10^{-20} \mathrm{~s}^{-1}$ criterion for the mean failure rate. If this population is $1 \%$ of the total, then its barrier heights (by the above method) need only exceed $294 \mathrm{maJ}$ at $300 \mathrm{~K}$ and $344 \mathrm{maJ}$ at $350 \mathrm{~K}$. For perspective, the former condition is almost met by isolated organic peroxide linkages (bond strength $\sim 259 \mathrm{maJ}$, Table 3.8), which are usually regarded as quite reactive.

c. Assumptions and damage rates. The single-point failure assumption and the radiation-damage dominance criterion are both subject to criticism and improvement, but neither is a hypothesis. Single-point failure is the most conservative rule of calculation, and can be relaxed if a detailed model of a component demonstrates that it is more robust. Radiation-damage dominance is a design objective that can be discarded whenever alternative objectives prove superior. Both are stated in order to guide design and analysis within the context of the present work.

So long as components meet the above $10^{-20}$ failure/bond-s criterion, the uncorrelated radiation-damage lifetime model, Eq. (6.53), can with reasonable accuracy be treated as the overall component lifetime model. Systems meeting the slightly more stringent $10^{-22}$ failures/bond-s criterion can be described by Eq. (6.54) over the range of component volumes graphed in Figure 6.13.

### 6.7.2. System lifetimes

For a given level of reliability, finite damage rates and the single-point failure assumption set upper bounds to component size. Figure 6.13 indicates that components of $10^{9} \mathrm{~nm}^{3}\left(=1 \mu^{3}\right)$ have annual failure rates of several percent if they meet the radiation-damage dominance criterion. Among macroscopic systems, the mean time to failure is quite brief unless damage can be tolerated.

Where component failures cannot be excluded but systems must be reliable, standard engineering practice resorts to redundancy. Although the existence of radiation tracks violates the assumption that component failures are randomly distributed in space and introduces geometrical complications, the essential effects of redundancy can be illustrated by a random-damage model.

Assume that a system consists of $N$ sets of components, $s_{1}, s_{2}, s_{3}, \ldots, s_{N}$, with each set $s_{\mathrm{i}}$ containing $n_{\mathrm{i}}$ components of type $c_{\mathrm{i}}$, and assume that the system remains functional so long as at least one component in each set remains functional. In other words, any component can substitute for the other components within its set, but components in different sets play different roles (e.g., in manufacturing systems like that discussed in Section 14.3). If $n_{i}=1$ for each set, the system is nonredundant, and the probability that it remains functional is the product of the probabilities that each of components remains functional:

$$
\begin{equation*}
P_{\text {func }}(\text { system })=\prod_{i=1}^{N} P_{\text {func }}\left(c_{i}\right)=\prod_{i=1}^{N} \exp \left(-10^{15} D m_{i}\right) \tag{6.55}
\end{equation*}
$$

where $m_{i}$ is the mass of a component of type $c_{i}$, and the final expression is based on Eq. (6.53). With redundancy, however, the probability that the system remains operational depends on the probability that at least one member of each set $s_{i}$ remains functional:

$$
\begin{equation*}
P_{\text {func }}\left(s_{i}\right)=1-\left[1-P_{\text {func }}\left(c_{i}\right)\right]^{n_{i}} \tag{6.56}
\end{equation*}
$$

hence

$$
\begin{equation*}
P_{\text {func }}(\text { system } 2)=\prod_{i=1}^{N} P_{\text {func }}\left(s_{i}\right)=\prod_{i=1}^{N}\left\{1-\left[1-\exp \left(-10^{15} D m_{i}\right)\right]^{n_{i}}\right\} \tag{6.57}
\end{equation*}
$$

To understand how reliability depends on redundancy and component lifetimes, it is useful to consider an idealized system in which all components have the same mass $m$ and all sets have the same degree of redundancy $n$ :

$$
\begin{align*}
P_{\text {func }}(\text { system } 3) & =\left\{1-\left[1-\exp \left(-10^{15} D m_{i}\right)\right]^{n_{i}}\right\}^{N}  \tag{6.58}\\
& \approx \exp \left\{-N\left[1-\exp \left(-10^{15} D m_{i}\right)\right]^{n_{i}}\right\} \tag{6.59}
\end{align*}
$$

in which the approximation is valid so long as the probability remains low that all of the components in a given set have failed. Choosing a value of $D$ and $m$ such that $10^{15} \mathrm{Dm}=0.1$ (implying a $\sim .9$ probability that a given component is functional), a nonredundant system with $N=1000$ sets will be functional with a probability of only $\sim 10^{-44}$. If $n=5$, however, the system will be functional with probability $\sim .992$, and if $n=10$, the probability of system failure shrinks to $<10^{-7}$.

Calculations show that substantial levels of redundancy can make failure extremely improbable, even in macroscopic systems, so long as each component has a reasonably large probability of remaining functional. For example, if the components have a mass of $\sim 10^{-18} \mathrm{~kg}$ (a diameter of $\sim 100 \mathrm{~nm}$, at ordinary densities), then $10^{15} \mathrm{Dm}=0.1$ after $>100$ years of background radiation (Figure 6.13). If these components are combined to form a $1000 \mathrm{~kg}$ system containing $N=4 \times 10^{19}$ sets of $n=25$ components, Eq. (6.54) predicts a failure probability of only $\sim 10^{-6}$.

Where indefinitely prolonged system life is required, the standard engineering answer is a combination of redundancy and replacement of damaged com-
ponents. This is feasible in nanoscale systems, but at the cost of substantial increases in system complexity.

### 6.8. Conclusions

Transition state theories based on statistical mechanics can adequately describe thermally driven transition rates in most processes of nanomechanical interest, including mechanosynthesis, thermomechanical bond cleavage, and nonchemical transitions between potential wells. A simpler model suffices to set bounds on error rates in placing objects in potential wells (a concept that requires treatment of time-dependent potential energy functions). In general, thermally driven transition rates are an exponentially decreasing function of barrier heights, and thermally driven placement errors are an exponentially decreasing function of differences in well depths. Placement errors can be made rare either by increasing the spacing between alternative wells, or by increasing the stiffness of the placement mechanism. Thermomechanical damage can be made rare by choosing strong covalent structures that lack unusually low-energy pathways leading to elimination or rearrangement reactions, and by limiting applied mechanical stress (exclusion of stray reactive molecules from the environment is assumed). Impinging energy can also cause damage: photochemical reactions can be prevented by excluding light, but reactions induced by ionizing radiation are inescapable, setting practical lower bounds on damage rates and component lifetime. Later chapters assume that damage from readily controllable mechanisms is limited to levels low enough that ionizing radiation damage is dominant.

Some open problems. An open problem, the solution of which would substantially aid nanomechanical design by nonchemists, is the development of software able to check nanomechanical structures for instability (e.g., as an adjunct to a molecular mechanics package). A realistic system would include a set of criteria for identifying clearly stable structures, a set of criteria for identifying clearly unstable structures, and an ability to report which substructures in a design are either unusable or questionable. A highly conservative rule set can easily be defined, but recognizing increasingly broad classes of stable structures (without making errors of inclusion) presents increasing challenges. For example, estimating rates of cleavage of sets of strained bonds (including shear forces not considered in Section 6.4.4a) must in general reflect nonlocal elastic deformation of the structure.

A further open problem relates to photochemical stability: What structures of nanomechanical interest are compatible with what ranges of photon energies? Progress in this area may relax the constraint of photochemical shielding.

[^13]: The configuration coordinates used to describe a well are assumed to be aligned with the principal axes of the hyperellipsoids describing equipotential surfaces; motion along one of these coordinates corresponds to a normal mode.
[^14]: A process that equilibrates different states can be described as freezing when the transitions that establish equilibrium effectively cease, that is, when they become rare on the time scale under consideration. Often this occurs because the temperature falls; here it occurs because the barrier height increases. The result is a frozen distribution.
[^15]: The four-membered ring in 6.1 resembles cyclobutadiene, which is stable at room temperature if intermolecular collisions are blocked (Cram et al., 1991).
[^16]: Based on difficulties arising in silicon micromachine research, P. Barth has raised concerns regarding electrostatic stiction and repulsion caused by charging of moving parts. Micromachines have irregular surface structures with sliding interfaces subject to highenergy processes including bond breakage, wear, and tribological charge separation; these phenomena can be avoided in nanomechanical systems. Dissimilar insulating surfaces brought into contact can transfer charge by a combination of thermal activation and tunneling, but only if the energies of occupied electronic states in one object approach those of unoccupied states in the other; avoiding this can impose design constraints (an experimental study of contact electrification forces is reported in Horn and Smith, 1992).