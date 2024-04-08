# Intermediate Subsystems


### 11.1. Overview

Between the simple components described in Chapters 9 and 10 and the complex systems described in Chapters 12-14 are subsystems of intermediate complexity. These subsystems find use in more complex systems, but are worthy of a separate description.

Section 11.2 describes mechanical measurement devices; these are useful in signaling (Section 16.3.2), in mechanical logic systems (Chapter 12), and in ${ }^{\circ}$ fault-tolerant molecular manufacturing systems (Section 13.3.6b). Section 11.3 describes stiff, high gear-ratio mechanisms suitable for use in molecular manipulation systems (Section 13.4.1). Section 11.4 surveys the principles of fluid flow in small volumes, then describes a set of components and subsystems for handling fluid flow: seals, valves, and pumps, including vacuum pumps. Section 11.5 describes systems using branched pipes for high-capacity convective cooling. Section 11.6 surveys the principles of electrical current flow in small conductors, then describes electromechanical devices including modulated tunneling junctions and electrostatic actuators. Section 11.7 describes direct-current (DC) electrostatic motors and generators.

### 11.2. Mechanical measurement devices

Mechanical measurement systems can latch an indicator into one of two or more distinct positions, making the position chosen depend on (or correlate with) some feature or property being measured. Two limiting cases of mechanical measurement (among others) are measurement of force and of shape. With suitable transducers, measurements of magnetic field, electric field, and pressure can be transformed into measurements of force. Measurements of conditions imposed from the outside (e.g., pressure resulting from acoustic waves, Section 13.3.6b) can be used as a means of receiving signals. Measurements of shape (or position) can discriminate among the internal states of a system, for example, in order to detect defective products in a manufacturing system. They can likewise be used to discriminate among external states, for example, in characterizing molecular structures in a biological context. Chapter 13 describes the use of shape measurements to detect errors in manufacturing.

This section does not attempt to describe measurement devices of optimal size, reliability, and so forth. It merely illustrates some basic approaches, and some conditions under which they enable good reliability. Of the wide variety of methods that might be used, only processes based on direct mechanical measurement of indicator displacements are discussed.

### 11.2.1. Well partitioning and indicator latching

Measurement systems of the sort considered here latch an indicator as shown in Figure 11.1. Latching is usually necessary if the measurement must represent the state of a time-varying measured system at a particular moment, or if the position of the indicator is subject to substantial thermal motion. The following will consider a latching mechanism that makes a binary distinction, but generalizations to more locations are straightforward.

An indicator moves in a potential well, driven by thermal excitation. Section 10.8.1 shows that the potential energy of an object sliding over a surface can be made nearly flat, or can be given more complex contours subject to resolution limits stemming from the finite scale lengths of interatomic potentials. A well can be partitioned by introducing an energy barrier; concretely, this can be accomplished by inserting a physical barrier that obstructs the motion of an atomically wide feature on the indicator. The resulting latched position of the indicator can then determine subsequent mechanical behaviors, most generally, by providing an input to a computational system (Chapter 12).

In the logic rod systems described in Section 12.3, each rod can be regarded as making a measurement of the position of the rod (or register) in the preceding stage, yet latching is unnecessary. All changes in state are sequenced by a clocking mechanism, the state of the measured system is stable for the duration of the measurement, and thermal displacements are small. Latching is, however, required in registers (Section 12.4), which must display the results of a measurement after the measured system has been reset.

At high speeds $\left(\sim 10^{-9} \mathrm{~s}\right.$ per operation) the energy cost of well partitioning is likely to be dominated by nonisothermal compression losses (Section 7.5). When the wells are later merged, further losses can occur if the input signal has changed (well merging losses are treated in Section 7.6.2). If the input has not

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-13.jpg?height=275&width=910&top_left_y=1742&top_left_x=290)

Figure 11.1. Well partitioning in a measurement system. Each curve represents the potential energy of the indicator as a function of its sliding displacement; the shading represents the probability density over that range of motion. In (1), the potential is flat, and the PDF is uniform. In (2) an applied force has skewed the potential and the PDF. In (3), a barrier has been introduced, trapping the indicator on the right hand side with high probability as a direct consequence of the presence of the applied force.

changed, then well merging is simply the reverse of well partitioning, and can be nearly thermodynamically reversible (save for further nonisothermal losses).

### 11.2.2. Force discrimination

A force can push an indicator toward one end of a potential well; a bias force can push it toward the other. In a system intended to distinguish between two forces differing by $\Delta F$, a typical bias force might have a magnitude of $\Delta F / 2$. If the length of the potential well is $\ell$, then the probability of an erroneous measurement is

$$
\begin{align*}
P_{\mathrm{err}} & \approx \frac{\exp (-\ell \Delta F / 4 k T)-\exp (-\ell \Delta F / 2 k T)}{1-\exp (-\ell \Delta F / 2 k T)}  \tag{11.1}\\
& \approx \exp (-\ell \Delta F / 4 k T), \quad \text { if } \exp (-\ell \Delta F / 4 k T) \ll 1
\end{align*}
$$

where the chief approximations are (1) that under an applied force of $-\Delta F / 2$ the well is square and uniform, and (2) that the partitioning process divides the well in the middle before disturbing the initial probability density function. (The nodisturbance assumption overestimates the error rate; the effect of the squareness assumption depends on the definition of $\ell$.) For $\ell=1 \mathrm{~nm}, \Delta F=1 \mathrm{nN}, P_{\mathrm{err}} \approx$ $6 \times 10^{-27}$ at $300 \mathrm{~K}$.

More generally, the magnitude of the bias force can be chosen to minimize the cost of errors, given differing costs for reading "high" when the sensed force is low vs. reading "low" when the sensed force is high. A well that is deeper at the ends (creating subwells) can reduce error rates, so long as the intervening barrier does not substantially impede equilibration of the subwells. Multivalue measurements are best made by partitioning a more nearly parabolic well.

### 11.2.3. Shape and position discrimination

The position of an indicator structure can be coupled to the position of a probe resting against a surface. If the probe and indicator are parts of a lever, small probe displacements can cause large indicator displacements; levers can thus be used to avoid scale-length problems in measuring probe displacements that are small compared to an atomic diameter.

A typical small difference in surface position is $\sim 0.1 \mathrm{~nm}$; a typical probe load is $\sim 2 \mathrm{nN}$; a typical stiffness associated with contact of the probe tip is $\sim 50 \mathrm{~N} / \mathrm{m}$ (allowing for some compliance in the probed surface itself). A rough estimate of the error rate in partitioning an indicator well that corresponds to a probe displacement distance of $0.1 \mathrm{~nm}$ is $\sim 10^{-5}$. For many purposes, error rates of this magnitude are unacceptable.

### 11.2.4. Reliability through iterated measurements

For weak forces and small displacements, and for small differences in shape and position, thermal excitation can render individual measurements unreliable. Iterated measurement processes can be devised, however, that correspond to incrementing a counter by one with each positive measurement, while decrementing it by one with each negative measurement. A series of these operations, followed by a measurement of the state of the counter, provides a measurement procedure that can reduce overall error rates to any desired level.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-15.jpg?height=396&width=779&top_left_y=241&top_left_x=339)

Figure 11.2. Cross sectional diagram of a harmonic drive. One revolution of the wave generator in the indicated direction causes the flexspline to turn in the opposite direction with respect to the stiff circular spline, moving it by a two-tooth increment.

### 11.3. Stiff, high gear-ratio mechanisms

Reliable positioning of parts in the presence of thermal excitation requires drive mechanisms of high stiffness. If these are to be powered by mechanisms of lower stiffness, then they must have high gear ratios. Both harmonic drive and toroidal worm drive subsystems can meet these requirements.

### 11.3.1. Harmonic drives

Some macroscale robots use harmonic drives as stiff, high gear-ratio mechanisms. Figure 11.2 illustrates the structure of a harmonic drive: the basic kinematics are those of a pair of dislocations moving along an interface bent into a cylinder, with the dislocation motions driven by the rotation of a wave generator, which in turn deforms a flexspline. Each rotation of the wave generator turns the flexspline by a two-tooth increment relative to the surrounding gear surface.

Harmonic drives are well suited to nanomechanical systems. Diamondoid materials have large elastic limits, enabling them to accommodate the required deformation of the flexspline. Any of several kinds of gear teeth (Section 10.7.1) can be used, and those that can operate without a substantial compressive load across the interface (e.g., by exploiting a bonding interaction) can impose lower loads on the stiff circular spline.

### 11.3.2. Toroidal worm drives

Another class of stiff, high gear-ratio mechanism is the toroidal worm drive. Since the toroidal worm drive as described here exploits unique properties of nanomechanical structures, it may be novel; since it has so few moving parts, however, it may well be described in some form in the existing literature.

A toroidal worm drive is built around a triply-threaded torus (illustrated in Figures 11.3 and 11.4). The torus would, if cut and allowed to relax, take the form of a straight rod. The inverting rotational motion shown in Figure 11.3 can occur essentially without energy barriers, since a small displacement in this mode is (in a good structure) a symmetry operation for the potential energy function. A structure of this sort is more practical here than in conventional engineering,

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-16.jpg?height=389&width=854&top_left_y=201&top_left_x=403)

Figure 11.3. Overall geometry of the triply-threaded torus of a toroidal worm drive, showing one set of threads and the inverting rotation (resembling that of a smoke ring) imposed on the torus. With a suitable choice of major and minor radii, the substantial strains occurring during this motion fall well within the elastic limit of diamondlike structures; cyclic strains will not cause fatigue (Section 6.7.1a). A similar design with conventional materials on a macroscopic scale would present serious difficulties.

owing both to the availability of strong, stiff materials having high elastic limits (strains >0.2), and to the feasibility of constructing rings that both relax to a straight rod if cut, and have no seams resulting from bending and joining. Figure 11.5 illustrates and discusses the structure of a triply-threaded torus in more detail. Figure 11.6 shows the components of a toroidal worm drive in cross section; its caption summarizes the kinematics of the device. The structure and dimensions of the torus must, of course, be chosen to avoid excessive strains; $J$. Soreff has suggested discontinuous designs with similar kinematics that avoid this constraint.

The energy barriers to the inverting rotation of a torus in an intersegment groove can be analyzed using the symmetry and spatial-frequency principles of Sections 10.4 and 10.5. Each segment of the torus is an object of low symmetry, and turns in an environment of low symmetry. Good design practice can readily avoid large, abrupt energy barriers by avoiding bad steric contacts in the sliding interfaces, but the resulting potential energy function will almost inevitably

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-16.jpg?height=478&width=686&top_left_y=1611&top_left_x=494)

Figure 11.4. Geometry of the driven and driving threads of the triply-threaded torus of a toroidal worm drive. The angles chosen for these threads are purely illustrative; in practice, angles can be chosen to provide the desired mechanical advantage for the drive system. The retaining grooves (not shown; see Figure 11.3) cut across this pattern.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-17.jpg?height=446&width=777&top_left_y=192&top_left_x=340)

Figure 11.5. A more detailed (but still schematic) illustration of two segments of a triply-threaded torus. The driving threads are formed by rows of atoms alternating with grooves; interfacial structures might resemble Figure 10.18. The driven threads are shallower, formed by the alignment of rows of atoms and shallow interatomic gaps in a direction roughly perpendicular to that of the driving threads. These features can be formed from a helical variant of one of the structures discussed in Section 10.4.7a; the angle of the driven threads can be determined by a suitable choice of the locked-in torsional strain of the torus. The final set of threads, forming the retaining grooves, fall at an angle to the natural lattice orientation of the structures just described, and hence have (at best) low-order symmetry with respect to the inverting rotation.

exhibit substantial residual fluctuations, which are periodic in the invertingrotation coordinate. A series of segments, however, forms a coupled system that can readily meet the conditions described in Section 10.3 .6 for treating the energy barriers using the rigid-coupling approximation. With a favorable choice of structural parameters, each segment has a different phase angle with respect to the inverting-rotation coordinate, giving the overall potential energy function

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-17.jpg?height=248&width=769&top_left_y=1410&top_left_x=349)

Figure 11.6. A cross-sectional diagram of a toroidal worm drive. Power (and positional control) are provided via the threaded drive ring, the inner surface of which can be geared to a drive gear in the arm's core structure (see Figure 13.11). The outer surface of the drive ring bears a helically threaded band consisting of ridges like those on the surfaces in Figure 10.18; this surface interlocks with the driven threads of the triply-threaded torus. The outer surface of the drive also bears a circularly threaded band forming an interlocking bearing surface with the lower, stationary tube ("stationary" only in the present frame of reference). Rotation of the threaded drive ring about its axis thus drives the inverting rotational motion of the triply-threaded torus within the groove formed by the junction of the stationary and driven tube segments (which in turn are held together by an additional interlocking bearing surface). Within this groove, the stationary tube bears ridges which interlock with the retaining rings of the torus, and the driven tube bears ridges which interlock with the driving threads of the torus. Thus, as the torus undergoes its inverting rotation, the driven tube segment is forced to turn.

a period of $2 \pi / N_{\mathrm{seg}}$ in that coordinate, where $N_{\mathrm{seg}}$ is the number of segments in the torus. If the minor diameter is $2 \mathrm{~nm}$ and $N_{\mathrm{seg}}=50$, the spatial frequency of the potential energy function (measuring displacements at the sliding interface) is $\sim 8 \mathrm{~nm}^{-1}$. This results in strong mutual cancellation of the residual fluctuations in potential energy associated with the individual segments, yielding a potential energy function with negligible barriers for motion of the torus as a whole. (These parameters are appropriate for the manipulator joints described in Section 13.4.1.)

### 11.4. Fluids, seals, and pumps

Nanomechanical systems often must be in contact with a fluid medium. Typical operating environments contain fluids, whether gases or liquids; control of the internal environment then requires that external fluids be excluded by some combination of walls, seals, and pumps. Similar devices are likewise required for fluid-based convective cooling systems (Section 11.5). Further, hydraulic devices may be useful in nanomechanical systems, although this possibility is not further explored here. The following sections survey the nature of fluid flow in nanoscale systems, then consider walls, seals, and pumps.

### 11.4.1. Fluid micromechanics

a. Scale lengths in gases and liquids. Classical continuum models of fluid flow fail when the dimensions of tubes (or other structural features) are comparable to the characteristic molecular length scales of the fluid. In a gas, the largest characteristic length scale is the mean free path for a molecule between collisions. In a liquid, the characteristic length scale is the molecular size.

The Knudsen number measures the ratio of the mean free path to the feature size $r$ in the flow system; where it is $\geq 100$, the process is termed free molecular flow; where it is $\sim 1$, the process is termed transition flow. In macroscale devices, transition flow occurs at low pressures ( $\sim 10^{-5}$ atmospheres). In nanoscale devices $(r \leq 100 \mathrm{~nm})$, transition flow occurs in air at atmospheric pressure. Free molecular flow can be modeled as a process of repeated scattering from surfaces.

The behavior of liquids in small spaces is more complex and is a subject of active research (much of the following paragraph is based on Israelachvili, 1992). Liquids have short-range order, and that order is strongly perturbed near surfaces. For example, two smooth surfaces brought into close proximity in a liquid ( $\leq 6$ to 10 molecular diameters) experience forces that oscillate strongly as a function of separation: gaps that accommodate an integral number of molecular layers are preferred; slightly smaller separations result in repulsive forces, slightly larger separations result in attractive forces. These oscillations are smaller with rough surfaces and in liquids that mix molecules of varying size. With smooth mica surfaces in water, force oscillations virtually disappear at separations $\geq 2 \mathrm{~nm}$. (In water, hydrophilic forces can cause short-range surfacesurface repulsion and hydrophobic forces can cause short-range attraction, both with ranges of a few nanometers.) In liquid films a few molecular layers thick, viscosity increases and finite shear strength can develop; at a thickness of 7 to 10 layers or more, the bulk fluid viscosity gives a good description of shear stresses (Israelachvili, 1992).

b. Shear rates. Nanoscale fluid flows can exhibit extreme rates of shear: for example, a $1 \mathrm{~m} / \mathrm{s}$ shear speed imposed on a $1 \mathrm{~nm}$ gap corresponds to a shear rate of $10^{9} \mathrm{~s}^{-1}$. For a slab of fluid a meter thick to undergo shear at this rate, one surface would have to exceed the speed of light. In typical liquids (composed of small molecules with only local order), viscosity is little affected by shear rate so long as the velocity differential across a molecular diameter is small compared to the mean thermal velocity. A shear rate of $10^{9} \mathrm{~s}^{-1}$ easily meets this criterion.

c. Formulas for drag and pressure drop. With the above caveats regarding phenomena on short length-scales, fluid flow in small structures can usually be described by the classical continuum equations. The Reynolds number

$$
\begin{equation*}
R=r \rho v / \eta \tag{11.2}
\end{equation*}
$$

(where $\eta$ is the viscosity of the fluid, $v$ is a characteristic flow speed, $\rho$ is the fluid density, and $r$ is a characteristic dimension) indicates whether flow will be laminar or turbulent around (or within) an object of a given shape. For nanoscale objects in fluids of ordinary viscosities and velocities, $R$ is low, and the flow laminar.

In this regime, Stokes's law relates the radius $r$ of a sphere, the viscosity $\eta$ of a fluid, and the speed of the sphere $v$ to the drag force $F$

$$
\begin{equation*}
F=6 \pi r \eta v \tag{11.3}
\end{equation*}
$$

This expression is routinely used to describe the motion of objects as small as protein molecules (Creighton, 1984). For $\eta=10^{-3} \mathrm{~N} \cdot \mathrm{s} / \mathrm{m}^{2}$ ( $=1$ centipoise, the viscosity of water at $20 \mathrm{C}$ ), $r=100 \mathrm{~nm}, F=1 \mathrm{nN}, v \approx 0.5 \mathrm{~m} / \mathrm{s}$, and the drag power is $\sim 0.5 \mathrm{nW}$. The Reynolds number (based on the radius $r$ ) is 0.05 , well within the range for laminar flow.

The Hagen-Poiseuille law relates the volumetric flow rate $\Delta V / \Delta t$ through a long tube to its length $\ell$, its radius $r$, and the pressure difference $\Delta p$ between its ends

$$
\begin{equation*}
\Delta V / \Delta t=\pi r^{4} \Delta p / 8 \ell \eta \tag{11.4}
\end{equation*}
$$

This expression (like Stokes's law) assumes incompressible laminar flow. The incompressibility assumption is significantly violated in gases where the pressure differential is substantial compared to the total pressure. The laminar flow assumption is seldom violated save in relatively large tubes with relatively high flow speeds. A tube with $r=100 \mathrm{~nm}, \ell=1000 \mathrm{~nm}, \Delta p=1 \mathrm{MPa}$, transports a fluid of $\eta=10^{-3} \mathrm{~N} \cdot \mathrm{s} / \mathrm{m}^{2}$ at $\sim 4 \times 10^{-14} \mathrm{~m}^{3} / \mathrm{s}$, at a mean fluid speed of $1.25 \mathrm{~m} / \mathrm{s}$. The Reynolds number is again low (flow is laminar up to a diameter-based $R$ of $\sim 2000$ ).

An approximation for the pressure gradient along a tube containing a fluid in turbulent flow is the Darcy-Weisbach formula

$$
\begin{equation*}
\Delta p / \Delta \ell=f \rho v^{2} / 4 r \tag{11.5}
\end{equation*}
$$

where $v$ is the mean velocity of the fluid, and $f$ is a friction factor that depends on the Reynolds number $R$ of the flow and the roughness of the wall. The parameter $f$ can be evaluated by methods described in Tapley and Poston (1990); a high value (for a rough pipe at low $R$ ) is 0.1 , a low value (for a smooth pipe at $R>10^{7}$ ) is 0.008 .

### 11.4.2. Walls and seals

A nonbonded interface can serve as a seal, permitting relative motion of the surfaces but hindering the flow of fluid between them. The bearing interfaces explicitly considered in Section 10.4 can also serve as sealing interfaces, provided that no deep, unfilled groove crosses the seal band.

a. Molecular mechanics analysis of sealing interfaces. A pair of surfaces in nonbonded contact has an equilibrium separation. An interposed molecule will introduce additional nonbonded repulsions that locally increase this separation. The energy of interposition includes the strain energy of the facing structures, any strain energy in the interposed molecule (none, if it is monatomic), and the energy of the nonbonded repulsions. The energy is greater if the interface is compressed, but can be large even without compression.

Computational experiments using molecular mechanics (MM2/CSC with added parameters for $\mathrm{H}_{2}$ and $\mathrm{He}$ ) indicate the magnitude of the energy required to interpose a molecule between a pair of N-terminated (111) diamond surfaces, modeled as a pair of clusters. With an equilibrium separation of $\sim 0.30 \mathrm{~nm}$ between the facing planes, the energy of a $\mathrm{He}$ atom at one of the local minima of the relaxed structure is estimated to be $\sim 170 \mathrm{maJ}$, and the restoring force confining it to the plane of symmetry has $k_{\mathrm{s}} \approx 150 \mathrm{~N} / \mathrm{m}$. For $\mathrm{H}_{2}$, an analogous energy is $\sim 470 \mathrm{maJ}$, and $k_{\mathrm{s}} \approx 380 \mathrm{~N} / \mathrm{m}$. The energy of a molecule passing through the transition state for insertion into the interface is presumably higher than that of the observed minima.

Once interposed between two surfaces, a molecule diffuses from site to site and may exit from the far side of a seal. It is conservative to assume that all molecules that enter the seal gap immediately exit on the far side, thus treating the gap as an aperture of zero length and internal resistance. Using the He parameters just discussed, at $300 \mathrm{~K}$ and $k_{\mathrm{s}}=150 \mathrm{~N} / \mathrm{m}$, the effective width of the gap [Eq. (6.5)] is $\sim 0.013 \mathrm{~nm}$; the Boltzmann factor corresponding to an interposition energy of $170 \mathrm{maJ}$ decreases the number density of molecules within that effective width by $\sim 1.5 \times 10^{-18}$. Accordingly, the interface at worst behaves like a gap with a width of $\sim 2 \times 10^{-29} \mathrm{~m}$. Assuming an atmospheric He number density of $\sim 10^{20} \mathrm{~m}^{-3}$, the leakage rate is $\sim 10^{-15}$ atom $/ \mathrm{nm} \cdot \mathrm{s}$. At this rate, the mean waiting time for a seal of $1000 \mathrm{~nm}$ length to pass a single $\mathrm{He}$ atom is $>10^{4}$ years. Leakage for $\mathrm{H}_{2}$ and larger species appears negligible.

b. Sealing against ionic species. Positive ions such as $\mathrm{Li}^{+}$and $\mathrm{Be}^{2+}$ have smaller radii than helium atoms, and from a purely steric perspective would more easily pass through a seal. (A bare proton, $\mathrm{H}^{+}$, is a chemically nonexistent species; protons rapidly bind to other molecules.) These ions will rarely be found in appreciable numbers outside a solvating liquid environment, owing to the large electrostatic (Born) energy of a free ion in the gas phase or in a nonpolar fluid.

The heat of solvation of a monovalent ion in water is $\sim 800 \mathrm{maJ}$, relative to the gas phase. Any substantial desolvation of an ion in moving from water to a site within a bearing interface will increase the energy of the ion by a substantial fraction of $800 \mathrm{maJ}$, in part because the rigid seal surface cannot rearrange to provide solventlike coordination of polar groups [in water, $\mathrm{Li}^{+}$and $\mathrm{Be}^{2+}$ are coordinated to some 4 to 6 water molecules (Israelachvili, 1992)]. Further, a
sealing interface can be surrounded by a guard band that provides an adverse electrostatic environment, resembling a nonpolar, low dielectric constant solvent. In this circumstance, the interposition energy can easily exceed $200 \mathrm{maJ}$, and the leakage rate for ionic species from an aqueous (or other highly polar) medium is negligible.

c. Applications of seals. Since tight seals can also serve as good bearings, eutactic nanomechanical systems can be placed in intimate contact with fluids. Internal actuators can drive sliding and rotating shafts that extend into liquid media, hydraulic mechanisms with pistons and cylinders are feasible, many standard macroscale valve designs can be implemented, and so forth.

d. Permeability of walls. The relative gas tightness of nonbonded interfaces suggests that continuous walls of diamondoid structure can be effectively impermeable at ordinary temperatures. Diffusion of gases through metal and glass barriers is accelerated by the presence of defects: conventional metals have high densities of dislocations and grain boundaries; silicate glasses are relatively open and irregular structures that permit substantial diffusion of helium. Some metals dissolve hydrogen and permit it to diffuse relatively freely.

Defect-free layers of diamond and graphite differ from these materials. It is difficult to see how a molecule can pass through these materials without undergoing a reactive transformation. The species of chief concern is hydrogen, but calculations indicate that the energy required to move atomic hydrogen from free space into a minimum-energy site in diamond is thermally prohibitive $\left[\geq 800 \mathrm{maJ}\right.$ (Chu and Estreicher, 1990)]. If the initial species is $\mathrm{H}_{2}$, the required energy is far higher.

In ordinary environments, it seems likely that walls can be constructed that transmit gas molecules at negligible rates. If this assumption proves wrong, then double-walled structures with an intervening space containing either getter materials or a pumped vacuum can provide the same result.

### 11.4.3. Pumps and vacuum systems

a. Positive displacement pumps. Seals enable the construction of valves, pistons and cylinders, and so forth (Section 11.4.2), therefore positive-displacement pumps can be made. Use of diamond and diamondoid structural materials can enable operation at pressures ranging from high vacuum to $>10 \mathrm{GPa}$, assuming that allowance is made for elastic deformation of the structures at high pressures. The dominance of viscous forces in fluid flow at small scales favors the use of positive displacement pumps over centrifugal pumps.

b. Vacuum pumps. Vacuum has advantages as an operational medium for nanomechanical systems: unlike typical solvents, it is unreactive, causes no viscous drag, and cannot jam a mechanism. Accordingly, nanomechanical vacuum pumps are of interest.

In macroscale systems, the performance of vacuum pumps frequently is limited by the vapor pressure of their lubricants. Sliding interface seals and bearings need no separate lubricants, and hence present no such problem. Positive displacement pumps can accordingly serve as high-vacuum pumps.

The high strength to density ratio of graphitic and diamondoid materials lends itself to the construction of turbomolecular pumps (Figure 11.7): their

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-22.jpg?height=704&width=1049&top_left_y=205&top_left_x=358)

Figure 11.7. Schematic diagram of a pair of blade disks in a turbomolecular pump; the illustrated rotor direction corresponds to downward pumping. (Axle, bearings, casing not shown; disks not of minimal size.)

effectiveness depends on the ratio of the blade speed to the characteristic thermal speed of the lightest gas molecule to be pumped. With diamondoid materials, this speed can easily exceed that of hydrogen, providing a compression ratio of $\geq 10$ per blade row (Chu and Hua, 1982). Blade thickness can be $<1 \mathrm{~nm}$, and the pump length per blade row can be $<10 \mathrm{~nm}$, permitting compression ratios $>10^{10}$ in a $100 \mathrm{~nm}$ length. Turbomolecular pumps are designed to operate under free-molecule flow conditions; with blade row spacings $<10 \mathrm{~nm}$, free molecule flow occurs at pressures up to atmospheric.

Conventional systems that cycle from dirty conditions at atmospheric pressure to high vacuum are designed to permit bakeout, the use of high temperatures to speed outgassing. Nanomechanical systems built in accord with the room-temperature design rules assumed in this volume would not tolerate the required temperatures. Note, however, that the systems and system-construction processes described in later chapters avoid this requirement: they either build in a clean vacuum environment (Chapters 13 and 14), or can produce such an environment gradually, by diluting a fixed burden of contaminants over an increasing volume of mechanisms (Chapter 16).

### 11.5. Convective cooling systems

Because operating nanomechanical systems dissipate energy, they must be cooled if they are to operate for an extended time. Owing to the short distance between the interior of a submicron structure and its environment, conductive cooling usually suffices for small, isolated devices. Larger systems, such as macroscopic arrays of nanomechanical computers, require some form of convective cooling. Although mechanical convection based on solid strips moving with the
aid of bearings may prove superior, cooling systems based on forced convection of liquids are examined here. It will be assumed that heat is generated at a uniform rate throughout a macroscopic volume that must be cooled by fluid flowing from an input port to an output port.

### 11.5.1. Murray's Law and fractal plumbing

For a given volumetric flow rate, large diameter tubes minimize resistance and hence pump energy. A single large tube linking the input port to the output port would, however, be an ineffective cooling system owing to poor thermal contact. Thin tubes improve thermal contact but long, thin tubes would cause excessive resistance.

The appropriate compromise uses large tubes to carry fluid over most of the distance, smaller tubes to carry fluid over most of the remaining distance, and so forth, yielding a branching structure resembling a biological circulatory system that links large arteries and veins via smaller vessels ultimately linked by capillary beds. Murray's Law states that, for a system of tubes containing a fluid in laminar flow, the minimum volume for a given pressure drop occurs when the radii of the tubes at a branch point satisfy the relationship

$$
\begin{equation*}
r_{0}^{3}=r_{1}^{3}+r_{2}^{3}+r_{3}^{3}+\ldots+r_{n}^{3} \tag{11.6}
\end{equation*}
$$

where $r_{0}$ is the radius of the incoming tube, and $r_{1}, r_{2}$, etc., are the radii of the outgoing tubes. This condition equalizes shear stresses in the tubes, and is approximately obeyed in many biological circulatory systems (LaBarbera, 1990). Murray's Law is obeyed by an approximately fractal structure of the sort illustrated in Figure 11.8, in which tube lengths are approximately proportional to their radii, giving each level of the hierarchical structure an approximately equal volume and fluid residence time. In a macroscale system, the larger tubes may operate in turbulent flow; these tubes have different optimal dimensions.

### 11.5.2. Coolant design

To increase heat capacity and minimize temperature variations in a system, it is desirable to use a coolant that absorbs large quantities of heat in a narrow temperature range. This can be accomplished by means of a phase transition or by the expansion of a slightly supercritical gas. The latter process resembles vaporization in that thermal energy is converted to intermolecular potential energy as molecules separate, but avoids problems of bubble formation.

Suspended particles can add their heat of fusion to the heat capacity of a fluid. An attractive class of coolants combines encapsulated submicron ice particles (having surface structures that prevent aggregation) with a low-viscosity, low-melting point carrier, such as a light hydrocarbon. An expression (Hiemenz, 1986) derived from the Einstein relationship relates the viscosity of a fluid suspension $\eta$, the volume fraction of spherical particles $f_{\text {vol }}$, and the viscosity without the particles $\eta_{0}$

$$
\begin{equation*}
\eta / \eta_{0}=\left(1-f_{\mathrm{vol}}\right)^{-2.5} \tag{11.7}
\end{equation*}
$$

and is reasonably accurate for $f_{\text {vol }} \leq 0.4$. Packaged ice particles with a volume fraction of 0.4 increase fluid viscosity by a factor of $\sim 3.6$; if pentane is used as a
carrier, the viscosity of the resulting suspension is $\sim 8 \times 10^{-4} \mathrm{~N} \cdot \mathrm{s} / \mathrm{m}^{2}$. On melting, ice particles at this volume fraction absorb $\sim 1.2 \times 10^{8} \mathrm{~J} / \mathrm{m}^{3}$, based on coolant volume. This use of distinct heat-carrying bodies parallels the use of red blood cells as oxygen carriers in the circulatory system.

### 11.5.3. Cooling capacity in a macroscopic volume

A preliminary design exercise has been performed based on the coolant suspension described in Section 11.5.2 and a 4-level system of tubing of the sort illustrated in Figure 11.8, but with a higher branching ratio. This calculation (which takes account of turbulent flow in the largest tubes) indicates that $\sim 10^{5} \mathrm{~W}$ of thermal power can be extracted at $\sim 273 \mathrm{~K}$ (the melting point of ice) from a cube a centimeter on a side (or, more generally, $\sim 10^{5} \mathrm{~W} / \mathrm{cm}^{3}$ from a slab not more than $1 \mathrm{~cm}$ thick). The thinnest tubes are $<1 \mu$ in diameter and pass within $<5 \mu$ of each point in the volume that is not itself inside a tube. The volume fraction of the tubing system is 0.25 , and the overall pressure drop is $20 \mathrm{MPa}$. A more nearly optimal design should yield better results.

The desirability of minimizing communications delays between processors favors the construction of macroscale systems full of high-speed, closely-packed computational devices; this encourages the design of high-capacity cooling systems. The large manufacturing systems described in Chapter 14 must be convectively cooled, but the required capacity is orders of magnitude smaller than that just described. The microscopic systems described elsewhere can (in small numbers) be cooled adequately by conduction to a surrounding environment.
![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-24.jpg?height=782&width=1050&top_left_y=1265&top_left_x=356)

Figure 11.8. Series of four panels illustrating hypothetical stages in the construction of a nearly fractal system of cooling tubes. After this pattern has been extended to a sufficiently fine scale, it would be broken by introducing connections between the light (inflow) and dark (outflow) tubes.

### 11.6. Electromechanical devices

Except in discussing certain damage and error mechanisms, all systems considered so far have been assumed to be in their electronic ${ }^{\circ}$ ground states, with their properties determined entirely by the arrangement of their atoms. In insulators with relatively large band gaps (e.g., diamond) this is a common and stable condition.

This section considers several classes of electromechanical devices. In these, mechanical motion is coupled to the motion of electric charge, allowing mechanical motion to control charge motion, and charge motion to control mechanical motion. In true molecular electronic devices (e.g., Aviram, 1988; Hopfield et al., 1988), electronic degrees of freedom would be central and mechanical displacements would play a secondary role; these will not be considered here. The flow of current in nanoscale structures, even in electromechanical systems, is a complex topic. The following makes only rough estimates of conductivity in the pursuit of estimates of device size and performance.

### 11.6.1. Conducting paths

a. Conductivity. As the diameter of a wire becomes comparable to the electron mean free path, surface scattering can increase resistance above the value suggested by scaling laws and bulk resistivity. This can be avoided by suppressing surface scattering. In particular, structures can be chosen that have matching lattice spacings across the interface between metal insulator, measuring the spacings along the axis of current flow (matching usually requires strain). Electrons with wave vectors that enable propagation without reflection from metallic lattice planes will then experience no degradation of their longitudinal momentum as a result of diffractive scattering from the metal-insulator interface; in the longitudinal direction, specular reflection will dominate.

Doped graphite and organic polymeric materials can exhibit conductivities comparable to or greater than that of copper (Kivelson, 1988). Organic polymeric materials such as doped polyacetylene are termed quasi-one-dimensional conductors and presumably show little degradation of conductivity through surface scattering.

By engineering semiconductor structures with suitable band gaps and doping patterns, conducting filaments can be constructed that are narrow enough that electron wave functions having a transverse node are substantially higher in energy than those lacking a transverse node. These filaments, termed quantum wires, strongly suppress the small-angle scattering processes that dominate the degradation of electron momentum in ordinary conductors; they can accordingly exhibit unusually high conductivities (Sakaki, 1980; Timp et al., 1990).

Experimental and theoretical work on conducting polymers and other lowdimensional conducting structures suggests that eutactic electronic structures can be built that provide conducting paths of substantially lower resistance than would be estimated from their dimensions and bulk metallic resistivities. Indeed, it is conceivable that the ability to build a far wider range of metastable structures will lead to the discovery of superconductors with critical temperatures substantially higher than those now known. The balance of this work, however,
assumes conductors of bulk metallic conductivity; as just noted, this can be achieved by tailoring the metal-insulator interface. Conductors with diameters $<1 \mathrm{~nm}$ will not be considered. For bulk aluminum, the room-temperature resistivity equals $\sim 2.7 \times 10^{-8} \Omega \cdot \mathrm{m}$.

b. Current density. In integrated circuits, high current densities can cause electromigration, in which metal is redistributed from one region of a conductor to another, eventually breaking circuit continuity. This phenomenon limits acceptable current densities.

Electromigration results from biased diffusion of metal atoms and vacancies, chiefly along dislocations and grain boundaries. It is strongly suppressed in fully-dense, single-crystal metallic structures where the energy required to form a vacancy is large (e.g., >150 maJ in $\mathrm{Cu}$ ). The required energy is still larger if the displaced atom cannot occupy a normal lattice site (in a slightly expanded crystal), but is instead forced to occupy a high-energy interstitial site. Accordingly, a single-crystal metal wire surrounded by a strongly bonded, latticematched sheath should be stable at far greater current densities than a conventional wire of the same material. The structural stability of (some) conducting polymers should likewise minimize electromigration and similar phenomena. Despite these considerations, the following sections assume current densities no higher than those used today; a typical limit for aluminum conductors in integrated circuits is $\sim 3 \times 10^{9} \mathrm{~A} / \mathrm{m}^{2}$ (Mead and Conway, 1980).

### 11.6.2. Insulating layers and tunneling contacts

As a result of electron tunneling and field emission, current can flow between conductors separated by nominally insulating layers. To keep the tunneling conductance of an insulator within acceptable bounds requires some minimum thickness of material (which increases with increasing voltage); in addition, conductance from field emission (tunneling into vacuum or the interior of an insulator, as distinct from tunneling into another conductor) places limits on the maximum electric field permissible at a negatively charged surface. At small voltages ( $\leq 1 \mathrm{~V}$ ), an insulating gap of $\sim 3 \mathrm{~nm}$ can limit tunneling current densities to magnitudes that can usually be neglected in a nanomechanical context (e.g., $\leq 10^{-18} \mathrm{~A} / \mathrm{nm}^{2}$ ); metals exposed to vacuum can sustain fields of $\sim 2 \mathrm{~V} / \mathrm{nm}$ with a negligible current density from field emission (Farrall, 1980).

At small separations, tunneling currents can provide a mechanism for electrical contact without the complications of a conventional mechanical contact. Experiment shows that tunneling currents crossing a vacuum gap in an STM apparatus can exceed $300 \mathrm{nA}$ at $20 \mathrm{mV}$ (Gimzewski, 1988), implying a resistance near zero voltage of $<10^{5} \Omega$; resistance falls with increasing field strength (for comparison, the resistance attributed by classical continuum models to an interatomic spacing in bulk aluminum is $\sim 100 \Omega$ ). In the STM, most of the current is transmitted through a single atom at the tip, hence devices with parallel surfaces of several square nanometers should exhibit resistances of $\sim 10^{4} \Omega$. The design of good tunneling contacts will be complex, requiring attention to surface stability, stability of pairs of surfaces at small separations, and factors (such as work functions) affecting the gap resistance; surfaces of negative electron affinity may be useful [e.g., hydrogenated diamond (111) surfaces (Himpsel et al., 1979) with suitable doping of the underlying material].

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-27.jpg?height=396&width=702&top_left_y=205&top_left_x=435)

Figure 11.9. Schematic diagram of a modulated tunneling junction for interfacing mechanical inputs to electrical outputs (moving parts and electrical components only).

### 11.6.3. Modulated tunneling junctions

The transduction of mechanical signals to electrical signals can be performed by mechanically modulated tunneling junctions of the sort diagrammed in Figure 11.9. Bonding forces tend to snap metallic surfaces together (Israelachvili, 1992), but this can be resisted by small-area compressive contacts between nonbonding protrusions. Together with other means of tailoring the potential energy as a function of displacement, these can enable the device to operate without requiring substantial stiffness in the driving mechanism.

Section 11.6.2 concludes that tunneling junction resistances as low as $10^{4} \Omega$ should be feasible with junction areas of a few square nanometers. Separation of the surfaces to a distance of a few nanometers increases the resistance of a typical junction by many orders of magnitude (roughly a factor of 10 per $0.1 \mathrm{~nm}$ ) and permits substantial voltages to be supported. Accordingly, a modulated junction can serve as a mechanically controlled electrical switch.

### 11.6.4. Electrostatic actuators

Electrostatic actuators (Figure 11.10) can produce substantial mechanical forces. In this mechanism, one plate of a small capacitor is fixed and connected to a signal source; the other plate is grounded via a tunneling junction, leaving it free to

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-27.jpg?height=509&width=707&top_left_y=1646&top_left_x=438)

Figure 11.10. Schematic diagram of an electrostatic actuator for interfacing electrical inputs to mechanical outputs (moving parts and electrical components only).

move within a small range of displacements. In a concrete example, an actuator with a stroke length of $1 \mathrm{~nm}$ (moving between plate separations of 3 and $4 \mathrm{~nm}$ ) and a potential ranging from 0 to $5 \mathrm{~V}$ can apply a force ranging from zero to $1 \mathrm{nN}$ with a plate area of $\sim 150 \mathrm{~nm}^{2} \approx(12 \mathrm{~nm})^{2}$.

Although this is perhaps the simplest kind of electrostatic actuator, many others are possible. For example, a solenoidlike system can draw a high-dielectric constant plate into a gap with a force depending on the field; this can produce a large displacement. A long structure with multiple actuator mechanisms along its length can produce a large force with a small displacement. Finally, the range of actuators that can be built by molecular manufacturing will likely have no sharp boundary separating electrostatic from piezoelectric devices. In a mechanism of a given size, piezoelectric structures can typically provide larger forces but smaller displacements than electrostatic actuators of the sort just described. The use of a direct piezoelectric drive mechanism for manipulaturs of the sort described in Section 13.4.1 would increase their similarity to existing proximal probes.

### 11.6.5. Electrostatic motors

Motors based on electrostatic forces (like those based on electromagnets) can be built to run on alternating or direct current, and can have a wide range of mechanical properties. Alternating-current (AC) motors can synchronize a mechanical system to an electrical input, but a substantial part of their complexity is in the power supply. Direct-current (DC) motors are discussed in the following section.

### 11.7. DC motors and generators

Electrostatic DC motors provide a straightforward means of supplying power to nanomechanical systems. In one implementation (Figure 11.11), electric charge is placed on the rim of a rotor as the rim passes within a dee electrode, and is then transported across a gap to the interior of the opposite dee electrode, where it is removed and replaced by a charge of the opposite sign. If a voltage of the proper sign is applied across the dees, the charges in transit between them experience a force that applies a torque to the rotor, delivering power. This resembles a Van de Graff generator operating in reverse.

### 11.7.1. Charge carriers and charge density

The rim of a rotor can be made of insulating material with embedded conductive electrodes (Figure 11.11) that serve as charge carriers. If the rim electrodes are separated by $3 \mathrm{~nm}$ and no large voltages are imposed between them, then interelectrode charge transfer can be neglected. Neglecting the beneficial effects of insulator polarization, the surface charge density of the rim electrodes corresponding to a (modest) field of $0.2 \mathrm{~V} / \mathrm{nm}$ is $\sim 0.0018 \mathrm{C} / \mathrm{m}^{2}$. Assuming an electrode diameter of $3 \mathrm{~nm}$ and length of $20 \mathrm{~nm}$, the charge per electrode is $\sim 3.3 \times 10^{-19} \mathrm{C}$, or $\sim 2$ electronic charge units; the corresponding charge per unit rotor circumference is $\sim 5.5 \times 10^{-11} \mathrm{C} / \mathrm{m}$. A vacuum gap of several nanometers can insulate the rim electrodes from a nearby dee electrode surface.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-29.jpg?height=623&width=927&top_left_y=195&top_left_x=306)

Figure 11.11. Schematic diagram of an electrostatic motor (not to scale). The dee electrodes and rotor-rim electrodes are conducting, the rotor structural material is insulating. Rotation and torque are in the direction shown.

### 11.7.2. Electrode charging mechanism

a. Work functions and contact potentials. The work function $\phi_{w}$ of a material is the energy required to remove an electron from its interior to a nearby exterior region. The work function of a material often depends strongly on its surface condition, and extreme values of $\phi_{w}$ can presumably be achieved by carefully tailoring surface structures. The range of work functions observed on clean surfaces of elemental metals of reasonably high melting-point places a lower bound on breadth of the range to be expected in a broader class of stable structures. Among the lower values (Lide, 1990) is $\phi_{\mathrm{w}}=2.7 \mathrm{eV}$ (for samarium, melting point $\sim 1350 \mathrm{~K}$ ); among the higher values is $\phi_{\mathrm{w}}=5.7 \mathrm{eV}$ (for platinum, melting point $\sim 2050 \mathrm{~K}$ ).

Placing two metals with differing work functions in electrical contact equalizes their electron energies and results in a potential difference (the contact potential) between the region of space immediately outside one surface and the region immediately outside the other. This potential difference implies an electric field and a corresponding surface charge density. Contact potentials provide a convenient mechanism for charging the rim electrodes.

b. Charging via contact potentials. Consider a rotor-rim electrode in electrical contact with the interior of a dee electrode, in an environment where its surface and the surrounding dee electrode surface share a common work function $\phi_{\mathrm{w}, \text { middle }}=4.2 \mathrm{eV}$. The surface charge density is accordingly zero. Now, while maintaining electrical contact through a tunneling junction, allow the rotor-rim electrode to move into a region in which the inner surface of the dee electrode has a work function $\phi_{\mathrm{w}, \text { high }}=5.7 \mathrm{eV}$. The magnitude of the contact potential is accordingly $1.5 \mathrm{~V}$; with a capacitance of $\sim 2.1 \times 10^{-19} \mathrm{~F}$, the charge on the rotorrim electrode will have a magnitude of 2 electronic units. Modeling the rim electrodes as well-separated cylinders parallel to a plane at a distance of $3 \mathrm{~nm}$ from their surfaces yields a capacitance per cylinder of $\sim 6.3 \times 10^{-19} \mathrm{~F}$; modeling them
as a continuous strip at the distance of their centers yields a capacitance per rimelectrode length of $\sim 2.4 \times 10^{-19} \mathrm{~F}$. Accordingly, the assumed charge could be induced in a system with a substantially smaller value of $\phi_{w, h i g h}-\phi_{w, \text { middle }}$. (Since $\phi_{w, h i g h}-\phi_{w, \text { middle }}$ can equal $\phi_{w, \text { middle }}-\phi_{w, \text { low }}$, charge of the opposite sign can be induced in a similar fashion.)

c. The rim electrode charge/discharge cycle. A rotor-rim electrode can be made to go through the following cycle in a revolution of the rotor: Starting in the middle of the positive dee, it is in electrical contact with the dee via a tunneling junction in an environment where its induced charge is zero. Moving clockwise (Figure 11.11), it enters a region where the dee surface has a higher work function, inducing a charge of $+2 e$. This change in mean equilibrium charge occurs gradually, because the mean work function of the surrounding electrode is made to vary gradually from position to position by changing the fraction of area occupied by surfaces of different kinds.[^30] Once this charge is induced, the tunneling contact (made to a narrow ridge on the inner surface of the dee) is gradually broken in surroundings that keep the equilibrium charge on the rim electrode constant. After traveling a further distance, the positively charged rim electrode exits the positively charged dee and enters the negatively charged dee, dropping through a potential difference of $\phi_{\text {motor }}$ as it does so. Once beyond the fringing fields at the entrance to the negative dee, the rim electrode encounters an electrostatic environment that is the same as it was before exiting the positive dee (in accord with basic electrostatic principles, the charge and field resulting from the dee's overall potential are chiefly distributed across its outer surface), and the approach to the middle of the negative dee is a nearly precise reversal of the sequence of environments and charge-transfers that occurred in the positive dee, ending with no net charge on the rim electrode. Continuing through the negative dee, exiting, entering the positive dee, and returning to the initial position proceeds in the same manner as the first half of the cycle, except that low surrounding work functions induce a negative charge on the rim electrode.

This cycle never permits electrical contact between conductors in electrical disequilibrium, and is directly analogous to mechanochemical cycles that avoid well merging losses (Section 7.6.5). By connecting conductors only at equilibrium, current flow is postponed until the contact resistance is low, enabling the charge-transfer process to be nearly thermodynamically reversible. (Note that reversing the direction of rotor motion would in fact reverse the directions of current flow and of work, making the system function as a DC generator.)

### 11.7.3. Motor power and power density

Neglecting resistive and frictional losses, DC electrostatic motors of this kind deliver a shaft power equal to the product of the current and the voltage $\phi_{\text {motor }}$. The current, in turn, is twice the product of the rim speed and the charge per unit length. With diamondoid structures to support centrifugal loads and an evacuated volume to avoid fluid drag, a rim speed of $\sim 1000 \mathrm{~m} / \mathrm{s}$ is readily achievable. With a charge per unit length of $\sim 5.5 \times 10^{-11} \mathrm{C} / \mathrm{m}$ (Section 11.7.1), the current is $\sim 110 \mathrm{nA}$ (including contributions from both sides of the rotor). If $\phi_{\text {motor }}=10 \mathrm{~V}$, the delivered power is $\sim 1.1 \mu \mathrm{W}$.

Allowing for the geometrical constraints of minimum gap sizes for insulation, and so forth, a motor radius of $50 \mathrm{~nm}$ is generous (to permit direct application of sample calculations in a later section, a radius of $195 \mathrm{~nm}$ is assumed in the following). A motor thickness of $25 \mathrm{~nm}$ is consistent with the rim electrode dimensions assumed in Section 11.7.1, yielding a motor volume of $\sim 2 \times 10^{-22} \mathrm{~m}^{3}$. The power density is large compared to that of macroscale motors: $>10^{15} \mathrm{~W} / \mathrm{m}^{3}$. For comparison, Earth intercepts $\sim 10^{17} \mathrm{~W}$ of solar radiation. (Cooling constraints presumably preclude the steady-state operation of a cubic meter of these devices at this power density.)

### 11.7.4. Energy dissipation and efficiency

a. Resistance in conductors. Since electrostatic motors do not exploit current-generated fields, they need no long, coiled conductors and have only small internal resistive losses. (Bearing friction could be regarded as a resistive loss associated with mechanical charge transport by the rotor, but is considered separately below.) Resistive losses are dominated by conducting paths outside the motor proper, making the following estimate somewhat arbitrary. At a current density of $1 \mathrm{nA} / \mathrm{nm}^{2}$, the cross sectional area of the leads for a $110 \mathrm{nA}$ motor is $110 \mathrm{~nm}^{2}$. If each lead has a length equal to the motor diameter, their series resistance is $\sim 200 \Omega$, assuming a resistivity equal to the bulk value for aluminum $\left(\sim 2.7 \times 10^{-8} \Omega \cdot \mathrm{m}\right)$. This yields an estimated resistive power dissipation in the leads of $\sim 2.4 \mathrm{pW}$. The current flow responsible for distributing charge along a rim electrode contributes $\sim 0.1 \mathrm{pW}$, calculated on a similar basis.

b. Resistance in tunneling contacts. Since the length of the rim contained in a dee is $\sim 500 \mathrm{~nm},>80$ rim electrodes can be in contact in a given dee at any given time. Assuming that the mean charge on a rim electrode increases steadily during its transit of a dee, the tunneling contacts in each dee can be treated as resistances in parallel. If a tunneling contact to a rim electrode has a resistance of $<10^{4} \Omega$ (Section 11.6.2), then the total resistance of the tunneling contacts through both dees is $<250 \Omega$, with a corresponding power dissipation of $<3 \mathrm{pW}$. As noted in Section 11.7.4d, however, larger gaps and resistive losses may prove desirable in order to reduce contact drag.

c. Bearing drag. A rotor remains below its lowest critical angular velocity so long as the condition

$$
\begin{equation*}
\sqrt{k_{\mathrm{s}, \mathrm{t}} / m_{\text {rotor }}}>\omega_{\text {rotor }} \tag{11.8}
\end{equation*}
$$

is met (where $k_{\mathrm{s}, \mathrm{t}}$ is the stiffness of the bearing structure in resisting displacement of the shaft in a direction perpendicular to its axis, and $m_{\text {rotor }}$ and $\omega_{\text {rotor }}$ are the rotor mass and angular velocity). With a rotor radius of $195 \mathrm{~nm}$ (chosen for compatibility with Section 12.7 .5 ) and rim speed of $1000 \mathrm{~m} / \mathrm{s}, \omega_{\text {rotor }} \approx 5 \times 10^{9}$ $\mathrm{rad} / \mathrm{s}$ and $m_{\text {rotor }}=8 \times 10^{-18} \mathrm{~kg}$, requiring a bearing with $k_{\mathrm{s}, \mathrm{t}} \geq \sim 200 \mathrm{~N} / \mathrm{m}$, a condition which is easily met (see Sections 10.4.5 and 10.4.6). Applying the combined drag model (Section 10.4.6f) to an axle bearing with a stiffness of $500 \mathrm{~N} / \mathrm{m}$ (ample for rotor stability), $r_{\text {eff }}=10 \mathrm{~nm}, \ell=20 \mathrm{~nm}, v=50 \mathrm{~m} / \mathrm{s}, R=10$, and the pessimistic value $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.4$, the estimated bearing drag power is $\sim 1.3 \mathrm{pW}$.

A more serious instability results from the negative stiffnesses associated with the attractive forces in tunneling contacts (Chen, 1991; Dürig et al., 1988). In a sliding-contact design, these may require bearing stiffnesses larger by two orders of magnitude, resulting in a bearing drag power on the order of several nanowatts.

d. Contact drag. A sliding tunneling contact between a rim electrode and the tunneling contact structures inside a dee can be expected to result in drag associated with electron transfer. Transfer of a single electron across the gap would (on the average, in a classical system) be expected to dissipate the kinetic energy corresponding to its mass and the relative speed of the rotor: $\sim 5 \times 10^{-25} \mathrm{~J}$, or $\sim 3 \times 10^{-7}$ of the energy delivered by an electron in dropping through a $10 \mathrm{~V}$ potential. Efficient, near-equilibrium electrode charging requires many electron exchanges for the net transfer of a single electron, multiplying the energy loss. As suggested by J. Soreff, however, the use of lowdimensional conductors lacking substantial conductivity parallel to the direction of motion should strongly suppress energy losses from electron transfer (and from associated scattering mechanisms).

The attractive forces associated with sliding tunneling contacts also cause losses through thermoelastic effects and phonon scattering. These remain to be evaluated and may prove to be the dominant loss mechanism in this design. If they are sufficiently large, alternative designs with rolling contacts would be preferable. This shift in design could also reduce the requisite bearing stiffnesses and resulting bearing drag.

e. Summary. Omitting contact drag, the energy dissipation appears to be dominated by the bearing drag (several nanowatts). If contact drag does not greatly change this picture, then motor efficiencies $>.99$ should be achievable at an extremely high power density; efficiencies can be higher at lower power densities and could likely be increased by replacing sliding with rolling electrical contacts. None of the analyses in later chapters require high motor efficiencies.

### 11.7.5. Motor start-up

If a motor is initially disengaged from any load, start-up can occur spontaneously. The mean thermal speed of the rotor is $\sim 0.01 \mathrm{~m} / \mathrm{s}$, with little damping. Rotation in reverse is effectively prohibited when the dees are charged; forward rotation is permitted and will begin to carry charge across the gap, producing torque and faster rotation, in $\sim 10^{-5} \mathrm{~s}$.

Forcible motor start-up can be ensured if the rim electrodes in the gap between the dees have the proper charge, producing a strong torque. This can be
accomplished by providing extensions from each dee that provide a weak tunneling current to the rim electrodes in the gap (on the side where they have the same charge in normal operation). If this rate is low, it has little effect on an operating motor, yet can ensure charging of electrodes in the gaps of a stationary motor.

### 11.7.6. Speed regulation

Precise speed regulation calls for a mechanism based on a frequency standard, such as a mechanical oscillator or an external AC source. For a system operating asynchronously with respect to other systems in its environment, approximate speed regulation can often suffice. A spring-loaded variant of the Watt governor can serve this purpose, opening and closing a tunneling contact instead of a steam valve. If designed for bistability, it will oscillate between having a closed contact and having an open contact, dissipating little energy in either state.

### 11.8. Conclusions

This chapter surveys several classes of subsystems of intermediate size and complexity. These include mechanical measurement systems, stiff mechanisms of high gear ratio, components for handling fluids, convective cooling systems, electrostatic switches and actuators, and DC electric motors of high efficiency and power density. A conclusion emerging from the chapter as a whole is that functional analogues of many macroscale systems can be constructed on a scale of tens to hundreds of nanometers; their detailed structures, operating principles, and performance parameters, however, often diverge widely from those of the corresponding macroscale systems.

Some open problems. As in Chapter 10, the task of expanding the range of well-characterized, atomically detailed models for devices defines a large set of open problems. Many subsystems (measurement devices, stiff drive mechanisms, seals and pumps) fall within the size range accessible with existing molecular modeling systems. Detailed studies of various combinations of seals and infiltrating species, using various modeling techniques, would be of considerable interest. The design of more nearly optimal convective cooling systems is of interest, and progress can be made using standard relationships for the pressure drop in pipes. Electromechanical devices present a set of open problems revolving around electron transport in well-designed, stable, eutactic structures on a nanometer scale, and in tunneling junctions in particular. Further study is needed to characterize drag mechanisms in sliding tunneling junctions. The performance estimates for electromechanical devices in this chapter are crude at best, and the junction structures remain to be specified.

[^30]: Under some conditions, Coulomb blockade effects (Barner and Ruggiero, 1987; Kuzmin et al., 1989) can become important. In particular, if the tunnel resistance is large compared to the quantum unit of resistance $\pi \hbar / 2 e^{2} \approx 6.5 \times 10^{3} \Omega$, then electrons will be sufficiently well localized that a rim electrode can be viewed as having a discrete number of electrons. If, in addition, the change in electrostatic energy caused by adding one electronic charge ( $e^{2} / 2 C$, where $C$ is the electrode capacitance) is large compared to $k T$, then the mean charge will vary in a staircase fashion, rather than smoothly. Under these conditions, a more uniform rate of charging can be achieved if the potential induced by work-function effects changes swiftly in the range where the mean equilibrium charge approximates an integral number, and more slowly in the range around half-integral values.