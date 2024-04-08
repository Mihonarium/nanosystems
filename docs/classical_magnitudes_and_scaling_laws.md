# Classical Magnitudes and Scaling Laws


### 2.1. Overview

Most physical magnitudes characterizing nanoscale systems differ enormously from those familiar in macroscale systems. Some of these magnitudes can, however, be estimated by applying scaling laws to the values for macroscale systems. Although later chapters seldom use this approach, it can provide orientation, preliminary estimates, and a means for testing whether answers derived by more sophisticated methods are in fact reasonable.

The first of the following sections considers the role of engineering approximations in more detail (Section 2.2); the rest present scaling relationships based on classical continuum models and discuss how those relationships break down as a consequence of atomic-scale structure, mean-free-path effects, and quantum mechanical effects. Section 2.3 discusses mechanical systems, where many scaling laws are quite accurate on the nanoscale. Section 2.4 discusses electromagnetic systems, where many scaling laws fail dramatically on the nanoscale. Section 2.5 discusses thermal systems, where scaling laws have variable accuracy. Finally, Section 2.6 briefly describes how later chapters go beyond these simple models.

### 2.2. Approximation and classical continuum models

When used with caution, classical continuum models of nanoscale systems can be of substantial value in design and analysis. They represent the simplest level in a hierarchy of approximations of increasing accuracy, complexity, and difficulty.

Experience teaches the value of approximation in design. A typical design process starts with the generation and preliminary evaluation of many options, then selects a few options for further elaboration and evaluation, and finally settles on a detailed specification and analysis of a single preferred design. The first steps entail little commitment to a particular approach. The ease of exploring and comparing many qualitatively distinct approaches is at a premium, and drastic approximations often suffice to screen out the worst options. Even the final design and analysis does not require an exact calculation of physical behavior: approximations and compensating safety margins suffice. Accordingly, a design process can use different approximations at different stages, moving toward greater analytical accuracy and cost.

Approximation is inescapable because the most accurate physical models are computationally intractable. In macromechanical design, engineers employ approximations based on classical mechanics, neglecting quantum mechanics, the thermal excitation of mechanical motions, and the molecular structure of matter. Since macromechanical engineering blends into nanomechanical engineering with no clear line of demarcation, the approximations of macromechanical engineering offer a point of departure for exploring the nanomechanical realm. In some circumstances, these approximations (with a few adaptations) provide an adequate basis for the design and analysis of nanoscale systems. In a broader range of circumstances, they provide an adequate basis for exploring design options and for conducting a preliminary analysis. In a yet broader range of circumstances, they provide a crude description to which one can compare more sophisticated approximations.

### 2.3. Scaling of classical mechanical systems

Nanomechanical systems are fundamental to molecular manufacturing and are useful in many of its products and processes. The widespread use in chemistry of molecular mechanics approximations together with the classical equations of motion (Sections 3.3, 4.2.3a) indicates the utility of describing nanoscale mechanical systems in terms of classical mechanics. This section describes scaling laws and magnitudes with the added approximation of continuous media.

### 2.3.1. Basic assumptions

The following discussion considers mechanical systems, neglecting fields and currents. Like later sections, it examines how different physical magnitudes depend on the size of a system (defined by a length parameter $L$ ) if all shape parameters and material properties (e.g., strengths, moduli, densities, coefficients of friction) are held constant.

A description of scaling laws must begin with choices that determine the scaling of dynamical variables. A natural choice is that of constant stress. This implies scale-independent ${ }^{\circ}$ elastic deformation, and hence scale-independent shape; since it results in scale-independent speeds, it also implies constancy of the space-time shapes describing the trajectories of moving parts. Some exemplar calculations are provided, based on material properties like those of diamond (Table 9.1): density $\rho=3.5 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$; Young's modulus $E=10^{12} \mathrm{~N} / \mathrm{m}^{2}$; and a low working stress ( $\sim .2$ times tensile strength) $\sigma=10^{10} \mathrm{~N} / \mathrm{m}^{2}$. This choice of materials often yields large parameter values (for speeds, accelerations, etc.) relative to those characteristic of more familiar engineering materials.

### 2.3.2. Magnitudes and scaling

Given constancy of stress and material strength, both the strength of a structure and the force it exerts scale with its cross-sectional area

$$
\begin{equation*}
\text { total strength } \propto \text { force } \propto \text { area } \propto L^{2} \tag{2.1}
\end{equation*}
$$

Nanoscale devices accordingly exert only small forces: a stress of $10^{10} \mathrm{~N} / \mathrm{m}^{2}$ equals $10^{-8} \mathrm{~N} / \mathrm{nm}^{2}$, or $10 \mathrm{nN} / \mathrm{nm}^{2}$. Stiffness in ${ }^{\circ}$ shear, like stretching stiffness, depends on both area and length

$$
\begin{equation*}
\text { shear stiffness } \propto \text { stretching stiffness } \propto \frac{\text { area }}{\text { length }} \propto L \tag{2.2}
\end{equation*}
$$

and varies less rapidly with scale; a cubic nanometer block of $E=10^{12} \mathrm{~N} / \mathrm{m}^{2}$ has a stretching stiffness of $1000 \mathrm{~N} / \mathrm{m}$. The bending stiffness of a rod scales in the same way

$$
\begin{equation*}
\text { bending stiffness } \propto \frac{\text { radius }^{4}}{\text { length }^{3}} \propto L \tag{2.3}
\end{equation*}
$$

Given the above scaling relationships, the magnitude of the deformation under load

$$
\begin{equation*}
\text { deformation } \propto \frac{\text { force }}{\text { stiffness }} \propto L \tag{2.4}
\end{equation*}
$$

is proportional to scale, and hence the shape of deformed structures is scale invariant.

The assumption of constant density makes mass scale with volume,

$$
\begin{equation*}
\text { mass } \propto \text { volume } \propto L^{3} \tag{2.5}
\end{equation*}
$$

and the mass of a cubic nanometer block of density $\rho=3.5 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$ equals $3.5 \times 10^{-24} \mathrm{~kg}$.

The above expressions yield the scaling relationship

$$
\begin{equation*}
\text { acceleration } \propto \frac{\text { force }}{\text { mass }} \propto L^{-1} \tag{2.6}
\end{equation*}
$$

A cubic-nanometer mass subject to a net force equaling the above working stress applied to a square nanometer experiences an acceleration of $\sim 3 \times 10^{15} \mathrm{~m} / \mathrm{s}^{2}$. Accelerations in nanomechanisms commonly are large by macroscopic standards, but aside from special cases (such as transient acceleration during impact and steady acceleration in a small flywheel) they rarely approach the value just calculated. (Terrestrial gravitational accelerations and stresses usually have negligible effects on nanomechanisms.)

Modulus and density determine the acoustic speed, a scale-independent parameter [along a slim rod, the speed is $(E / \rho)^{1 / 2}$; in bulk material, somewhat higher]. The vibrational frequencies of a mechanical system are proportional to the acoustic transit time

$$
\begin{equation*}
\text { frequency } \propto \frac{\text { acoustic speed }}{\text { length }} \propto L^{-1} \tag{2.7}
\end{equation*}
$$

The acoustic speed in diamond is $\sim 1.75 \times 10^{4} \mathrm{~m} / \mathrm{s}$. Some vibrational modes are more conveniently described in terms of lumped parameters of stiffness and mass,

$$
\begin{equation*}
\text { frequency } \propto \sqrt{\frac{\text { stiffness }}{\text { mass }}} \propto L^{-1} \tag{2.8}
\end{equation*}
$$

but the scaling relationship is the same. The stiffness and mass associated with a cubic nanometer block yield a vibrational frequency characteristic of a stiff, nanometer-scale object: $\left[(1000 \mathrm{~N} / \mathrm{m}) /\left(3.5 \times 10^{-24} \mathrm{~kg}\right)\right]^{1 / 2} \approx 1.7 \times 10^{13} \mathrm{rad} / \mathrm{s}$.

Characteristic times are inversely proportional to characteristic frequencies

$$
\begin{equation*}
\text { time } \propto \text { frequency }^{-1} \propto L \tag{2.9}
\end{equation*}
$$

The speed of mechanical motions is constrained by strength and density. Its scaling can be derived from the above expressions

$$
\begin{equation*}
\text { speed } \propto \text { acceleration } \cdot \text { time }=\text { constant } \tag{2.10}
\end{equation*}
$$

A characteristic speed (only seldom exceeded in practical mechanisms) is that at which a flywheel in the form of a slim hoop is subject to the chosen working stress as a result of its mass and centripetal acceleration. This occurs when $v=$ $(\sigma / \rho)^{1 / 2} \approx 1.7 \times 10^{3} \mathrm{~m} / \mathrm{s}$ (with the assumed $\sigma$ and $\rho$ ). Most mechanical motions considered in this volume, however, have speeds between 0.001 and $10 \mathrm{~m} / \mathrm{s}$.

The frequencies characteristic of mechanical motions scale with transit times

$$
\begin{equation*}
\text { frequency } \propto \frac{\text { speed }}{\text { length }} \propto L^{-1} \tag{2.11}
\end{equation*}
$$

These frequencies scale in the same manner as vibrational frequencies, hence the assumption of constant stress leaves frequency ratios as scale invariants. At the above characteristic speed, crossing a $1 \mathrm{~nm}$ distance takes $\sim 6 \times 10^{-13} \mathrm{~s}$; the large speed makes this shorter than the motion times anticipated in typical nanomechanisms. A modest $1 \mathrm{~m} / \mathrm{s}$ speed, however, still yields a transit time of only $1 \mathrm{~ns}$, indicating that nanomechanisms can operate at frequencies typical of modern micron-scale electronic devices.

The above expressions yield relationships for the scaling of mechanical power

$$
\begin{equation*}
\text { power } \propto \text { force } \cdot \text { speed } \propto L^{2} \tag{2.12}
\end{equation*}
$$

and mechanical power density

$$
\begin{equation*}
\text { power density } \propto \frac{\text { power }}{\text { volume }} \propto L^{-1} \tag{2.13}
\end{equation*}
$$

A $10 \mathrm{nN}$ force and a $1 \mathrm{~nm}^{3}$ volume yield a power of $17 \mu \mathrm{W}$ and a power density of $1.7 \times 10^{22} \mathrm{~W} / \mathrm{m}^{3}$ (at a speed of $1.7 \times 10^{3} \mathrm{~m} / \mathrm{s}$ ) or $10 \mathrm{nW}$ and $10^{19} \mathrm{~W} / \mathrm{m}^{3}$ (at a speed of $1 \mathrm{~m} / \mathrm{s}$ ). The combination of strong materials and small devices promises mechanical systems of extraordinarily high power density, even at low speeds (an example of a mechanical power density is the power transmitted by a gear divided by its volume).

Most mechanical systems use bearings to support moving parts. Macromechanical systems frequently use liquid lubricants, but (as noted by Feynman, 1961), this poses problems on a small scale. The above scaling law ordinarily holds speeds and stresses constant, but reducing the thickness of the lubricant layer increases shear rates and hence viscous shear stresses:

$$
\begin{equation*}
\text { viscous stress at constant speed } \propto \text { shear rate } \propto \frac{\text { speed }}{\text { thickness }} \propto L^{-1} \tag{2.14}
\end{equation*}
$$

In Newtonian fluids, shear stress is proportional to shear rate. Molecular simulations indicate that liquids can remain nearly Newtonian at shear rates in excess of $100 \mathrm{~m} / \mathrm{s}$ across a $1 \mathrm{~nm}$ layer (e.g., in the calculations of Ashurst and Hoover, 1975), but they depart from bulk viscosity (or even from liquid behavior) when film thicknesses are less than 10 molecular diameters (Israelachvili, 1992; Schoen et al., 1989), owing to interface-induced alterations in liquid structure. Feynman suggested the use of low-viscosity lubricants (such as kerosene) for micromechanisms (Feynman, 1961); from the perspective of a typical nanomechanism, however, kerosene is better regarded as a collection of bulky molecular objects than as a liquid. If one nonetheless applies the classical approximation to a $1 \mathrm{~nm}$ film of low-viscosity fluid $\left(\eta=10^{-3} \mathrm{~N} \cdot \mathrm{s} / \mathrm{m}^{2}\right)$, the viscous shear stress at a speed of $1.7 \times 10^{3} \mathrm{~m} / \mathrm{s}$ is $1.7 \times 10^{9} \mathrm{~N} / \mathrm{m}^{2}$; the shear stress at a speed of $1 \mathrm{~m} / \mathrm{s}, 10^{6} \mathrm{~N} / \mathrm{m}^{2}$, is still large, dissipating energy at a rate of $1 \mathrm{MW} / \mathrm{m}^{2}$.

The problems of liquid lubrication motivate consideration of dry bearings (as suggested by Feynman, 1961). Assuming a constant coefficient of friction,

$$
\begin{equation*}
\text { frictional force } \propto \text { force } \propto L^{2} \tag{2.15}
\end{equation*}
$$

and both stresses and speeds are once again scale-independent. The frictional power,

$$
\begin{equation*}
\text { frictional power } \propto \text { force } \cdot \text { speed } \propto L^{2} \tag{2.16}
\end{equation*}
$$

is proportional to the total power, implying scale-independent mechanical efficiencies. In light of engineering experience, however, the use of dry bearings would seem to present problems (as it has in silicon micromachine research). Without lubrication, efficiencies may be low, and static friction often causes jamming and vibration.

A yet more serious problem for unlubricated systems would seem to be wear. Assuming constant interfacial stresses and speeds (as implied by the above scaling relationships), the anticipated surface erosion rate is independent of scale. Assuming that wear life is determined by the time required to produce a certain fractional change in shape,

$$
\begin{equation*}
\text { wear life } \propto \frac{\text { thickness }}{\text { erosion rate }} \propto L \tag{2.17}
\end{equation*}
$$

and a centimeter-scale part having a ten-year lifetime would be expected to have a $30 \mathrm{~s}$ lifetime if scaled to nanometer dimensions.

Design and analysis have shown, however, that dry bearings with atomically precise surfaces need not suffer these problems. As shown in Chapters 6, 7, and 10 , dynamic friction can be low, and both static friction and wear can be made negligible. The scaling laws applicable to such bearings are compatible with the constant-stress, constant-speed expressions derived previously.

### 2.3.3. Major corrections

The above scaling relationships treat matter as a continuum with bulk values of strength, modulus, and so forth. They readily yield results for the behavior of iron bars scaled to a length of $10^{-12} \mathrm{~m}$, although such results are meaningless because a single atom of iron is over $10^{-10} \mathrm{~m}$ in diameter. They also neglect the influence of surfaces on mechanical properties (Section 9.4), and give (at best) crude estimates regarding small components, in which some dimensions may be only one or a few atomic diameters.

Aside from the molecular structure of matter, major corrections to the results suggested by these scaling laws include uncertainties in position and velocity resulting from statistical and quantum mechanics (examined in detail in Chapter 5). Thermal excitation superimposes random velocities on those intended by the designer. These random velocities depend on scale, such that

$$
\begin{equation*}
\text { thermal speed } \propto \sqrt{\frac{\text { thermal energy }}{\text { mass }}} \propto L^{-3 / 2} \tag{2.18}
\end{equation*}
$$

where the thermal energy measures the characteristic energy in a single degree of freedom, not in the object as a whole. For $\rho=3.5 \times 10^{3} \mathrm{~kg} / \mathrm{m}^{3}$, the mean thermal speed of a cubic nanometer object at $300 \mathrm{~K}$ is $\sim 55 \mathrm{~m} / \mathrm{s}$. Random thermal velocities (commonly occurring in vibrational modes) often exceed the velocities imposed by planned operations, and cannot be ignored in analyzing nanomechanical systems.

Quantum mechanical uncertainties in position and momentum are parallel to statistical mechanical uncertainties in their effects on nanomechanical systems. The importance of quantum mechanical effects in vibrating systems depends on the ratio of the characteristic quantum energy ( $\hbar \omega$, the quantum of vibrational energy in a harmonic oscillator of angular frequency $\omega$ ) and the characteristic thermal energy ( $k T$, the mean energy of a thermally excited harmonic oscillator at a temperature $T$, if $k T \gg \hbar \omega$ ). The ratio $\hbar \omega / k T$ varies directly with the frequency of vibration, that is, as $L^{-1}$. An object of cubic nanometer size with $\omega=1.7 \times 10^{13} \mathrm{rad} / \mathrm{s}$ has $\hbar \omega / k T_{300} \approx 0.4\left(T_{300}=300 \mathrm{~K} ; k T_{300} \approx 4.14 \mathrm{maJ}\right)$. The associated quantum mechanical effects (e.g., on positional uncertainty) are smaller than the classical thermal effects, but still significant (see Figure 5.2).

### 2.4. Scaling of classical electromagnetic systems

### 2.4.1. Basic assumptions

In considering the scaling of electromagnetic systems, it is convenient to assume that electrostatic field strengths (and hence electrostatic stresses) are independent of scale. With this assumption, the above constant-stress, constant-speed scaling laws for mechanical systems continue to hold for electromechanical systems, so long as magnetic forces are neglected. The onset of strong field-emission currents from conductors limits the electrostatic field strength permissible at the negative electrode of a nanoscale system; values of $\sim 10^{9} \mathrm{~V} / \mathrm{m}$ can readily be tolerated (Section 11.6.2).

### 2.4.2. Major corrections

Chapter 11 describes several nanometer scale electromechanical systems, requiring consideration of the electrical conductivity of fine wires and of insulating layers thin enough to make tunneling a significant mechanism of electron transport. These phenomena are sometimes (within an expanding range of conditions) understood well enough to permit design calculations.

Corrections to classical continuum models are more important in electromagnetic systems than in mechanical systems: quantum effects, for example, become dominant and at small scales can render classical continuum models useless even as crude approximations. Electromagnetic systems on a nanometer scale commonly have extremely high frequencies, yielding large values of $\hbar \omega / k T_{300}$. Molecules undergoing electronic transitions typically absorb and emit light in the visible to ultraviolet range, rather than the infrared range characteristic of thermal excitation at room temperature. The mass of an electron is less than $10^{-3}$ that of the lightest atom, hence for comparable confining energy barriers, electron ${ }^{\circ}$ wave functions are more diffuse and permit longer-range tunneling. At high frequencies, the inertial effects of electron mass become significant, but these are neglected in the usual macroscopic expressions for electrical circuits. Accordingly, many of the following classical continuum scaling relationships fail in nanoscale systems. The assumption of scale-independent electrostatic field strengths itself fails in the opposite direction, when scaling up from the nanoscale to the macroscale: the resulting large voltages introduce additional modes of electrical breakdown. In small structures, the discrete size of the electronic charge unit, $\sim 1.6 \times 10^{-19} \mathrm{C}$, disrupts the smooth scaling of classical electrostatic relationships (Section 11.7.2c).

### 2.4.3. Magnitudes and scaling: steady-state systems

Given a scale-invariant electrostatic field strength,

$$
\begin{equation*}
\text { voltage } \propto \text { electrostatic field } \cdot \text { length } \propto L \tag{2.19}
\end{equation*}
$$

At a field strength of $10^{9} \mathrm{~V} / \mathrm{m}$, a one nanometer distance yields a $1 \mathrm{~V}$ potential difference. A scale-invariant field strength implies a force proportional to area,

$$
\begin{equation*}
\text { electrostatic force } \propto \text { area } \cdot(\text { electrostatic field })^{2} \propto L^{2} \tag{2.20}
\end{equation*}
$$

and a $1 \mathrm{~V} / \mathrm{nm}$ field between two charged surfaces yields an electrostatic force of $\sim 0.0044 \mathrm{nN} / \mathrm{nm}^{2}$.

Assuming a constant resistivity,

$$
\begin{equation*}
\text { resistance } \propto \frac{\text { length }}{\text { area }} \propto L^{-1} \tag{2.21}
\end{equation*}
$$

and a cubic nanometer block with the resistivity of copper would have a resistance of $\sim 17 \Omega$. This yields an expression for the scaling of currents,

$$
\begin{equation*}
\text { ohmic current } \propto \frac{\text { voltage }}{\text { resistance }} \propto L^{2} \tag{2.22}
\end{equation*}
$$

which leaves current density constant. In present microelectronics work, current densities in aluminum interconnections are limited to $<10^{10} \mathrm{~A} / \mathrm{m}^{2}$ or less by electromigration, which redistributes metal atoms and eventually interrupts circuit continuity (Mead and Conway, 1980). This current density equals $10 \mathrm{nA} / \mathrm{nm}^{2}$ (as discussed in Section 11.6.1b, however, present electromigration limits are unlikely to apply to well-designed eutactic conductors).

For field emission into free space, current density depends on surface properties and the electrostatic field intensity, hence

$$
\begin{equation*}
\text { field emission current } \propto \text { area } \propto L^{2} \tag{2.23}
\end{equation*}
$$

and field emission currents scale with ohmic currents. Where surfaces are close enough together for tunneling to occur from conductor to conductor, rather than from conductor to free space, this scaling relationship breaks down.

With constant field strength, electrostatic energy scales with volume:

$$
\begin{equation*}
\text { electrostatic energy } \propto \text { volume } \cdot(\text { electrostatic field })^{2} \propto L^{3} \tag{2.24}
\end{equation*}
$$

A field with a strength of $10^{9} \mathrm{~V} / \mathrm{m}$ has an energy density of $\sim 4.4 \mathrm{maJ}$ per cubic nanometer $\left(\approx k T_{300}\right)$.

Scaling of capacitance follows from the above,

$$
\begin{equation*}
\text { capacitance } \propto \frac{\text { electrostatic energy }}{(\text { voltage })^{2}} \propto L \tag{2.25}
\end{equation*}
$$

and is independent of assumptions regarding field strength. The calculated capacitance per square nanometer of a vacuum capacitor with parallel plates separated by $1 \mathrm{~nm}$ is $\sim 9 \times 10^{-21} \mathrm{~F}$; note, however, that electron tunneling causes substantial conduction through an insulating layer this thin.

In electromechanical systems dominated by electrostatic forces,

$$
\begin{equation*}
\text { electrostatic power } \propto \text { electrostatic force } \cdot \text { speed } \propto L^{2} \tag{2.26}
\end{equation*}
$$

and

$$
\begin{equation*}
\text { electrostatic power density } \propto \frac{\text { electrostatic power }}{\text { volume }} \propto L^{-1} \tag{2.27}
\end{equation*}
$$

These scaling laws are identical to those for mechanical power and power density. Like them, they suggest high power densities for small devices (see Section 11.7).

The power density caused by resistive losses scales differently, given the above current density:

$$
\begin{equation*}
\text { resistive power density } \propto(\text { current density })^{2}=\text { constant } \tag{2.28}
\end{equation*}
$$

The current density needed to power an electrostatic motor, however, scales differently from that derived from a constant-field scaling analysis. In an electrostatic motor, surfaces are charged and discharged with a certain frequency, hence

$$
\begin{equation*}
\text { motor current density } \propto \frac{\text { charge }}{\text { area }} \text { frequency } \propto \text { field } \cdot \text { frequency } \propto L^{-1} \tag{2.29}
\end{equation*}
$$

and the resistive power losses climb sharply with decreasing scale:

$$
\begin{equation*}
\text { motor resistive power density } \propto(\text { motor current density })^{2}=L^{-2} \tag{2.30}
\end{equation*}
$$

Accordingly, the efficiency of electrostatic motors decreases with decreasing scale. The absence of long conducting paths (like those in electromagnets) makes resistive losses smaller to begin with, however, and a detailed examination (Section 11.7) shows that efficiencies remain high in absolute terms for motors of submicron scale. The above relationships show that electromechanical systems cannot be scaled in the simple manner suggested for purely mechanical systems, even in the classical continuum approximation.

Electromagnets are far less attractive for nanoscale systems, since

$$
\begin{equation*}
\text { magnetic field } \propto \frac{\text { current }}{\text { distance }} \propto L \tag{2.31}
\end{equation*}
$$

At a distance of $1 \mathrm{~nm}$ from a conductor carrying a current of $10 \mathrm{nA}$, the field strength is $2 \times 10^{-6} \mathrm{~T}$. The corresponding forces,

$$
\begin{equation*}
\text { magnetic force } \propto \text { area } \cdot(\text { magnetic field })^{2} \propto L^{4} \tag{2.32}
\end{equation*}
$$

are minute in nanoscale systems: two parallel, $1 \mathrm{~nm}$ long segments of conductor, separated by $1 \mathrm{~nm}$ and carrying $10 \mathrm{nA}$, interact with a force of $2 \times 10^{-23} \mathrm{~N}$. This is 14 orders of magnitude smaller than the strength of a typical covalent bond and 11 orders of magnitude smaller than the characteristic electrostatic force just calculated. Magnetic forces between nanoscale current elements are usually negligible. Magnetic fields generated by magnetic materials, in contrast, are independent of scale: forces, energies, and so forth follow the scaling laws described for constant-field electrostatic systems. Nanoscale current elements interacting with fixed magnetic fields can produce more significant (though still small) forces: a $1 \mathrm{~nm}$ long segment of conductor carrying a $10 \mathrm{nA}$ current experiences a force of up to $10^{-17} \mathrm{~N}$ when immersed in a $1 \mathrm{~T}$ field.

The magnetic field energy of a nanoscale current element is small:

$$
\begin{equation*}
\text { magnetic energy } \propto \text { volume } \cdot(\text { magnetic field })^{2} \propto L^{5} \tag{2.33}
\end{equation*}
$$

The scaling of inductance can be derived from the above, but is independent of assumptions regarding the scaling of currents and magnetic field strengths:

$$
\begin{equation*}
\text { inductance } \propto \frac{\text { magnetic energy }}{(\text { current })^{2}} \propto L \tag{2.34}
\end{equation*}
$$

The inductance per nanometer of length for a fictitious solenoid with a $1 \mathrm{~nm}^{2}$ cross sectional area and one turn per nanometer of length would be $\sim 10^{-15} \mathrm{~h}$.

### 2.4.4. Magnitudes and scaling: time-varying systems

In systems with time-varying currents and fields, skin-depth effects increase resistance at high frequencies; these effects complicate scaling relationships and are ignored here. The following simplified relationships are included chiefly to illustrate trends and magnitudes that preclude the scaling of classical AC circuits into the nanometer size regime.

For $L R$ circuits,

$$
\begin{equation*}
\text { inductive time constant } \propto \frac{\text { inductance }}{\text { resistance }}=L^{2} \tag{2.35}
\end{equation*}
$$

Combining the characteristic $17 \Omega$ resistance and $10^{-15} \mathrm{~h}$ inductance calculated above yields an $L R$ time constant of $\sim 6 \times 10^{-17} \mathrm{~s}$. This time constant is nonphysical: it is, for example, short compared to the electron ${ }^{\circ}$ relaxation time in a typical metal at room temperature ( $\left.\sim 10^{-14} \mathrm{~s}\right)$. In reality, current decays more slowly because of electron inertia (which has effects broadly similar to those of inductance) and because of the related effect of finite electron relaxation time.

With the approximation of scale-independent resistivity,

$$
\begin{equation*}
\text { capacitative time constant } \propto \text { resistance } \cdot \text { capacitance }=\text { constant } \tag{2.36}
\end{equation*}
$$

This implies that the time required for a capacitor to discharge through a resistor in a pure $R C$ circuit is independent of scale; with the scale dependence of the $L R$ time constant, however, a structure with fixed proportions can change from a nearly pure $R C$ circuit (if built on a small scale) to a nearly pure $L R$ circuit (if built on a large scale). The nanometer-scale $R C$ time constant indicated by this expression is $(17 \Omega) \times\left(9 \times 10^{-21} \mathrm{~F}\right) \approx 1.5 \times 10^{-19} \mathrm{~s}$, but this result is nonphysical because it neglects the effects of electron inertia and relaxation time.

The $L C$ product defines an oscillation frequency

$$
\begin{equation*}
\text { oscillation frequency } \propto \sqrt{\frac{1}{\text { inductance } \cdot \text { capacitance }}} \propto L^{-1} \tag{2.37}
\end{equation*}
$$

The characteristic inductance and capacitance calculated above would yield an $L C$ circuit with an angular frequency of $\sim 3 \times 10^{17} \mathrm{rad} / \mathrm{s}$. Alternatively, in structures such as waveguides,

$$
\begin{equation*}
\text { oscillation frequency } \propto \frac{\text { wave speed }}{\text { length }} \propto L^{-1} \tag{2.38}
\end{equation*}
$$

To propagate in a hypothetical waveguide $1 \mathrm{~nm}$ in diameter, an electromagnetic wave would require a frequency of $\sim 9 \times 10^{17} \mathrm{rad} / \mathrm{s}$ or more. Even the lower of the two frequencies just mentioned corresponds to quanta with an energy of $\sim 30 \mathrm{aJ}$, that is, to photons in the $\mathrm{x}$-ray range with energies of $\sim 200 \mathrm{eV}$. These frequencies and energies are inconsistent with physical circuits and waveguides (metals are transparent to $\mathrm{x}$-rays, electrons are stripped from molecules at energies well below $200 \mathrm{eV}$, etc.). Quantum effects and electron inertia make Eq. (2.38) inapplicable in the nanometer range.

Scale also affects the quality of an oscillator:

$$
\begin{equation*}
Q \propto \text { oscillation frequency } \frac{\text { inductance }}{\text { resistance }} \propto L \tag{2.39}
\end{equation*}
$$

Since $\mathbf{Q}$ is a measure of the damping time relative to the oscillation time, small $A C$ circuits will be heavily damped unless nonclassical effects intervene.

Where the following chapters consider electromagnetic systems at all, they describe systems with currents and fields that are slowly varying by the relevant standards. High-frequency quantum electronic devices, though undoubtedly of great importance, are not discussed here.

### 2.5. Scaling of classical thermal systems

### 2.5.1. Basic assumptions

The classical continuum model assumes that volumetric heat capacities and thermal conductivities are independent of scale. Since heat flows in nanomechanical systems are typically a side effect of other physical processes, no independent assumptions are made regarding their scaling laws.

### 2.5.2. Major corrections

Classical, diffusive models for heat flow in solids can break down in several ways. On sufficiently small scales (which can be macroscopic for crystals at low temperatures) thermal energy is transferred ballistically by ${ }^{\circ}$ phonons for which the mean free path would, in the absence of bounding surfaces, exceed the dimensions of the structure in question. In the ballistic transport regime, interfacial properties analogous to optical reflectivity and emissivity become significant. Radiative heat flow is altered when the separation of surfaces becomes small compared to the characteristic wavelength of blackbody radiation, owing to coupling of nonradiative electromagnetic modes in the surfaces. In gases, separation of surfaces by less than a mean free path again modifies conductivity. The following assumes classical thermal diffusion, which can be a good approximation for liquids and for solids of low thermal conductivity, even on scales approaching the nanometer range.

### 2.5.3. Magnitudes and scaling

With a scale-independent volumetric heat capacity,

$$
\begin{equation*}
\text { heat capacity } \propto \text { volume } \propto L^{3} \tag{2.40}
\end{equation*}
$$

A cubic nanometer volume of a material with a (typical) volumetric heat capacity of $10^{6} \mathrm{~J} / \mathrm{m}^{3} \cdot \mathrm{K}$ has a heat capacity of $1 \mathrm{maJ} / \mathrm{K}$.

Thermal conductance scales like electrical conductance, with

$$
\begin{equation*}
\text { thermal conductance } \propto \frac{\text { area }}{\text { length }} \propto L \tag{2.41}
\end{equation*}
$$

and a cubic nanometer of material with a (fairly typical) thermal conductivity of $10 \mathrm{~W} / \mathrm{m} \cdot \mathrm{K}$ has a thermal conductance of $10^{-8} \mathrm{~W} / \mathrm{K}$.

Characteristic times for thermal equilibration follow from these relationships, yielding

$$
\begin{equation*}
\text { thermal time constant } \propto \frac{\text { heat capacity }}{\text { thermal conductance }} \propto L^{2} \tag{2.42}
\end{equation*}
$$

For a cubic nanometer block separated from a heat sink by a thermal path with a conductance of $10^{-8} \mathrm{~W} / \mathrm{K}$, the calculated thermal time constant is $\sim 10^{-13} \mathrm{~s}$, which is comparable to the acoustic transit time. (In an insulator, a calculated thermal time constant approaching the acoustic transit time signals a breakdown of the diffusive model for transport of thermal energy and the need for a model accounting for ballistic transport; in the fully ballistic regime, time constants scale in proportion to $L$, and thermal energy moves at the speed of sound.)

The scaling relationship for frictional power dissipation, Eq. (2.16), implies a scaling law for the temperature elevation of a device in thermal contact with its environment,

$$
\begin{equation*}
\text { temperature elevation } \propto \frac{\text { frictional power }}{\text { thermal conductance }} \propto L \tag{2.43}
\end{equation*}
$$

This indicates that nanomechanical systems are more nearly isothermal than analogous systems of macroscopic size.

Table 2.1. Summary of classical continuum scaling laws.

| Physical quantity | Scaling <br/> exponent | Typical <br/> magnitude | Scaling accuracy |
| :--- | ---: | :--- | :--- |
| Area | 2 | $10^{-18} \mathrm{~m}^{2}$ | Definitional |
| Force, strength | 2 | $10^{-8} \mathrm{~N} / \mathrm{m}^{2}$ | Good |
| Stiffness | 1 | $1000 \mathrm{~N} / \mathrm{m}$ | Good |
| Deformation | 1 | $10^{-11} \mathrm{~m}$ | Good |
| Mass | 3 | $10^{-24} \mathrm{~kg}$ | Good |
| Acceleration | -1 | $10^{15} \mathrm{~m} / \mathrm{s}^{2}$ | Good |
| Vibrational frequency | -1 | $10^{13} \mathrm{rad} / \mathrm{s}$ | Good |
| Stress-limited speed | 0 | $10^{3} \mathrm{~m} / \mathrm{s}$ | Good |
| Motion time | -1 | $10^{-12} \mathrm{to} 10^{-9} \mathrm{~s}$ | Good |
| Power | 2 | $10^{-8} \mathrm{~W}$ | Good |
| Power density | -1 | $10^{19} \mathrm{~W} / \mathrm{m}^{3}$ | Good |
| Viscous stress | -1 | $10^{6} \mathrm{~N} / \mathrm{m}^{2}$ | Moderate to poor |
| Frictional force | 2 | $\left(\mathrm{see}^{\mathrm{Ch} .10)}\right.$ | Moderate to inapplicable |
| Wear life | 1 | $\left(\mathrm{see}^{\mathrm{Ch} .6,10)}\right.$ | Moderate to inapplicable |
| Thermal speed | $-3 / 2$ | $100 \mathrm{~m} / \mathrm{s}$ | Good |
| Voltage | 1 | $1 \mathrm{~V}$ | Good at small scales |
| Electrostatic force | 2 | $10^{-12} \mathrm{~N}$ | Good at small scales |
| Resistance | -1 | $10 \Omega$ | Moderate to poor |
| Current | 2 | $10^{-8} \mathrm{~A}$ | Moderate to poor |
| Electrostatic energy | 3 | $10^{-21} \mathrm{~J}$ | Good at small scales |
| Capacitance | 1 | $10^{-20} \mathrm{~F}$ | Good |
| Magnetic field | 1 | $10^{-6} \mathrm{~T}$ | Good |
| Magnetic force | 4 | $10^{-23} \mathrm{~N}$ | Good |
| Inductance | 1 | $10^{-15} \mathrm{~h}$ | Good |
| Inductive time constant | 2 | $<10^{-16} \mathrm{~s}$ | Bad[^59] |
| Capacitive time constant | 0 | - | Moderate to poor[^60] |
| Elect. oscill. frequency | -1 | $>10^{18} \mathrm{rad} / \mathrm{s}$ | Bad[^59] |
| Oscillator Q | 1 | - | Moderate to poor[^60] |
| Heat capacity | 3 | $10^{-21} \mathrm{~J} / \mathrm{K}$ | Good |
| Thermal conductance | 1 | $10^{-8} \mathrm{~W} / \mathrm{K}$ | Good to poor |
| Thermal time constant | 2 | $10^{-13} \mathrm{~s}$ | Good to poor |

### 2.6. Beyond classical continuum models

This chapter has described the scaling laws implied by classical continuum models for mechanical, electromagnetic, and thermal systems, together with the magnitudes they suggest for the physical parameters of nanometer scale systems. It has also considered limits to the validity of these models, imposed by statistical mechanics, quantum mechanics, the molecular structure of matter, and so forth. Different classical models fail at different length scales, with the most dramatic failures appearing in AC electrical circuits.

The following chapters go beyond classical continuum models. Chapters 3 and 4 examine models of molecular structure, dynamics, and statistical mechanics from a nanomechanical systems perspective. Chapters 5 and 6 examine the combined effects of quantum and statistical mechanics on nanomechanical systems, first analyzing positional uncertainty in systems subject to a restoring force, and then analyzing the rates of transitions, errors, and damage in systems that can settle in alternative states. Chapter 7 examines mechanisms for energy dissipation. These chapters provide a foundation for analyzing specific nanomechanical systems. Later chapters examine not only nanomechanical systems, but a few specific electrical and fluid systems; where analysis of the latter must go beyond classical continuum approximations, the needed principles are discussed in context.

### 2.7. Conclusions

The accuracy of classical continuum models and scaling laws to nanoscale systems depends on the physical phenomena considered. It is low for electromagnetic systems with small calculated time constants, reasonably good for thermal systems and slowly varying electromagnetic systems, and often excellent for purely mechanical systems, provided that the component dimensions substantially exceed atomic dimensions. Scaling principles indicate that mechanical components can operate at high frequencies, accelerations, and power densities. The adverse scaling of wear lifetimes suggests that bearings are a special concern. Later chapters support these expectations regarding frequency, acceleration, and power density; Chapter 10 describes suitable bearings. Table 2.1 summarizes many of the relationships discussed in this chapter.

[^59]: Values included only to illustrate the failure of the scaling law.
[^60]: Values omitted; realistic geometries would require several arbitrary parameters.