# Energy Dissipation


### 7.1. Overview

Energy dissipation imposes constraints on the design of nanomechanical devices, particularly when they are aggregated to form macroscale systems. Owing to limits on feasible cooling capacity, energy dissipation in macroscale systems limits the feasible rate of operations, for example, in massively parallel computers. It could likewise reduce the attractiveness of nanomechanical systems relative to alternatives, for example, in performing chemical transformations that could be achieved through diffusive, solution-phase chemistry.

Despite its importance, energy dissipation seldom imposes qualitative limits, that is, constraints on the kinds of operations that can be performed on a nanoscale, as opposed to constraints on the speed and efficiency with which they can be performed. In studies of the potential of molecular nanotechnology, energy dissipation is often important to estimate, yet seldom crucial to estimate precisely. Moderate overestimates of dissipation yield conservative estimates of performance, while seldom falsely implying that a design is infeasible.

The present chapter surveys mechanisms of energy dissipation that appear significant, estimating or bounding their magnitudes. Mechanisms of energy dissipation specific to metals are ignored since the systems under consideration are chiefly dielectric; mechanisms occurring during plastic deformation are ignored (except as analogies) since, under the rules adopted in Chapter 6, any degree of plastic deformation is counted as catastrophic damage.

Several kinds of dissipation mechanisms are described. These are:

- Acoustic radiation from forced oscillations, which transports mechanical energy to remote regions where it is thermalized
- Phonon scattering, in which mechanical motions disturb ${ }^{\circ}$ phonon distributions by reflection
- ${ }^{\circ}$ Thermoelastic effects and phonon viscosity, in which elastic deformations disturb phonon distributions via anharmonic effects and shear
- Compression of potential wells, in which nonisothermal processes result in thermodynamic irreversibility
- Transitions among time-dependent potential wells, in which the merging of initially separate wells dissipates free energy by a combination of free expansion and forced oscillation.

Different mechanisms result in power dissipation rates that scale differently with speed. For acoustic radiation from an oscillating force, $P \propto v^{2}$; for radiation from an oscillating torque, $P \propto v^{4}$. Phonon scattering, thermoelastic and phonon viscosity effects, and nonisothermal compression of potential wells all (to a good approximation) exhibit $P \propto v^{2}$. Transitions among time-dependent potential wells, in contrast, are better described by $P \propto v$. Of these mechanisms, all but the last exhibit a speed-dependent energy dissipation per operation (or per unit displacement) which approaches zero as $v \rightarrow 0$.

Note that qualifiers such as typically, frequently, many systems, and the like are used throughout this chapter to indicate situations and parameters characteristic of systems of practical interest. This usage reflects the results of design and analysis from Part II of the present work. Parameter values used in sample calculations are usually chosen to yield significant but moderate energy dissipation by one or more mechanisms.

### 7.2. Radiation from forced oscillations

### 7.2.1. Overview

Time-varying forces in an extended material system can excite mechanical vibrations that are eventually thermalized. The energy dissipated in this fashion is distinct from the energy transiently stored in local elastic deformations, which is (unless subject to other dissipation mechanisms) recovered in the course of a cycle. This mode of energy dissipation is affected by the structure of the system in a substantial region surrounding the device in question. In estimating magnitudes, it is natural to begin by modeling the structure as a uniform elastic medium and the vibrations as acoustic waves in that medium. At the frequencies and energies of interest here, quantum effects are small.

The accuracy of this approximation varies, but it is good when the wavelength of the acoustic radiation is long compared to the scale of inhomogeneities in the mechanical system. Many systems considered in later chapters have structures that include an extended matrix or housing that supports numerous nanoscale moving parts. To estimate dissipation via acoustic radiation, it is reasonable to treat such a system as uniform on a scale of tens of nanometers or more. If a structural matrix of diamondlike stiffness is roughly $1 / 10$ the total mass (larger fractions lower losses), then the speed of sound across the system is $\sim(1 / 10)^{1 / 2}$ times the speed of sound in diamond, or $\sim 5000 \mathrm{~m} / \mathrm{s}$. For $\lambda=100 \mathrm{~nm}$, $\omega \approx 3 \times 10^{11} \mathrm{rad} / \mathrm{s}$. At higher frequencies, the acoustic radiation model should still yield results of the right order, so long as estimates are based on mean properties of the structure within a wavelength of the device. (Phonon scattering processes depend on material properties on a nanometer scale.)

Treating dissipation as simple acoustic radiation still leaves a complex problem. Only a few cases are treated here, and then by approximation. Acoustic radiation in fluids is commonly described; expressions for the power radiated by a pulsating sphere and a piston in a wall appear in Gray (1972); Nabarro (1987) adapts an expression for a pulsating cylinder in a fluid to describe analogous radiation losses in a solid. Of more interest in the present context is radiation resulting from a sinusoidally varying force, torque, or pressure at a point (or small region) in an elastic medium. General expressions for radiation from
a time-varying force applied at a point within a solid medium appear in the physics literature (e.g., Hudson, 1980). Sections 7.2.3, 7.2.4, and 7.2.5 derive approximations for a sinusoidally varying force, torque, and pressure. Section 7.2.6 discusses radiation from traveling disturbances in a medium, taking dislocations in crystals as a model.

### 7.2.2. Acoustic waves and the equal-speed approximation

An isotropic elastic medium supports transverse waves of velocity

$$
\begin{equation*}
v_{\mathrm{s}, \mathrm{t}}=\sqrt{G / \rho} \tag{7.1}
\end{equation*}
$$

(where $G$ is the ${ }^{\circ}$ shear modulus and $\rho$ the density), together with longitudinal waves of velocity

$$
\begin{equation*}
v_{\mathrm{s}, \ell}=\sqrt{\frac{E}{\rho} \frac{1-v}{(1+v)(1-2 v)}} \tag{7.2}
\end{equation*}
$$

where $E$ is Young's modulus and $v$ is ${ }^{\circ}$ Poisson's ratio, which [except in unusual structures of negative $v$ (Lakes, 1987)] falls in the range $0 \leq v \leq 0.5$. In an isotropic medium,

$$
\begin{equation*}
E=2 G(1+v) \tag{7.3}
\end{equation*}
$$

hence $v_{\mathrm{s}, \ell}>v_{\mathrm{s}, \mathrm{t}}$. For diamond, $v \approx 0.1$, and $v_{\mathrm{s}, \ell} \approx 1.5 v_{\mathrm{s}, \mathrm{t}}$.

Given the approximations involved in treating a nanomechanical system as a uniform medium, it is not unreasonable to add the approximation that $v_{\mathrm{s}, \ell}=v_{\mathrm{s}, \mathrm{t}}$ for waves radiated from the origin. This equal-speed approximation in effect assumes anisotropic elastic properties that simplify the mathematics, rather than making the mathematics fit an arbitrarily assumed isotropy. The equalspeed approximation also underlies the standard Debye model of heat capacity and phonon distributions. It is used extensively in the phonon-drag models of Section 7.3.

### 7.2.3. Oscillating force at a point

Many mechanical systems cause disturbances that can be approximated by an oscillating force applied to a point. Among these are unbalanced rotors, reciprocating power-driven mechanisms, and vibrating, elastically restrained masses.

a. A model. With the equal-speed approximation (Section 7.2.2), propagating disturbances can be a function of radius alone: the restoring forces between uniformly displaced spherical shells are then uniform over each shell, leading to uniform accelerations and continued spherical uniformity of displacements. The linearized dynamical equation has the form

$$
\begin{equation*}
\frac{\partial}{\partial r}\left(4 \pi r^{2} M \frac{\partial}{\partial r} \mathrm{y}(r, t)\right)=4 \pi r^{2} \rho \frac{\partial^{2}}{\partial t^{2}} \mathrm{y}(r, t) \tag{7.4}
\end{equation*}
$$

where the function $\mathrm{y}(r, t)$ specifies a displacement along the line of the force, and $M$ is a modulus of elasticity, uniform in magnitude but differing in nature from the axis aligned with the force [where it is equivalent to $E(1-v) /(1+v)(1-2 v)$ ] to the plane perpendicular to that axis (where it is equivalent to $G$ ).

The oscillating force of amplitude $F_{\max }$ is introduced through the boundary condition

$$
\begin{equation*}
\left.4 \pi r^{2} M \frac{\partial}{\partial r} \mathrm{y}(r, t)\right|_{r=0}=F_{\max } \sin (\omega t) \tag{7.5}
\end{equation*}
$$

and solutions corresponding to outbound waves are required. These constraints yield

$$
\begin{equation*}
\mathrm{y}(r, t)=-\frac{F_{\max }}{4 \pi M r} \sin \omega(t-r \sqrt{\rho / M}) \tag{7.6}
\end{equation*}
$$

The instantaneous power at a given radius is the force transmitted times the velocity

$$
\begin{equation*}
P=\left(4 \pi r^{2} M \frac{\partial}{\partial r} \mathrm{y}(r, t)\right) \frac{\partial}{\partial t} \mathrm{y}(r, t) \tag{7.7}
\end{equation*}
$$

which has a time-average value equaling the isotropic mean radiated power

$$
\begin{equation*}
P_{\mathrm{rad}}=F_{\max }^{2} \omega^{2} \sqrt{\rho} \frac{1}{8 \pi M^{3 / 2}} \tag{7.8}
\end{equation*}
$$

b. Damping of an embedded harmonic oscillator. A harmonic oscillator like that in Figure 7.1 is damped by acoustic radiation. At a given amplitude, the force is related to the energy and effective stiffness by

$$
\begin{equation*}
F_{\max }=\sqrt{2 k_{\mathrm{s}} \mathscr{E}} \tag{7.9}
\end{equation*}
$$

Equating the net radiated power to the time-average value, Eq. (7.8), yields an exponential decay of the oscillation energy with a time constant (in seconds) of

$$
\begin{equation*}
\tau_{\mathrm{osc}} \approx \frac{4 \pi m M^{3 / 2}}{k_{\mathrm{s}}^{2} \sqrt{\rho}} \tag{7.10}
\end{equation*}
$$

Alternatively, the fractional energy loss per cycle can be expressed as

$$
\begin{equation*}
f \approx \frac{1}{2} \sqrt{\rho / m}\left(k_{\mathrm{s}} / \mathrm{M}\right)^{3 / 2} \tag{7.11}
\end{equation*}
$$

for $f \ll 1$.

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-17.jpg?height=362&width=721&top_left_y=1751&top_left_x=515)

Figure 7.1. Model of a mechanical harmonic oscillator embedded in a medium. The oscillator can be treated as a point source of force so long as its dimensions are small compared to the wavelength of the sound emitted at its characteristic frequency.

Many systems of low stiffness will be constrained by nonbonded interactions with strong anharmonicity. In the limiting case, the stiffness at equilibrium is small, and the oscillation can be viewed as a series of collisions with bounding walls. Energy loss is then better modeled using thermal accommodation coefficients (Section 7.5.1).

### 7.2.4. Oscillating torque at a point

Torsional harmonic oscillators are directly analogous to the linear oscillators just discussed, and can be modeled as sinusoidally varying torques applied to a point. The potential energy of an imperfect bearing varies with the rotational angle, causing a varying torque. For a bearing in uniform rotation, the resulting torque can be treated as a sum of sinusoidally varying components, each causing acoustic radiation.

a. A model. An oscillating torque in a uniform, isotropic medium radiates pure shear waves, hence such media serve as a convenient approximation for real systems. The analysis roughly parallels that given in Section 7.2.3. Again, spherical shells can be treated as undergoing rigid motion (here rotation rather than displacement), reducing the problem to a linearized equation with a single spatial dimension. The linearized dynamical equation is

$$
\begin{equation*}
\frac{\partial}{\partial r}\left(\frac{8}{3} \pi r^{4} G \frac{\partial}{\partial r} \mathrm{y}_{\theta}(r, t)\right)=\frac{8}{3} \pi r^{4} \rho \frac{\partial^{2}}{\partial t^{2}} \mathrm{y}_{\theta}(r, t) \tag{7.12}
\end{equation*}
$$

where the function $\mathrm{y}_{\theta}(r, t)$ specifies an angular displacement about the axis of the applied torque, which sets the boundary condition at the origin:

$$
\begin{equation*}
\left.\frac{8}{3} \pi r^{4} G \frac{\partial}{\partial r} \mathrm{y}_{\theta}(r, t)\right|_{r=0}=T_{\max } \cos (\omega t) \tag{7.13}
\end{equation*}
$$

Together with the requirement for outbound waves, this yields the solution

$$
\begin{equation*}
\mathrm{y}_{\theta}(r, t)=\frac{T_{\max } \omega \sqrt{\rho}}{8 \pi G^{3 / 2}}\left[\frac{1}{r^{2}} \sin \omega\left(t-r \sqrt{\frac{\rho}{G}}\right)+\frac{1}{r^{3} \omega} \sqrt{\frac{G}{\rho}} \cos \omega\left(t-r \sqrt{\frac{\rho}{G}}\right)\right] \tag{7.14}
\end{equation*}
$$

(which includes a near-field component). This solution implies a time-average radiated power

$$
\begin{equation*}
P_{\mathrm{rad}}=T_{\max }^{2} \omega^{4} \frac{\rho^{3 / 2}}{48 \pi G^{5 / 2}} \tag{7.15}
\end{equation*}
$$

which is steeply dependent on frequency.

b. Damping of an embedded torsional harmonic oscillator. Paralleling the development in Section 7.2.3b, a torsional harmonic oscillator characterized by an angular spring constant $k_{\theta}\left(\mathrm{J} / \mathrm{rad}^{2}\right)$ and a moment of inertia $I\left(\mathrm{~kg} \cdot \mathrm{m}^{2}\right)$ has a time constant for radiative decay of oscillation energy

$$
\begin{equation*}
\tau_{\mathrm{osc}} \approx \frac{24 \pi I^{2} G^{5 / 2}}{k_{\theta}^{3} \rho^{3 / 2}} \tag{7.16}
\end{equation*}
$$

and a fractional energy loss per cycle

$$
\begin{equation*}
f \approx \frac{1}{12}(\rho / I)^{3 / 2}\left(k_{\theta} / \mathrm{G}\right)^{5 / 2} \tag{7.17}
\end{equation*}
$$

### 7.2.5. Oscillating pressure in a volume

A component sliding through a channel with corrugated walls exerts a varying pressure on its surroundings. The force applied in one direction is balanced by the force applied in the opposite direction, distinguishing this from the case described in Section 7.2.3. This and related systems can be modeled as a sinusoidally varying pressure in a spherical cavity.

a. A model. An oscillating pressure in a spherical cavity in an isotropic, homogeneous medium radiates spherical, longitudinal waves. In the near field, however, hoop stresses transverse to the wave can play a dominant role in the balance of forces. The materials of greatest engineering interest have low values of $v$; for example, diamond has $v \approx 0.1$; the analysis can be simplified and rendered somewhat more conservative by assuming $v=0$ and treating the effective modulus $M$ as equal to ${ }^{\circ}$ Young's modulus $E$. With these approximations, the linearized dynamical equation is

$$
\begin{equation*}
\frac{\partial}{\partial r}\left(4 \pi r^{2} M \frac{\partial}{\partial r} \mathrm{y}(r, t)\right)-8 \pi M \mathrm{y}(r, t)=4 \pi r^{2} \rho \frac{\partial^{2}}{\partial t^{2}} \mathrm{y}(r, t) \tag{7.18}
\end{equation*}
$$

where the function $y(r, t)$ specifies a radial displacement. Because the effects of the applied pressure are opposed and contained by surrounding layers of the medium in a way impossible for forces or torques (which must be transmitted), a radius of application $r_{0}$ must be defined for the applied pressure $p$ and the associated total force $F\left(=\pi r^{2} p\right)$. The boundary condition imposed by the oscillating force is then

$$
\begin{equation*}
\left.4 \pi r^{2} M \frac{\partial}{\partial r} \mathrm{y}(r, t)\right|_{r=r_{0}}=F_{\max } \sin (\omega t) \tag{7.19}
\end{equation*}
$$

Together with the requirement for outbound waves, this yields the solution

$$
\begin{align*}
\mathrm{y}(r, t)= & \frac{F_{\max }}{4 \pi M}\left(\frac{\rho \omega^{2} r_{0}^{2}}{M}+\frac{4 M}{\rho \omega^{2} r_{0}^{2}}\right)^{-1 / 2}  \tag{7.20}\\
& \times\left[\frac{1}{r} \sin \omega\left(t-r \sqrt{\frac{\rho}{M}}\right)-\frac{1}{\omega r^{2}} \sqrt{\frac{M}{\rho}} \cos \omega\left(t-r \sqrt{\frac{\rho}{M}}\right)\right]
\end{align*}
$$

This again includes a near-field component. This solution implies a time-average radiated power

$$
\begin{equation*}
P_{\mathrm{rad}}=F_{\max }^{2} \omega^{2} \sqrt{\rho} \frac{1}{16 \pi M^{3 / 2}}\left(\frac{\rho \omega^{2} r_{0}^{2}}{2 M}+\frac{2 M}{\rho \omega^{2} r_{0}^{2}}\right)^{-1} \tag{7.21}
\end{equation*}
$$

The trailing factor, in parentheses, strongly reduces the radiated power when the radius of the driven region is small compared to the radiated wavelength.

### 7.2.6. Moving disturbances

a. Dislocations as a model. Dislocations provide a model for nanometerscale mechanical disturbances moving through a medium, exhibiting many distinct energy dissipation mechanisms. The major role of dislocation motion in
determining the strength of bulk materials has encouraged extensive analysis and experimentation; recent reviews include Nabarro (1987) and Alshits and Indenbom (1986). Several of the following sections draw directly or indirectly on this body of analysis.

b. Subsonic disturbances. Among the sources of moving mechanical disturbance are objects sliding or rolling on a surface and alignment bands (Section 7.3.5a) in sliding interfaces. At any given point, the motion imposed by a moving disturbance takes the form of an imposed oscillation. Nonetheless, in a uniform environment, a uniform disturbance moving at a uniform, subsonic speed radiates no acoustic power. In a real system, inhomogeneities and variations in speed and in force as a function of time cause forced-oscillation radiation, but these mechanisms can be considered separately.

c. Supersonic disturbances. Material motions of subsonic speed can cause supersonic patterns of disturbance. The chief mechanism of interest here is the motion of bands of atomic alignment (closely analogous to dislocations) in sliding interfaces.

Figure 7.2 illustrates the geometry for two rows of atomic bumps, with spatial frequencies $\boldsymbol{k}_{1}$ and $\boldsymbol{k}_{2}(\mathrm{rad} / \mathrm{m})$. Panels (a), (b), and (c) show three successive configurations as surface 2 moves over surface 1 : the arrow to the left shows the motion of an atom in surface 2 ; the arrow to the right shows the motion of an alignment band. Taking $v$ as the velocity of 2 with respect to 1 , and $k_{2}$ as the spatial frequency of surface 2 , it can be seen that the spatial frequency of the alignment bands is $\left|k_{\text {bands }}\right|=\left|k_{2}-k_{1}\right|$, and that the velocity ratio $R$ is

$$
\begin{equation*}
R=\frac{v_{\text {bands }}}{v}=\frac{\left|k_{1}\right|}{\left|k_{2}-k_{1}\right|} \tag{7.22}
\end{equation*}
$$

which can attain arbitrarily high values as $\left|\boldsymbol{k}_{1}-\boldsymbol{k}_{2}\right| \rightarrow 0$.

More generally, each surface can be viewed as having many sets of rows, with sets being described by wave vectors that are not necessarily collinear with each other, or with the sliding velocity vector. Interpreting $\boldsymbol{k}_{1}$ and $\boldsymbol{k}_{2}$ as vectors with signs chosen to minimize $\left|k_{2}-k_{1}\right|$, each pair of opposed row-sets defines a set of alignment bands in which $\boldsymbol{k}_{\text {bands }}=\boldsymbol{k}_{2}-\boldsymbol{k}_{1}$. From a geometrical construction, it

(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-20.jpg?height=415&width=622&top_left_y=1662&top_left_x=514)

Figure 7.2. The motion of bands of atomic alignment as two surfaces with differing row spacings slide over each other. Panels (a), (b), and (c) represent three successive positions, the left-hand arrow traces the motion of an atom in surface 1; the right-hand arrow traces the motion of an alignment band between the surfaces.

can be seen that

$$
\begin{align*}
R & =\frac{v_{\text {bands }}}{v}=\left|\left(k_{2}-k_{1}\right) \frac{\left|k_{1}\right|}{\left|k_{2}-k_{1}\right|^{2}} \cos \theta+\frac{k_{1} \times\left(k_{2} \times k_{1}\right)}{\left|k_{1} \times\left(k_{2} \times k_{1}\right)\right|} \sin \theta\right|  \tag{7.23}\\
& \leq \frac{\left|k_{1}\right|}{\left|k_{2}-k_{1}\right|}+1
\end{align*}
$$

where $\theta$ measures the angle between the velocity vector $v$ and the vector $k_{1}$.

In the limiting case, $\left|\boldsymbol{k}_{2}-\boldsymbol{k}_{1}\right|=0, R=\infty$, and the interface as a whole periodically enters and leaves the aligned state, radiating sound like an oscillating piston [Eq. (7.21), considering the power per unit area in the limit of large $r_{0}$ ]. This limiting case sets an upper bound to the power dissipation of supersonic alignment bands. Nanomechanical bearings of several kinds contain sliding interfaces (Chapter 10). The present work adopts the design constraint that the alignmentband speeds remain subsonic, thereby avoiding this mode of energy dissipation.

The limiting case just described can be modeled as a compliant interface in which a sinusoidal variation in the equilibrium separation occurs at a frequency $\omega=k v$. The time-average radiated power is then

$$
\begin{equation*}
P_{\mathrm{rad}}=A^{2} \omega^{2} \sqrt{M \rho}\left(M \rho \omega^{2} / k_{\mathrm{a}}^{2}+4\right)^{-1} S \tag{7.24}
\end{equation*}
$$

where $S$ is the area of the interface, $A$ is the amplitude of the variation in equilibrium separation (the limit of the actual amplitude as $\omega \rightarrow 0$ ), both media are assumed identical, and the calculated value includes power radiated from both sides of the surface. Typically, unless $\omega$ is unusually high or the interfacial stiffness $k_{\mathrm{a}}$ is unusually low, the approximation

$$
\begin{equation*}
P_{\mathrm{rad}} \approx A^{2} \omega^{2} \sqrt{M \rho} \frac{S}{4} \tag{7.25}
\end{equation*}
$$

is accurate (it is always conservative). For $M=10^{11} \mathrm{~N} / \mathrm{m}^{2}, \rho=2000 \mathrm{~kg} / \mathrm{m}^{3}, k=$ $2 \times 10^{10} \mathrm{rad} / \mathrm{m}$, and $A=0.05 \mathrm{~nm}$, the radiated acoustic power is $\sim 4 \times 10^{6} \mathrm{~W} / \mathrm{m}^{2}$ at a speed of $1 \mathrm{~m} / \mathrm{s}$, and $\sim 4 \times 10^{2} \mathrm{~W} / \mathrm{m}^{2}$ at a speed of $1 \mathrm{~cm} / \mathrm{s}$. Again, most sliding interfaces need not suffer losses by this mechanism.

d. Nonadiabatic processes. J. Soreff (1991) notes that, if one surface of a sliding interface is modeled as an array of atomic-scale harmonic oscillators, these are exposed to mechanical perturbations resulting from the passage of atomic features on the other surface and are subject to excitation at some rate by nonadiabatic processes (that is, "nonadiabatic" in the quantum-mechanical rather than the thermodynamic sense). From first-order perturbation theory (Kogan and Galitskiy, 1963), the probability of an encounter causing an excitation is proportional to a ratio of the perturbing energy to the oscillator quantal energy $(\hbar \omega)$, a quantity typically of order unity, times the factor $\exp (-2 \omega \tau)$, where $\tau$ is the characteristic time of the perturbation. Since $\omega \tau \approx v_{s} / v$, Soreff observes that $\exp (-2 \omega \tau)$ typically is extremely small. For example, in a material with $v_{\mathrm{s}}=10^{4} \mathrm{~m} / \mathrm{s}$, a system with $v$ as high as $10^{2} \mathrm{~m} / \mathrm{s}$ has a transition probability on the order of $10^{-85}$. In a typical system, a single excitation dissipates $\sim 1 \mathrm{maJ}$.

### 7.3. Phonons and phonon scattering

### 7.3.1. Phonon momentum and pressure

Thermal phonons in a crystal resemble blackbody radiation in a cavity, and both resemble a gas. As discussed further in Sections 7.3.3, 7.4.1, and 7.4.2, the phonon gas is responsible for energy dissipation by several mechanisms analogous to those in ordinary gases. Here, we consider drag resulting from scattered and reflected phonons.

In calculating drag owing to scattering, phonons can be treated (Lothe, 1962) as having a momentum equal to their quasi-momentum (i.e., crystal momentum), of magnitude

$$
\begin{equation*}
|\mathbf{p}|=\hbar \mathfrak{k}=\hbar \omega / v_{\mathrm{s}}=\mathscr{E} / v_{\mathrm{s}} \tag{7.26}
\end{equation*}
$$

where $k$ in this section is to be taken as the magnitude of the wave vector (in $\mathrm{rad} / \mathrm{m}$ ) and $v_{\mathrm{s}}$ is the speed of sound (here again approximated as constant for all frequencies and modes). With the substitution of $c$ for $v_{\mathrm{s}}$, Eq. (7.26) also describes the momentum of photons in vacuum.

A phonon-reflecting surface in an isotropic medium with an energy density $\varepsilon$ experiences a pressure

$$
\begin{equation*}
p=\varepsilon / 3 \tag{7.27}
\end{equation*}
$$

Note that this pressure is exerted on a (hypothetical) surface able to move with respect to the medium, but not on features, such as a free surface of a crystal, that can move only by virtue of elastic deformation of the medium. Accordingly, phonon pressure makes no contribution to the thermal coefficient of expansion, which for an ideal harmonic crystal is zero (Ashcroft and Mermin, 1976).

### 7.3.2. The Debye model of the phonon energy density

Phonon scattering drag depends on the phonon energy density and (more generally) on the energy distribution vs. wave vector. The commonly used Debye model of the distribution (discussed at greater length in Ashcroft and Mermin, 1976) assumes that all waves propagate at a uniform speed $v_{\mathrm{s}}$. It gives the total phonon energy density as an integral over a spherical volume in $\boldsymbol{k}$-space,

$$
\begin{equation*}
\varepsilon=\frac{3 \hbar v_{s}}{2 \pi^{2}} \int_{0}^{k_{\mathrm{D}}} k^{3}\left[\exp \left(\hbar k v_{s} / k T\right)-1\right]^{-1} d k \tag{7.28}
\end{equation*}
$$

where $\boldsymbol{k}$ is to be interpreted as the magnitude of the wave vector, and $\boldsymbol{k}_{\mathrm{D}}$ (the Debye radius) is a function of $n_{\mathrm{v}}$, the atomic number density $\left(\mathrm{m}^{-3}\right)$ :

$$
\begin{equation*}
k_{\mathrm{D}}=\left(6 \pi n_{\mathrm{v}}\right)^{1 / 3} \tag{7.29}
\end{equation*}
$$

The Debye temperature

$$
\begin{equation*}
T_{\mathrm{D}}=\hbar k_{\mathrm{D}} v_{s} / k \tag{7.30}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-23.jpg?height=716&width=1051&top_left_y=158&top_left_x=343)

Figure 7.3. Phonon energy density per unit interval of $k$ in the Debye model for $n_{\mathrm{v}}=$ $100 / \mathrm{nm}^{3}$ and $T=300 \mathrm{~K}$, normalized to constant total energy. The maximum value of $\boldsymbol{k}=$ $\boldsymbol{k}_{\mathrm{D}}=1.24 \times 10^{10} \mathrm{rad} / \mathrm{m}$.

is a measure of the temperature at which the highest-frequency modes of a solid are excited. For $T \ll T_{\mathrm{D}}, \varepsilon \propto T^{4}$, as in blackbody radiation. To yield the correct value of the phonon energy density for $T \ll T_{\mathrm{D}}, v_{\mathrm{s}}$ in the preceding expressions must (in an isotropic material) be taken as

$$
\begin{equation*}
v_{\mathrm{s}}=\left(\frac{1}{3} v_{\mathrm{s}, \ell}^{-3}+\frac{2}{3} v_{\mathrm{s}, \mathrm{t}}^{-3}\right)^{-1 / 3} \tag{7.31}
\end{equation*}
$$

which has a maximum value of $1.084 v_{\mathrm{s}, \mathrm{t}}$ in the limiting case of $E=2 G$. For a hypothetical isotropic substance with $v_{\mathrm{s}, \mathrm{t}}$ and $v_{\mathrm{s}, \ell}$ equal to those of diamond along an axis of cubic symmetry, these relations give $v_{\mathrm{s}}=1.38 \times 10^{4} \mathrm{~m} / \mathrm{s}$ and $T_{\mathrm{D}}=$ $1570 \mathrm{~K}$ [vs. a value for diamond itself of $2230 \mathrm{~K}$ (Gray, 1972)]. Phonon energy distributions and magnitudes according to the Debye model are plotted in Figures 7.3 and 7.4.

The Debye model has several shortcomings in describing real crystals, to say nothing of nanomechanical systems treated as continuous media; in the present context, its chief defects arise from its neglect of waves of low group velocity. Near the limiting value of $k$, acoustic dispersion (ignored in the Debye model) results in group velocities approaching zero. The Debye model also neglects socalled optical modes of vibration, which typically have low group velocities. The effect of these shortcomings can be significant, but typically is small for $T \ll T_{\mathrm{D}}$ (Alshits and Indenbom, 1986).

### 7.3.3. Phonon scattering drag

A scattering center moving with velocity $v$ experiences drag from the "phonon wind" resulting from its velocity (Alshits and Indenbom, 1986); this can be treated as analogous to scattering of photons in a vacuum. In the simplest situation, a scattering center has both an isotropic cross section in the rest frame and an isotropic emission pattern in its own frame. Drag can then be calculated from

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-24.jpg?height=1500&width=1088&top_left_y=176&top_left_x=223)

Figure 7.4. Phonon energy density in the Debye model vs. the effective speed of sound, $v_{\mathrm{s}}$, and the atomic number density, $\boldsymbol{n}$. For perspective, in diamond the effective speed $v_{\mathrm{s}} \approx 13.8 \mathrm{~km} / \mathrm{s}$, Eq. (7.31), and $n \approx 176 / \mathrm{nm}^{3}$.

the anisotropic momentum distributions and encounter frequencies of phonons seen in the moving frame.

Phonons approaching at an angle $\theta$ from the forward direction are Doppler shifted, changing their frequency and energy by a factor $\left[1+v \cos (\theta) / v_{\mathrm{s}}\right]$; the rate of encounter for phonons from this direction is altered by the same factor. Phonons approaching from the side experience an aberrational shift in direction through an angle $-v \sin (\theta) / \nu_{\mathrm{s}}$ (for $v \ll v_{\mathrm{s}}$ ). Combining these factors, discarding terms of order $v^{2} / v_{\mathrm{s}}^{2}$ and higher, and integrating yields an approximation to the
phonon-scattering drag and power dissipation for the scattering center:

$$
\begin{equation*}
F_{\text {drag }} \approx-\frac{4}{3} \varepsilon \sigma_{\text {therm }} \frac{v}{v_{\mathrm{s}}}, \quad P_{\text {drag }} \approx \frac{4}{3} \varepsilon \sigma_{\text {therm }} \frac{v^{2}}{v_{\mathrm{s}}} \tag{7.32}
\end{equation*}
$$

where $\sigma_{\text {therm }}$ is a thermally weighted scattering cross section (in $\mathrm{m}^{2}$ ) derived from a scattering cross section $\sigma(k)$ that is a function of the magnitude of the wave vector. For the Debye model of the phonon distribution,

$$
\begin{equation*}
\sigma_{\text {therm }}=\frac{\int_{0}^{k} \mathrm{D}(k) k^{3}\left[\exp \left(\frac{\hbar k v_{s}}{k T}\right)-1\right]^{-1} d k}{\int_{0}^{k} \mathrm{D} k^{3}\left[\exp \left(\frac{\hbar k v_{s}}{k T}\right)-1\right]^{-1} d k} \tag{7.33}
\end{equation*}
$$

### 7.3.4. Scattering from harmonic oscillators

Various nanomechanical components can be treated as moving scattering centers. A roller bearing moving across a surface, $a^{\circ}$ follower moving over $a^{\circ} \mathrm{cam}$, an object sliding in a tube: each results in the motion of a small region of contact with respect to a medium. The effect of the contact can be modeled as an embedded harmonic oscillator of the sort described in Section 7.2.3b, excited by incident phonons and radiating to a degree that can be approximated by Eq. (7.8). (Dissipation from broad sliding contacts of regular structure can be modeled as described in Sections 7.3.5, 7.3.6, and 7.4.3.)

In the limit of large mass and low stiffness, the motion of the mass is small and the oscillating force is proportional to the stiffness, making $\sigma \circ k_{\mathrm{s}}^{2}$. In the limit of low mass and large stiffness, the deformation of the spring is small and the force is proportional to the mass, making $\sigma \propto m^{2}$. In general, far from resonance,

$$
\begin{equation*}
\sigma \approx \frac{1}{2 \pi}\left(\frac{k_{\mathrm{s}}}{\mathrm{M}}\right)^{2}\left(\frac{k_{\mathrm{s}}}{\mathrm{m} \omega^{2}}+1\right)^{-2} \tag{7.34}
\end{equation*}
$$

Resonant scattering occurs when $k v_{\mathrm{s}} \approx\left(k_{\mathrm{s}} / m\right)^{1 / 2}$, with resonant cross sections limited by radiation damping. Values of $\sigma_{\text {therm }}$ can be estimated by numerical integration of the damped harmonic oscillator cross section over the Debye phonon distribution. The results for representative values of material parameters at $300 \mathrm{~K}$ are graphed in Figure 7.5, for oscillators with isotropic effective stiffnesses and masses. For oscillators with differing values along three principal axes, the cross section is the mean of those that would be exhibited by three isotropic oscillators with these values.

A sliding scattering center typically is coupled to the medium by nonbonded interactions. The relationships summarized in Figure 3.8 suggest that, regardless of how low the equilibrium stiffness may be, thermal excitation of small scattering centers at $300 \mathrm{~K}$ frequently explores regions in which the stiffness is of the order of $10 \mathrm{~N} / \mathrm{m}$. Thus, anharmonicity and thermal excitation place an effective lower bound on the effective mean stiffness, and hence on the phonon scattering cross section.

It is useful to examine the magnitude of drag for a typical case. A sliding contact with a stiffness of $\sim 30 \mathrm{~N} / \mathrm{m}$ has $\sigma \approx 10^{-20} \mathrm{~m}^{2}$ in a moderately stiff medium. With $v_{\mathrm{s}} \approx 10^{4} \mathrm{~m} / \mathrm{s}$ and $\varepsilon \approx 2 \times 10^{8} \mathrm{~J} / \mathrm{m}^{3}$, the power dissipation [Eq. (7.32)] is

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-26.jpg?height=724&width=1107&top_left_y=183&top_left_x=209)

Figure 7.5. Values of $\sigma_{\text {therm }}$ at $300 \mathrm{~K}$ for a range of values of $m$ and $k_{\mathrm{s}}$ and three values of the modulus $M$. For perspective, $10^{-25} \mathrm{~kg}$ is the approximate mass of 5 carbon atoms, and the Young's modulus of diamond is $\sim 1000 \mathrm{GPa}\left(=10^{12} \mathrm{~N} / \mathrm{m}^{2}\right)$. The assumed density is $2000 \mathrm{~kg} / \mathrm{m}^{2}$ (vs. $\sim 3500$ for diamond), with $n_{\mathrm{v}}=100 / \mathrm{nm}^{3}$.

$\sim 3 \times 10^{-16} \mathrm{~W}$ at $1 \mathrm{~m} / \mathrm{s}$ and $\sim 3 \times 10^{-20} \mathrm{~W}$ at $1 \mathrm{~cm} / \mathrm{s}$, or (equivalently) $3 \times 10^{-25}$ and $3 \times 10^{-27} \mathrm{~J} / \mathrm{nm}$ traveled.

### 7.3.5. Scattering from alignment bands in bearings

a. Alignment bands in bearings. Sliding interfaces between regular surfaces contain alignment bands that are closely analogous to dislocations. Phononscattering drag plays a major role in dislocation dynamics and has accordingly received substantial attention (Alshits and Indenbom, 1986; Lothe, 1962; Nabarro, 1987). Causes of scattering include both the mechanical inhomogeneity of the dislocation core and flutter, in which phonons excite oscillations in dislocations, which then reradiate power.

In typical materials, dislocations are narrow, causing severe disruption of crystalline alignment over $\sim 5$ atomic spacings (Lothe, 1962), and inducing local variations in stress that are significant compared to the modulus $E$. Alignment bands in sliding-interface bearings, however, typically are broad and induce only small variations in stress. These variations in stress, however, can yield significant variations in the stiffness of the interface owing to the strong anharmonicity of nonbonded interactions (Section 3.3.2e). Alignment bands are sufficiently similar to dislocations that analogues of both flutter scattering and inhomogeneity scattering occur, yet are different enough to invalidate the approximations that have been used to model them. Suitable approximations are developed in Sections 7.3.5b-7.3.5e.

b. Common features of the models. Alignment bands in interfaces can be modeled as sinusoidally varying disturbances moving at a speed $v_{\text {bands }}$, related to the sliding speed $v$ by Eq. (7.22) or the final expression in Eq. (7.23), in two limiting cases. The nature of the disturbance varies with the mode of scattering.

Both flutter scattering and stiffness scattering are here described by approximate models, intended to provide only upper bounds.

In many systems of engineering interest, the shear stresses transmitted across the interface are small compared to the normal stresses, and the shear stiffnesses are likewise small compared to the normal stiffnesses. Shear stresses and stiffnesses are accordingly neglected in the following discussion, although their treatment would be entirely analogous.

As noted by Soreff (1991), the assumption that $v_{\mathrm{s}, \ell}=v_{\mathrm{s}, \mathrm{t}}$ permits waves to be resolved into components with $x, y$, and $z$ polarizations, where the polarization axes may be chosen for convenience, without regard to the direction of propagation. For scattering from band stiffness variations, only polarizations perpendicular to the interface are relevant; for flutter scattering, only polarizations parallel to the interface and oriented in the band-shifting direction are relevant.

c. Band-stiffness scattering. The interface can be treated as a compliant sheet with a stiffness per unit area $k_{\mathrm{a}}$ and a transmission coefficient (Section 7.3.5e) of $T_{\text {trans }}$ (this coefficient includes the factor of $1 / 3$ resulting from the effectiveness of only one of three polarizations). The mechanical inhomogeneity of the alignment bands can be approximately described as a sinusoidal variation in stiffness of amplitude $\Delta k_{\mathrm{a}} / 2$, which (across interfaces with small values of $T_{\text {trans }}$ ) causes variations in the transmission coefficient on the order of $\Delta T_{\text {trans }}=$ 1.7 $T_{\text {trans }} \Delta k_{\mathrm{a}} / k_{\mathrm{a}}$ (Section 7.3.5e).

Neither specular reflection nor simple transmission of phonons contributes to the drag, but a fraction of incident phonons $\leq \Delta T_{\text {trans }}$ is subject to diffractive scattering from the bands owing to the spatial variation in the transmission (and accordingly reflection) coefficient. For normally incident phonons of $k \gg k_{\text {bands }}$, the diffraction angle is small, and for $k<k_{\text {bands }}$, it is zero. In these cases, the scattering contribution to drag is relatively small or nonexistent. (Owing to the angular variation in the transmission coefficient, the actual results are strongly influenced by the diffraction of phonons at grazing incidence.) The present estimate nonetheless assumes isotropic scattering for all $k$, tending to overestimate the drag.

The incident power on a single side of a surface is $v_{\mathrm{s}} \varepsilon / 4$, and hence the average collision cross section for a flat surface of area $S$ (counting both sides and all angles of incidence) is $S / 2$. (The quantity $\varepsilon / 4$ appears frequently in normalization expressions and can be termed the effective energy density.) Combining these factors yields the bound

$$
\begin{equation*}
P_{\text {drag }}<0.85 \varepsilon T_{\text {trans }} \frac{\Delta k_{\mathrm{a}}}{k_{\mathrm{a}}} R^{2} \frac{v^{2}}{v_{\mathrm{s}}} S \tag{7.35}
\end{equation*}
$$

where $v$ is the sliding speed of the interface and a factor of order unity [analogous to the $4 / 3$ in Eq. (7.32)] has been dropped. (Note that this and similar expressions do not hold when the value of $k_{\mathrm{a}} \approx 0$.)

As discussed in Chapter 10, $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}$ can be made small in properly designed bearings of certain classes, and values of $T_{\text {trans }}$ (Section 7.3.5e) can easily be less than $10^{-3}$. A not-atypical value for $R$ is 10 . For these values, with $\Delta k_{\mathrm{a}} / k_{\mathrm{a}} \approx 0.1$, $v_{\mathrm{s}}=10^{4} \mathrm{~m} / \mathrm{s}$, and $\varepsilon=2 \times 10^{8} \mathrm{~J} / \mathrm{m}^{3}, P_{\text {drag }}$ from this mechanism is bounded by
$\sim 200 \mathrm{~W} / \mathrm{m}^{2}$ at $v=1 \mathrm{~m} / \mathrm{s}$, and $\sim 0.02 \mathrm{~W} / \mathrm{m}^{2}$ at $1 \mathrm{~cm} / \mathrm{s}$. The latter values correspond to $2 \times 10^{-25}$ and $2 \times 10^{-27} \mathrm{~J} / \mathrm{nm}^{2}$ per nanometer of travel.

d. Band-flutter scattering. Alignment bands also cause deformations of the equilibrium shape of each surface of the interface with amplitude $A$ and spatial frequency $\boldsymbol{k}_{\text {bands }}$; this results in sinusoidally varying slopes with a maximum magnitude of $A \boldsymbol{k}_{\text {bands }}$. A shear wave of the proper polarization causes the bands to move by a distance that is a multiple $R$ [see Eqs. (7.22) and (7.23)] of the particle displacements caused by the shear wave itself. The ratio of the amplitude of the equilibrium displacement of the interface to the amplitude of the incident shear wave is $A k_{\text {bands }} R$. These displacements are like those imposed by an incident wave of perpendicular polarization and scaled amplitude; after this transformation, the interface can again be regarded as a moving diffraction grating.

Taking the mean square value of the slope over the interface introduces a factor of $1 / 2$ in the scattered power; consideration of radiation from both surfaces introduces a compensating factor of 2 . A time-reversed equilibrium system is an equilibrium system, hence in the limit of slow band motion, power scattered from parallel to perpendicular polarizations by band flutter must equal power scattered from perpendicular to parallel. This introduces a further factor of 2 in the drag expression.

With these bounding approximations, the analysis proceeds essentially as before, yielding

$$
\begin{equation*}
P_{\text {drag }}<\varepsilon T_{\text {trans }}\left(A k_{\text {bands }} R\right)^{2} R^{2} \frac{v^{2}}{v_{\mathrm{s}}} S \tag{7.36}
\end{equation*}
$$

Equation (7.22) implies that the product $k_{\text {bands }} R=k_{1}=2 \pi / d$, where $d$ is the spacing of atomic rows in either surface. [In the general case described by Eq. (7.23), this remains a reasonable approximation.] This yields the expression

$$
\begin{equation*}
P_{\text {drag }}<\varepsilon T_{\text {trans }}\left(\frac{2 \pi A}{d}\right)^{2} R^{2} \frac{v^{2}}{v_{\mathrm{s}}} S \tag{7.37}
\end{equation*}
$$

As with stiffness variations, $A / d$ can be made small in properly designed bearings of certain classes; a reasonable value is $10^{-2}$. For values of other variables as previously assumed, the drag power from this mechanism is bounded by $\sim 10 \mathrm{~W} / \mathrm{m}^{2}$ at $1 \mathrm{~m} / \mathrm{s}$.

e. The transmission coefficient. As Sections 7.3.5c and 7.3.5d illustrate, the phonon transmission coefficient $T_{\text {trans }}$ greatly affects drag at sliding interfaces. In a simple one-dimensional model of longitudinal vibrations propagating along a rod with a linear modulus $E_{\ell}$ interrupted by spring of stiffness $k_{\mathrm{s}}$, the transmission coefficient is

$$
\begin{equation*}
T_{\text {trans, rod }}=\left[1+\left(E_{\ell} k / 2 k_{\mathrm{s}}\right)^{2}\right]^{-1} \tag{7.38}
\end{equation*}
$$

where $k$ is the spatial frequency $(\mathrm{rad} / \mathrm{m})$.

A detailed analysis by Soreff (1991) shows that in a medium in which all speeds of sound are equal, the transmission coefficient at a planar interface takes the same form,

$$
\begin{equation*}
T_{\text {trans,perp }}=\left[1+\left(M k_{z} / 2 k_{\mathrm{a}}\right)^{2}\right]^{-1} \tag{7.39}
\end{equation*}
$$

in which $k_{z}$ is the $z$-component of the wave vector of an incident wave of perpendicular polarization, and $M$ is the single modulus. The overall mean power transmission coefficient can then be estimated by an integral over one hemisphere of the allowed volume of $k$-space, weighting contributions from different wave vectors in accord with the Debye model of the distribution of phonon energy and including a factor of $1 / 3$ to account for the transmission of incident power in only one of the three possible polarizations:

$$
\begin{equation*}
T_{\mathrm{trans}}=\frac{\frac{4}{3} \int_{0}^{1} \frac{\boldsymbol{k}^{\prime 3}}{\exp \left(\boldsymbol{k}^{\prime} / T^{\prime}\right)-1} \int_{0}^{\pi / 2} \frac{\sin (2 \theta)}{\left(d^{\prime} \boldsymbol{k}^{\prime} \cos \theta\right)^{2}+4} d \theta d \boldsymbol{k}^{\prime}}{\int_{0}^{1} \frac{\boldsymbol{k}^{\prime 3}}{\exp \left(\boldsymbol{k}^{\prime} / T^{\prime}\right)-1} d \boldsymbol{k}^{\prime}} \tag{7.40}
\end{equation*}
$$

where $T^{\prime}=T / T_{\mathrm{D}}$, and $d^{\prime}$ is a dimensionless measure of the stiffness of the interface, $d^{\prime}=k_{\mathrm{D}} M / k_{\mathrm{a}}$. Values of $T_{\text {trans }}$ are plotted in Figure 7.6 with respect to $d_{\mathrm{n}}=$ $n^{-1 / 3} M / k_{\mathrm{a}}\left(\propto d^{\prime}\right)$ for a range of values of interest in the present context. The parameter $d_{n}$ can be interpreted as the thickness of a slab of the medium, in atomic layers (assuming a simple cubic lattice), that has a stiffness per unit area equaling that of the interface itself.

Equation (7.40) does not lend itself to easy evaluation or use in analytical models. A reasonable engineering approximation is

$$
\begin{equation*}
T_{\mathrm{trans}} \approx z / 1+3 z ; \quad z=0.6 d_{\mathrm{n}}^{-1.7}\left(1+0.075 T^{\prime-1.8}\right) \tag{7.41}
\end{equation*}
$$

or

$$
\begin{equation*}
T_{\text {trans }} \approx z, \quad z \ll 1 \tag{7.42}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-29.jpg?height=665&width=1059&top_left_y=1421&top_left_x=336)

Figure 7.6. The transmission coefficient for a compliant interface, Eq. (7.40), plotted for several values of a dimensionless measure of temperature, $T / T_{\mathrm{D}}$, and a dimensionless measure of interface compliance, $d_{\mathrm{n}}$. Dotted curves represent the approximation given by Eq. (7.41).

Equation (7.41) is plotted in Figure 7.6. Both expressions consistently overestimate transmission (and hence drag), yielding conservative results for most purposes; their forms have been chosen to give a good fit for parameters in the anticipated region of engineering interest, rather than to exhibit correct behavior at the simple physical limits (e.g., $T^{\prime} \rightarrow 0$ ).

f. Curved interfaces and dissimilar media. In the model described by Eq. (7.40), when $d_{\mathrm{n}}$ is large and $T^{\prime}$ is not small, normally incident phonons are reflected almost perfectly and grazing-incidence phonons make a large contribution to $T_{\text {trans }}$. The efficient transmission of grazing-incidence phonons results from a resonant process that depends on (1) the prolonged interaction associated with grazing-incidence collisions, and (2) the matching acoustic speeds of the media on either side of the interface. In the limit of small angles, the transmission probability approaches unity.

Short or curved interfaces disrupt this process, reducing $T_{\text {trans }}$. A difference in acoustic speed between the two media does likewise, causing the grazingincidence transmission probability to fall to zero on one side (owing to total internal reflection) and to approach zero in the limit of small angles on the other side (as shown by the angular variation of reflectivity in analogous optical systems). Sharply curved interfaces are common in nanomechanical bearings, and differences in acoustic speed are likewise common; indeed, such differences can be a design objective. In critical applications, practically significant differences in acoustic speed can be ensured even between chemically identical structures by building them from different isotopes (e.g., ${ }^{12} \mathrm{C}$ vs. ${ }^{13} \mathrm{C}$ ). An analysis taking account of curved interfaces or differentiated media would be desirable, but models based on Eq. (7.40) provide an upper bound on transmission-dependent drag processes. This suffices for present purposes.

### 7.3.6. Shear-reflection drag

The asymmetry of Doppler shifts among phonons transmitted through a sliding interface shows that a (symmetrical) equilibrium distribution is transformed into a nonequilibrium distribution, implying an increase in the free energy of the phonons at the expense of the energy of sliding. Analyzing this energy loss mechanism, however, is difficult. A study by Soreff (1991) of sound propagation through the model interface of Section 7.3.5e yields an expression for the wavevector resolved transmission coefficient of an interface as a function of the Mach number, $M_{\mathrm{s}}$, and the dimensionless measures of interfacial stiffness and phonon spatial frequency described in Section 7.3.5e:

$$
\begin{equation*}
T_{\text {trans,perp }}=4 r_{z}\left[\left(1+r_{z}\right)^{2}+\left(d^{\prime} k^{\prime} r_{z} \sin \psi \cos \phi\right)^{2}\right]^{-1} \tag{7.43}
\end{equation*}
$$

where

$$
\begin{equation*}
r_{z}=\frac{\sqrt{\sin ^{2} \psi \cos ^{2} \phi-2 M_{\mathrm{s}} \cos \psi+M_{\mathrm{s}}^{2} \cos ^{2} \psi}}{\sin \psi \cos \phi} \tag{7.44}
\end{equation*}
$$

In this expression, the coordinates are chosen such that sliding motion occurs along the $x$ axis with the $z$ axis perpendicular to the interface; $\psi$ measures the angle between the wave vector and the $x$ axis, and $\phi$ measures the angle between
the $x-k^{\prime}$ plane and the $x-z$ plane. The square root in Eq. (7.44) is to be taken as positive, with formally imaginary values taken as zero. Soreff observes that phonons crossing the interface experience no change in the component of their wave vector parallel to the interface and hence no change in that component of momentum; only velocity-dependent asymmetries in the transmission coefficient cause momentum transfer and hence drag. (Soreff has verified the correctness of equating crystal momentum and ordinary momentum in this instance by a detailed analysis of transverse forces in the phonon-deformed interface.)

The drag per unit area per unit phonon effective energy density can be expressed as the ratio of integrals in Eq. (7.45). This closely resembles the expression for the transmission coefficient save for a change of coordinates, use of the velocity-dependent expression for transmission, and the introduction of a $\cos (\psi)$ factor in the numerator to account for contributions to the $x$ momentum. At low Mach numbers, contributions from the leading and trailing regions of $\boldsymbol{k}$ space nearly cancel and are associated with rapidly varying length scales; these characteristics make numerical analysis difficult. Soreff reports that several different approaches for developing analytical approximations or bounds fail to yield useful results.

On physical grounds, one expects that at low Mach numbers the drag is approximately proportional to the energy density, to the zero-velocity transmission coefficient, and to the Mach number itself. This encourages consideration of the expression

$$
\begin{equation*}
D_{\mathrm{sr}}=\frac{-\frac{8}{3 \pi} \int_{0}^{1} \frac{k^{\prime 3}}{\exp \left(k^{\prime} / T^{\prime}\right)-1} \int_{0}^{\pi / 2} \int_{0}^{\pi} \frac{r_{z} \sin ^{2} \psi \cos \psi \cos \phi}{\left(1+r_{z}\right)^{2}+\left(d^{\prime} k^{\prime} r_{z} \sin \psi \cos \phi\right)^{2}} d \psi d \phi d k^{\prime}}{M_{\mathrm{s}} T_{\text {trans }} \int_{0}^{1} \frac{k^{\prime 3}}{\exp \left(k^{\prime} / T^{\prime}\right)-1} d k^{\prime}} \tag{7.45}
\end{equation*}
$$

in hopes that $D_{\text {st }}$ is a slowly varying quantity. A numerical investigation suggests that $D_{\mathrm{st}}$ is of order unity and does indeed vary only moderately across a range of parameters in which the drag varies by more than seven orders of magnitude. Use of the approximation $D_{\mathrm{st}}=1$ appears conservative for the systems of interest in the present context, frequently overestimating drag by a factor of 10 or more (a more thorough numerical investigation would be desirable). The considerations raised in Section 7.3.5f often introduce a further measure of conservatism in the use of this approximation.

The expression for the power dissipation from shear-reflection drag includes a factor of two to account for phonons approaching an interface from each side:

$$
\begin{equation*}
P_{\text {drag }} \approx \frac{\varepsilon}{2} T_{\text {trans }} M_{\mathrm{s}} D_{\mathrm{sr}} v S=\frac{\varepsilon}{2} T_{\text {trans }} D_{\mathrm{sr}} \frac{v^{2}}{v_{\mathrm{s}}} S \tag{7.46}
\end{equation*}
$$

The magnitude of drag from this mechanism relative to those described by Eqs. (7.35) and (7.37) varies with the design parameters. For bearings in which alignment-band drag has been minimized, it can be dominant. With the assumptions of Section 7.3.5c, the drag power is $\sim 10 \mathrm{~W} / \mathrm{m}^{2}$ at $1 \mathrm{~m} / \mathrm{s}$.

### 7.3.7. Interfacial phonon-phonon scattering

Nonlinear interactions permit phonons to scatter from one another, and the restoring forces in a nonbonded interface are substantially nonlinear. In particular, phonons in one medium can scatter from corrugations in the interface induced by phonons in the other medium; interfacial sliding will give these corrugations a drift velocity, enabling them to transmit net energy to the scattered phonons and so cause drag. A preliminary evaluation suggests that this effect is small, but a more thorough investigation would be desirable.

### 7.4. Thermoelastic damping and phonon viscosity

The phonon gas causes energy loss by mechanisms analogous to those occurring in the compression and shear of ordinary gases. These mechanisms are termed thermoelastic damping and phonon viscosity.

### 7.4.1. Thermoelastic damping

When a typical solid is compressed, the energy of its normal modes increases. In the absence of equilibration, phonon energies likewise increase and the solid becomes hotter. Since this process involves changes in the dimensions of the solid rather than motions with respect to the lattice, no work is done against the pressure of the phonon gas directly (as in the compression of an ordinary gas or a photon gas). Instead, phonon energies increase because of anharmonic effects: interatomic potentials become stiffer as distances shrink. A widely used measure of anharmonicity is the Grüneisen number,

$$
\begin{equation*}
\gamma_{\mathrm{G}}=\beta K / C_{\mathrm{vol}} \tag{7.47}
\end{equation*}
$$

where $\beta$ is the volume coefficient of thermal expansion $\left(\mathrm{K}^{-1}\right), K$ is the bulk modulus $\left(\mathrm{N} / \mathrm{m}^{2}\right)$, and $C_{\mathrm{vol}}$ is the heat capacity per unit volume $\left(\mathrm{J} / \mathrm{K} \cdot \mathrm{m}^{3}\right) .\left(C_{\mathrm{vol}}\right.$ equals the molar heat capacity at constant volume divided by the molar volume.) Values of $\gamma_{\mathrm{G}}$ for many ordinary materials fall in the range 1.5 to 2.5 and have little temperature dependence near $300 \mathrm{~K}$. For diamond, $\beta=3.5 \times 10^{-6} \mathrm{~K}^{-1}, K \approx$ $4.4 \times 10^{11} \mathrm{~N} / \mathrm{m}^{2}$, and $C_{\mathrm{vol}} \approx 1.7 \times 10^{6} \mathrm{~J} / \mathrm{K} \cdot \mathrm{m}^{3}$ at $300 \mathrm{~K}$, yielding $\gamma_{\mathrm{G}} \approx 0.9$.

Thermoelastic damping arises from the difference between the adiabatic and the isothermal work of compression. Starting with an expression for small values of $\Delta V$ and $\Delta T$ (Lothe, 1962), and applying thermodynamic identities,

$$
\begin{align*}
\Delta W & =\frac{1}{2}\left(K_{\text {adiabatic }}-K\right) \frac{\Delta V^{2}}{V}  \tag{7.48}\\
& =\frac{1}{2} \gamma_{\mathrm{G}}^{2} T C_{\mathrm{vol}} \frac{\Delta V^{2}}{V} \\
& =\frac{1}{2} \beta^{2} \frac{T}{C_{\mathrm{vol}}} \Delta p^{2} V \tag{7.49}
\end{align*}
$$

A worst-case thermodynamic cycle involves adiabatic compression of a volume (increasing the temperature) followed by nonequilibrium cooling (producing entropy), followed by adiabatic expansion and nonisothermal warming, causing an overall energy dissipation of $2 \Delta W$, from Eq. (7.49). For diamond, this amounts to $\sim 2.2 \times 10^{-24}(\Delta p)^{2} \mathrm{~J} / \mathrm{nm}^{3}$.cycle, where $p$ is here measured in $\mathrm{nN} / \mathrm{nm}^{2}$ $(=\mathrm{GPa})$.

Thermoelastic damping falls to zero if the cycle is either adiabatic or isothermal, and nanomechanical systems frequently approach the isothermal limit. The ratio of the energy dissipated in a nearly isothermal cycle to that dissipated in the worst-case cycle equals the ratio of the mean displacement-weighted temperature increments. A component undergoing smooth mechanical cycling with a period $t_{\text {cycle }}$ and a characteristic time for thermal equilibration $\tau_{\text {therm }}$ experiences a temperature rise during the cycle on the order of $\tau_{\text {therm }} / t_{\text {cycle }}$ times that of the adiabatic case, implying

$$
\begin{equation*}
\Delta W_{\text {cycle }} \approx 2 \beta^{2} \frac{T}{C_{\text {vol }}}(\Delta p)^{2} \frac{\tau_{\text {therm }}}{t_{\text {cycle }}} V \tag{7.50}
\end{equation*}
$$

For a component in good thermal contact with its environment, $\tau_{\text {therm }}$ is on the order of

$$
\begin{equation*}
\tau_{\text {therm }} \approx \max \left(\frac{C_{\text {vol }}}{K_{\mathrm{T}}} \ell^{2}, \frac{\ell}{v_{\mathrm{s}}}\right) \tag{7.51}
\end{equation*}
$$

where $K_{\mathrm{T}}$ is the thermal conductivity $(\mathrm{W} / \mathrm{m} \cdot \mathrm{K})$ and $\ell$ is a characteristic dimension. Values of $K_{\mathrm{T}}$ for glasses and nonporous ceramics typically are between 1 and $10 \mathrm{~W} / \mathrm{m} \cdot \mathrm{K}$, with the value for diamond being $\sim 700$ (Gray, 1972). For $K_{\mathrm{T}}=$ $10, \ell=10 \mathrm{~nm}$, and $C_{\text {vol }}=2 \times 10^{6} \mathrm{~J} / \mathrm{K} \cdot \mathrm{m}^{3}, \tau_{\text {therm }} \approx 10^{-11} \mathrm{~s} ; \Delta W_{\text {cycle }}$ accordingly is multiplied by a factor of $\sim 10^{-2}$ at $1 \mathrm{GHz}$ and $\sim 10^{-5}$ at $1 \mathrm{MHz}$ relative to the values given by the worst-case expression, Eq. (7.49). These calculations are in terms of an isotropic pressure; a compressive load of the same formal magnitude but applied along a single axis will have a lesser effect. This correction will be neglected here, tending to favor overestimates of energy dissipation.

### 7.4.2. Phonon viscosity

Shear deformation causes no volume change and hence no thermoelastic losses. Shear does, however, cause compression along one axis and extension along another: phonons traveling along one axis are increased in energy; those along the other, reduced. Within a factor of $3 / 2$, an analogy between this and the thermoelastic effect yields an estimate of the difference between the adiabatic and isothermal shear moduli (Lothe, 1962), resulting in an effective viscosity

$$
\begin{equation*}
\eta_{\text {phonon }}=\tau_{\text {relax }} \frac{3}{2} \gamma_{\mathrm{G}}^{2} T C_{\text {vol }} \tag{7.52}
\end{equation*}
$$

The analysis of the energy dissipation proceeds essentially as for thermoelastic damping, but with the substitution of the phonon relaxation time $\tau_{\text {relax }}$ for $\tau_{\text {thermal }}$, and the shear stress $\gamma$ for the pressure $p$, yielding

$$
\begin{equation*}
\Delta W_{\text {cycle }} \approx \frac{3}{2} \beta^{2} \frac{T}{C_{\text {vol }}}(\Delta \gamma)^{2} \frac{\tau_{\text {relax }}}{t_{\text {cycle }}} V \tag{7.53}
\end{equation*}
$$

The time $\tau_{\text {relax }}$ measures the rate of equilibration of phonon energy between different directions in the solid, which can be accomplished by elastic scattering such as that occurring at the boundaries of a solid body or at internal inhomogeneities. In nanomechanical systems, scattering typically limits phonon mean free

Table 7.1. Values of the volumetric thermal coefficient of expansion $\beta$ for several strong solids in the neighborhood of $300 \mathrm{~K}$ (Gray, 1972).

| Material | $\beta$ <br/> $\left(10^{-6} \mathrm{~K}^{-1}\right)$ |
| :--- | :---: |
| Diamond | 3.5 |
| Silicon | 7.5 |
| Silicon carbide | 11.1 |
| Sapphire | 15.6 |
| Silica, crystalline (quartz) | 36.0 |
| Silica, vitreous | 1.2 |

paths to nanometer distances, resulting in values of $\tau_{\text {relax }} \approx 10^{-13} \mathrm{~s}$ for $v_{\mathrm{s}} \approx$ $10^{4} \mathrm{~m} / \mathrm{s}$. Because of this small time constant, phonon viscosity losses typically are small compared to thermoelastic losses, save in systems undergoing very high frequency motion or nearly pure shear.

### 7.4.3. Application to moving parts and alignment bands

Alignment bands, like sliding and rolling components, impose moving regions of stress on the surrounding medium. These regions can be characterized by their volume $V \approx \ell^{3}$ (for contact regions) or $\approx d \ell^{2}$ (for bands extending over a distance $d$ ), where $\ell$ is a measure of the scale of the region (e.g., the wavelength of the alignment bands). For motions of velocity $v, \tau_{\text {cycle }} \approx \ell / v$. This leads to an estimate of the magnitude of the thermoelastic drag of a set of bands:

$$
\begin{equation*}
P_{\mathrm{drag}} \approx \beta^{2} \frac{T}{K_{\mathrm{T}}} \ell(\Delta p)^{2} R^{2} v^{2} S \tag{7.54}
\end{equation*}
$$

based on the assumption that phonon mean free paths are shorter than $\ell$. With $\beta=3.5 \times 10^{-6} \mathrm{~K}^{-1}, K_{\mathrm{T}}=10 \mathrm{~J} / \mathrm{m} \cdot \mathrm{K}, \ell=10 \mathrm{~nm}, R=10, T=300 \mathrm{~K}$, and $\Delta p=$ $10^{8} \mathrm{~N} / \mathrm{m}^{2}, P_{\text {drag }} \approx 4 \mathrm{~W} / \mathrm{m}^{2}$ at $v=1 \mathrm{~m} / \mathrm{s}$, or $0.04 \mathrm{~W} / \mathrm{m}^{2}$ at $1 \mathrm{~cm} / \mathrm{s}$. As with stiffness and displacement, good design can in many instances yield low values of $\Delta p$.

These estimates of thermoelastic dissipation have used a value of $\beta$ appropriate for diamond. Table 7.1 lists values for several other strong solids that can serve as models for the materials of nanomechanical components. The large difference between $\mathrm{SiO}_{2}$ as quartz and as vitreous silica indicates that $\beta$ is sensitive to patterns of bonding and hence is subject to substantial design control in the products of molecular manufacturing, including nanomechanical components.

### 7.5. Compression of potential wells

### 7.5.1. Square well compression

Many useful nanomechanical systems contain components that move over a relatively flat potential energy surface within a bounded region of variable size. Thermodynamically, the motion of the component within this region is like the motion of a gas molecule in a container; changes in the size of the region correspond to compression and expansion. At any finite speed, compression is a
nonisothermal process, heating the gas, raising its pressure, and so increasing the work of compression and causing energy dissipation. The better the thermal contact between the component and its environment, the lower the dissipation. A conservative model assumes contact only between the "gas molecule" component and two moving pistons (Figure 7.7), treating the component as a onedimensional gas consisting of one molecule.

a. Accommodation coefficients. Thermal contact between a gas and a solid is usually described by a thermal accommodation coefficient $\alpha$ that measures the extent to which the excess energy of an impinging gas molecule is lost in a single collision with a wall:

$$
\begin{equation*}
\left(T_{1}-T_{\mathrm{s}}\right) \alpha=T_{1}-T_{2} \tag{7.55}
\end{equation*}
$$

where the temperature of the incident molecules is $T_{1}$, that of the surface is $T_{\mathrm{s}}$, and that of the outbound molecules is $T_{2}$. Separate accommodation coefficients can be defined for the energy of translation, rotation, and vibration. The most accurate measurements have been made for monatomic gases, in which all the energy is translational. As just defined, $\alpha$ is a function of three temperatures; in the limit as $T_{1}, T_{2}$, and $T_{\mathrm{s}}$ become equal, $\alpha$ becomes a function of a single temperature. A value of the latter sort (an equilibrium accommodation coefficient) can be used with reasonable accuracy so long as none of the three temperatures differs greatly from the reference temperature. Theory and experimental data for thermal accommodation coefficients are reviewed in Goodman (1980), Goodman and Wachman (1976), and Saxena and Joshi (1989).

Save for light gases (helium, neon) impinging on a clean surface with massive atoms (tungsten), most tabulated values of $\alpha$ range from 0.25 to $\sim 1.0$. Surface contamination tends to increase accommodation; stable structures with similar effects could be provided in many systems.

b. A square-well temperature-increment model. A simple model for the temperature rise assumes that the statistics of the velocity of a moving component of mass $m$ are those of a system at equilibrium at some temperature $T_{\text {rest }}$, with a root mean square velocity (along the axis) of $v_{\mathrm{g}, \mathrm{rms}}=\left(k T_{\mathrm{g}} / \mathrm{m}\right)^{1 / 2}$. If each piston moves at a speed $(f / 2)\left(k T_{\mathrm{g}} / \mathrm{m}\right)^{1 / 2}$ relative to the wall, then

$$
\begin{align*}
& v_{1, \mathrm{rms}}=v_{\mathrm{g}, \mathrm{rms}}\left(1+f / \sqrt{\pi}+f^{2} / 4\right)  \tag{7.56}\\
& v_{2, \mathrm{rms}}=v_{\mathrm{g}, \mathrm{rms}}\left(1-f / \sqrt{\pi}+f^{2} / 4\right)
\end{align*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-35.jpg?height=268&width=656&top_left_y=1834&top_left_x=499)

Figure 7.7. Two-piston model of a compressed square well; cylinder walls are assumed adiabatic.

where $v_{1, \mathrm{rms}}$ and $v_{2, \mathrm{rms}}$ are measured in the frame of reference of the scattering piston ( pistons are assumed to interact only with particles moving in their direction in the rest frame, neglecting molecules overtaken; this approximation is good for small $f$ ). Since mean square velocity is proportional to temperature, Eq. (7.55) can be converted to velocity terms, yielding the condition

$$
\begin{equation*}
\left(v_{1, \mathrm{rms}}^{2}-k T_{\mathrm{s}} / m\right) \alpha=v_{1, \mathrm{rms}}^{2}-v_{2, \mathrm{rms}}^{2} \tag{7.57}
\end{equation*}
$$

where $k T / m$ is the mean square thermal speed, and hence

$$
\begin{equation*}
R_{\text {temp }}=\frac{T_{\mathrm{g}}}{T_{\mathrm{s}}}=\left[1+\frac{f^{2}}{4}-f \sqrt{\frac{2}{\pi}}\left(\frac{2}{\alpha}-1\right)\right]^{-1} \tag{7.58}
\end{equation*}
$$

A useful approximation, good for small $f$ and moderate to large $\alpha$, is

$$
\begin{equation*}
R_{\text {temp }} \approx 1+f \sqrt{\frac{2}{\pi}}\left(\frac{2}{\alpha}-1\right) \tag{7.59}
\end{equation*}
$$

c. Energy losses. The cases of greatest interest in the present context are those in which $f \ll 1$, and $T_{\mathrm{g}} \approx T_{\mathrm{s}}$. The work done in isothermally compressing a freely moving particle from a range of motion $\ell_{1}$ to a range $\ell_{2}$ is

$$
\begin{equation*}
W=-\int_{\ell_{1}}^{\ell_{2}} \frac{k T}{\ell} d \ell=k T \ln \frac{\ell_{1}}{\ell_{2}} \tag{7.60}
\end{equation*}
$$

and for a system undergoing compression at a uniform speed, resulting in a constant value of $\Delta T_{\text {comp }}$, the free energy lost (with the above approximations) is

$$
\begin{align*}
\Delta W & \approx k \Delta T_{\text {comp }} \ln \frac{\ell_{1}}{\ell_{2}}=k T_{\mathrm{s}} f \sqrt{\frac{2}{\pi}}\left(\frac{2}{\alpha}-1\right) \ln \frac{\ell_{1}}{\ell_{2}}  \tag{7.61}\\
& \approx \sqrt{\frac{2 m k T_{\mathrm{s}}}{\pi}}\left(\frac{2}{\alpha}-1\right) \ln \frac{\ell_{1}}{\ell_{2}} v_{\text {total }} \tag{7.62}
\end{align*}
$$

where $v_{\text {total }}$ is the speed of one piston with respect to the other. For a sliding component with $m=2 \times 10^{-25} \mathrm{~kg}$, a compression ratio of $10, \alpha=0.5$, and $T_{\mathrm{s}}=$ $300 \mathrm{~K}$, the energy lost is $\sim 1.6 \times 10^{-22} \mathrm{~J}$ at $1 \mathrm{~m} / \mathrm{s}$, and $\sim 1.6 \times 10^{-24} \mathrm{~J}$ at $1 \mathrm{~cm} / \mathrm{s}$. So long as $f$ remains small, Eqs. (7.61) and (7.62) are equally applicable to nonisothermal expansion losses.

d. Large molecules. For relatively massive moving components, the literature values of $\alpha$ for ordinary gas molecules offer only a poor guide. As molecular motions become slow, collisions become more nearly elastic, and energy transfer decreases, but as molecules become large, the slowing of their free motion is offset by the effect of their increased van der Waals attraction energy (Goodman, 1980): the final approach to a surface is accelerated, and the loss of a small portion of the resulting increment in kinetic energy can result in a negative total energy relative to the free state. This results in adsorption, complete thermal accommodation, and (in the present context) elimination of further nonisothermal-compression losses until the pistons begin to press the molecule from
both sides. (Energy losses resulting from the fall into the van der Waals potential well can be described within the framework of Section 7.6.)

### 7.5.2. Harmonic well compression

Nanomechanical systems sometimes contain components confined to approximately harmonic wells of time-varying stiffness. This is, for example, a reasonable description of the final compression of a single-molecule gas when it is subject to repulsive forces from both pistons. Compression corresponds to an increase in $k_{\mathrm{s}}$, reducing the effective volume (Section 6.2.2b) available to the oscillator. Thermal exchange with the medium in these instances can be modeled as acoustic radiation from a harmonic oscillator with an energy equaling the excess thermal energy; near equilibrium, the same coefficients describe the absorption of energy by an oscillator undergoing expansion.

a. A harmonic-well temperature-increment model. Assume that the compression process is slow compared to the vibrational period, and that the temperature increment $\Delta T_{\text {comp }}$ is small compared to the equilibrium temperature $T$. The total work done in compressing the system by increasing the stiffness from $k_{\mathrm{s}, 1}$ to $k_{\mathrm{s}, 2}$ is

$$
\begin{equation*}
W=k T \ln \sqrt{k_{\mathrm{s}, 2} / k_{\mathrm{s}, 1}} \tag{7.63}
\end{equation*}
$$

Equating the derivative of $W$ with respect to $k_{\mathrm{s}}$ to the net radiated acoustic power, Eq. (7.8), associated with the excess energy $k \Delta T_{\text {comp }}$ yields the expression

$$
\begin{equation*}
\Delta T_{\text {comp }}=2 \pi m M^{3 / 2} \rho^{-1 / 2} T \frac{\partial k_{\mathrm{s}}}{\partial \mathrm{t}} k_{\mathrm{s}}^{-3} \tag{7.64}
\end{equation*}
$$

where the constants are as defined in Section 7.2.2.

b. Energy dissipation models. The energy dissipated is the integral of the difference in work resulting from $\Delta T_{\text {comp }}$, or

$$
\begin{equation*}
\Delta W=\int_{k_{\mathrm{s}, 1}}^{k_{\mathrm{s}, 2}} \frac{k \Delta T_{\text {comp }}}{2 k_{\mathrm{s}}} d k_{\mathrm{s}}=\frac{\pi m M^{3 / 2}}{3 \sqrt{\rho}} k T \frac{\partial k_{\mathrm{s}}}{\partial t}\left(k_{\mathrm{s}, 1}^{-3}-k_{\mathrm{s}, 2}^{-3}\right) \tag{7.65}
\end{equation*}
$$

assuming that the stiffness increases linearly with time. In systems where $k_{\mathrm{s}}$ results from nonbonded repulsions, Eq. (3.18) implies that $k_{\mathrm{s}} \approx 3.5 \times 10^{10} F_{\text {load }}$ $(\mathrm{N} / \mathrm{m})$; a roughly linear increase of $F_{\text {load }}$ is not uncommon.

The value of this expression is strongly sensitive to the value of $k_{\mathrm{s}, 1}$, the stiffness at the onset of compression. This frequently is on the order of the stiffness of an unloaded nonbonded contact between two objects. A model for this, in turn, is the contact between two planes in solid graphite. With an interlayer spacing of $0.335 \mathrm{~nm}$ and a modulus of $1.0 \times 10^{10} \mathrm{~N} / \mathrm{m}^{2}$ (Kelly, 1973), the stiffness of this contact is $\sim 3 \times 10^{19} \mathrm{~N} / \mathrm{m}^{3}$, or $30 \mathrm{~N} / \mathrm{m}$ per $\mathrm{nm}^{2}$. The contact area between a blocky component and a surface typically is on the order of

$$
\begin{equation*}
S \approx\left(m / \rho_{\mathrm{c}}\right)^{2 / 3} \tag{7.66}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-38.jpg?height=330&width=572&top_left_y=204&top_left_x=476)

Figure 7.8. Model of compression by an elastic system.

and hence

$$
\begin{equation*}
k_{\mathrm{s}, 1} \approx 3 \times 10^{19}\left(\mathrm{~m} / \rho_{\mathrm{c}}\right)^{2 / 3} \tag{7.67}
\end{equation*}
$$

In a typical situation (Figure 7.8), a system with a finite stiffness external to the interfaces under consideration, $k_{\mathrm{s}, \mathrm{ext}}$, is loaded by a steady displacement at a rate $v_{\text {ext }}$. Using Eq. (7.65) and assuming substantial compression ratios,

$$
\begin{equation*}
\Delta W \approx k T \frac{\pi m M^{3 / 2}}{3 \sqrt{\rho}} 3.5 \times 10^{10} \frac{k_{\mathrm{s}, \mathrm{ext}} v_{\mathrm{ext}}}{k_{\mathrm{s}, 1}^{3}} \tag{7.68}
\end{equation*}
$$

where the approximation assumes a $k_{\mathrm{s}, \mathrm{ext}}$ substantially less than $k_{\mathrm{s}, 1}$. Assuming that $T=300 \mathrm{~K}, m=10^{-24} \mathrm{~kg}, M=5 \times 10^{11} \mathrm{~N} / \mathrm{m}^{2}, \rho=\rho_{\mathrm{c}}=2000 \mathrm{~kg} / \mathrm{m}^{3}, k_{\mathrm{s}, \mathrm{ext}}=$ $10 \mathrm{~N} / \mathrm{m}$, and $k_{\mathrm{s}, 1}=19 \mathrm{~N} / \mathrm{m}, \Delta W \approx 2 \times 10^{-21} \mathrm{~J}$ at $v_{\mathrm{ext}}=1 \mathrm{~m} / \mathrm{s}$, and $\approx 2 \times 10^{-23} \mathrm{~J}$ at $1 \mathrm{~cm} / \mathrm{s}$.

These estimates indicate magnitudes of energy dissipation that are large relative to those identified thus far. Of the parameters subject to design control, the most significant is $M$; the value assumed above is for a diamondlike material, which strongly suppresses radiative coupling and increases $\Delta T$. In the immediate neighborhood of a component undergoing fast compression, a better choice is a structure with properties like those of an engineering polymer, $M \approx$ $3 \times 10^{9} \mathrm{~N} / \mathrm{m}^{2}, \rho \approx 1000 \mathrm{~kg} / \mathrm{m}^{3}$. This decreases $\Delta W$ by a factor $\sim 7 \times 10^{-4}$, yielding $\sim 1 \times 10^{-24} \mathrm{~J}$ at $v=1 \mathrm{~m} / \mathrm{s}$, and $\sim 1 \times 10^{-26} \mathrm{~J}$ at $1 \mathrm{~cm} / \mathrm{s}$.

It would be of interest to test the predictions of Eqs. (7.62) and (7.68) against direct molecular dynamics simulations. Studies along these lines could reduce uncertainties regarding accommodation coefficients and velocity distributions in the square-well regime and could probe energy losses in the transition to a harmonic well compression regime. For this purpose, the routines for integrating the equations of motion must conserve energy with considerable accuracy.

### 7.5.3. Multidimensional systems

Sections 7.5.1 and 7.5.2 assume one-dimensional motion of the compressed component. Real systems have two additional degrees of freedom in translation and further degrees of freedom in torsion and internal vibration. Usually, excitation of a single translational degree of freedom by nonisothermal compression results in rapid equilibration with the other degrees of freedom, approaching equipartition of energy. Each of these degrees of freedom opens new channels
for equilibration with the environment, reducing $\Delta T_{\text {comp }}$; commonly, some have higher frequencies and more effective radiative coupling than the single mode considered above. Consequently, energy dissipation is lower than that implied by a one-dimensional model.

a. Multidimensional square-wells. In a simple gas-in-cylinder model, the one-dimensional approximation is equivalent to assuming that the walls of the cylinder are adiabatic, permitting energy loss only to the pistons. A realistic, multidimensional model would include equilibration through collisions with the walls.

b. Multidimensional harmonic wells. In a realistic, approximately harmonic well, longitudinal vibrations are coupled (at a minimum) to transverse vibrations, providing two additional vibrational modes for equilibration through acoustic radiation. Further, vibrational frequencies in these transverse modes can often be made substantially higher than those in the longitudinal mode: a component can be tightly clamped against transverse motion while performing a function requiring relatively low longitudinal stiffness. This can greatly reduce $\Delta T_{\text {comp }}$.

c. Mixed systems. A component may be subject to strong harmonic constraints against transverse motion, yet move in an approximately square-well potential in longitudinal motion. Again the modes are coupled, and again the transverse modes provide relatively effective coupling to the heat bath of the surrounding medium.

### 7.6. Transitions among time-dependent wells

### 7.6.1. Overview

Each of the energy dissipation mechanisms discussed in Sections 7.2 through 7.5 approaches zero energy per operation (or per unit displacement) as the speed of the system approaches zero. The merging of potential wells, in contrast, can dissipate energy no matter how slowly it is performed. Since well merging can dissipate on the order of $k T$ or more per cycle, it can impose a significant energy cost on systems operation.

### 7.6.2. Energy dissipation in merging wells

Energy dissipation in merging wells occurs when transitions between states move a disequilibrium system closer to equilibrium: the dissipation equals the reduction in free energy. In analyzing time-dependent wells, we begin by describing wells as distinct states linked by cols which are divided by transition surfaces (Section 6.2.2). For concreteness, we will consider the case of systems with two wells linked by a single col, using the harmonic approximations made in Section 6.2.

In the cases of interest, transition rates are low compared to vibration times, and the partition function of each state can be evaluated separately under the assumption of internal equilibrium. Losses owing to nonisothermal compression within a well can be estimated by adapting the methods of Section 7.5.2; this mechanism can be treated as independent given either that the transition
rate is negligible, or that the temperature rise has little effect on the transition rate. The latter condition is satisfied if

$$
\begin{equation*}
\Delta T_{\text {comp }} / T \ll k T / \Delta \mathscr{V}^{\ddagger} \tag{7.69}
\end{equation*}
$$

a. Free energy. The free energy for a system of two wells can conveniently be written as the sum of the free energy of each well (assuming unit probability of occupancy), weighted by the actual probabilities of occupancy, plus an entropic term reflecting the uncertainty regarding which well is occupied:

$$
\begin{equation*}
\mathscr{F}_{1,2}=P_{1} \mathscr{F}_{1}+\left(1-P_{1}\right) \mathscr{F}_{2}+k T\left[P_{1} \ln \left(P_{1}\right)+\left(1-P_{1}\right) \ln \left(1-P_{1}\right)\right] \tag{7.70}
\end{equation*}
$$

or, applying Eq. (4.5) and simplifying,

$$
\begin{equation*}
\mathscr{F}_{1,2}=-k T\left[P_{1} \ln \left(q_{1} / P_{1}\right)+\left(1-P_{1}\right) \ln \left(q_{2} / 1-P_{1}\right)\right] \tag{7.71}
\end{equation*}
$$

where $q_{1}$ and $q_{2}$ are the partition functions of the wells considered as isolated, occupied systems.

b. Free-energy changes. For a fixed value of $P_{1}$, the free energy of the twowell system $\mathscr{F}_{1,2}$ depends on the shape of the PES. This changes over time, but so long as equilibrium is maintained, $\Delta \mathscr{F}_{1,2}$ exactly equals the work done on the system by whatever mechanisms are responsible for the change in the PES. The total free energy is then conserved, and no dissipation results.

For a fixed PES, a finite change $\Delta P_{1}$ results in a change in free energy without work being done by (or on) the external mechanisms. Accordingly, $\Delta \mathscr{F}_{1,2}$ can only be negative and corresponds to an increment of energy dissipation. The rate of decrease of free energy, holding the PES constant, is thus

$$
\begin{align*}
\left(\frac{\partial \mathscr{F}_{1,2}}{\partial t}\right)_{\mathrm{PES}} & =\frac{\partial P_{1}}{\partial t} \frac{\partial \mathscr{F}_{1,2}}{\partial P_{1}}=-R_{12}\left(\mathscr{F}_{1}-\mathscr{F}_{2}+k T \ln \frac{P_{1}}{1-P_{1}}\right) \\
& =-R_{12} k T \ln \frac{P_{1} q_{2}}{\left(1-P_{1}\right) q_{1}} \tag{7.72}
\end{align*}
$$

Note that at equilibrium

$$
\begin{equation*}
\mathscr{F}_{1}-\mathscr{F}_{2}=-k T \ln \left(P_{1, \mathrm{eq}} / 1-P_{1, \mathrm{eq}}\right) \tag{7.73}
\end{equation*}
$$

hence

$$
\begin{equation*}
P_{1, \text { equil }}=\exp \left(-\frac{\mathscr{F}_{1}-\mathscr{F}_{2}}{k T}\right)\left[\exp \left(-\frac{\mathscr{F}_{1}-\mathscr{F}_{2}}{k T}\right)+1\right]^{-1} \tag{7.74}
\end{equation*}
$$

and the flow of probability from well to well occurs without dissipation.

The net rate of transitions from 1 to $2, R_{12}$, can be expressed in terms of the unidirectional transitions rates $k_{12}$ and $k_{21}$ calculated from an appropriate version of transition state theory (Section 6.2):

$$
\begin{equation*}
R_{12}=-\partial P_{1} / \partial t=P_{1} k_{12}-\left(1-P_{1}\right) k_{21} \tag{7.75}
\end{equation*}
$$

The total energy dissipation in a process between times $t_{1}$ and $t_{2}$ is

$$
\begin{gather*}
\Delta \mathscr{F}_{\mathrm{diss}}=-\int_{t_{1}}^{t_{2}} R_{12}(t)\left(\mathscr{F}_{1}(t)-\mathscr{F}_{2}(t)+k T \ln \left(P_{1}(t) / 1-P_{1}(t)\right)\right) d t  \tag{7.76}\\
\text { where } \quad P_{1}(t)=P_{1, \text { init }}-\int_{t_{1}}^{t} R_{12}(\tau) d \tau
\end{gather*}
$$

c. Switched-coupling models. As in calculations of error rates (Section 6.3), one useful approximation treats the transition rate as switching between rapid and negligible. As two wells merge and the barrier between them shrinks, energy dissipation typically is low when transition rates are negligible, and low again when rates are high enough to ensure the maintenance of near equilibrium values of $P_{1}$; between these regimes is a period in which transition rates first become significant and then establish and maintain near equilibrium. The switched coupling model approximates that period as a single time, $t_{\mathrm{cpl}}$, hence

$$
\begin{equation*}
\Delta \mathscr{F}_{\text {diss }}=\mathscr{F}_{1,2}\left(t_{\text {cpl }}, P_{1, \text { equil }}\right)-\mathscr{F}_{1,2}\left(t_{\text {cpl }}, P_{1, \text { init }}\right) \tag{7.77}
\end{equation*}
$$

where the equilibrium probability $P_{1, \text { equil }}$ is given by Eq. (4.74) with values of $\mathscr{F}_{1}$ and $\mathscr{F}_{2}$ evaluated at $t_{\text {equil }}$. A value of $t_{\text {cpl }}$ can always be chosen such that Eq. (7.77) yields the same value as Eq. (7.76); in practice, simple rules for choosing $t_{\text {cpl }}$ yield approximations to this value.

### 7.6.3. Free expansion and symmetrical well merging

A simple and important case is the symmetrical merging of two identical wells [e.g., Figure 7.9(a)], where one is initially occupied with $P_{1}=1$. At all times, $\mathscr{F}_{1}=$ $\mathscr{F}_{2}$, the losses resulting from transitions are purely entropic, and the switchedcoupling model yields

$$
\begin{equation*}
\Delta \mathscr{F}_{\text {diss }}=-k T \ln 2 \tag{7.78}
\end{equation*}
$$

which is simply $-T \mathscr{S}$, where $\mathscr{S}$ is the entropy increase resulting from a volumedoubling free expansion of a single-molecule gas; this equals the work required to restore the initial condition by isothermally compressing a single-molecule

![](https://nanosystems.contact.ms/cropped/2024_03_29_3ef2075ad7697743cc5cg-41.jpg?height=449&width=936&top_left_y=1691&top_left_x=359)

Figure 7.9. Merging of symmetrical (a) and asymmetrical (b) potential wells, showing potentials at a series of times.

gas to half its initial volume. In computational systems, the symmetrical merging of two wells corresponds to the erasure of one bit of information; information erasure is the only abstract computational process that of necessity results in an increase in entropy and a corresponding loss of free energy (Bennett, 1982; Landauer, 1988; see also Section 4.3.5).

### 7.6.4. Asymmetrical well merging

Simple approximations suffice when merging wells are sufficiently different in free energy, as in Figure 7.9(b). If $\left(\mathscr{F}_{1}-\mathscr{F}_{2}\right) \gg k T$ during the time of equilibration, and $P_{1, \text { init }}=1$, then

$$
\begin{equation*}
\Delta \mathscr{F}_{\text {diss }} \approx \mathscr{F}_{2}\left(t_{\text {equil }}\right)-\mathscr{F}_{1}\left(t_{\text {equil }}\right) \tag{7.79}
\end{equation*}
$$

In this case, equilibration changes $P_{1}$ from 1 to $\sim \exp \left[-\left(\mathscr{F}_{1}-\mathscr{F}_{2}\right) / k T\right] \approx 0$, hence the entropy of uncertain well-occupancy is almost unchanged. If the difference in free energy between the wells chiefly results from a difference in potential energy (rather than within-well entropy), then the system can be viewed as falling into a deeper well, with subsequent thermalization of the energy of the fall. Processes of this sort occur, for example, when an elementary step in a chemical reaction is exothermic, or when a mechanical process places an elastic component under load, then allows it to slip past an obstacle. $\Delta \mathscr{F}_{\text {diss }}$ can be large compared to $k T$.

If $\left(\mathscr{F}_{1}-\mathscr{F}_{2}\right) \gg k T$ during the time of equilibration, and $P_{1, \text { init }}=0$, then

$$
\begin{equation*}
\Delta \mathscr{F}_{\text {diss }} \approx-k T \exp \left[-\left(\mathscr{F}_{1}-\mathscr{F}_{2}\right) / k T\right] \tag{7.80}
\end{equation*}
$$

In this case, $\Delta \mathscr{F}_{\text {diss }} \ll k T$, and is dominated by the entropy of free expansion into the small effective volume of the upper well.

### 7.6.5. Optimal well merging under uncertainty

The value of $\Delta \mathscr{F}_{12}=\mathscr{F}_{1}-\mathscr{F}_{2}$ for a pair of merging wells often is subject to design control, since well depths can be modulated by various influences. If so, and if the value of $P_{1}$ is known, then the energy dissipation resulting from well merging can be kept near zero by ensuring that $\Delta \mathscr{F}_{12}$ nearly satisfies Eq. (7.74) at $t=$ $t_{\text {cpl }}$ in the switched coupling model, or during the critical period surrounding $t_{\text {cpl }}$ in the model described by Eq. (7.77). Note that in a cyclic process where $P_{1} \neq 0$ or 1 , this uncertainty indicates that some other step in the cycle has increased the entropy and dissipated a corresponding increment of free energy; optimal well merging merely avoids imposing an additional loss.

### 7.7. Conclusions

Multiple energy dissipation mechanisms operate in nanomechanical systems, each strongly influenced by design parameters. Most have a magnitude per operation or per unit displacement that is proportional to the speed of the system; merging of potential wells (including information erasure in computational systems) is the chief exception, since the energy per operation typically is speed independent, or nearly so. With the exception of the last, each of these mechanisms causes an energy dissipation small compared to $k T$ for nanoscale systems with reasonable choices of physical parameters (one criterion for a reasonable
choice, of course, is that it result in acceptable energy dissipation). The approximations and bounds described and developed in this chapter are applied and occasionally elaborated in the chapters of Part II.

Some open problems. Many of these mechanisms are associated with open problems. The theory of phonon transmission through sliding interfaces, in particular, is challenging and in need of further work. For example, in the regime of lowest drag-at separations where the mean interfacial stiffness goes to zerothe phonon transmission model described here becomes unrealistic. Further, the interfaces of greatest engineering interest are not between identical half-spaces; they may be curved, or juxtapose dissimilar materials, or couple a small component to large environment. Finally, drag resulting from interfacial phononphonon scattering deserves a thorough treatment. A survey of the devices discussed in Chapters 10-14 reveals many situations of practical interest for which the models presented in this chapter provide only rough estimates of energy dissipation. In addition, many of these models can be improved by means of better approximations or more thorough analysis.