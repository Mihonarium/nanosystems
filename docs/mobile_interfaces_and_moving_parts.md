# Mobile Interfaces and Moving Parts


### 10.1. Overview

Moving parts-gears, bearings, and so forth-typically have sliding or rolling interfaces. Mobile interfaces and strong, stiff nanostructures like those discussed in Chapter 9 can be combined to build a wide range of nanomechanical systems, including mechanical computers (Chapter 12) and molecular manufacturing systems (Chapter 14).

Stable molecular liquids show that interfaces between molecules can be both stable and mobile at ordinary temperatures. Familiar examples include saturated hydrocarbons, fluorocarbons, ${ }^{\circ}$ ethers, and ${ }^{\circ}$ amines; diamondoid structures having analogous surface moieties appear in the examples of this chapter. A more diverse range of surface moieties are stable when incorporated into diamondoid structures operating in well-ordered environments.

Two mutually inert surfaces in contact can be characterized by their potential energy of interaction. Models like those described in Section 3.5 can estimate the potential energy as a function of separation for two relatively smooth surfaces, but in gears and bearings, the potential energy function associated with sliding motions is of central importance. The two cases of greatest interest are those in which the potential energy is nearly flat along the direction of motion, permitting smooth sliding, and those in which it has large corrugations, entirely blocking sliding. Smooth interfaces can be used in bearings; corrugated interfaces can be used in gears.[^24]

The following sections explore mobile interfaces and their applications in gears, bearings, and related devices. Section 10.2 begins by characterizing properties of the spatial Fourier transforms of interatomic nonbonded potentials, which prove useful in analyzing the properties of sliding interface bearings. Section 10.3 considers the problem of sliding motion between irregular covalent objects and regular covalent surfaces, developing a Monte Carlo model that predicts the fraction of irregular structures expected to exhibit smooth sliding motion with respect to such surfaces. Section 10.4 develops the theory of symmetrical sleeve bearings, presenting results from analytical models of idealized bearings, and characterizing two specific designs using molecular mechanics methods. Section 10.5 generalizes from these results to several other systems incorporating sliding-interface bearings, including nut-and-screw systems, rods sliding in sleeves, and constant-force springs. Section 10.6 briefly describes bearings that exploit single atoms as axles. Section 10.7 moves from sliding interfaces to nonsliding interfaces, examining analytical models of gears, and using these as a basis for examining the properties of roller bearings and systems resembling chain drives. Section 10.8 examines some general issues arising in the construction of extended systems that have nearly flat potentials. Finally, Section 10.9 briefly surveys devices that use surfaces intermediate between freely sliding and nonsliding: dampers, detents, and clutches.

### 10.2. Spatial Fourier transforms of nonbonded potentials

In the design of nanomechanical systems, smooth sliding motions can be most simply achieved when one or both surfaces at an interface have a periodic or nearly periodic structure of high spatial frequency, that is, when the surface has a series of closely spaced features that repeat at regular intervals, with each feature found in essentially the same local environment. In one-dimensional sliding motion (by convention, along the $x$ axis), only periodicity along the $x$ axis is significant; the corresponding spatial frequency is $k \mathrm{rad} / \mathrm{m}$, or $f_{x}$ cycles $/ \mathrm{m}(=k / 2 \pi)$.

The variations in the potential $\mathscr{V}(x)$ associated with sliding of a component over a surface can in the standard molecular mechanics approximations be decomposed into a sum of the pairwise nonbonded potentials between the atoms in the object and those in the surface, together with terms representing variations in the internal strain energy of the object and the surface. For stiff components under small interfacial loads, the soft, nonbonded interactions dominate the variations in $\mathscr{V}(x)$, and structural relaxation causes only small deviations from straight-line motion of the interfacial atoms. Under these conditions, variations in the total potential $\mathscr{V}(x)$ are accurately approximated by a sum of the pairwise nonbonded potentials between atoms in straight-line relative motion. Figure 10.1 plots a set of such interaction potentials for pairs of $s p^{2}$ carbon atoms moving on paths with differing closest-approach distances $d$, based the MM2 exp-6 potential, Eq. (3.8).

### 10.2.1. Barrier heights and sums of sinusoids

Barrier heights $\Delta \mathcal{V}_{\text {barrier }}$ for sliding of components over periodic surfaces can be described in terms of a sum of contributions associated with integral multiples of the spatial frequency $f_{x}$. This sum can be divided into contributions each resulting from an atom in the sliding object interacting with a row of evenly spaced atoms in the periodic surface. The energy of an atom with respect to a row consists of a sum

$$
\begin{equation*}
\mathcal{V}(x)=\sum_{i=-\infty}^{\infty} \mathscr{V}_{\mathrm{vdw}}\left(\sqrt{d^{2}+\left(x+i / f_{x}\right)^{2}}\right) \tag{10.1}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-44.jpg?height=707&width=1092&top_left_y=163&top_left_x=168)

Figure 10.1. Nonbonded potentials, Eq. (3.8), as a function of $x$-axis displacement for two $s p^{2}$ carbon atoms moving in straight lines of differing closest-approach distance $d$.

where $\mathscr{V}_{\text {vdw }}(r)$ is the nonbonded energy as a function of distance for the two atom types, Eq. (3.8). Graphically, such a sum can be represented as an evenly spaced set of sample points, and the difference between two sums separated by one-half cycle can be represented by an evenly spaced set with weights alternating between +1 and -1 (Figure 10.2); in the typical cases of interest, the maximum value of this difference equals the barrier height for sliding of a single atom with respect to a single row.

Figures 10.3 and 10.4 plot amplitude spectral densities,[^25] $\left|\mathrm{H}\left(f_{x}\right)\right|$, derived from the spatial Fourier transforms of a set of interaction potentials like those in Figure 10.1. At large spatial frequencies $f_{x}$, the associated amplitudes drop steadily on a logarithmic scale as $f_{x}$ increases. Exceptions to the "typical cases of interest" in the previous paragraph can arise when $f_{x} \approx f_{x, 0}$ (see Figure 10.3), but these exceptional cases have unusually low barrier heights. The designs discussed here do not exploit this phenomenon, as it relies on a delicate cancellation rather than on robust properties of intermolecular potentials.

The sampling shown in Figure 10.2 can be described as a sequence of positive and negative delta functions. The Fourier transform for such a sequence yields the relationship

$$
\begin{equation*}
\Delta \mathscr{V}_{\text {barrier }} \propto\left|\mathrm{H}\left(f_{x}\right)-\mathrm{H}\left(3 f_{x}\right)+\mathrm{H}\left(5 f_{x}\right)-\mathrm{H}\left(7 f_{x}\right) \ldots\right| \tag{10.2}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-45.jpg?height=442&width=510&top_left_y=174&top_left_x=282)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-45.jpg?height=207&width=506&top_left_y=287&top_left_x=883)

Figure 10.2. A nonbonded potential (as in Figure 10.1) sampled at regular intervals (a), and sampled with a shift in phase (b). The difference in the sum of the sample energies as the phase shifts is the energy of a sum of samples with positive and negative weights $(a-b)$; this observation can be used to relate spatial Fourier transforms of pairwise potentials to energy barriers in sliding motion.

From the results plotted in Figures 10.3 and 10.4, it can be seen that with reasonable values of $d$ (e.g., $\geq 0.2 \mathrm{~nm}$ ) and with a moderately high spatial frequency (e.g., $f_{x} \geq 3.0$ cycles $/ \mathrm{nm}$ ), the first term in Eq. (10.2) dominates the rest by multiple orders of magnitude because contributions from spatial frequencies $\geq 9.0$ cycles $/ \mathrm{nm}$ are quite small. For a diamond (111) surface in the high- $f_{x}$ direction, $f_{x} \approx 4.0$ cycles $/ \mathrm{nm}$; for graphite, $f_{x} \approx 4.1$ cycles $/ \mathrm{nm}$. As a consequence, the potential of a component sliding over such a surface can be accurately approximated as a sum of sinusoidal contributions from interactions between the atoms of the component and each of the component rows of the surface, all of spatial frequency $f_{x}$, but of varying amplitudes and phases.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-45.jpg?height=690&width=1085&top_left_y=1387&top_left_x=285)

Figure 10.3. Amplitude spectral densities derived from spatial Fourier transforms of nonbonded $\mathrm{C} \mid \mathrm{C}\left(s p^{2}\right)$ potentials like those in Figure 10.1, for a range of closestapproach distances $d$. For relatively large values of $d$, the Fourier transform changes sign, resulting in a zero at some spatial frequency $f_{x, 0}$.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-46.jpg?height=699&width=1085&top_left_y=174&top_left_x=191)

Figure 10.4. Amplitude spectral densities as in Figure 10.3, but for nonbonded $\mathrm{H} \mid \mathrm{H}$ potentials. Note that these graphs would be identical (within a constant energy factor) if all distances were measured in units scaled to the equilibrium nonbonded separation.

### 10.3. Sliding of irregular objects over regular surfaces

Section 9.5 estimates the enormous number of possible nanometer-scale diamondoid structures, and observes that constraints on surface structure can drastically reduce the size of this set. In particular, requiring that surface structures be regular imposes a requirement that interior structures be regular (to a depth dependent on the tolerance for residual irregularities); this reduces the set of possible structures to a minute fraction of that available without this constraint. Regular structures can make excellent bearings (as shown in Section 10.4), and this is their chief value in the present context. This section examines the bearing performance that can be achieved in the far larger set of irregular structures.

### 10.3.1. Motivation: a random-walk model of barrier heights

Consider an atom sliding over a regular surface with spatial frequency $f_{x}$ at a height $h$ (note that $h \leq$ the minimum value of $d$ with respect to any of the rows of the surface). As shown in Section 10.2, the potential energy of such an atom can be represented as a sum of sinusoids, each characterized by some amplitude $\Delta \mathscr{V} / 2$ and phase $\phi$. For a surface of high spatial frequency, and for values of $h$ corresponding to modest loads, the sum is dominated by a single sinusoid with a spatial frequency $f_{x}$.

Consider an irregular object sliding over a surface with $N$ such atoms in contact. In the approximation just described, the interaction energy of each is dominated by a sinusoid of the same $f_{x}$, but with differing values of $\Delta \mathcal{V}$ and $\phi$. In the vector representation (Figure 10.5), the summing of these sinusoids can be visualized as a walk over a plane. For a set of irregular objects with randomly distributed values of $\phi$ and bounded values of $\Delta \mathcal{V}$, the resulting random walk has familiar properties: in the limit of many steps, the probability density for the end

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-47.jpg?height=304&width=468&top_left_y=193&top_left_x=265)

Figure 10.5. Sinusoidal energy terms (defined by magnitude and phase) represented as vectors, illustrating the magnitude and phase of the sum as the result of a random walk over the plane.

points is Gaussian, and the mean value of the radius is

$$
\begin{equation*}
\overline{\Delta \mathscr{V}}_{\text {sum }}=\overline{\Delta \mathscr{V}}_{\text {barrier }} \propto \sqrt{N} \tag{10.3}
\end{equation*}
$$

hence the area over which the end points are scattered varies as $N$. For a set of irregular structures in which there are $n_{\text {opt }}$ choices for the properties of the $N$ atoms, the number of possible structures increases as $n_{\mathrm{opt}}^{N}$, and thus the density of endpoints in the plane (Figure 10.5) near the origin varies as

$$
\begin{equation*}
\rho_{\text {area }} \propto n_{\mathrm{opt}}^{N} / N \tag{10.4}
\end{equation*}
$$

and the mean distance from the origin to the closest point (i.e., the value of the smallest barrier for any member of the family of structures) is

$$
\begin{equation*}
\overline{\Delta \mathscr{V}}_{\text {barrier }} \propto \sqrt{N / n_{\mathrm{opt}}^{N}} \tag{10.5}
\end{equation*}
$$

Thus, although the expected barrier height for any given irregular structure increases with increasing $N$, the minimum expected barrier height for a family of structures decreases.

### 10.3.2. A Monte Carlo analysis of barrier heights

The scaling principles discussed in Section 10.3.1 do not translate directly into an accurate statistical model; such a model would require a treatment taking account of the nature of the available choices of interacting atoms and their interactions with the regular surface, which in turn affects the value(s) of $n_{\mathrm{opt}}$ and the distribution of values of $\Delta \mathcal{V}$. Further, as values of $\Delta \mathcal{V}_{\text {barrier }}$ become small, sinusoidal terms of higher spatial frequency become important, and the end points must be treated as being scattered in a space of higher dimension. The complexity of these interacting physical effects and design choices suggests the use of a Monte Carlo model to estimate the distribution of $\Delta \mathcal{V}_{\text {barrier }}$ for model systems of interest.

a. Approximations and assumptions. To reduce the computational burden while retaining the essential physical and statistical features of the problem, a set of approximations was adopted:

- Use of the MM2 exp-6 potential to represent nonbonded interaction energies. The exp-6 potential is realistic over a wide range of separations (Section 3.3.3b), and the neglected electrostatic terms (Section 3.3.2d) would have little effect on $\Delta \mathcal{V}_{\text {barrier }}$.
- Use of a straight-line translation model, which effectively treats structures as infinitely stiff. For $x$-axis sliding, neglect of $y$-and $z$-axis relaxation is
conservative in this context, while neglect of $x$-axis relaxation is the reverse; at modest loads, the neglected effects are minor.
- Lack of rotational relaxation of the sliding object. An irregular object pressed against a surface tends to rotate to distribute load over several contact points; neglect of this artificially increases the disparity in contact loads, which tends to increase barrier heights.

With these approximations, the interaction energy of an object is just the sum of the energies of a set of atoms, each interacting with the surface independently. Atomic interaction energies can be precomputed and then combined to represent different structures.

Families of structures can be modeled using a further set of assumptions and approximations:

- Each family is characterized by a framework structure having a set of $N s p^{3}$ surface sites within a certain range of distances $\left(h_{\min }\right.$ to $h_{\max }$ ) from the regular surface.
- To generate the members of a family, each surface site can either be occupied by an $\mathrm{N}$ atom with a lone pair, or by a $\mathrm{C}$ atom bonded to $\mathrm{H}, \mathrm{F}$, or $\mathrm{Cl}$, or can be deleted (locally modifying the framework); each site thus has 5 states, giving each structural family $5^{N}$ possible members.
- To model irregular structures, sites are assumed to be randomly distributed with respect to the unit cells of the regular surface, and bond orientations are assumed to be randomly distributed within a cone directed toward the regular surface with an angle of $40^{\circ}$ (a wider angle is expected to be more favorable).
- Site positions are treated as fixed, with lone pair, $\mathrm{H}, \mathrm{F}$, and $\mathrm{Cl}$ positions determined by the site coordinates and bond orientation, together with standard bond lengths (Section 3.3.2a).
- To ensure that each structure examined is in firm contact with the regular surface, site-states are characterized by their $z$-axis stiffnesses relative to the regular surface. Members of a structural family containing a site with a stiffness less than some threshold $k_{\mathrm{s} \text {,thresh }}$ are discarded, as are those with less than three nondeleted sites. These exclusions ensure that the $z$-axis stiffness for each structure is $\geq 3 k_{\mathrm{s} \text {, thresh }}$, and usually reduce the number of retained members of a structural family to far fewer than $5^{N}$.

b. Computational procedure. Based on the preceding assumptions, the computation proceeds by generating a set of sites characterized by locations and bond orientations ( 200 sites were used), constructing a set of site states for each site, filtering this set for stiffness $\geq k_{\mathrm{s}, \text { thresh }}$, and computing the energy of each remaining site state at a series of displacements (16) spanning one cycle of motion over the regular surface. A structural family is defined by randomly choosing $N$ sites from the final set, and a list of the acceptable members of that family is generated by forming all possible combinations consisting of one state from each site and discarding those with more than $N-3$ deletion states. The energy of each structure as a function of displacement is computed by summing the corresponding precomputed values for each of its constituent site states, and the barrier height for sliding motion of the structure is taken as the difference between the maximum and minimum energies in the resulting sum. Finally,

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-49.jpg?height=461&width=432&top_left_y=223&top_left_x=652)

Figure 10.6. View across a nitrogen-terminated diamond (111) surface with lone pairs illustrated, indicating the direction of sliding assumed in the calculations summarized in Figures 10.7 and 10.8 (this direction is taken as the $x$ axis).

$\Delta \mathcal{V}_{\text {barrier }}$ for the structural family is taken as the minimum of the energy differences found for any member of that family.

c. Results. The results of a set of calculations based on the preceding model for sliding motion of irregular structures over a strip of nitrogen-substituted diamond (111) surface (as illustrated in Figure 10.6) are summarized in Figure 10.7, taking the initial sampling bounds for site generation as $h_{\min }=0.2 \mathrm{~nm}$ and $h_{\max }=0.5 \mathrm{~nm}$. The statistical distribution of values of $\Delta \mathscr{V}_{\text {barrier }}$ is presented as a

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-49.jpg?height=692&width=1088&top_left_y=1277&top_left_x=281)

Figure 10.7. Cumulative distributions resulting from a Monte Carlo study of barrier heights encountered by irregular structures sliding over a regular surface, based on the model described in Section 10.3.2. Each curve is the result of 1000 trials, where each trial selects the best member of a particular family of structures (as described in the text); note that sampling statistics result in substantial scatter, particularly toward the left tail of the distributions. The surface modeled is nitrogen-substituted diamond (111), Figure 10.6.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-50.jpg?height=709&width=1090&top_left_y=174&top_left_x=186)

Figure 10.8. Cumulative distributions like those in Figure 10.7, but with minimum values of $z$-axis stiffness 10 times higher. The author thanks L. Zubkoff for his help with the computations used to acquire the data plotted in Figures 10.7 and 10.8.

series of cumulative distributions for samples of randomly generated structural families with $N=3,4,5,6,7$, and 8 . As can be seen, for $N \geq 5$, about $10 \%$ of randomly selected structural families have a member yielding $\Delta \mathscr{V}_{\text {barrier }} \leq 1 \mathrm{maJ}$ $\left(<0.25 k T_{300}\right)$. Barriers this low will be surmounted on most encounters, and hence will for most purposes fail to act as barriers: the result is a bearing surface without static friction. Further, if one assumes that the potential is characterized by a sinusoid with the period of the lattice $(\sim 0.28 \mathrm{~nm})$, then the peak negative stiffness during sliding along the $x$ axis is $\sim-0.25 \mathrm{~N} / \mathrm{m}$; this low magnitude enables a bearing interface to be coupled to relatively distant structures with sufficient stiffness that the net stiffness is positive (Section 10.8), enabling smooth motion even at low temperatures.

Figure 10.8 presents the results of a similar calculation with $h_{\min }=0.19 \mathrm{~nm}$, $h_{\max }=0.49$, and $k_{\mathrm{s}, \text { thresh }}=10 \mathrm{~N} / \mathrm{m}$. Values of $\Delta \mathcal{V}_{\text {barrier }}$ are higher owing to the combined effects of higher energies and a shift toward higher spatial frequencies in the interatomic potentials (Figures 10.3 and 10.4).

### 10.3.3. Implications for constraints on structure

Assume that a nanomechanical component has been designed to meet some set of functional constraints along one surface (the functionally constrained surface), and that some other surface of the component (the sliding surface) must slide smoothly over a regular surface. One would like the design of the sliding surface to place few additional constraints on the structure of the functionally constrained surface. One can define a set of compatible-framework structures that consists of diamondoid frameworks that satisfy the constraints of the functionally constrained surface and extend for some indefinite distance toward (and beyond) the desired location of the sliding surface. If the two surfaces are separated by a distance on the order of $1 \mathrm{~nm}$, then the set of compatible-frame-
work structures (now considering only variations in the region that falls short of the desired sliding surface) contains a large combinatorial number of elements, typically $>10^{10}$. Candidate families of sliding surface structures can be generated (in a design sense, not a fabrication sense) by truncating these compatibleframework structures so as to generate a set of $s p^{3}$ sites falling between $h_{\min }$ and $h_{\max }$; members of each family can then be generated by modifying these sites in the manner suggested by the model of Section 10.3.2a.[^26]

The results of the model described in Section 10.3.2 suggest that (for modest loads applied to regular surfaces of high spatial frequency) a substantial fraction of these truncated compatible-framework structures permits low values of $\Delta \mathcal{V}_{\text {barrier }}$, provided that the number of available sites between $h_{\min }=0.2 \mathrm{~nm}$ and $h_{\max }=0.5 \mathrm{~nm}$ is $>5$. If all atoms in the slab could serve as $s p^{3}$ sites, then for structures with an atomic number density $n_{\mathrm{v}}=100 \mathrm{~nm}^{-3}$, a cross-sectional bearing area $S_{\text {bear }}=0.25 \mathrm{~nm}^{2}$ would often suffice. If the areal density of available sites equaled that of atoms in a diamond (111) surface, then a somewhat larger area, $S_{\text {bear }}=0.28 \mathrm{~nm}^{2}$, would be necessary. For design work, values of $S_{\text {bear }}$ $\geq 0.5 \mathrm{~nm}^{2}$ should prove ample. Larger areas (or the selection of structures from a set of many compatible frameworks) can permit both greater $z$-axis stiffness and lower $\Delta \mathcal{V}_{\text {barrier }}$.

In summary, it is safe to assume that any component with a surface in contact with a strip of regular, high-spatial-frequency structure can be made to slide smoothly with respect to that strip, provided that loads are modest, that the contact surface is of a reasonable shape (with a length of at least $2 \pi / k$ in the $x$ direction) with $S_{\text {bear }} \geq 0.5 \mathrm{~nm}^{2}$, and that the contact surface is only loosely constrained in structure. The latter condition is usually satisfied a few atomic layers from a tightly constrained surface. This conclusion generalizes to irregular structures that slide along regular grooves and ridges, and to irregular structures sliding along regular curved surfaces in rotary bearings.

### 10.3.4. Energy dissipation models

a. Phonon scattering. Interaction between a small sliding contact and ambient phonons can be modeled as scattering from a moving harmonic oscillator (Section 7.3.4). With surface interaction stiffnesses of several $\mathrm{N} / \mathrm{m}$ per atom, a total stiffness on the order of $30 \mathrm{~N} / \mathrm{m}$ will not be atypical. This corresponds to the example in Section 7.3.4, which yielded an estimated energy dissipation of $\sim 3 \times 10^{-16} \mathrm{~W}$ at a sliding speed of $1 \mathrm{~m} / \mathrm{s}$, and $\sim 3 \times 10^{-20} \mathrm{~W}$ at $1 \mathrm{~cm} / \mathrm{s}$.

b. Acoustic radiation. A small sliding contact exerts a time-varying force with an amplitude roughly proportional to the amplitude of the energy variation $\left(=\Delta \mathscr{V}_{\text {barrier }} / 2\right)$. From Eq. (3.19), the approximate force amplitude is

$$
\begin{equation*}
F_{\max } \approx 1.7 \times 10^{10} \Delta \mathcal{V}_{\text {barrier }} \tag{10.6}
\end{equation*}
$$

( $F_{\max }$ in $\mathrm{N}, \Delta \mathscr{V}_{\text {barrier }}$ in $\mathrm{J}$ ). Assuming sinusoidal variations in force, Eqs. (10.6) and (7.8) yield

$$
\begin{equation*}
P_{\mathrm{rad}} \approx 2.9 \times 10^{20} \Delta V_{\text {barrier }}^{2} v^{2} \boldsymbol{k}^{2} \sqrt{\rho} \frac{1}{8 \pi M^{3 / 2}} \tag{10.7}
\end{equation*}
$$

Assuming $\Delta \mathcal{V}_{\text {barrier }}=1 \mathrm{maJ}$, a surface with a stiffness and density like those of diamond, and $k \approx 2.2 \times 10^{10} \mathrm{~m}^{-1}$, Eq. (10.7) predicts a radiated acoustic power of $\sim 3 \times 10^{-19} \mathrm{~W}$ at $1 \mathrm{~m} / \mathrm{s}$, and $\sim 3 \times 10^{-23} \mathrm{~W}$ at $1 \mathrm{~cm} / \mathrm{s}$. These losses are small compared to those resulting from phonon scattering; in geometries in which the energy variations reflect variations in pressure (for example, sliding in a tube or a slot with balanced forces on either side), then a relationship like Eq. (7.21) applies and losses are still lower.

c. Thermoelastic damping. Eq. (7.50) can be applied to estimate losses resulting from thermoelastic damping. Using diamond material parameters for the surface (save for $K_{\mathrm{T}}$, which is taken as $10 \mathrm{~W} / \mathrm{m} \cdot \mathrm{K}$ ), and treating the alternating forces in the system as being applied to square nanometer areas and cubic nanometer volumes, the estimated energy loss per cycle (at a sliding speed of $1 \mathrm{~m} / \mathrm{s}$ ) is $\sim 3 \times 10^{-30} \mathrm{~J}$, or $\sim 1 \times 10^{-20} \mathrm{~W}$. In addition, the total (nonalternating) force varies with time from the perspective of a site on the surface. Assuming that the force is adequate to ensure a nonbonded stiffness of $\sim 30 \mathrm{~N} / \mathrm{m}(\sim 1 \mathrm{nN})$ and that the length scale $\ell$ of the loaded region is $\sim 1 \mathrm{~nm}$, the pressure is $\sim 1 \mathrm{GPa}$; at a sliding speed $v=1 \mathrm{~m} / \mathrm{s}$ the estimated energy loss per cycle $\left(t_{\text {cycle }} \approx \ell / v\right)$ is $\sim 10^{-27} \mathrm{~J}$, or $\sim 10^{-18} \mathrm{~W}$. Thermoelastic-damping losses thus are small compared to phonon-scattering losses.

### 10.3.5. Static friction

Where $\Delta \mathscr{V}_{\text {barrier }} \ll k T$, static friction is effectively zero. At low temperatures, however, and neglecting tunneling, the static friction of a sinusoidal potential can be identified with the maximum value of $\partial \mathcal{V} / \partial x$, where $x$ measures the displacement of the surface. Where the sinusoid has a period $d_{\mathrm{a}}$ (as is the case whenever amplitudes are significant),

$$
\begin{equation*}
F_{\text {frict }}=\left(\frac{\partial \mathscr{V}}{\partial x}\right)_{\max }=4 \pi \frac{\Delta \mathscr{V}_{\text {barrier }}}{d_{\mathrm{a}}} \tag{10.8}
\end{equation*}
$$

For a typical value of $d_{\mathrm{a}}(\sim 0.25 \mathrm{~nm}), F_{\text {frict }} / \Delta \mathcal{V}_{\text {barrier }} \approx 0.05 \mathrm{nN} / \mathrm{maJ}$.

### 10.3.6. Coupled sites

An extended object (such as a rod) can contact a periodic surface at regions spread over a considerable distance. For smooth motion, the positive stiffness between different regions within the extended object must exceed in magnitude
the negative stiffnesses resulting from the interaction of these regions with the periodic surface (i.e., as they cross energy barriers). This condition must hold on all length scales.

Consider a contact region for which families of compatible structures yield $N$ vectors (in the space considered in Section 10.3.1) falling within a disk of radius $\Delta \mathscr{V}_{1}$. Within the approximations used here, the distribution of these vectors is (for small values of $\Delta \mathscr{V}_{1}$ ) essentially random. Now consider a second such contact region, with an independent set of families of structures. Given that the density of vectors is approximately constant within a region of radius $1.5 \Delta \mathscr{V}_{1}$, each vector in the first region will have (on the average) $N / 4$ vectors in the second region that are within a radius $\Delta \mathscr{V}_{1} / 2$ of $-\mathcal{V}$. Choosing a pair of structures for which this holds would, in the rigid coupling approximation, yield a system with $\Delta \mathcal{V}_{\text {barrier }} \leq \Delta \mathscr{V}_{1} / 2$; the negative stiffness of the interaction between the two sites is bounded by

$$
\begin{equation*}
\left|k_{\mathrm{s}}\right| \leq 3 \Delta \mathscr{V}_{1}\left(\pi / d_{\mathrm{a}}\right)^{2} \tag{10.9}
\end{equation*}
$$

For $d_{\mathrm{a}}=0.25 \mathrm{~nm}$ and $\Delta \mathscr{V}_{1}=1 \mathrm{maJ},\left|k_{\mathrm{s}}\right| \leq 0.5 \mathrm{~N} / \mathrm{m}$. So long as the stiffness coupling the two regions is large compared to this small value, the two regions can be treated as rigidly coupled for purposes of the present analysis. For comparison, the stretching stiffness of a diamond rod with a length of $10 \mathrm{~nm}$ and a structural cross sectional area of $1 \mathrm{~nm}^{2}$ is $\sim 100 \mathrm{~N} / \mathrm{m}$; relatively long, slim, lowmodulus rods will accordingly have stiffnesses $>0.5 \mathrm{~N} / \mathrm{m}$.

The mean number of candidate structures with this property is $N^{2} / 4$. If we require

$$
\begin{equation*}
N^{2} / 4 \geq N \tag{10.10}
\end{equation*}
$$

then the same reasoning can be applied between pairs of regions of the sort just described, with $\Delta \mathscr{V}_{2}=\Delta \mathscr{V}_{1} / 2$ playing the role of $\Delta \mathscr{V}_{1}$. By induction, sets of regions can be constructed on all length scales, with $\Delta \mathcal{V}_{\text {barrier }}$ varying inversely with size. Note that, in a rod, stiffness varies as $\ell^{-1}$, but for a system with these scaling properties, the magnitude of the negative stiffness between regions likewise varies as $\ell^{-1}$. A threshold value for this argument to proceed (neglecting statistical considerations) is $N \geq 4$; larger values ensure reliability in the face of statistical fluctuations, and can ensure that the magnitude of the negative stiffness between regions varies as $\ell^{-}, \mathrm{b}>1$.

### 10.4. Symmetrical sleeve bearings

The results of the previous section indicate that irregular sleeve bearings with small energy barriers are feasible provided (1) that either the shaft or the sleeve has a rotational symmetry such that a rotation corresponding to a small tangential displacement is a symmetry operation, and (2) that the other component is sufficiently weakly constrained in its structure that a design can be selected from a large set of possible structures. Sleeve bearings, however, lend themselves to analysis and design that exploit symmetry in both components. This section extends a preliminary study (Drexler, 1987b) that indicated the promise of this

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-54.jpg?height=622&width=702&top_left_y=198&top_left_x=455)

Figure 10.9. Coplanar ring model for a symmetrical sleeve bearing.

class of structures. The resulting analyses can in several instances be extended directly to sliding-interface bearings with noncylindrical geometries.

### 10.4.1. Models of symmetrical sleeve bearings

For calculations involving bearing stiffness, interfacial stiffness, and dynamic friction, a sleeve bearing can often be approximated as a cylindrical interface with a certain stiffness per unit area $k_{\mathrm{a}}$ for displacements perpendicular to the surface, and a distinct stiffness per unit area $k_{\text {a,para }}$ (which can be low) for displacements of the surface parallel to the axis of the bearing.

Where static friction is concerned, sleeve bearing models must take account of atomic detail. Both the outer surface of a shaft and the inner surface of a sleeve can be decomposed into rings of atoms, each having the rotational symmetry of the corresponding component. In the no-relaxation approximation, the potential energy of the system as a function of the angular displacement of the shaft with respect to the cylinder can be treated as a sum of the pairwise interaction of each inner ring with each outer ring. These pairwise potentials are well approximated by sinusoids of a single frequency, which will in the worst case add in phase, and in the best case will substantially cancel. A single ringring interaction thus captures the essential characteristics of a shaft-sleeve interaction, save for the omission of (potentially favorable) cancellations. For concreteness, coplanar rings are used as a model in the following section, with parameters illustrated in Figure 10.9.

### 10.4.2. Spatial frequencies and symmetry operations

Consider an inner ring with $n$-fold rotational symmetry and an outer ring of $m$ fold symmetry. If $n=m$, then the inner ring must be displaced by an angle $\theta_{\text {sym }}=2 \pi / n$ to restore the initial geometry and potential energy, and the spatial frequency corresponding to this symmetry operation is approximately that of
the interatomic spacing in the inner ring, $d_{\mathrm{a}}\left(r_{\text {inner }}=d_{\mathrm{a}} n / 2 \pi\right)$. In a better approximation, it can be taken as the interatomic spacing of the inner ring projected to the mean radius

$$
\begin{equation*}
r_{\text {eff }}=\frac{r_{\text {inner }}+r_{\text {outer }}}{2}=r_{\text {inner }}+\frac{s_{\text {gap }}}{2} \tag{10.11}
\end{equation*}
$$

yielding an effective spatial frequency for rotational displacements of the inner ring

$$
\begin{equation*}
f_{\theta}=\frac{1}{r_{\text {eff }} \theta_{\text {sym }}}=\left[d_{\mathrm{a}}\left(1+\frac{s_{\text {gap }}}{2 r_{\text {inner }}}\right)\right]^{-1}, n=m \tag{10.12}
\end{equation*}
$$

When $n \neq m$, a smaller relative displacement can yield a geometry that is identical to one resulting from a combined rotation of the two rings. Since a combined rotation leaves the energy unchanged, this smaller rotation is a symmetry operation for the potential energy function (note that this still holds in the presence of relaxation). Numerical experiments indicate that the required angle is related to the least common multiple of $n$ and $m$,

$$
\begin{equation*}
\theta_{\text {sym }}=2 \pi / \operatorname{lcm}(n, m) \tag{10.13}
\end{equation*}
$$

yielding an effective spatial frequency

$$
\begin{equation*}
f_{\theta}=\left[\frac{n d_{\mathrm{a}}}{\operatorname{lcm}(n, m)}\left(1+\frac{s_{\text {gap }}}{2 r_{\text {inner }}}\right)\right]^{-1} \tag{10.14}
\end{equation*}
$$

Merkle (1992b) has constructed a mathematical proof of Eq. (10.13) based on results in number theory.

### 10.4.3. Properties of unloaded bearings

Figure 10.10 presents a logarithmic plot of calculated barrier heights for coplanar-ring bearing models for $1 \leq n, m \leq 15$ in the concentric (unloaded) case. Figure 10.11 shows the closely corresponding pattern of spatial frequencies calculated from a relationship based on Eq. (10.14); this correspondence results from the smooth fall-off of amplitude spectral densities $\left|\mathrm{H}\left(f_{x}\right)\right|$ with increasing $f_{x}$ shown in Section 10.2; calculations using curved trajectories and $f_{\theta}$ would differ little. Figure 10.12 shows the effect of variations in $s_{\text {gap }}$ for two examples with fixed $n$ and $m$. (Note that $H$ interactions, small values of $s_{\text {gap }}$, and relatively large values of $d_{\mathrm{a}}$ have been used in these calculations because each choice is significantly adverse; larger atoms, larger gaps,[^27] and smaller interatomic spacings all are feasible and reduce $\Delta \mathcal{V}_{\text {barrier }}$ )

Unloaded bearings for which $\operatorname{lcm}(n, m) \gg n$ and $d_{\mathrm{a}}$ is reasonably small usually have minute values of $\Delta^{\mathcal{V}} \mathcal{V}_{\text {barrier }}$; the best values of $n$ and $m$ are relatively prime. Small loads, however, destroy the symmetries upon which this result depends.

Anisotropies in the potential for displacements perpendicular to the axis (ideally characterized by a single stiffness $k_{\mathrm{s}}$ ) give an indication of how rapidly

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-56.jpg?height=700&width=1107&top_left_y=159&top_left_x=170)

Figure 10.10. Barrier heights for rotation in the coplanar-ring model, based on the MM2 exp-6 potential, Eq. (3.8), for the $\mathrm{H} \mid \mathrm{H}$ interaction, using parameters from Table 3.1. All rings were constructed with $d_{\mathrm{a}}=0.3 \mathrm{~nm}$ and $s_{\text {gap }}=0.2 \mathrm{~nm}$. (In the shaded region of this and similar graphs, barriers are negligible and roundoff errors dominate the calculation.)

barrier heights increase with load. Where $k_{\mathrm{s}}$ is nearly isotropic, small loads perpendicular to the axis store nearly equal energies, independent of the angle of rotation; where $k_{\mathrm{s}}$ varies greatly, so will differences in stored energy. Where $n-2 \leq m \leq n+2$, problems of commensurability and anisotropic stiffness tend to be severe. For relatively isotropic ring systems with the parameters used in Figure $10.10, k_{\mathrm{s}} \approx 10 \mathrm{n} / \mathrm{m}$. Sleeves with multiple rings have correspondingly greater stiffnesses.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-56.jpg?height=697&width=1124&top_left_y=1465&top_left_x=169)

Figure 10.11. Spatial frequencies (in units of $1 / d_{\mathrm{a}}$ ) for ring systems of the sort shown in Figure 10.9.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-57.jpg?height=680&width=1090&top_left_y=191&top_left_x=282)

Figure 10.12. Barrier heights as in Figure 10.10, for sleeve bearings with $\boldsymbol{n}=9$ and 19, $m=1$ to 30 , and values of $s_{\text {gap }}$ varying from 0.18 to $0.24 \mathrm{~nm}$. Lines for $n=9$ are solid, for $n=19$, dashed.

### 10.4.4. Properties of loaded bearings

The effects of load perpendicular to the bearing axis can be modeled by displacing the center of the inner ring by a distance $\Delta x$ perpendicular to its axis and examining the potential as a function of angular displacement of the inner ring about its new, offset axis. Figures 10.13 and 10.14 show the results of such an investigation for a series of ring systems with $n=9$ and 19 respectively. As can

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-57.jpg?height=678&width=1102&top_left_y=1441&top_left_x=286)

Figure 10.13. Barrier heights as in Figure 10.10, for sleeve bearings with $n=9, s_{\text {gap }}=$ $0.2 \mathrm{~nm}$, and varying values of transverse offset.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-58.jpg?height=687&width=1110&top_left_y=187&top_left_x=188)

Figure 10.14. Barrier heights as in Figure 10.13, for sleeve bearings with $n=19$.

be seen, even small displacements destroy the delicate cancellations required for extremely low $\Delta \mathcal{V}_{\text {barrier }}$, but for suitably chosen systems with $n$ and $m \geq 25$, values of $\Delta \mathcal{V}_{\text {barrier }}$ can be negligible compared to $k T_{300}$, even at substantial displacements. This continues to hold for bearings having multiple interacting rings, so long as their number is modest or (as can often be arranged) they contribute sinusoidal potentials that add out of phase and approximately cancel.

For $n=9, m=14$, and the parameters of Figure 10.10, a displacement of $\Delta x=$ $0.01 \mathrm{~nm}$ corresponds to a mean restoring force of $\sim 0.96 \mathrm{nN}$, and an energy barrier of $\sim 1 \mathrm{maJ}$. The restoring force, however, fluctuates by $\sim 0.1 \mathrm{nN}$, and since $k_{\mathrm{s}}$ is $\sim 100$, the associated fluctuations in stored energy from this source $\sim\left(\Delta F^{2} / 2 k_{\mathrm{s}}\right)$ would be $\sim 0.05 \mathrm{maJ}$ for shafts subject to no other source of stiffness. For $n=19$, $m=27$, the corresponding force and stiffness are $\sim 2 \mathrm{nN}, 210 \mathrm{~N} / \mathrm{m}$, with fluctuations in force $<0.0001 \mathrm{nN}$ and fluctuations in stored energy from this source $\sim 10^{-29} \mathrm{~J}$. These quantities have been neglected in the calculations described above.

Load along the axis can be supported by interlocking circumferential corrugations, and do not disrupt the rotational symmetry of the bearing. Effects of load on sliding-interface drag are considered in Section 10.4.6.

### 10.4.5. Bearing stiffness in the transverse-continuum approximation

Section 3.5.2 develops a model of surfaces that averages overlap repulsion and van der Waals attraction over displacements transverse to the interface. This model can be used to estimate the energy, force, and stiffness per unit area as a function of separation for a pair of nonpolar, nonreactive, diamondoid surfaces (so long as those surfaces are smooth, regular, and out of register with one another), and provides a good approximation for a broad class of sleeve bearings.

A simple sleeve bearing can be characterized by a cylindrical interface of radius $r_{\text {eff }}$, length $\ell$, and interfacial stiffness per unit area $k_{\mathrm{a}}$. As indicated by Figure $3.12, k_{\mathrm{a}}$ can range from large positive values to moderate negative values, depending on the separation $s_{\text {gap }}$ (these models assume $r_{\text {eff }} \gg s_{\text {gap }}$ ). Where $k_{\mathrm{a}} \approx$ 0 , the tensile stress across the interface can be $\sim 1 \mathrm{GPa}$, but this is only a few percent of the tensile strength of diamond.

So long as $k_{\mathrm{a}}>0$, an unloaded shaft remains centered in the sleeve; small displacements perpendicular to the bearing axis are characterized by a positive stiffness $k_{\mathrm{s}, \text { bear }}$ (larger displacements result in larger stiffnesses, owing to the nonlinearity of overlap repulsions). The contribution of a patch of interface to $k_{\mathrm{s}, \text { bear }}$ varies with the angle $\theta$ between the normal and the direction of displacement, yielding an expression for $k_{\mathrm{s}, \text { bear }}$ in terms of the interfacial area and $k_{\mathrm{a}}$ :

$$
\begin{equation*}
k_{\mathrm{s}, \text { bear }}=\int_{0}^{2 \pi} k_{\mathrm{a}} \ell r_{\mathrm{eff}} \sin ^{2}(\theta) d \theta=\pi k_{\mathrm{a}} \ell r_{\mathrm{eff}} \tag{10.15}
\end{equation*}
$$

### 10.4.6. Mechanisms of energy dissipation

Energy dissipation in sleeve bearings has several sources. These include acoustic radiation (Section 7.2), shear-reflection drag (Section 7.3.6), band-stiffness scattering (Section 7.3.5c), band-flutter scattering (Section 7.3.5d), and thermoelastic damping (Section 7.4.1). Aside from acoustic radiation, all of the following models estimate dissipation at the cylindrical interface between the shaft and the sleeve using relationships developed for the limiting case of a flat interface between indefinitely extended solids. Sample calculations are presented for bearings of large stiffness $(1000 \mathrm{~N} / \mathrm{m})$ and moderate size $\left(r_{\text {eff }}=\ell=2 \mathrm{~nm}\right)$.

a. Acoustic radiation. For unloaded symmetrical sleeve bearings of high spatial frequency, oscillating forces are zero and oscillating torques and pressures are negligible. Significant radiation can be expected only from loaded bearings, where oscillating torques are on the order of $\pi \Delta \mathcal{V}_{\text {barrier }} r_{\text {eff }} / d_{\mathrm{a}} \mathrm{N} \cdot \mathrm{m}$, and the radiated torsional acoustic power, Eq. (7.15), is accordingly on the order of

$$
\begin{align*}
P_{\text {rad }} & \approx\left(\frac{\pi \Delta \mathcal{V}_{\text {barrier }} r_{\text {eff }}}{d_{\mathrm{a}}}\right)^{2}\left(\frac{2 \pi v_{\text {inter }}}{d_{\mathrm{a}}}\right)^{4} \frac{\rho^{3 / 2}}{48 \pi G^{5 / 2}}  \tag{10.16}\\
& \approx\left(\Delta \mathcal{V}_{\text {barrier }} r_{\text {eff }}\right)^{2} v_{\text {inter }}^{4} \frac{102 \rho^{3 / 2}}{d_{\mathrm{a}}^{6} G^{5 / 2}}
\end{align*}
$$

With diamondlike material properties, $\Delta \mathcal{V}_{\text {barrier }}=1 \mathrm{maJ}, r_{\text {eff }}=1 \mathrm{~nm}$, the interfacial sliding speed $v_{\text {inter }}=1 \mathrm{~m} / \mathrm{s}$, and $d_{\mathrm{a}}=0.25 \mathrm{~nm}$, the power resulting from torsional acoustic radiation $P_{\mathrm{rad}} \approx 10^{-25} \mathrm{~W}$.

Oscillating forces in loaded bearings depend on the nature of the load, the frequency of the oscillation, and the mass of the rotor. From Eq. (7.8),

$$
\begin{equation*}
P_{\mathrm{rad}}=F_{\max }^{2}\left(\frac{2 \pi v_{\text {inter }}}{d_{\mathrm{a}}}\right)^{2} \sqrt{\rho} \frac{1}{8 \pi M^{3 / 2}} \tag{10.17}
\end{equation*}
$$

In typical instances, $F_{\max } \ll 0.1 \mathrm{nN}$, and hence with the previous assumptions $P_{\text {rad }} \ll 10^{-17} \mathrm{~W}$ at $v_{\text {inter }}=1 \mathrm{~m} / \mathrm{s}$; for the example with $n=19, m=27$ (Section

10.4.4) $F_{\max }<0.0001 \mathrm{nN}$, and $P_{\mathrm{rad}} \approx 10^{-23} \mathrm{~W}$. With good designs, losses from acoustic radiation decrease as bearing size increases, since $n$ and $m$ can then have large and favorable values.

The fluctuating forces in a loaded bearing can excite transverse vibrations of the bearing with respect to the sleeve. To avoid this, it is necessary to avoid more than transient operation near the condition

$$
\begin{equation*}
\frac{\omega_{\text {bearing }} r_{\text {inner }}}{d_{\mathrm{a}}}=\frac{v}{d_{\mathrm{a}}}=\frac{1}{2 \pi} \sqrt{\frac{k_{\mathrm{s}, \text { trans }}}{m_{\text {rotor }}}} \tag{10.18}
\end{equation*}
$$

For rotors with transverse stiffnesses $\sim 1000 \mathrm{~N} / \mathrm{m}$ and dimensions of a few nanometers, the critical interfacial sliding speed $v \approx 100 \mathrm{~m} / \mathrm{s}$, and the critical frequency $\omega_{\text {bearing }}>10^{12} \mathrm{rad} / \mathrm{s}$.

b. Shear-reflection drag. Several of the following energy dissipation mechanisms depend on the thermally averaged phonon transmission coefficient of the bearing interface, $T_{\text {trans }}$. Using the approximations of Eqs. (7.41) and (7.42) and assuming materials with the modulus, atom number density, and Debye temperature of diamond, the transmission coefficient at $300 \mathrm{~K}$ is

$$
\begin{align*}
& T_{\text {trans }} \approx \frac{z}{1+3 z}, \quad \text { where } z=2.4 \times 10^{-37} k_{\mathrm{a}}^{1.7}, \text { and }  \tag{10.19}\\
& T_{\text {trans }} \approx 2.4 \times 10^{-37} k_{\mathrm{a}}^{1.7}, \text { if } k_{\mathrm{a}} \leq 300 \mathrm{~N} / \mathrm{m} \cdot \mathrm{nm}^{2} \tag{10.20}
\end{align*}
$$

As discussed in Section 7.3.5f, these approximations should overestimate the transmission coefficient for interfaces that are curved or that have mismatched acoustic speeds, and hence should prove conservative in the present context.

Applying the approximations of Section 7.3.6 and again assuming the material properties of diamond at $300 \mathrm{~K}$ yields an estimate of the drag power as a function of the sliding speed $v$, area $S$, and stiffness $k_{\mathrm{a}}$ of the interface:

$$
\begin{equation*}
P_{\text {drag }}<1.8 \times 10^{-33} k_{\mathrm{a}}^{1.7} v^{2} S \tag{10.21}
\end{equation*}
$$

or, applying Eq. (10.15) with the same restriction,

$$
\begin{equation*}
P_{\text {drag }}<1.6 \times 10^{-33} k_{\mathrm{s}, \text { bear }}^{1.7}\left(\ell r_{\text {eff }}\right)^{-0.7} v^{2} \tag{10.22}
\end{equation*}
$$

For a bearing with $r_{\text {eff }}=\ell=2 \mathrm{~nm}$ and $k_{\text {s,bear }}=10^{3} \mathrm{~N} / \mathrm{m}, P_{\text {drag }} \approx 3 \times 10^{-16} \mathrm{~W}$ at $v=1 \mathrm{~m} / \mathrm{s}$, and $\approx 3 \times 10^{-20} \mathrm{~W}$ at $1 \mathrm{~cm} / \mathrm{s}$.

Sleeve bearings can be used both to support loads along the shaft axis and to provide stiffness in resisting axial displacements; this can be accomplished by ensuring that the shaft and sleeve have interlocking circumferential corrugations (e.g., as shown in Figure 10.17). An interface of this sort exhibits a stiffness per unit area for transverse displacements (in the axial direction) of $k_{\mathrm{a}, \text { trans }}$. This coupling mode permits phonons of a different polarization to cross the interface, providing an independent mechanism for energy dissipation characterized by expressions like those above, but with $k_{\mathrm{a} \text {,trans }}$ substituted for $k_{\mathrm{a}}$ (and in a more thorough analysis, a different modulus, etc.). Where the axial stiffness equals $k_{\mathrm{s} \text {,bear }}$, the increment in energy dissipation is $\sim 0.5^{1.7} P_{\mathrm{drag}} \approx 0.3 P_{\mathrm{drag}}$.

c. Band-stiffness scattering. Following the procedure in the previous section, expressions analogous to Eqs. (10.21) and (10.22) for power dissipation from band-stiffness scattering, Eq. (7.35), are

$$
\begin{equation*}
P_{\text {drag }}<3.0 \times 10^{-33} k_{\mathrm{a}}^{1.7} R^{2} \frac{\Delta k_{\mathrm{a}}}{k_{\mathrm{a}}} v^{2} S \tag{10.23}
\end{equation*}
$$

and

$$
\begin{equation*}
P_{\text {drag }}<2.7 \times 10^{-33} k_{\mathrm{s}, \text { bear }}^{1.7}\left(\ell r_{\text {eff }}\right)^{-0.7} R^{2} \frac{\Delta k_{\mathrm{a}}}{k_{\mathrm{a}}} v^{2} \tag{10.24}
\end{equation*}
$$

In the coplanar ring model, $R$ (Section 7.2.6c) equals $|m /(m-n)|$; if the interatomic spacings in the inner and outer rings are equal, then $R \approx 10$ when $s_{\text {gap }} \approx$ $0.2 \mathrm{~nm}$, and $r_{\text {inner }} \leq 2 \mathrm{~nm}$. Regardless of bearing radius, differences in surface structure or strain on opposite sides of the interface can be used to ensure that $R \leq 10$.

The parameter $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}$ can be estimated from variations in the stiffness of nonbonded interactions between rows of equally spaced atoms as a function of their offset from alignment. Like many differential quantities, it is strongly dependent on the spatial frequencies involved. For first-row atoms (taking carbon as a model), $\Delta k_{\mathrm{a}} / k_{\mathrm{a}} \approx 0.3$ to 0.4 (at a stiffness-per-atom of 1 and $10 \mathrm{~N} / \mathrm{m}$, respectively) where $d_{\mathrm{a}}=0.25 \mathrm{~nm}$, and $\sim 0.001$ to 0.003 where $d_{\mathrm{a}}=0.125 \mathrm{~nm}$. This value of $d_{\mathrm{a}}$ cannot be physically achieved in coplanar rings, but it correctly models a ring sandwiched between two other equidistant rings having $d_{\mathrm{a}}=0.25 \mathrm{~nm}$ and a rotational offset of $0.125 \mathrm{~nm}$.

With the parameters used in the previous section, and $R=10$ and $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=$ $0.4, P_{\text {drag }} \approx 2 \times 10^{-14} \mathrm{~W}$ at $v=1 \mathrm{~m} / \mathrm{s}$; with $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.003, P_{\text {drag }} \approx 1.5 \times 10^{-16} \mathrm{~W}$.

d. Band-flutter scattering. Again following the procedure in Section 10.4.6b, the expression for power dissipation from band-flutter scattering, Eq. (7.37), becomes

$$
\begin{equation*}
P_{\text {drag }}<1.2 \times 10^{-31} k_{\mathrm{s}, \text { bear }}^{1.7}\left(\ell r_{\text {eff }}\right)^{-0.7} R^{2}\left(A / d_{\mathrm{a}}\right)^{2} v^{2} \tag{10.25}
\end{equation*}
$$

The amplitude of the interfacial deformation, $A$, can be roughly estimated from $\Delta k_{\mathrm{a}}, R, d_{\mathrm{a}}$, and a characteristic elastic modulus $M$. From Eq. (3.18) and the associated discussion, it can be seen that $\Delta p$ in the interface $\leq 3 \times 10^{-11} \Delta k_{\mathrm{a}}$. A pressure distribution varying sinusoidally across a surface with a spatial frequency $k$ produces displacements that decrease with depth on a length scale $w=1 / k \approx R d_{\mathrm{a}} / 2 \pi$, or $\sim 0.4 \mathrm{~nm}$ for systems with $d_{\mathrm{a}}=0.25 \mathrm{~nm}$ and parameters like those described in Section 10.4.6b. The amplitude $A \approx w \Delta p / M$; with $k_{\mathrm{a}}=$ $8 \times 10^{19}\left(\mathrm{~N} / \mathrm{m} \cdot \mathrm{m}^{2}\right), \Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.4$, and the previous values, $P_{\mathrm{drag}}<5 \times 10^{-18} \mathrm{~W}$ at $v=1 \mathrm{~m} / \mathrm{s}$; this is negligible in comparison to band-stiffness scattering.

e. Thermoelastic damping. Using diamond material parameters and the effective thickness $w$ from the previous section together with $\tau_{\text {therm }}=10^{-12} \mathrm{~s}$ yields the following specialization of Eq. (7.54):

$$
\begin{equation*}
P_{\text {drag }} \approx 4.3 \times 10^{-27} 2 \pi r_{\text {eff }} \ell w\left(\Delta p v / d_{\mathrm{a}}\right)^{2} \tag{10.26}
\end{equation*}
$$

Applying the assumptions of Section 7.4.1 with the parameters assumed in Section 10.4.6c and the estimate of $\ell$ and $\Delta p$ from the previous section yields $P_{\text {drag }} \approx 6 \times 10^{-16} \mathrm{~W}\left(\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.4\right)$ and $\sim 8 \times 10^{-20} \mathrm{~W}\left(\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.003\right)$, for $v=$ $1 \mathrm{~m} / \mathrm{s}$. This too is negligible in comparison to band-stiffness scattering.

f. Summary. For well-designed bearings on a nanometer scale at $300 \mathrm{~K}$, acoustic radiation losses typically are negligible compared with losses resulting from phonon interactions. The latter loss mechanisms all scale as $v^{2}$. Dropping the apparently negligible contributions from mechanisms other than shearreflection and band-stiffness scattering interactions, and multiplying drag by 1.3 to approximately account for the effects of a transverse interfacial stiffness giving an axial bearing stiffness equaling $k_{\mathrm{s} \text {, bear }}$, yields an estimated bound on the total bearing drag:

$$
\begin{equation*}
P_{\text {drag }}<\left(2.0 \times 10^{-33}+3.5 \times 10^{-33} \frac{\Delta k_{\mathrm{a}}}{k_{\mathrm{a}}} R^{2}\right) \frac{k_{\mathrm{s}, \text { bear }}^{1.7}}{\left(\ell r_{\text {eff }}\right)^{0.7}} v^{2} \tag{10.27}
\end{equation*}
$$

With $k_{\mathrm{s}, \text { bear }}=1000 \mathrm{~N} / \mathrm{m}, r_{\text {eff }}=\ell=2 \mathrm{~nm}$, and $R=10, P_{\text {drag }} \approx 2.7 \times 10^{-14} v^{2} \mathrm{~W}$ $\left(\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.4\right)$, dominated by band-stiffness scattering, or $\approx 5.8 \times 10^{-16} v^{2} \mathrm{~W}$ $\left(\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.003\right)$, with a substantial contribution from shear-reflection drag. Using the higher value and $v=1 \mathrm{~m} / \mathrm{s}$, a bearing of this sort is estimated to dissipate $<0.06 k T_{300}$ per rotation. This energy dissipation (which can be reduced with changes in design) is consistent with high system efficiency, if a rotation of the bearing is associated with some process that does many times $k T_{300}$ of useful work (e.g., in a motor, Section 11.7, or a mechanosynthetic system, Section 13.3). It is high, however, if one instead considers power dissipation per unit volume $\left(\sim 10^{11} \mathrm{~W} / \mathrm{m}^{3}\right)$.

(Note that the approximations made in deriving the drag expressions in this section are intended to provide only a gross upper bound on the magnitude of the drag. Constants in these expressions are sometimes written to two significant digits, but usually lack the accuracy that this notation might imply.)

### 10.4.7. Sleeve bearings in molecular detail

Sleeve bearings can usefully be examined at two levels of molecular detail: interfacial structure and overall structure. The design of relatively large bearings can exploit strained cylindrical shells (Section 9.6.1). Bearings of this sort can be viewed as forming families with specific unstrained structures and crystallographic orientations (relative to the interface and the bearing axis), and with specific surface terminations at the sliding interface. Within such a family, the bearing radius $r_{\text {eff }}$ and the spacing between the surfaces $s_{\text {gap }}$ are determined within broad limits by the choice of the inner and outer circumferences (in lattice units). For these bearings, specification of the interfacial structure is primary, since the overall structure is simple and repetitive.

For smaller bearings, in contrast, strained cylindrical shells become a poor model. The structure of the shaft then becomes a special case rather than a member of a parameterized family, and the overall structure must be considered as a unit. Examples drawn from both classes are given in the following sections.

a. Bearing interfaces for strained-shell structures. Figures 10.15 and 10.16 illustrate several pairs of terminated diamond surfaces, each forming an interface suitable for use in a symmetrical sleeve bearing. These interfaces have differing properties with respect to axial stiffness and drag.

Each of the interfaces shown exhibits substantial axial stiffness at suitably small values of $s_{\text {gap }}$. Along the axis, the surface atomic rows on opposite sides of each interface have identical spacings, hence the sinusoidal potentials for sliding

(a)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=178&width=208&top_left_y=614&top_left_x=542)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=205&width=213&top_left_y=862&top_left_x=540)

(c)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=196&width=215&top_left_y=1132&top_left_x=534)

(d)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=220&width=200&top_left_y=1390&top_left_x=551)

(e)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=210&width=219&top_left_y=1668&top_left_x=532)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=212&width=234&top_left_y=598&top_left_x=886)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-63.jpg?height=1056&width=256&top_left_y=842&top_left_x=866)

Figure 10.15. Several sliding interfaces based on diamond (111) surfaces, with nitrogen termination (a), hydrogen termination (b), alternating, interlocking rows with nitrogen and hydrogen termination (c), fluorine termination (d), and alternating, interlocking rows of nitrogen and fluorine termination (e). Note that pairs of surfaces from (a), (b), and (d) could be combined, as could a pair from (c) and (e). In each diagram the direction of sliding is nearly perpendicular to the page. Different terminations offer different functional relationships among spacing, shear stiffness, and compressive stiffness.

(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=188&width=268&top_left_y=244&top_left_x=406)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=171&width=202&top_left_y=484&top_left_x=437)

(c)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=164&width=200&top_left_y=731&top_left_x=440)

(d)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=178&width=205&top_left_y=958&top_left_x=443)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=208&width=287&top_left_y=229&top_left_x=773)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-64.jpg?height=700&width=254&top_left_y=457&top_left_x=788)

Figure 10.16. Several sliding interfaces based on diamond (100) surfaces, with oxygen termination and aligned rows (a); oxygen termination and crossed rows (b); oxygen termination with alternating deleted rows, providing an interlocking surface (c); and surfaces like (c), but with the exposed terminating rows on one surface consisting of sulfur rather than oxygen (d). In each diagram the direction of sliding is nearly perpendicular to the page. Different terminations offer different functional relationships among spacing, shear stiffness, and compressive stiffness.

in this direction add in phase over the entire interface. Interfaces 10.15(c), 10.15(e), 10.16(c), and 10.16(d) include interlocking grooves, increasing the energy barrier for axial sliding and (in most instances) the stiffness as well. In these structures, the axial stiffness can equal or exceed the transverse-displacement stiffness $k_{\mathrm{s} \text {, bear }}$. An interface with mismatched spacings in both dimensions [e.g., combining 10.15(b) and 10.16(a), can permit both rotation and axial sliding (see Section 10.5.2].

Interfaces 10.15(c), 10.15(e), and 10.16(a-d) exhibit values of $d_{\mathrm{a}} \approx 0.25 \mathrm{~nm}$, corresponding to the high-drag cases in Sections 10.4.6c and 10.4.6d. Interfaces 10.15(b) and 10.15(d), however, will (in the absence of significant axial loads) exhibit $d_{\mathrm{a}, \text { eff }} \approx 0.125 \mathrm{~nm}$ : an atom on one surface interacts equally with two staggered rows on the other, halving the effective spacing for most purposes. This value of $d_{\mathrm{a}, \text { eff }}$ corresponds to the low-drag cases in Sections 10.4.6c and 10.4.6d. A nitrogen-terminated (111) surface, Figure 10.15(a), has $d_{\mathrm{a}, \text { eff }} \approx 0.125 \mathrm{~nm}$ where first-layer interactions are concerned, but the second atomic layer introduces significant interactions with $d_{\mathrm{a}} \approx 0.25 \mathrm{~nm}$.

b. Interfacial stability. Each of the interfaces in Figures 10.15 and 10.16 (and that shown in Figures 10.17 and 10.18) appears stable enough for practical use under the baseline conditions assumed in this volume (i.e., no extreme temperatures, no UV exposure, no extraneous reactive molecules, no extreme mechanical loads); further, the symmetrical and low-polarity interfaces should guarantee the absence of contact charging (Section 6.4.7). The low-valence atoms used to terminate each surface form strong bonds to carbon and (usually) weaker bonds to one another. A reaction between one surface and the other typically must form a bond between two low-valence atoms at the expense of cleaving two bonds to carbon. Since this would be a strongly endoergic process, the energy barrier is large ( $>500 \mathrm{maJ}$ ) and the rate of occurrence negligible

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-65.jpg?height=354&width=586&top_left_y=795&top_left_x=532)

exploded view

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-65.jpg?height=321&width=728&top_left_y=1176&top_left_x=456)

(a)

$1 \mathrm{~nm}$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-65.jpg?height=314&width=741&top_left_y=1563&top_left_x=440)

(b)

2808 atoms

Figure 10.17. A 2808-atom strained-shell sleeve bearing with an interlocking-groove interface derived by modifying a diamond (100) surface; (b) shows the shaft within the sleeve, (a) shows an exploded view. This design was developed in collaboration with $\mathbf{R}$. Merkle at the Xerox Palo Alto Research Center, using an automated structuregeneration package (Merkle, 1991). It was then energy minimized and analyzed using the Polygraf molecular modeling software (Polygen Molecular Simulations, Inc., Waltham, MA).

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-66.jpg?height=398&width=1207&top_left_y=187&top_left_x=130)

Figure 10.18. A section through the interface of the bearing shown in Figure 10.17. The view roughly parallels the planar diagrams shown in Figure 10.16, differing in the presence of curvature and in the use of a different (100)-based surface modification for the interface structure. The use of sulfur bridges on the outer shaft surface rather than oxygen both reduces strain (via longer bonds) and increases interfacial stiffness (via larger steric radii).

$\left(<10^{-39} \mathrm{~s}^{-1}\right)$. These remarks apply with equal force to a wide variety of sliding and rolling interfaces with similar termination by low-valence atoms.

Graphitic interfaces are also desirable, but the potential reactivity of their unsaturated tetravalent atoms demands attention. Experiments show that graphite transforms to a transparent, nondiamond phase at room temperature under pressures of $\sim 18 \mathrm{GPa}$ (Utsumi and Yagi, 1991); this pressure corresponds to a compressive load of $\sim 0.5 \mathrm{nN}$ per atom (with an associated stiffness on the order of $20 \mathrm{~N} / \mathrm{m}$ ). The transformation is nucleated at specific sites in a crystal, and can be observed to spread over a period of $\sim 1$ hour. Small areas of graphitic bearing interface can presumably be made that lack suitable nucleation sites, hence interfacial pressures of $\sim 18 \mathrm{GPa}$ should be consistent with chemical stability.

c. A specific strained-shell structure. Figure 10.17 illustrates a strained-shell structure containing 2808 atoms, with a shaft of 34-fold rotational symmetry and a sleeve of 46 -fold rotational symmetry; $\operatorname{lcm}(n, m) / n=23$. The dimensions of the interface are somewhat ill defined, but approximate values are $r_{\text {eff }} \approx 3.5 \mathrm{~nm}$ and $\ell \approx 1.0 \mathrm{~nm}$; the external radius at the illustrated termination surface is $\sim 4.8 \mathrm{~nm}$. This bearing was designed (perhaps over designed) for large axial stiffness, achieved by combining interlocking ridges with large nonbonded contact forces (Figure 10.18 shows a section through the interface). A molecular mechanics model (see Figure 10.17 caption) predicts that the maximally strained $\mathrm{C}-\mathrm{C}$ bonds of the outer surface of the sleeve have lengths of $\sim 0.166 \mathrm{~nm}$, well within the estimated positive-stiffness limit of $0.187 \mathrm{~nm}$ (Section 3.3.3a). The closest nonbonded contacts across the interface are $\sim 0.284$ (for $\mathrm{S} \mid \mathrm{O}$ ) and $\sim 0.270$ (for $\mathrm{S} \mid \mathrm{N}$ ); the corresponding forces are $\sim 0.56$ and $\sim 1.1 \mathrm{nN}$; the corresponding stiffnesses are $\sim 20$ and $\sim 40 \mathrm{~N} / \mathrm{m}$. The compliance of the interface stemming from nonbonded forces is $\sim 10^{-21} \mathrm{~m}^{2} \cdot \mathrm{m} / \mathrm{N}$ (from MM2/CSC), comparable to the shear compliance of $a \sim 0.5 \mathrm{~nm}$ thickness of diamond. Bond angle bending adds significant compliance to the interface, but the total compliance does not exceed the shear compliance of a sheet of diamond a few nanometers thick. For the bearing as a whole, the axial stiffness should exceed $2000 \mathrm{~N} / \mathrm{m}$.

Energy minimization of this structure yielded no rotation of the shaft with respect to the sleeve, regardless of angular displacement. Examination of energy differences for minimized structures as a function of angular displacement indicates values of $\Delta \mathcal{V}_{\text {barrier }}<0.03 \mathrm{maJ}$. Owing to high interfacial stiffnesses, however, the estimated drag in a bearing of this sort is larger than that calculated in the examples of Section 10.4.6.

d. Small sleeve-bearing structures. In small sleeve bearings, the pursuit of high-order rotational symmetry dramatically limits the set of acceptable structures, although this set remains large enough to make enumeration challenging. A segment of any of the structures shown in Figures 9.5 and 9.6 could serve as a shaft, given a suitable sleeve. Thin strained shells, backed up by layers with regular dislocation-like structures, could serve as shafts or sleeves, as could less-regular, special-case structures.

e. A specific small sleeve-bearing structure. An example combining a special shaft with a special sleeve is shown in Figure 10.19. This structure makes use of chains of $s p^{3}$ nitrogen atoms to form ridges (having high stiffness and spatial frequency) on both the shaft and the sleeve. These features require attention because $\mathrm{N}-\mathrm{N}$ bonds are known to be weak, and isolated chains of this sort are apparently unstable (a search of the chemical literature failed to identify a wellcharacterized example). In the present instance, however, these chains are not isolated. Each $\mathbf{N}$ atom is also bonded to carbon and subject to the familiar constraints of a diamondoid structure: momentary thermal cleavage of an $\mathrm{N}-\mathrm{N}$ bond is resisted (and usually reversed) by elastic restoring forces from the surrounding structure. The most accessible failure mode in this system is appar-
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-67.jpg?height=750&width=988&top_left_y=1404&top_left_x=327)

exploded view

258 atoms

Figure 10.19. Views of a small sleeve-bearing structure: (a) end, (b) exploded.

(a)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-68.jpg?height=190&width=630&top_left_y=204&top_left_x=400)

(b)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-68.jpg?height=238&width=646&top_left_y=380&top_left_x=396)

Figure 10.20. The shaft of the bearing shown in Figure 10.19 (a), showing a hypothetical failure mode (b).

ently the transformation of a nitrogen chain in the shaft into a series of $\mathrm{N}=\mathrm{N}$ dimers (Figure 10.20), but estimates of bond energies and strain energies suggest that this transformation is only moderately exoergic ( $\sim 70 \mathrm{maJ}$ ?) on a perbond-cleaved basis. Moreover, the formation of a single pi-bonded dimer by cleavage of two adjacent sigma bonds is strongly endoergic (sacrificing two sigma bonds to create, initially, one strongly twisted pi bond), and the simultaneous cleavage of six sigma bonds should be energetically prohibitive. Accordingly, these structures appear sufficiently stable for use, although none of the following design and analysis relies on this.

The stiffness of the bearing interface can be computed from the change in nonbonded interaction energies as a function of relative displacement of the shaft and sleeve, in the absence of structural relaxation. Calculations yield an axial stiffness of $\sim 360 \mathrm{~N} / \mathrm{m}$ and an isotropic transverse stiffness of $\sim 470 \mathrm{~N} / \mathrm{m}$. Rotational energy barriers (computed with structural relaxation) were found to be $<0.001 \mathrm{maJ}$. All computations used the MM2/CSC model extended with parameters to accommodate $\mathrm{N}-\mathrm{N}-\mathrm{N}$ bond angles. The parameter $\theta_{0}$ for $\mathrm{N}-\mathrm{N}-\mathrm{N}$ angle bending was set at $114.5^{\circ}$ to fit AM1 semiempirical computations on $\mathrm{H}_{2} \mathrm{NNHNH}_{2}$ (performed in collaboration with R. Merkle); $k_{\theta}$ was set at $0.740 \mathrm{aJ} / \mathrm{rad}^{2}$, equaling the MM2 value for $\mathrm{N}-\mathrm{N}-\mathrm{C}$ angle bending. Bearing stiffnesses (but not barriers) are sensitive to the choice of $\theta_{0}$. Supplemental torsional parameters are of less significance; values were chosen to match analogous MM2 values.

The total strain energy in this structure is large $(\sim 12 \mathrm{aJ})$, but only $\sim 530 \mathrm{maJ}$ of this is in the form of bond stretching, and this energy is well distributed over many bonds; $\sim 71 \%$ of the strain energy is in the form of bond angle-bending, much of this owing to the presence of 22 cyclobutane rings within the structure. The closest nonbonded distance between shaft and sleeve is $\sim 0.26 \mathrm{~nm}(\mathrm{~N} / \mathrm{N})$. For a relaxed model of a shaft popping into (or out of) a sleeve, with the nitrogen chains approximately coplanar, the total energy is increased by $\sim 1.7 \mathrm{aJ}$, and the closest $\mathrm{N} \mid \mathrm{N}$ distance is $\sim 0.236 \mathrm{~nm}$ : bond lengths remain reasonable, the $\mathrm{N}-\mathrm{N}$ bonds are under stabilizing, compressive loads, and the estimated peak forces in achieving this configuration are small compared to bond tensile strengths. Assembly of this bearing from separate components thus appears feasible.

This structure is the first nanomechanical sleeve bearing designed in atomic detail (in 1990). Note that the bearing in Figure 1.1, although superficially similar, is an entirely different structure. It was designed (in 1992) to resemble the structure of Figure 10.19 while omitting questionable $s p^{3}$ nitrogen atoms.

### 10.4.8. Less symmetrical sleeve bearings

a. Asymmetries to compensate for load. Transverse loads on bearings shift the axis of the shaft with respect to that of the sleeve; the use of a symmetrical sleeve is then no longer motivated by the symmetry of the situation. Assume that the sleeve is fixed, and that the shaft rotates under a constant transverse load with an orientation fixed in space (Figure 10.21). The previous analysis in this chapter assumes that this asymmetric load is supported by the topmost atomic layers, chiefly through differences in overlap repulsion caused by shaft displacement. Alternatively, however, the load on the shaft can (in many instances) be supported by differences in van der Waals attraction resulting from an asymmetric structure having regions of different Hamaker constant $\mathscr{A}$ (e.g., differing atom number densities) immediately behind the surface layer. This approach can reduce $\Delta \mathcal{V}_{\text {barrier }}$, and can increase load-bearing capacity without increasing interfacial stiffness.

In small loaded bearings, $\Delta \mathcal{V}_{\text {barrier }}$ can be large (Figure 10.13). Where the shaft is of high symmetry and the sleeve has $>10$ interfacial atoms, the calculations of Section 10.3 suggest that an asymmetric placement of sleeve atoms can be chosen to ensure that $\Delta \mathcal{V}_{\text {barrier }}<1 \mathrm{maJ}$. In many instances, a slightly perturbed version of a symmetrical structure can accomplish this.

b. Asymmetries to simplify construction. Bearings having interfaces with shallow grooves or relatively large $s_{\text {gap }}$ often can be assembled from separate shafts and sleeves in the obvious manner, by pressing the shaft into the sleeve. Large loads often can be applied, and the final energy minimum with respect to axial displacement can be deep and stiff.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-69.jpg?height=617&width=700&top_left_y=1561&top_left_x=417)

Figure 10.21. Schematic diagram of a loaded bearing, with compensating asymmetric van der Waals attractions.

Structures with more strongly interlocking grooves cannot be assembled in this fashion. If they are to have full symmetry, the sleeve must be synthesized in situ around the shaft (e.g., building out from polymeric bands that become the ridges on the sleeve), or must have a final assembly step that closes an adhesive interface. Sleeves made from two $\mathrm{C}$-shaped segments with an atomic-scale discontinuity at the two seams have lower symmetry but can nonetheless be designed to exhibit low $\Delta \mathscr{V}_{\text {barrier }}$

### 10.5. Further applications of sliding-interface bearings

The preceding results regarding irregular objects and symmetrical sleeve bearings shed light on a wide range of other sliding-interface systems. Among these are nuts turning on screws, rods sliding in sleeves, and a class of constant-force springs. Energy dissipation analyses are omitted, but follow the principles discussed in Section 10.4.6.

### 10.5.1. Nuts and screws

The thread structure of a nut-and-screw combination can formally be generated by dividing a grooved, strained-shell sleeve bearing parallel to the axis along one side, shifting one cut surface in the axial direction by an integral number of groove spacings, and reconnecting. The result is locally similar to the original bearing, save for the introduction of a helical pitch in the grooves and ridges, which accordingly must come to an end at some point (in any straight, finite structure).

What is the static friction of such a structure, assuming that the helical atomic rows of the inner and outer surfaces have nonmatching spacings? (Note that these spacings need not be commensurate; in good designs, the spacings can lack small common multiples.) Figure 10.5 approximates the potential of an atom with respect to a row as a single sinusoidal potential with some amplitude and phase, represented as a vector magnitude and angle in a plane. In this representation, the potential of a series of atoms in one surface of a uniform, nonmatching interface takes the form shown in Figure 10.22: all vectors are of the same magnitude, and each is rotated with respect to the last by a fixed angle. Where that angle is not zero, the resultant vector always lies on a circle passing through the origin. Its magnitude oscillates between fixed bounds and periodically assumes a small value; $\Delta \mathscr{V}_{\text {barrier }}$ and the static friction accordingly do the same. A bound on the magnitude of the barrier is

$$
\begin{equation*}
\Delta \mathscr{V}_{\text {barrier, max }}=\frac{\Delta \mathscr{V}_{\text {barrier, single }}}{2} \sqrt{1+\tan ^{2}\left(\frac{\pi-\phi}{2}\right)} \tag{10.28}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-70.jpg?height=270&width=412&top_left_y=1988&top_left_x=146)

Figure 10.22. Vector representation of interatomic potentials (see Figure 10.5) for a row of regularly spaced atoms in one surface sliding over regularly spaced atoms in another. Each atom experiences an approximately sinusoidal potential, and the phase difference between the sinusoid experienced by one atom and that experienced by its successor in the row corresponds to a constant difference in the angle between their vectors.

(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-71.jpg?height=150&width=579&top_left_y=195&top_left_x=576)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-71.jpg?height=152&width=719&top_left_y=404&top_left_x=514)

Figure 10.23. Linear representation of the sliding of two finite but otherwise regular surfaces over one another. In (a), the range of motion of one surface places it within the width of the other surface at all times; this corresponds (for example) to a nut turning on the middle of a long screw. In (b), the range of motion of the surfaces enables each to extend beyond one limit of the other at all times; this corresponds (for example) to a screw partially inserted into a deep threaded hole. In (a), the irregularities corresponding to both ends of the overlap region move together over a surface of a single spatial frequency; tuned irregularities at one end can keep $\Delta \mathcal{V}_{\text {barrier }}$ low. In (b), the irregularities move in opposite directions over surfaces of differing spatial frequency, and tuned irregularities are usually needed at both ends (that is, on both sides of the interface) if the two sinusoidal components of the potential are both to be cancelled.

where $\phi$ is the phase angle between succeeding atoms in the surface under consideration.

This result indicates that the static friction of a nut-and-screw system (under low loads) depends chiefly on the end conditions. With the right choice of interface length, $\Delta \mathcal{V}_{\text {barrier }}$ is low because the resultant vector is of small magnitude. For other choices of interface length, $\Delta \mathscr{V}_{\text {barrier }}$ can be made low by the methods discussed in Section 10.3, that is, tuned structural irregularities can be introduced at one end of a nut in such a way that the amplitude and phase of their contribution to the potential cancels the residual contribution from the regular portion of the nut. As shown in Figure 10.23, where the overlap of the nut and screw is variable, minimizing the sinusoidal component of the potential can require tuned irregularities at two sites.

Nut-and-screw systems with high potential barriers can be used as components of adjustable-length struts (see the related discussion in Section 10.9.2). Systems with low potential barriers can be used in jacks or power screws.

### 10.5.2. Rods in sleeves

The analysis of rod-in-sleeve systems is entirely analogous to that for nut-andscrew systems, save that the helical grooves take the degenerate form of straight lines. Again, end conditions determine the magnitude of the static friction, and again, choice of length or tuning of irregular structures can yield low values of $\Delta \mathcal{V}_{\text {barrier }}$ As noted in Section 10.4.7a, cylindrical interfaces can be designed to permit simultaneous axial sliding and rotation in any proportion.

### 10.5.3. Constant force springs

In the variable-overlap case mentioned in Section 10.5.1, suppression of sinusoidal potentials does not leave a flat potential, because the energy of the system is in general a function of the overlap. Where local interactions are dominant, the
potential energy is proportional to the overlap, with a positive or negative constant of proportionality depending on the net energy of the surface-surface interaction. A sliding rod in a sleeve of this sort, tuned for smooth motion, acts as a constant-force spring over its available range of motion.[^28] Since the characteristic attractive interaction energies of surfaces (Section 3.5.2) are on the order of $100 \mathrm{maJ} / \mathrm{nm}^{2}$, the force with which a rod can be made to retract into a sleeve is on the order of $0.6 \mathrm{rnN}$, where $r$ is in nanometers (linear scaling fails for very slim rods). Since repulsive interaction energies can be much larger, forces for a constant-force spring operating in this mode can be much larger, and considerable energy can be stored in elastic deformation of the rod and sleeve.

### 10.6. Atomic-axle bearings

### 10.6.1. Bonded bearings

Sigma bonds permit rotation, in the absence of mechanical interference between the bonded moieties. Barriers for rotation vary. Two model systems are cubylcubane $\mathbf{1 0 . 1}$ and phenylcubane $\mathbf{1 0 . 2}$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-72.jpg?height=179&width=280&top_left_y=962&top_left_x=417)

10.1

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-72.jpg?height=181&width=294&top_left_y=961&top_left_x=750)

10.2

with MM2/CSC values of $\Delta V_{\text {barrier }}$ equaling 11.5 and $0.3 \mathrm{maJ}$ respectively; note that the latter has a structure with 3 -fold rotational symmetry interacting with one with 2 -fold symmetry. The stiffness for shearing displacements of sigma bearings of this sort is about twice the transverse-displacement stiffness of a sigma bond (Section 3.3.2b), $\sim 60 \mathrm{~N} / \mathrm{m}$ for structures like cubylcubane. A rotor supported by two such bearings has a transverse displacement stiffness of $\sim 120 \mathrm{~N} / \mathrm{m}$, and (with a proper choice of relative phases) small values of $\Delta \mathcal{V}_{\text {barrier }}$. Figure 10.32 shows a planetary gear system that includes nine sigmabond bearings.

Using a $-\mathrm{C} \equiv \mathrm{C}-$ unit in place of a sigma bond can drop $\Delta \mathcal{V}_{\text {barrier }}$ to near zero (Knox, 1971), at the expense of increasing the volume and greatly decreasing resistance to shearing displacements. Organometallic bearings based on the ferrocene structure can have fairly low barriers [ 7 maJ (Huheey, 1978)] and should have good stiffness.

### 10.6.2. Atomic-point bearings

A rotor with protruding atoms on opposite sites can be captured between a pair of surfaces with matching hollows. Values of $\Delta \mathscr{V}_{\text {barrier }}$ can be low if the interacting surfaces are well designed. Under substantial compressive loads, stiffness can be moderately high. A macroscale analogue of a bearing of this sort would have sliding interfaces, but the reduction of the contact region to a single atom (on one side of the interface), together with the placement of that atom on the axis of rotation, makes atomic-point bearings qualitatively different.

### 10.7. Gears, rollers, belts, and cams

### 10.7.1. Spur gears

Spur gears find extensive use in machinery, chiefly for transmitting power between shafts of differing angular frequency. Spur gears achieve zero slip (so long as the teeth remain meshed), and ideally exhibit minimal energy barriers during rotation, minimal dynamic friction, and maximal stiffness in resisting interfacial shear.

Nanomechanical gears can exploit various physical effects to implement "teeth." These include complementary patterns of charge, of hydrogen bonds, or of ${ }^{\circ}$ dipolar bonds. The most straightforward effect to analyze, however, is overlap repulsion between surfaces with complementary shapes (the effect exploited by macroscale gears).

In conventional gearing, teeth are carefully shaped (e.g., in involute curves) to permit rolling motion of one tooth across another. Because a tooth on one gear meshes between two teeth on the opposite gear, but can only roll across one of them, a clearance (backlash) must be provided. Accordingly, on reversal of torque, teeth lift from one surface before contacting another. These complexities of geometry are both impossible and unnecessary in nanomechanical gears. Since sliding of one tooth over another is just another variation on a slidinginterface bearing, there is no need to construct involute surfaces. Since the steric interaction between atoms is soft, and since sliding contacts between teeth are acceptable, no backlash need be provided (and would not be a well-defined quantity if it were).

Small nanomechanical gears of this class use single atoms or rows of atoms as steric teeth; any of the grooved interfaces in Figures 10.15 and 10.16 could serve this role in a strained-shell structure. As with bearings, small special-case structures are also feasible. And again, models based on rigid, circular arrays of atoms reduce computational costs while preserving the essential physics.

a. A relaxation-free model of meshing gear teeth. Figure 10.24 illustrates a model of steric gears as rigid, coplanar rings of atoms. The calculations described in this section, like those in the discussion of bearings, assume the MM2 exp-6 nonbonded potential, Eq. (3.8), with $\mathrm{H}$ atoms separated by $d_{\mathrm{a}}=$ $0.3 \mathrm{~nm}$. Again, the general nature of the results is insensitive to the choice of potential, atom type, and interatomic spacing.Figure 10.25 plots barrier heights as a function of the number of teeth $n$ (here, equal for both gears) and the separation $s_{\text {gap }}$ (see Figure 10.24). The lower family of curves shows barriers for corotation at a uniform angular velocity without slippage. The upper family of curves shows barriers for slipping of one ring with respect to another, based on a search for minimum-energy pathways at a range of rotational angles. As can be seen, with small values of $s_{\text {gap }}(<0.12 \mathrm{~nm})$

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-74.jpg?height=417&width=659&top_left_y=182&top_left_x=423)

Figure 10.24. Coplanar ring model for a steric gear.

and moderate numbers of teeth ( $>20$ ), energy barriers to slippage are large ( $>500 \mathrm{maJ}$ ) and energy barriers to corotation are small ($<0.01$ maJ).

Under interfacial shear loads (required, for example, to transmit power), the symmetry of the system is degraded, and corotational barriers are larger. The effects of load can be modeled by a constant angular offset between the rings relative to their minimum-energy, symmetrically meshed geometry. Figure 10.26 shows corotational barrier heights for two values of $n$ at several values of the offset (measured by displacement at the ring circumference). For $n$ as small as 10 and offsets as large as $0.01 \mathrm{~nm}$, the corotational barrier remains $<1 \mathrm{maJ}$; at small values of $s_{\text {gap }}$, this offset is adequate to transmit a shear force of $\sim 1 \mathrm{nN}$ per fully meshed tooth. At a gear rim speed $v=1 \mathrm{~m} / \mathrm{s}$, this corresponds to a transmitted power of $1 \mathrm{nW}$.

A prominent feature of Figures 10.25 and 10.26 is the presence of sharp dips in the barrier height at locations that depend both on $n$ and $s_{\text {gap }}$. Sharp dips in barrier height are a robust feature of a broad class of nanomechanical systems,

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-74.jpg?height=685&width=1109&top_left_y=1399&top_left_x=169)

Figure 10.25. Barriers for gear corotation (solid lines) and slippage (dashed lines) in the rigid coplanar ring model (Section 10.7.1a), for a range of between-ring separations $s_{\text {gap }}$ and several tooth-numbers $n$. Energies increase as matching rings are added.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-75.jpg?height=697&width=1107&top_left_y=168&top_left_x=267)

Figure 10.26. Barriers for gear corotation as in Figure 10.25, for $n=10$ and 50, modeling various torsional loads with varying values of between-ring rotational offset.

for reasons illustrated by the diagrams in Figure 10.27. For a single tooth, the energy is low (and nearly constant) before and passing through the meshing zone, and is high (and nearly constant) as it passes directly between the two gears (as in the potential energy curves shown in Figure 10.27). The potential energy of a gear (in the present model) is simply the sum of the nonbonded interaction energies of its teeth, occupying evenly spaced points along a suitable potential curve. When a single tooth, or a gap between a pair of teeth, is precisely between the two gears, the slope of the potential energy function is zero by symmetry [see (a) and (b) in Figure 10.27]. The potential is periodic (again by symmetry); in the sinusoidal approximation, the slope of the potential is maximal at position (c), halfway between (a) and (b). The slope of the bearing potential energy function at position (c) can be represented as the sum of the slopes at the points in diagram (d), folding points from the left side to the right, and giving them negative weights in the sum.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-75.jpg?height=357&width=801&top_left_y=1672&top_left_x=453)

Figure 10.27. Schematic illustration of the potential energies of gear teeth as a function of rotational angles (shoulders exaggerated). Diagrams (a) and (b) represent symmetrical positions, and (c) an intermediate position. Diagram (d) represents (c) with the left-hand points folded over and reversed in sign, to illustrate certain properties of the slope of the potential function with respect to gear rotation angle.

The sign of this slope depends on the positions and weights of the points on the shoulder of the potential curve. Where this shoulder is well away from the center (as it was not in Figure 10.2), changes in the spacing of the points, or in the position of the shoulder (e.g., by changing $n$ or $s_{\text {gap }}$ ), can readily change the sign of the slope. For a clear example, consider an interpoint spacing that places only one point in a region of high slope: by varying the parameters, points of either positive or negative weight can be placed in that position.

Finally, where state (c) is of zero slope, it becomes an extreme of the potential energy function, the spatial frequency of barrier crossing is doubled, and the barrier heights are greatly reduced (much as barrier heights are reduced by higher spatial frequencies in bearings). In moving along a curve like those in Figures 10.25 and 10.26, the energy difference between states like (a) and (b) in Figure 10.27 changes sign. A result of this sort can be expected in a wide range of circumstances.

b. Energy dissipation in gear contacts. The energy dissipation mechanisms in gears parallel those for sliding contacts on a surface (within the approximations already adopted). Acoustic radiation losses are small for most welldesigned gears. Relative to the figures used in Section 10.3.4, typical stiffnesses and compressive loads are anticipated to be $\sim 10$ times larger $(\sim 300 \mathrm{~N} / \mathrm{m}$, $\sim 10 \mathrm{nN}$ ), resulting in phonon scattering cross sections and thermoelastic effects $\sim 100$ times larger. The corresponding power levels (at a $1 \mathrm{~m} / \mathrm{s}$ interfacial rolling speed) are $\sim 3 \times 10^{-14}$ and $\sim 10^{-16} \mathrm{~W}$ for phonon scattering and thermoelastic drag, respectively. For a gear system operating at a shear force of $1 \mathrm{nN}$, these losses amount to $\sim 0.003 \%$ of the transmitted power.

c. Integrated bearings and gears. Gears of the sort discussed in this section require substantial compressive loads at the interface to ensure good meshing and stiff contact between teeth. In macroscale gearing this would be achieved (were it necessary) by means of loads transmitted through bearing surfaces on adjacent shafts. In nanomechanical gearing, however, the distinction between a gear interface and a bearing interface is chiefly a matter of relative interatomic spacings and curvatures of the opposing surfaces. The computational examples of bearings and gears in this chapter have used the same spacings and atom types on the convex surface of each interface, differing only in the nature of the opposed surfaces. Thus, a single surface can serve both roles, as in Figure 10.28,

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-76.jpg?height=506&width=564&top_left_y=1766&top_left_x=152)

Figure 10.28. Schematic diagram of two gears supported by bearing surfaces.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-77.jpg?height=362&width=769&top_left_y=193&top_left_x=443)

Figure 10.29. Schematic illustration of a roller between two race surfaces (one omitted), showing gearlike meshing of atomic rows.

and the required compressive loads can be transmitted to the housing structure by the gear surfaces themselves. In a system of this sort, symmetry constraints do not guarantee low values of $\Delta \mathcal{V}_{\text {barrier }}$, but tuning of the interface can readily be applied.

### 10.7.2. Helical gears

Gears can be constructed from concentric strained shells with opposing torsional shear deformations locked into each shell by bonding them together at the ends. The resulting structures can subject surface atomic rows to substantial helical deformations. Matching gear surfaces of this sort can be made to mesh more smoothly than spur gears of the same radius; in effect, $n$ is larger.

### 10.7.3. Rack-and-pinion gears and roller bearings

The principles of spur and helical gears are equally applicable when one of the toothed surfaces is flat (producing a rack-and-pinion gear system) or concave (as in planetary gearing). A gear without a shaft can serve as a roller bearing between two flat surfaces (Figure 10.29), or between two concentric cylindrical surfaces. The barrier to slippage in this instance need not be high enough to transmit large shear forces, but if it is sufficiently high to prevent thermally activated transitions, then a series of roller bearings can be made to keep a uniform spacing around the raceway without requiring a cage.

### 10.7.4. Bevel gears

Where the axes of two coplanar shafts intersect at an angle, power can be transmitted from one to another by means of bevel gears (essentially, rolling cones). In nanomechanical systems, the soft interactions of atomic teeth permit two noncoplanar rings of teeth to mesh essentially as well as coplanar rings; bevel gears with single-atom teeth thus present no special problem.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-01.jpg?height=386&width=688&top_left_y=193&top_left_x=375)

Figure 10.30. Surfaces for a matched pair of small bevel gears; light and dark circles represent protruding atoms (e.g., $\mathrm{F}$ ) and hollows (e.g., $\mathbf{N}$ termination sites) on a modified (111) surface.

Larger nanomechanical bevel gears, however, cannot be directly patterned on macroscale gears, owing to the impossibility of making atomic rows that converge smoothly (in spacing and steric radii) toward the tips of the cones. One alternative is to make bevel gears from conical surfaces with matching patterns of teeth and holes, without attempting to form rows like those in traditional bevel gears. The modified (111) surfaces in Figure 10.30, developed into cones, have this property; with a modest degree of strain ( $\sim 6 \%$ ), they can form cones having a $45^{\circ}$ half angle, suitable for shafts meeting at $90^{\circ}$. In small bevel gears based on this approach, the structure immediately beneath the surface must depart from that of a simple strained lattice, and the degree of achievable regularity is at present uncertain. Where all radii of curvature exceed $1 \mathrm{~nm}$, however, irregularities can be buried more deeply and the structural choices for those irregularities become ample to ensure solutions permitting low values of $\Delta \mathcal{V}_{\text {barrier }}$

# 10.7.5. Worm gears 

Worm gears combine characteristics of nuts and screws with those of gears to yield large gear ratios in a small package. A simple implementation combines a driven screw tangent to (and meshing with) the rim of a helical gear, creating an interface which has short-term fluctuations in potential energy driven by the sliding of the screw with respect to the gear surface, with superimposed long-term fluctuations driven by the meshing and unmeshing of helical teeth with the thread of the screw.

Where static friction is concerned, the low-frequency components are of relatively low importance, owing to the high gear ratio. Further, the smoothness properties of the low-frequency component resemble those of a spur (or more accurately, rack and pinion) gear system with a comparable number of teeth; these properties can be favorable even in the absence of mechanical advantage. The high-frequency components of the fluctuations in potential energy can be made to cancel (to a good approximation) given suitable choices of gear geometry and compressive load, but the analysis is complicated by the superimposed rotation of the helical gear.

### 10.7.6. Belt-and-roller systems

In engineering practice, tension members stretched over rotors commonly are used to transmit either materials or power (or both). Examples include conveyor belts moving over rollers, drive belts moving over pulleys, and chain drives moving over sprockets.

In nanomechanical structures, surfaces commonly have periodicity like chains and sprockets; accordingly, it is natural to design devices in such a way that belts and rollers mesh. The meshing and unmeshing of a belt and roller then locally resembles the meshing and unmeshing of a rack and pinion, and values of $\Delta \mathcal{V}_{\text {barrier }}$ can have parallel behavior. A significant difference is that the larger region of contact (where the belt wraps around the roller) decreases the required contact pressure and areal stiffness for a given interfacial shear load, and this, in turn, decreases thermoelastic damping and phonon scattering. The discussion in following chapters assumes that the dominant energy dissipation mechanism is shear in the bearing interface of the roller.

The meshing of bumps on rollers and belts can excite resonant transverse vibrational modes in the belts. For example, in a belt with a length of $20 \mathrm{~nm}$ and a ratio of tension to linear mass density equal to that of diamond under a tensile stress of $10 \mathrm{GPa}$, the transverse wave speed is $\sim 1.7 \times 10^{3} \mathrm{~m} / \mathrm{s}$, and the frequency of the lowest normal mode is $\sim 1.3 \times 10^{11} \mathrm{rad} / \mathrm{s}$. If bumps on the rollers have a spacing $d_{\mathrm{a}}=0.25 \mathrm{~nm}$, then the lowest resonant belt speed is $\sim 5 \mathrm{~m} / \mathrm{s}$. Operation of equipment between (rather than below) resonant modes is common practice in macroscale engineering, but requires attention to start-up dynamics as resonant conditions are traversed; nanomechanical engineering is no different in this regard.

Belt-and-roller devices play a central role in the mechanochemical systems discussed in Section 13.3, providing for molecular conveyance and reactive encounters. It might seem that mechanical conveyance must consume more energy than spontaneous diffusion in the solution phase, but motions in eutactic systems can in fact be more efficient than comparable motions in disordered systems. The entropic free-energy cost of diffusive transport down a concentration gradient is exactly the same as the free-energy cost of the work required to force the molecules to move through the liquid at the same mean velocity against the resistance of viscous drag. Belts in vacuum move molecules more efficiently.

### 10.7.7. Cams

In a cam mechanism, a contoured surface moves beneath a follower, and its bumps and hollows cause the follower to rise and fall. This provides a way of deriving complex follower motions from a simple motion of the cam surface, and is thus of broad usefulness in mechanical design.

A contoured surface can be constructed (conceptually, as distinct from mechanosynthetically) as a thin slab of diamond distorted by a buried array of dislocations. The resulting surface can be reasonably smooth and regular, save for the irregularities necessitated by the contour itself.

A follower can either slide or roll over the cam surface. Owing to the irregularity associated with the varying slope (and elastic strain) of the cam surface, the principles discussed in Sections 10.3 through 10.5 do not guarantee that a follower can be designed to slide with low energy barriers. A follower surface that is left free to pivot, thereby keeping it flat to the cam surface, could in some instances reduce the effect of these irregularities. A structure with a region of sliding contact that is wide but short (in the sliding direction) should permit the
design of cam surfaces with irregularities that sum to a smooth potential; this appears attractive where the cam surface contour must change slope substantially over small distances. Finally, many cam surfaces based on distorted crystals are compatible with a rolling follower having smoothly meshing teeth and low energy barriers.

### 10.7.8. Planetary gear systems

Planetary gears can be used to convert shaft power from one angular frequency to another in a stiff colinear mechanism. Figure 10.31 provides a schematic illustration; Figure 10.32 shows the first such mechanism that has been designed in atomic detail (several earlier designs were unstable: energy minimization extruded the gears and produced only wreckage). This design and the following analysis results from a collaboration with R. Merkle.

If the planets are to be arranged symmetrically, the structure must meet the condition

$$
\begin{equation*}
n_{\text {outer }}=i n_{\text {planets }}-n_{\text {inner }} \tag{10.29}
\end{equation*}
$$

where $n_{\text {outer }}$ is the number of teeth in the outer ring gear, $n_{\text {inner }}$ is the number of teeth in inner sun gear, $n_{\text {planets }}$ is the number of planet gears, and $i$ is an integer (note that the number of teeth on a planet gear does not appear in this relationship). A quantity that correlates with the smoothness of the potential energy as a function of rotation is the number of distinct orientations $m$ of the planet gears with respect to the radius vector

$$
\begin{equation*}
m=n_{\text {planets }} / \operatorname{gcd}\left(n_{\text {planets }}, n_{\text {inner }}\right) \tag{10.30}
\end{equation*}
$$

Where the number of teeth per planet is small, a large value of $m$ is desirable. In the mechanism illustrated in Figure 10.32, $n_{\text {inner }}=16, n_{\text {planets }}=9$, and $n_{\text {outer }}=29 ; m$ has its maximal value, $m=n_{\text {planets }}=9$. The planet gears have 6

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-03.jpg?height=521&width=704&top_left_y=1503&top_left_x=384)

Figure 10.31. Schematic diagram of a planetary gear (end view). Fast rotation of the sun gear drives slower rotation of the planet carrier, if the ring gear is held fixed. In general, either the sun gear, the ring gear, or the planet carrier can be held fixed, imposing a constraint on the relative motion of the other two components.
![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-04.jpg?height=498&width=1022&top_left_y=216&top_left_x=328)

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-04.jpg?height=451&width=388&top_left_y=768&top_left_x=327)

(c)

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-04.jpg?height=495&width=179&top_left_y=756&top_left_x=750)

ring gear $1 \mathrm{~nm}$

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-04.jpg?height=202&width=371&top_left_y=905&top_left_x=965)

sun gear

3,557 atoms

Figure 10.32. A planetary gear, (a) end view, (b) side view, (c) exploded view. The ring gear structure is a strained $\mathrm{Si}$ shell with $\mathrm{S}$ termination; the sun gear is a special-case structure related to an O-terminated (100) diamond surface; the planet gears resemble multiple hexaasterane structures with $\mathrm{O}$ (rather than $\mathrm{CH}_{2}$ ) bridges between the parallel rings; view (c) retains elastic deformations occurring in (a), hence gears are bowed. The planet carrier is adapted from the structure shown in Figure 9.10, and linked to the planet gears using $\mathrm{C}-\mathrm{C}$ bonded bearings (Section 10.6.1). These bonded linkages are visible in (b). This design results from a collaboration with R. Merkle at the Xerox Palo Alto Research Center; energy minimization was performed using the Polygraf molecular modeling software (Polygen Molecular Simulations, Inc., Waltham, MA).

teeth, hence a motion of the system that carries a planet gear through $1 /(6 \cdot 9)=$ $1 / 54$ of a full rotation is a symmetry operation for the potential energy function.

### 10.8. Barriers in extended systems

In a typical nanomechanical subsystem, a series of components is mechanically coupled, moving as a nearly rigid unit with respect to some motion coordinate $q$. Examples include rotating shafts supported by multiple bearings, sliding rods moving over multiple surface regions, and sets of shafts and rods linked by gearing. In each case, where the local negative stiffnesses of energy barriers in the
components are small compared to the positive stiffnesses of the structures linking those components, the energy barriers for the system as a whole are not those resulting from the potentials of the components taken individually, but those resulting from the sum of the component potentials with respect to $q$. In systems of this sort, the overall barriers are bounded by the sum of the component barriers, but can be much lower if nearly sinusoidal contributions from different components have the same period and are made to cancel.

More generally, a coupled subsystem of this sort can commonly be extended by adding a tuning component that undergoes simple linear or circular motion in an environment with no function save that of adjusting the overall subsystem potential. Using levers or gears, the ratio of physical displacements in the tuning component to those found elsewhere in the subsystem can be made $\geq 1$, and therefore the characteristic frequencies (with respect to $q$ ) of interactions between moving and stationary surfaces in the tuning component can be made greater than or equal to those in the subsystem as a whole. (Note that the high spatial frequencies resulting from special symmetries are associated with low barriers, and hence seldom motivate the introduction of a tuning component.)

### 10.8.1. Sliding of irregular objects over irregular surfaces

One class of tuning component could be used to smooth the potential associated with the sliding of an irregular object over an irregular surface, for example, a rod with irregular features sliding in a sleeve with irregular features. There is no obvious procedure for choosing object irregularities so as to result in a nearly constant potential at all displacements with respect to a given irregular surface; in general, there is some fluctuating potential $\mathscr{V}(q)$. Given that $\mathscr{V}(q)$ does not result in excessive negative stiffnesses, however, a tuning component can be introduced (Figure 10.33) in which one or more atoms on the moving part interact with an irregular surface shaped so as to provide a compensating potential $\mathscr{V}^{\prime}(q) \approx-\mathscr{V}(q)$.

This design task is feasible if each strip of the fixed surface of the tuning component interacts with only one moving atom. Each such moving atom can interact strongly with several stationary atoms at each point, and $\mathcal{V}^{\prime}(q)$ can be generated as a sum of the interactions of an indefinitely large number of moving atoms. Multiple strips of interacting atoms in a system of this sort suffice to provide (1) an indefinitely large energy range for ${ }^{\prime}{ }^{\prime}(q),(2)$ multiple, independent contributions to $V^{\prime}(q)$ in each atomic-scale range of $q$, permitting fine control of its magnitude, and (3) control of $\mathscr{V}^{\prime}(q)$ with a spatial resolution comparable to that of the features in $\mathscr{V}(q)$. This provides sufficient freedom to design systems with $\mathscr{V}^{\prime}(q) \approx-\mathscr{V}(q)$.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-05.jpg?height=215&width=663&top_left_y=1943&top_left_x=397)

Figure 10.33. Linear representation of irregular surfaces sliding over one another.

### 10.9. Dampers, detents, clutches, and ratchets

The previous sections of this chapter focus on components that can move with smooth or flat potential energy functions (implying low static friction), and with low energy dissipation. Macroscale engineering practice demonstrates the utility of components with properties quite different from these, which are briefly discussed here.

### 10.9.1. Dampers

Dissipation of energy (e.g., vibrational energy) is often desirable in a dynamical system, and can be accomplished in various ways in nanoscale systems. Stiff, interlocking siding interfaces with large values of $R$ and $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}$ (Section 7.3.5) can exhibit relatively large phonon drag (although the models developed here should not be used to estimate this drag, since they are expected to be conservative when drag is to be minimized, not maximized). Alternatively, interfaces with short, flexible protrusions (e.g., $-\mathrm{C} \equiv \mathrm{C}-\mathrm{H}$ ) can be designed such that the protrusions hop from one potential well to another as they slide over a facing surface; this can provide substantial damping together with a threshold shear strength for the interface. Energy release per transition must be limited to avoid damage from vibrational stresses. Other linear and nonlinear damping devices can be developed based on the energy dissipation mechanisms described in Chapter 7.

### 10.9.2. Detents

Violations of the design principles for bearings result in devices with relatively deep potential wells along some motion coordinate. These devices can serve as detents, snap fasteners, and the like. One class of devices resembles a sleeve bearing with a moderately large value of $\operatorname{lcm}(n, m)$, but with flexible protrusions bearing the interfacial load. For a proper choice of (positive) bending stiffness and (negative) interaction stiffness between a protrusion and the opposite surface, the protrusions will approach flexural instability as they move from one potential well to the next, and the single-protrusion potential at that point can have arbitrarily high spatial frequency components, relative to the overall rotational coordinate of the device. The result can be a system with $\operatorname{lcm}(n, m)$ equally spaced potential wells, where $\operatorname{lcm}(n, m) \gg n$ or $m$.

### 10.9.3. Clutches

The depth of the potential wells encountered as one surface moves past another depends on their relative positions and the magnitude of the interfacial load. Where two complementary, gearlike surfaces can be pressed together or separated under the control of one subsystem, while one of them moves in an orthogonal degree of freedom under the control of another subsystem, the result is a clutch. As in standard engineering practice, clutches can be used to couple and decouple mechanisms and power sources. The design of such devices is constrained by the potential for excessive stresses or energy dissipation during coupling.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-07.jpg?height=258&width=640&top_left_y=182&top_left_x=404)

Figure 10.34. Schematic diagram of a ratchet-and-pawl mechanism able to move more easily to the right than to the left under the influence of applied force. Thermal excitation does not constitute an applied force, and the asymmetry of the interface does not bias the direction of thermal hopping.

### 10.9.4. Ratchets and reversibility

Ratchet mechanisms typically are based on an asymmetric, spring-loaded contact that can resist a large applied force in one direction, yet permit relatively free motion in the other (Figure 10.34). These can readily be implemented on a nanoscale, given suitable teeth and a force (whether from a spring or other source) large enough to make thermally activated hopping rare.

It may be tempting to think that a nanoscale ratchet mechanism would exhibit biased motion purely as a result of thermal excitation, but it cannot. A mechanically-driven motion in one direction may be blocked, but the energy barriers are the same in both directions. In terms of the PES, asymmetries of shape do not destroy the symmetry of detailed balancing (Section 4.3.3a): at equilibrium, transitions in one direction always occur at the same rate as those in the other. A ratchet with biased thermal motion could steadily extract useful work from a heat reservoir at a single temperature, in violation of the second law of thermodynamics.[^29] Thermally excited ratchets are discussed in (Feynman et al., 1963).

### 10.10. Perspective: nanomachines and macromachines

Macroscale machines are familiar; their properties shape our intuitive sense of what machines are and how they work. Accordingly, it is useful to compare and contrast them with nanomachines, both to encourage free use of sound analogies and to warn of crucial differences.

### 10.10.1. Similarities between nanomachines and macromachines

The similarities between nanomachines and macromachines are pervasive and fundamental. At the analytical level, systems of both kinds can be described by applying classical mechanics to objects that occupy space, exclude other objects from that space, and resist deformation. At the design level, systems of both kinds must apply forces, guide motions, limit friction, and so forth.

As this chapter illustrates, nanoscale components can serve functions familiar in the macroscale world. Because functions at the system level can usually be implemented in many different ways at the component level, the parallels between macro and nanoscale systems can be even stronger than those between their components. Accordingly, many of the lessons of macroscale mechanical engineering can be applied directly. When nanomechanical designs are drawn at a scale and resolution that omits atomic detail, they can be almost indistinguishable (save for dimensioning labels) from designs for macromachines.

### 10.10.2. Differences between nanomachines and macromachines

Macroscale machines can be made of many different materials and parts, but many consist chiefly of steel and a lubricant; these suffice to build gears, bearings, drive shafts, cams, and so forth. Lubricated steel systems are accordingly taken as the basis for comparison in this section.

a. Soft surfaces, different frictional behavior. On a macroscopic scale, steel surfaces are hard: objects have well-defined boundaries, and any attempt to force a geometric overlap between two steel objects instead results in contact forces and elastic or plastic deformation. On a nanometer scale, diamondoid surfaces are soft: if one defines object boundaries by (for example) assigning radii to the surface atoms, the repulsion forces will increase smoothly as the objects approach and overlap. This nonlinear surface compliance is distinct from (and additive with) the compliance from elastic deformations of the objects, and has a characteristic length scale of $\sim 0.03 \mathrm{~nm}$. This length is small enough to make the concepts of "shape" and "surface" useful, yet large enough to bar the direct and uncritical application of macroscopic concepts.

Because of these surface properties, nanoscale components need not meet precise dimensional specifications to achieve a good fit. Centimeter-scale steel components commonly are designed to tolerances less than 0.001 of their linear dimensions. For a nanometer-scale component, a fractional deviation of $\leq 0.01$ from a hypothetical ideal is insignificant, and a deviation of 0.03 or more is often acceptable. This tolerance for deviations from ideal geometries helps compensate for the discrete nature of nanomechanical structures, and for the consequent unavailability of a continuum of sizes and shapes.

As a result of these surface properties, nanomechanical components are better viewed as moving smoothly in a force field than as sliding subject to friction. Static friction (in the conventional sense) does not exist in well-designed eutactic bearings: its closest analogues-energy barriers and force gradients-can be lower for two coupled objects sliding over a surface than for either object considered separately (Section 10.8), even though their contact forces are additive. This is alien to the familiar tribology of disordered interfaces. These interfacial properties make distinct lubricating substances needless and harmful (an oil molecule is not a lubricant on this scale: it is an object).

b. No wear, no contaminants. In macromachines with sliding or rolling interfaces, cumulative wear commonly limits device lifetimes. The strong, precise surfaces of nanomachines, in contrast, experience no change in a typical operational cycle, and hence no wear. Within the single-point failure model (Section 6.7.1a), the first step in a wear process is regarded as fatal, and hence cumulative wear plays no role in determining device lifetimes.

In macromachines, wear particles often contaminate lubricants, accelerating wear. In eutactic nanomachines, contaminants of all kinds are rigorously excluded and the equivalent of wear particles cannot appear until the device has failed. Accordingly, contaminants are not found in devices operating within the guidelines assumed here. (The design of devices that tolerate contamination is relatively complex; Section 13.2 touches on this subject in discussing the purification of feedstocks for molecular manufacturing.)

c. No fatigue, tolerance of high strains. In a typical load cycle, a welldesigned nanomechanism undergoes no structural change. As with wear, the single-point failure assumption implies that devices are not subject to cumulative damage before failure, hence cumulative fatigue plays no role in determining device lifetimes (Section 6.7.1a).

Conventional macroscale structures contain numerous defects (e.g., dislocations) of varying mobility. Even a slight load usually moves some of these defects (or biases their thermally activated diffusion), causing slight plastic deformation. Eutactic nanomechanisms need not have defects of significant mobility, and hence can entirely escape plastic deformation and resulting fatigue. Conventional steel mechanisms commonly operate for years with cycle frequencies of 1 to $100 \mathrm{~Hz}$, with stresses chosen to avoid fatigue failure. Diamondoid nanomechanisms can operate for years at $>10^{9} \mathrm{~Hz}$, executing many more cycles.

Few steel objects can tolerate deformations as large as 0.01 without substantial plastic flow. Some diamondoid structures, in contrast, can tolerate deformations $>0.1$ without plastic flow or fatigue. Accordingly, nanomechanical devices relying on the repeated, large-amplitude elastic deformation of strong, stiff components are practical, though their macroscale analogues would promptly fail. Exploiting large elastic strains can further relax constraints on component dimensions, where parts can stretch to fit. Further, components locked together by mechanical interferences (e.g., the bearing in Figure 10.17) can often be assembled via strained intermediate geometries. Where elastic deformation is concerned, typical diamondoid structures act more like an extremely stiff elastomer than like a ductile metal.

d. Insensitivity to parts count. The cost and reliability of conventional macromachines depends strongly on the number of parts they contain. To make a part, surfaces must be shaped; to use a part, it must be assembled to other parts. These steps add costs and potential defects. In operation, most moving parts have interfaces subject to wear, decreasing reliability. Good design practice in macroscale engineering aims to minimize parts count.

The reliability and fabrication cost of nanomachines will be almost independent of the number of mechanical parts they contain. In molecular manufacturing, the number of assembly operations is roughly proportional to the number of atoms in the product, and hence roughly proportional to the mass. Costs will be insensitive to the number of nonbonded interfaces in the product, and hence insensitive to the number of separate mechanical parts. If the design follows the principles and analytical assumptions outlined in Section 6.7.1b, component lifetimes are determined by radiation damage, and hence (approximately) by mass; this again is independent of the number of separate parts. (Component interiors
are somewhat less sensitive to damage than component surfaces, but the resulting incentive to reduce the number of parts-here, merely to reduce the total area of interfaces-is weak compared to that in conventional engineering.)

### 10.11. Bounded continuum models revisited

As discussed in Section 9.5, diamondoid components can approximate any desired shape, so long as strong precision and symmetry requirements are not imposed, and so long as features either have a specified structure or dimensions $\geq 1 \mathrm{~nm}$. Further, the mechanical properties of these components can approximate those of diamond, save for a surface correction to the effective component size (to allow for the difference between nonbonded and covalent radii), and degradation of stiffness by a factor no worse than 0.5 , to account for less dense arrays of bonds, the use of second-row elements, and the like. Finally, so long as one of the conditions for smoothly sliding or rolling interfaces holds (Sections 10.3 to 10.5), smooth motion may be assumed. These generalizations permit the use of bounded continuum models in the design of a certain range of structures.

Within a bounded continuum model, as in the bulk-material models used in mechanical engineering, design work can proceed without reference to the positions of individual atoms. In nanomechanical engineering, the production of devices requires atomically detailed specifications, but-if one is willing to accept a performance penalty resulting from conservative assumptions regarding size, stiffness, and so forth-this specification process can in many instances be postponed to a phase relatively late in the design process. Models of this sort are used for much of the analysis in the following chapters.

### 10.12. Conclusions

Both sliding and meshing interfaces can be constructed in various nanoscale geometries, as can interfaces with intermediate properties and specially tailored potential energy functions along a sliding coordinate. As a consequence (and together with more elementary devices, such as springs), it is feasible to construct nanomechanical rotary bearings, sliding shafts, drive shafts, screws and nuts, power screws, snaps, brakes, dampers, worm gears, constant-force springs, roller bearings, levers, cams, toggles, cranks, clamps, hinges, harmonic drives, bevel gears, spur gears, planetary gears, detents, ratchets, escapements, indexing mechanisms, chains and sprockets, differential transmissions, Clemens couplings, flywheels, clutches, Stewart platforms, robotic positioning mechanisms, and suitably adapted working models of the Jacquard loom, Babbage's Difference and Analytical Engines, and so forth.

The analysis presented in this chapter does not establish that all classes of sliding-interface bearing are feasible in the nanometer size range. For example, a smoothly sliding ball-and-socket joint requires a potential energy function that is smooth with respect to three rotational degrees of freedom; neither the symmetry properties exploited in Sections 10.3 and 10.4, nor the tuning approaches discussed in Section 10.8 guarantee that this can be accomplished in a stiff, nanoscale device. (Note that most properties of a ball-and-socket joint can be provided by a Hooke joint.)

The conclusions of Sections 10.3 and 10.8 support the extension of bounded continuum models to the design of moving parts and their interfaces. As discussed in Section 9.5, diamondoid components with dimensions $\geq 1 \mathrm{~nm}$ can be of almost any desired shape. These components can be assumed to have smoothly sliding interfaces so long as one of the conditions established in this chapter holds. These conditions include either (1) translational or rotational symmetry in one component and adequate size and design flexibility in the other (Section 10.3), (2) suitable symmetry properties in both components (Sections 10.4 and 10.5), or (3) the ability to couple an interface with a given irregular potential to another with a designed and compensating irregular potential (Section 10.8). Energy dissipation can be estimated using the methods of Chapter 7. With this extension, bounded continuum models can provide a basis for the analysis of conservatively designed nanomechanical systems specified in less than atomic detail.

Some open problems. The most immediate open problems associated with mobile nanomechanical components are chiefly those of design. Devices of several classes have been described and abstractly characterized in this chapter, but examples specified in atomic detail are sparse. It would be useful to have a large set of examples spanning many different classes, and to characterize those examples in detail (e.g., considering all plausible instabilities, measuring stiffness in all important degrees of freedom, and so forth), including studies of the sensitivity of device properties to variation in the assumed potential energy function. (The particular structures used in this chapter to illustrate desirable geometries and intercomponent potential energy functions may prove defective in other respects, but alternatives are abundant.) Software like Merkle's diamond-tube generating package can greatly help in this work, and should be developed and extended. Beyond this, the design of devices and their integration into mechanical systems using existing chemistry-oriented molecular modeling software can better define requirements for nanomechanical CAD systems, and can better define the objectives of mechanosynthesis. Eventually, one would like to have a large library of specifications for well-characterized components, procedures for designing systems that use those components, and procedures for specifying mechanosynthetic sequences to construct such systems. Although there are many easy and rewarding steps toward this objective, reaching it will require an enormous amount of work, both in nanomechanical design and in software development.

[^24]: The two conditions compatible with zero energy dissipation are zero sliding resistance and zero slip. Interfaces with smooth potentials can approximate zero resistance at low sliding speeds; interfaces with strongly corrugated potentials can exhibit zero slip (though the interface deforms and other energy dissipation mechanisms intervene).
[^25]: The concept of spectral density stems from the analysis of waves carrying power. The power spectral density of a radio transmission, for example, measures its power per unit frequency-range (substantial in a narrow band of radio wavelengths, negligible at $x$-ray wavelengths), and can be derived from the time-domain shape of the emitted electromagnetic wave by Fourier transform methods. These methods are equally applicable to functions in the spatial domain, but the resulting "power spectral density" has a purely nominal relationship to power. An amplitude spectral density is proportional to the square root of a power spectral density. Because only ratios of values are considered here, units for these quantities are omitted.
[^26]: This discussion implicitly assumes that modification of surface sites does not make compatible-framework structures incompatible. Strains introduced by modifying the sliding surface will have little effect on the constrained surface if the separation is adequate ( $\sim 1 \mathrm{~nm}$ ), and if the modifications do not cause large net tensile or compressive stresses. These conditions will often be met. Where they are not, the conversion of compatible to incompatible structures by distortions induced by surface modification will, in typical design problems, be balanced statistically by the conversion of incompatible structures to compatible structures by similar distortions. In circumstances where this is significant, however, the task of designing a sliding surface cannot be treated separately from the task of designing a compatible framework.
[^27]: A bearing interface can support a net tensile load yet retain a positive stiffness.
[^28]: Conventional springs, in which force is approximately proportional to displacement, can be implemented in many ways. Most stable diamondoid structures (as well as many rod and cage structures of lower compliance and less diamondlike structure) are perfectly elastic, save for energy dissipation mechanisms that depend on the speed of deformation.
[^29]: If this could be done by a mere molecular ratchet, the complex machinery of photosynthesis and digestion might never have evolved.