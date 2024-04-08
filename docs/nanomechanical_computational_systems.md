# Nanomechanical Computational Systems


### 12.1. Overview

This chapter examines a representative set of components and subsystems for nanomechanical computers, chiefly applying the bounded continuum model (Sections 9.3.3, 9.4, and 9.5). The range of useful components and subsystems is, however, larger than that considered here. The following sections describe systems capable of digital signal transmission, fan-out, switching, data storage, and interfacing with existing electronics; this suffices to demonstrate the feasible scale, speed, and efficiency of nanomechanical technologies for computation. A brief discussion surveys other components, including carry chains, randomaccess memory (RAM), and tape memory systems. The discussion of logic rods parallels that in Drexler (1988b) but applies a wider range of analytical tools to a different set of physical structures.

Within the bounded continuum model, the design of nanomechanical systems resembles that of macromechanical systems. In neither case are structures specified in atomic detail, and in both, structural properties are described in terms of parameters such as strength, density, and modulus. The special characteristics addressed in the bounded continuum model include surface corrections to strength, density, and modulus; constraints on feature size and shape; models for static friction derived from analyses based on intermolecular potentials; and phonon-interaction based models for dynamic friction. Further, many nanomechanical designs are significantly constrained by statistical mechanics and the resulting trade-offs among structural stiffnesses, positional tolerances, and error rates.

### 12.2. Digital signal transmission with mechanical rods

### 12.2.1. Electronic analogies

In conventional microelectronics, digital signals are represented by the voltages of conducting paths: a high voltage within a certain range can be taken as a 1 , and a low voltage within a certain range can be taken as a 0 . Propagation of voltages through circuits requires the flow of current, with associated delays and energy losses.

Analogously, digital signals in nanomechanical computers can be represented by displacements of solid rods; for example, a large displacement falling within a certain range can be taken as a 1 , and a small displacement falling within a different range can be taken as 0 . Propagation of displacements along rods requires motion, with associated delays and energy losses.

The parallels between existing microelectronics and proposed nanomechanical systems are not exact. The time constants in microelectronics are dominated by resistance, not inductance; time constants in the nanomechanical systems are dominated by inertia (analogous to inductance), not by drag (analogous to resistance). Elastic deformation of rods plays a role resembling (but different from) that of parasitic capacitance in conductors.

### 12.2.2. Signal propagation speed

The speed of signal propagation in rods is limited to the speed of sound, in diamond $\sim 17 \mathrm{~km} / \mathrm{s}\left(\sim 6 \times 10^{-5} \mathrm{c}\right)$. Energy dissipation caused by the excitation of longitudinal vibrational modes in a rod is small provided that the characteristic motion times are long compared to the acoustic transit time (Section 12.3.4b). Adhering to this constraint lowers the effective signal propagation speed, but delays can still be in the range familiar in microelectronic practice: at an effective propagation speed of only $1.7 \mathrm{~km} / \mathrm{s}$, for example, the delay over a $100 \mathrm{~nm}$ distance is $\sim 60 \mathrm{ps}$, and over a $1 \mu$ distance is $\sim 0.6 \mathrm{~ns}$. As will be seen, these distances are comparable to the diameter of a ${ }^{\circ} \mathrm{CPU}$. Note that the exemplar parameters developed in the following sections assume a material of lower modulus (500 GPa, vs. $\sim 1 \mathrm{TPa}$ ) and acoustic speed ( $\sim 12 \mathrm{~km} / \mathrm{s})$.

Signals can be transmitted over greater distances at higher speeds by acoustic pulses, at the cost of either dissipating the acoustic energy or requiring accurate frequency control in the drive system to permit its recovery. (Further discussion of acoustic signal propagation is deferred to Section 12.5.4, after gates, drive systems, etc., have been introduced.)

### 12.3. Gates and logic rods

### 12.3.1. Electronic analogies

In conventional microelectronics, logic ${ }^{\circ}$ gates are built using transistors. In ${ }^{\circ} \mathrm{CMOS}$ systems, a transistor makes the current-carrying ability of a path dependent on the voltage applied to a gate, which can be constructed either to transmit current at a high gate voltage and block it at low, or to block current at a high gate voltage and permit it at low.

Analogously, logic gates in nanomechanical computers can be built using interlocks. These can resemble CMOS transistors, in that interlocks can make the mobility of a rod dependent on the displacement applied to a gate knob, either permitting motion when the gate knob is at a large displacement and blocking it at low displacements, or vice versa.

Again, the parallels are not exact. In particular, CMOS transistor gates have a large capacitance relative to a comparable length of simple conducting path, causing substantial propagation delays; interlock gates, in contrast, only slightly delay signal propagation along a logic rod. Accordingly, fan-out has less effect on speed in rod logic than in CMOS logic.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-36.jpg?height=364&width=316&top_left_y=228&top_left_x=339)

(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-36.jpg?height=380&width=330&top_left_y=233&top_left_x=674)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-36.jpg?height=386&width=449&top_left_y=227&top_left_x=996)

Figure 12.1. Components of an interlock: an input rod with a gate knob and an output rod with a probe knob, shown separated (a), in their working positions (b), and constrained by a housing structure (c).

### 12.3.2. Components and general kinematics

Figure 12.1 schematically illustrates the components of an interlock, including two rods, two knobs, and a housing structure. Figure 12.2 uses a more abstract graphical notation to represent the structure and kinematics of a small logic rod system (some components are included only for compatibility with descriptions of rods having greater fan-out). In the following, the term logic rod will refer to a particular rod under consideration, and the otherwise-similar rods that interact with it will be termed input and output rods.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-36.jpg?height=619&width=787&top_left_y=1210&top_left_x=412)

(a)
![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-36.jpg?height=752&width=170&top_left_y=1190&top_left_x=1203)

(c)

Figure 12.2. Schematic diagram of a short logic rod with two inputs and one output. Diagram (a) shows the initial state, with both input rods in the blocking position. Diagram (b) shows a state in which both input rods have been moved to the unblocking position, enabling the driver to move the vertical rod and switch the output gate; diagram (c) shows a state in which one of the input rods has remained in the blocking position, forcing the drive spring to accommodate the motion of the driver and leaving the vertical rod unmoved.

a. Drivers and drive springs. The rod logic systems considered here are clocked, with a distinct clock signal for each level of gates in a combinational logic system (this approach helps minimize energy dissipation). Each rod is accordingly attached to a driver, a source of periodic, nonsinusoidal displacements; the implementation considered here achieves this motion using a follower sliding on a sinusoidally oscillating cam surface (Section 2.7.1). (The cam surface, in turn, is part of a thick drive rod, which in turn is part of a power distribution and clocking system ultimately driven by crankshafts coupled to a motor-flywheel system; Section 12.7.5.) Multiple rods can be attached to a single driver mechanism.

Driver displacements are coupled to a single rod via a drive spring. This can be a constant force spring that retains a fixed length until the force exceeds a threshold. If the rod is not blocked, as in Figure 12.2(b), displacements of the driver are transmitted through the drive spring and cause comparable displacements of the rod. If the rod is blocked, as in Figure 12.2(c), displacements of the driver chiefly cause stretching of the drive spring. The driver and drive spring thus form a drive system that periodically tensions and de-tensions the rod, without forcing motion.

b. The housing structure. A stiff housing structure surrounds the moving parts of a rod logic system, constraining their motions (within small excursions) to simple linear displacements. The surface of this housing structure serves as a bearing for the sliding motions of rods, and the rod-housing interaction can be analyzed as an extended system along the lines developed in Chapter 10.

c. Gate knobs, probe knobs, and interlocks. Each logic rod bears a series of protrusions termed knobs. A gate knob and a probe knob in a suitable housing form an interlock, as shown in Figure 12.1. A gate knob on a rod in its 0 position can be positioned to either block or fail to block the corresponding probe knob. Displacement of the gate-knob rod from 0 to 1 can thus either unblock or block a probe knob, depending on the how the interlock has been constructed. (A knob-free crossover structure can permit motion in either state.)

d. Input rods. The mobility of a logic rod can be determined by the state of an indefinitely large number of input rods, each bearing a gate knob and interacting with a probe knob on the logic rod. When none of the input rods blocks its corresponding probe knob, the logic rod is free to move when the drive system next applies tension. Figure 12.2 shows a gate with two input rods, both of which must be displaced to unblock the vertical logic rod; it implements the NAND (not-and) operation.

e. Alignment knobs. To fix the displacements of the two logic states requires an alignment mechanism. The alignment knob of a logic rod slides within a certain range, bounded by alignment stops, so that a net force in one direction places the rod in one positional state, and a net force in the other direction places it in the other positional state. If rods were rigid, the alignment knob could be located at any point; given a finite rod compliance per unit length, a location immediately adjacent to the gate knob (output) segment of the rod minimizes thermal displacements. Placing it between the probe and gate knob segments isolates the gate knob segment from fluctuations in tension caused by the drive
system, and thus ensures greater dimensional stability and better gate knob alignment relative to the output rods.

(A small advantage in alignment stiffness could be gained at the cost of a less regular structure by placing the alignment knob somewhat inside the gate knob segment. A greater advantage can be gained by placing a second alignment knob at the far end of the gate knob segment.)

f. Output rods. The displacement of a logic rod determines further steps in a computation by blocking or unblocking an indefinitely large number of output rods, each bearing a probe knob and interacting with a gate knob on the logic rod. An interlock in the output segment of one rod is in the input segment of the next. The state of the interlocks of an output segment switch when the input segment is unblocked, the drive system applies tension, and the seating knob shifts from the 0 to 1 position. In the NAND gate of Figure 12.2, the single output switches from unblocked to blocked if the rod is mobile.

g. Reset springs. When the drive system de-tensions a logic rod, a restoring force returns the rod to its resting state. This can be provided by a constant-force spring (drawn in Figure 12.2 as a large, low-stiffness spring). With this choice, the tension (and hence the strain) in the gate knob segment remains fixed throughout the cycle, allowing the gate knobs to be properly aligned with the interlocks in both the 0 and 1 logic states. Note that the tension in the probeknob segment varies, but that the resulting fluctuations in length do not affect the reliability of the logic operations.

### 12.3.3. A bounded continuum model

To explore how system performance parameters such as gate density, speed, error rate, and energy dissipation vary with device geometry and other parameters, a bounded continuum model can be applied. For components of sufficient size, and for a suitable choice of material and interface parameters, it can provide a realistic description. (For smaller components, it can give a preliminary indication of the performance to be expected, provided that a structure can be found having the appropriate geometry and properties.)

a. Geometric assumptions and parameters. For simplicity, it will be assumed that probe knob segments and gate knob segments are perpendicular, and that rods and knobs can be approximated as rectangular solids (Figure 12.3). Probe knobs can be spaced at regular intervals $d_{\text {knob }}$. The position of each gate knob depends on its logical function, but the spacing between knobs of the same kind

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-38.jpg?height=422&width=1121&top_left_y=1854&top_left_x=308)
(blocking on 1 or blocking on 0 ) is here assumed to be the same as the spacing of probe knobs, $d_{\text {knob }}$. Accordingly, each interlock in a grid of intersecting probe segments and gate segments (as in a programmable logic array, Section 12.5) occupies a square region with sides of length $d_{\text {knob }}$. Gate knobs and probe knobs are assumed to have the same dimensions.

The geometry of a rod can in some regions be described in terms of hypothetical sliding-contact surfaces (with no overlap and no gap between objects). This description implies a choice of atomic radii, which can (for uniformity) also be applied where surfaces do not make a sliding contact. For atoms in the carbon row of the periodic table, typical radii of this kind are $\sim 0.14$ to $0.17 \mathrm{~nm}$. Rod dimensions can then be described by a set of widths $w_{\text {rod }}$ and $w_{\text {knob }}$ and heights $h_{\text {rod }}$ and $h_{\text {knob }}$ defined as shown in Figure 12.3. The total height of the moving parts in an interlock is then $h_{\text {knob }}+2 h_{\text {rod }}$.

The function of a rod logic system demands that the knob length $\ell_{\text {rod }}$ meet the condition

$$
\begin{equation*}
\ell_{\mathrm{knob}} \leq d_{\mathrm{knob}}-w_{\mathrm{knob}} \tag{12.1}
\end{equation*}
$$

A simple and attractive set of choices that meets this condition is

$$
\begin{equation*}
w_{\mathrm{knob}}=w_{\mathrm{rod}}=\ell_{\mathrm{knob}}=d_{\mathrm{knob}} / 2 \tag{12.2}
\end{equation*}
$$

With these choices, the thickness of the housing structure also equals $w_{\text {rod }}$, and the minimum feature dimensions are uniform throughout. For the exemplar calculations in the following sections, it will be assumed that $w_{\text {rod }}=1 \mathrm{~nm}$, and that $h_{\text {knob }}=0.5 \mathrm{~nm}$.

The overall dimensions of a rod can be characterized by the number of input rods $n_{\text {in }}$ and output rods $n_{\text {out }}$. The length of the input segment is $\ell_{\text {in }}=d_{\text {knob }} n_{\text {in }}$; the length of the output segment is $\ell_{\text {out }}=d_{\text {knob }} n_{\text {out }}$; and (with a correction for the length of the alignment knob mechanism) the total length of the rod is

$$
\begin{equation*}
\ell_{\text {rod }}=d_{\text {knob }}\left(n_{\text {in }}+n_{\text {out }}+1\right) \tag{12.3}
\end{equation*}
$$

This length will be used in estimating several dynamical quantities; for estimating system dimensions, however, allowances must also be made for the drive system and reset spring, and their associated structures. The exemplar calculations will assume $n_{\text {in }}=n_{\text {out }}=16$, implying $\ell_{\text {rod }}=66 \mathrm{~nm}$.

b. Interactions and applied forces. The dynamics and error rates of a logic rod can be described in terms of the potential energy function of the rod, including interactions with its environment (the housing and crossing rods) and the forces applied to it by the drive and reset springs. From the description in Section 12.3.2, it can be seen that the environment of a specific mobile logic rod is the same in every cycle, with the exception of crossovers that permit mobility in either of two states. If the interaction energy of the crossing rod with the logic rod is made nearly equal in both states (e.g., with differences in van der Waals attraction compensated by differences in steric and electrostatic repulsion), then the potential energy function of the logic rod in its mobile state is nearly invariant and can be adjusted to near constancy within the permitted range of motion (as discussed in Section 10.8).

The force with which the alignment knob is pressed against a limit stop affects the PDF for thermal displacements that carry the knob away from the stop, and hence affects the error rate. Symmetry considerations suggest that the alignment force applied to one stop in the tensioned state and that applied to the other in the de-tensioned state should both be of the same magnitude, $F_{\mathrm{al}}$. Accordingly, the (constant) force applied by the reset spring equals $F_{\mathrm{al}}$, and the peak force applied by the drive spring equals $2 F_{\mathrm{al}}$. The exemplar calculations will assume $F_{\text {al }}=1 \mathrm{nN}$.

c. Stiffness and mass. In the bounded continuum model, the stiffness of knobs and rods is estimated by applying a bulk-phase modulus of elasticity to component dimensions modified by a surface correction. Assuming that rods are of diamondoid structure, with surface termination chiefly using di- and trivalent (rather than monovalent) atoms, it appears reasonable to compute stiffnesses and strengths on the basis of effective dimensions that discard a surface layer $\delta_{\text {surf }}=0.1 \mathrm{~nm}$ thick; this allows for the difference between steric and covalent radii, along with a further margin for the effects of surface relaxation. The effective cross sectional area of the rod is then

$$
\begin{equation*}
S_{\text {eff }}=\left(w_{\text {rod }}-2 \delta_{\text {surf }}\right)\left(h_{\text {rod }}-2 \delta_{\text {surf }}\right) \tag{12.4}
\end{equation*}
$$

or $0.64 \mathrm{~nm}^{2}$ in the exemplar case.

A conservative value of Young's modulus, $E=5 \times 10^{11} \mathrm{~N} / \mathrm{m}^{2}$, is used here; this is about $1 / 2$ the modulus of diamond and only moderately greater than the modulus of silicon carbide, silicon nitride, or alumina. In strong covalent solids, the shear modulus $G$ commonly is $\sim 0.5 E$, as it is in diamond.

The bending stiffness of the rod and the transverse constraint forces from the housing are large enough that the effect of the transverse vibrational modes of the rod on longitudinal stiffness and positional variance (Section 5.6) can be neglected. The stretching stiffness of a segment of rod of length $\ell$ is then simply

$$
\begin{equation*}
k_{\mathrm{s}}=S_{\mathrm{eff}} E / \ell \tag{12.5}
\end{equation*}
$$

(neglecting the stiffening effect of the knobs). For $\ell=\ell_{\text {rod }}, k_{\mathrm{s}, \text { rod }}=4.85 \mathrm{~N} / \mathrm{m}$.

In the bounded continuum model, masses are estimated by combining a density with adjusted component dimensions. In general, a slightly different value of $\delta_{\text {surf }}$ is appropriate for mass calculations, but for simplicity $\delta_{\text {surf }}=0.1 \mathrm{~nm}$ will be used throughout the exemplar calculations. With these assumptions,

$$
\begin{equation*}
m_{\text {rod }} \approx \rho \ell_{\text {rod }}\left(w_{\text {rod }}-2 \delta_{\text {surf }}\right)\left[\left(h_{\text {rod }}-2 \delta_{\text {surf }}\right)+h_{\text {knob }}\left(\ell_{\text {knob }}-2 \delta_{\text {surf }}\right) / d_{\text {knob }}\right] \tag{12.6}
\end{equation*}
$$

A density $\rho=3500 \mathrm{~kg} / \mathrm{m}^{3}$ (approximately that of diamond, somewhat higher than that of silicon carbide or silicon nitride) will yield conservative estimates of device performance. With the exemplar parameters, $m_{\text {rod }}=1.9 \times 10^{-22} \mathrm{~kg}$.

### 12.3.4. Dynamics and energy dissipation in mobile rods

The small drag forces in the exemplar system can be neglected in calculating the magnitude of dynamical quantities, then reintroduced to estimate energy dissipation. Since the elastic deformation of a mobile rod is small relative to its overall displacement, accelerations and kinetic energies are well approximated by a rigid-body analysis. Again, corrections are introduced later, both in estimating
energy dissipation and in computing requirements for the drive system. This section discusses mobile rods; Section 12.3.5 considers blocked rods.

a. Dynamics in the rigid-body approximation. The use of a cam surface in the drive mechanism (Sections 10.7.7 and 12.7.1) enables flexible control of the displacements $\Delta x(t)$ imposed on the driver, and hence of the forces applied by the drive spring. In particular, these can be chosen such that a mobile rod executes a smooth motion that (in the rigid-body approximation) can be approximated by

$$
\Delta x(t)=\left\{\begin{array}{l}
0, t<0  \tag{12.7}\\
\frac{d_{\mathrm{knob}}}{4}\left[1-\cos \left(\pi t / t_{\text {switch }}\right)\right], 0 \leq t \leq t_{\text {switch }} \\
d_{\mathrm{knob}} / 2, t>t_{\text {switch }}
\end{array}\right.
$$

This motion switches the logic state of the rod in a time $t_{\text {switch }}$. (A more accurate model would include a finite rate of onset of acceleration.)

The rod mass

$$
\begin{equation*}
m_{\text {rod }}=\rho \ell_{\text {rod }}\left(w_{\text {rod }}-2 \delta_{\text {surf }}\right)\left(h_{\text {rod }}+h_{\text {knob }} / 2-2 \delta_{\text {surf }}\right) \tag{12.8}
\end{equation*}
$$

can be combined with the peak rigid-body acceleration to yield an estimate of the peak drive force for rod acceleration

$$
\begin{equation*}
F_{\text {accel }} \approx m_{\text {rod }}\left(\pi / t_{\text {switch }}\right)^{2} d_{\text {knob }} / 4 \tag{12.9}
\end{equation*}
$$

The peak speed in this model is

$$
\begin{equation*}
v_{\max } \approx \pi d_{\mathrm{knob}} / 4 t_{\mathrm{switch}} \tag{12.10}
\end{equation*}
$$

With the exemplar parameters, if $t_{\text {switch }}=0.1 \mathrm{~ns}$, and $m_{\text {rod }}=1.94 \times 10^{-22} \mathrm{~kg}$, then $F_{\text {accel }} \approx 0.096 \mathrm{nN}$, and $v_{\max }=15.7 \mathrm{~m} / \mathrm{s}$. (The balance of this analysis assumes $F_{\text {accel }} \leq F_{\mathrm{al}}$, as is true for the exemplar parameters.)

b. An estimate of vibrational excitation. A detailed examination of the vibrational dynamics of a logic rod (e.g., taking account of the effects of alignment knob contacts and drive system force profiles on each vibrational mode) is beyond the scope of the present work. The chief interest in vibrational excitation in the present context is its role as a mechanism of energy dissipation. The energy of excitation can be estimated from a harmonic-oscillator model of the lowest vibrational mode of the rod (coupling of energy from the drive system to higher-frequency modes is much lower). The energy of vibrations excited in the housing structure should be small by comparison.

A harmonic oscillator with mass $m$, stiffness $k_{\mathrm{s}}$, and natural frequency $\omega$ will, if suddenly subject to a constant longitudinal acceleration $a$, acquire a vibrational energy

$$
\begin{equation*}
\Delta \mathscr{E}=(m a)^{2} / 2 k_{\mathrm{s}}=k_{\mathrm{s}} a^{2} / 2 \omega^{4} \tag{12.11}
\end{equation*}
$$

Substituting the peak acceleration derived from Eq. (12.9) yields

$$
\begin{equation*}
\Delta \mathscr{E}=\frac{k_{\mathrm{s}} d_{\mathrm{knob}}^{2}}{32}\left(\pi / \omega t_{\text {switch }}\right)^{4} \tag{12.12}
\end{equation*}
$$

For $\lambda \gg d_{\text {knob }}$, the speed of a longitudinal wave along a rod is

$$
\begin{equation*}
v_{\mathrm{s}} \approx \sqrt{E / \rho\left(1+h_{\mathrm{knob}} / 2 h_{\mathrm{rod}}\right)} \tag{12.13}
\end{equation*}
$$

which includes an approximate correction for knob mass (for the exemplar system, $v_{\mathrm{s}} \approx 11 \mathrm{~km} / \mathrm{s}$ ). The angular frequency of the fundamental mode of the rod (in which the far end, lacking restoring forces, is essentially free) is

$$
\begin{equation*}
\omega_{0} \approx \pi v_{\mathrm{s}} / 2 \ell_{\mathrm{rod}} \tag{12.14}
\end{equation*}
$$

To estimate the vibrational energy introduced into a rod, $\omega_{0}$ can be substituted for $\omega$ in Eq. (12.11), and $\ell_{\text {rod }} / 2$ for $\ell$ in Eq. (5.22); the resulting value of $k_{\mathrm{s}}$ can (conservatively) be substituted for $k_{\mathrm{s}}$ in Eq. (12.11). Vibrational excitations induced by deceleration can add in phase with, or cancel, those induced by acceleration. Averaging over these cases introduces a factor of two in the total vibrational energy per displacement, and yields the estimate

$$
\begin{equation*}
\Delta \mathscr{E}_{\mathrm{vib}} \approx \frac{2 S_{\mathrm{eff}} d_{\mathrm{knob}}^{2} \rho^{2} \ell_{\mathrm{rod}}^{3}}{E t_{\mathrm{switch}}^{4}}\left(1+h_{\mathrm{knob}} / 2 h_{\mathrm{rod}}\right)^{2} \tag{12.15}
\end{equation*}
$$

As can be seen from this expression, energy dissipation via the excitation of irrecoverable vibrational energy in logic rods is strongly sensitive to design choices. In particular, choosing sufficiently small values of $\ell_{\text {rod }}$ or sufficiently large values of $t_{\text {switch }}$ can reduce $\Delta \mathscr{E}_{\text {vib }}$ to negligible values. In the exemplar system, $\Delta \mathscr{E}_{\text {vib }} \approx$ $0.56 \mathrm{maJ}$.

A more detailed analysis might choose a force profile to be applied by the drive spring that delivers the alignment knob to the alignment stop with approximately zero mean relative velocity, and then tensions the input with a load of $2 F_{\text {al }}$. The smaller displacement (with the exemplar parameters, $\sim d_{\text {knob }} / 8$ ) and higher characteristic frequency $\left(\sim 4 \omega_{0}\right)$ of this tensioning motion allow it to be fast, yet induce little vibrational excitation.

c. An estimate of sliding-interface drag. The sample calculations of Section 10.4.6 indicate that band-stiffness scattering is the dominant energy dissipation mechanism in systems where $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}=0.4$ and $R=10$. Since the sliding interface between a logic rod and a housing is analogous to the sliding interface in other bearing systems, Eq. (10.23), applied with these parameters, should yield a conservative estimate of the drag in the logic rod system.

The contact area can be taken as

$$
\begin{equation*}
S=\ell_{\text {rod }}\left(w_{\text {rod }}+2 h_{\text {rod }}\right) \tag{12.16}
\end{equation*}
$$

and Eq. (10.23) with the preceding values of $\Delta k_{\mathrm{a}} / k_{\mathrm{a}}$ and $R$ yields the estimate

$$
\begin{equation*}
\Delta \mathscr{E}_{\mathrm{drag}} \approx 3.3 \times 10^{-32} \ell_{\text {rod }}\left(w_{\text {rod }}+2 h_{\text {rod }}\right) \frac{d_{\mathrm{knob}}^{2} k_{\mathrm{a}}^{1.7}}{t_{\text {switch }}} \tag{12.17}
\end{equation*}
$$

(the use of mean square rather than peak speed introduces a factor of 1/2). Assuming an interfacial stiffness $k_{\mathrm{a}}=10 \mathrm{~N} / \mathrm{m} \cdot \mathrm{nm}^{2}$ and the exemplar parameters, this yields an energy dissipation of $0.052 \mathrm{maJ}$ per displacement. Since this energy loss is small compared to the kinetic energy of motion ( $\sim 23 \mathrm{maJ}$ ), damping can (as has been assumed) be neglected in computing velocities, accelerations, and so forth.

d. Sliding-interface drag in the cam surface. If the maximum slope of the cam surface in the driver mechanism (Section 12.7.1) is $1 / 2$, then the sliding speed of the cam surface is

$$
\begin{equation*}
v_{\mathrm{cam}} \approx 2 v_{\max }\left(1+4 F_{\mathrm{al}} \ell_{\mathrm{in}} / d_{\mathrm{knob}} S_{\mathrm{eff}} E\right) \tag{12.18}
\end{equation*}
$$

where the expression in parentheses provides an upper-bound correction for the effect of the elastic deformation of the input segment. Applying the exemplar parameters, $v_{\text {cam }} \approx 38 \mathrm{~m} / \mathrm{s}$. In the contemplated system context, multiple logic rods share a drive-system cam. Reasonable values for the sliding interface in the cam are $\sim 4 \mathrm{~nm}^{2}$ per logic rod, with an interfacial stiffness $k_{\mathrm{a}}=10 \mathrm{~N} / \mathrm{m} \cdot \mathrm{nm}^{2}$. The energy dissipation per rod per $0.1 \mathrm{~ns}$ period is then $\sim 0.012 \mathrm{maJ}$. Since the cam surface continues to move when the rod is stationary, this energy must be multiplied by the reciprocal of the fraction of time spent in rod motion, $\sim 5$, yielding $\sim 0.06 \mathrm{maJ}$ per switching event.

e. An estimate of thermoelastic losses. In the transition to the tensioned state, the tension in the probe segment increases by $2 F_{\mathrm{al}}$, causing thermoelastic losses. A bound on the energy dissipation in this process can be derived from Eq. (7.49)

$$
\begin{equation*}
\Delta \mathscr{E}_{\text {therm }}<8.2 \times 10^{-5} \beta^{2} \frac{\left(2 F_{\mathrm{al}}\right)^{2}}{S_{\text {eff }}} \ell_{\text {in }} \tag{12.19}
\end{equation*}
$$

in which a volumetric heat capacity $C_{\mathrm{vol}}=1.7 \times 10^{6} \mathrm{~J} / \mathrm{K} \cdot \mathrm{m}^{2}$ and temperature $T=$ $300 \mathrm{~K}$ have been assumed. The value of the volumetric thermal coefficient of expansion $\beta$ varies widely among materials, and is occasionally negative. The values found in Table 7.1 suggest that $\beta=5 \times 10^{-6}$ will prove conservative for many diamondoid structures chosen with some attention to this parameter. With this assumption, the exemplar parameters yield $\Delta \mathscr{E}_{\text {therm }}<0.41 \mathrm{maJ}$.

f. Other energy dissipation mechanisms in mobile logic rods. Treating the knobs as phonon-scattering centers of large mass leads to estimated scattering cross sections $\sim 10^{-23} \mathrm{~m}^{2}$, and to comparatively negligible power dissipation. Thermoelastic effects caused by the motion of knobs with respect to the housing are likewise small. Compression of the alignment knob against its limit stop results in minimal nonisothermal losses because the knob is in good thermal contact with the rest of the rod, which provides a substantial heat sink.

g. The resetting process. A logic rod is reset after its output rods have been reset and before its input rods are reset. Thus, the resetting process occurs in the same environment as the switching process. Further, the motion of the driver approximates the time reversal of the switching motion, since it is driven by the same follower tracking the same cam surface, but on its return stroke. Accordingly, the overall dynamics of resetting approximate the time reversal of the switching motion, in those systems for which vibrational excitation of the rod is small. Energy losses for a switching cycle, including resetting, are therefore approximately twice those that result from the switching motion itself.

h. Nonthermal vibrations as source of noise. The motion of components generates vibrational excitations in the structure as a whole, and these are not immediately thermalized. The magnitude and effects of these vibrations depend
on the design, and nonthermal vibrations can render sufficiently bad designs unworkable. Good design practices will include the use of stiff housing structures, vibration cancellation between different components, the avoidance of structures that resonate at the major frequencies of excitation, and provision for effective damping at those frequencies.

### 12.3.5. Dynamics and energy dissipation in blocked rods

If one or more probe knobs is blocked by an input gate knob, no large displacement of the logic rod occurs, and sliding interface losses are minimal. As the driver displacement increases, the tension climbs to $\sim 2 F_{\mathrm{al}}$, the drive spring begins to extend, and the tension becomes constant. The lowest longitudinal modal frequencies of a blocked input segment are $\geq \sim 4 \omega_{0}$, reducing vibrational energy losses. The tensioned length is $\leq \ell_{\text {in }}$; hence the thermoelastic losses are comparable to or less than those for a mobile rod.

### 12.3.6. Fluctuations in stored energy

The flow of energy between the drive system and rod is large compared to the energy dissipated. Logic-state-dependent fluctuations in the energy stored in the rods (at a given point in the clock cycle) determine certain requirements for the drive system (Section 12.6), and hence must be estimated.

The greatest mechanical difference in the state of a rod occurs between a cycle in which it is mobile and one in which it is blocked near the drive spring. In a mobile cycle, the energy stored by tensioning is dominated by the energy in the reset spring $\left(\Delta \mathscr{E}_{\text {reset }}\right)$ and the strain energy of the input segment $\left(\Delta \mathscr{E}_{\text {input }}\right)$. In a blocked cycle, it is dominated by the energy stored in the drive spring ( $\left.\Delta \mathscr{E}_{\text {drive }}\right)$. The energy difference is thus

$$
\begin{align*}
\Delta \mathscr{E}_{\text {state }} & \approx \Delta \mathscr{E}_{\text {drive }}-\left(\Delta \mathscr{E}_{\text {reset }}+\Delta \mathscr{E}_{\text {input }}\right) \\
& \approx 2 F_{\mathrm{al}}\left(\frac{d_{\text {knob }}}{2}+2 F_{\text {al }} \frac{\ell_{\text {in }}}{E S_{\text {eff }}}\right)-\left(F_{\mathrm{al}} \frac{d_{\text {knob }}}{2}+\frac{\left(2 F_{\mathrm{al}}\right)^{2}}{2} \frac{\ell_{\text {in }}}{E S_{\text {eff }}}\right) \\
& \approx F_{\mathrm{al}}\left(\frac{d_{\text {knob }}}{2}+2 F_{\mathrm{al}} \frac{\ell_{\text {in }}}{E S_{\text {eff }}}\right) \tag{12.20}
\end{align*}
$$

With the parameters of the exemplar system, $\Delta \mathscr{E}_{\text {state }} \approx 1.2 \mathrm{aJ}$.

### 12.3.7. Thermal excitation and error rates

Thermal displacement of gate knobs can cause errors in switching. In principle, these errors could occur either because a gate knob blocks a probe knob when it should pass, or because it lets a probe knob pass when it should be blocked. Erroneous blockage, however, is transient relative to the switching time because (given low damping, Section 12.3.4c) the maximum delay before the obstructing knob moves from the path is $\sim 2 \ell_{\text {out }} / v_{\mathrm{s}}$, or $\sim 0.006 \mathrm{~ns}$ for the exemplar system. Accordingly, the probe knob will begin to pass the gate knob early in the switching period, even if a thermal fluctuation places the gate knob in a blocking position for a brief time.

Erroneous probe knob passage, in contrast, does not undergo fast, spontaneous reversal: it causes a faulty output. The resulting error rate can be estimated from a model of positional uncertainty in gate knob position.

a. A conservative bound on acceptable gate knob displacement. Gate knobs and probe knobs are here regarded as blocks with facing surfaces of equal extent, $w_{\text {knob }}$. In the bounded continuum model, corners are regarded as occupied by atoms, and hence are rounded. If the contact between gate knob and probe knob occurs solely through a glancing contact of corner atoms, the probe knob will exert a force tending to push the gate knob aside. For a wide range of geometries and stiffness and force parameter, this tendency can be resisted by gate-knob restoring forces.

A simple, conservative model neglects these restoring forces, and treats as an error condition any contact in which the line of travel of the center of the corner atom of a probe knob falls beyond the center of the corner atom of the corresponding gate knob. In terms of the effective steric radii for the atoms, $r_{\text {eff }}$, the effective width of the knobs is $w_{\text {eff }}=\ell_{\text {eff }}=w_{\text {knob }}-2 r_{\text {eff }}$. The acceptable gate knob displacement is then $\Delta x_{\text {thresh }}=w_{\text {eff }}$ (assuming that the knobs are aligned at $\Delta x=0$ ). For the exemplar system, assuming $r_{\text {eff }}=0.15 \mathrm{~nm}, \Delta x_{\text {thresh }}=w_{\text {eff }}=$ $0.7 \mathrm{~nm}$.

b. Probability densities and error rates. Transverse elastic displacements of the probe knob with respect to the housing are characterized by a stiffness $k_{\mathrm{s}, \mathrm{p}}$, and the parallel, longitudinal displacements of the gate knob with respect to the alignment knob are characterized by a stiffness $k_{\mathrm{s}, \mathrm{g}}$. In the size and temperature range considered here, quantum mechanical effects on positional uncertainty are negligible (Section 5.3), hence the variance in relative positions resulting from these elastic displacements is

$$
\begin{equation*}
\sigma_{\mathrm{el}}^{2}=k T\left(1 / k_{\mathrm{s}, \mathrm{p}}+1 / k_{\mathrm{s}, \mathrm{g}}\right) \tag{12.21}
\end{equation*}
$$

and the associated PDF for the elastic contribution to the relative displacement is

$$
\begin{equation*}
f_{\Delta x_{\mathrm{el}}}\left(\Delta x_{\mathrm{el}}\right)=\frac{1}{\sqrt{2 \pi} \sigma_{\mathrm{el}}} \exp \left[-\frac{1}{2}\left(\Delta x_{\mathrm{el}} / \sigma_{\mathrm{el}}\right)^{2}\right] \tag{12.22}
\end{equation*}
$$

In the approximation of hard-surface interactions between the alignment knob and its limit stops, the PDF for the corresponding contribution to the relative displacement is the exponential

$$
\begin{equation*}
f_{\Delta x}(\Delta x)=\frac{F_{\mathrm{al}}}{k T} \exp \left(-F_{\mathrm{al}} \Delta x / k T\right) \tag{12.23}
\end{equation*}
$$

The probability of a relative displacement greater than $\Delta x_{\text {thresh }}$ is then

$$
\begin{align*}
P_{\text {err-disp }} & =\int_{0}^{\infty} f_{\Delta x_{\mathrm{al}}}\left(\Delta x_{\mathrm{al}}\right) \quad \int_{\Delta x_{\mathrm{thresh}}-\Delta x_{\mathrm{al}}}^{\infty} f_{\Delta x_{\mathrm{ll}}}\left(\Delta x_{\mathrm{el}}\right) d\left(\Delta x_{\mathrm{el}}\right) d\left(\Delta x_{\mathrm{al}}\right)  \tag{12.24}\\
& \approx \exp \left[\frac{1}{2}\left(\frac{\sigma_{\mathrm{el}} F_{\mathrm{al}}}{k T}\right)^{2}-\frac{\Delta x_{\mathrm{thresh}} F_{\mathrm{al}}}{k T}\right] ; \quad \frac{\sigma_{\mathrm{el}} F_{\mathrm{al}}}{k T}<\frac{\Delta x_{\text {thresh }}}{\sigma_{\mathrm{el}}} \tag{12.25}
\end{align*}
$$

Applying the exemplar parameters, $k_{\mathrm{s}, \mathrm{p}}=10 \mathrm{~N} / \mathrm{m}$; assuming (conservatively) $k_{\mathrm{s}, \mathrm{p}}=40 \mathrm{~N} / \mathrm{m}, \sigma_{\mathrm{el}} \approx 0.023 \mathrm{~nm}$. The condition for Eq. (12.25) then holds, implying $P_{\text {err-disp }} \approx 1.3 \times 10^{-67}$.

A worst-case analysis of the resulting error rate assumes that a properly positioned rod is not latched in place by impinging probe knobs, and hence can subsequently move, allow knobs to pass, and permit an error. The characteristic frequency of rod vibration is $<10^{3}$ times the frequency of the CPU, permitting $<10^{3}$ opportunities for an error per logic-rod motion, and hence an error rate $<10^{-64}$. Error rates of this order are negligible by almost any standard.

### 12.3.8. Summary observations based on the exemplar calculations

The sample calculations in the preceding sections describe the characteristics and performance of a nonoptimized logic rod design with 16 inputs and 16 outputs. One cycle of this rod represents one-half cycle for 32 interlocks, or a total of 16 complete switching events.

a. Volume per interlock. Allowing a $0.5 \mathrm{~nm}$ thickness of material to partition one layer of interlocks from the next, the volume per interlock in a tightly packed array is $12 \mathrm{~nm}^{3}$. Including the length of the alignment knob and adding $6 \mathrm{~nm}$ at one end for the drive system and $2 \mathrm{~nm}$ at the other for the reset spring (and adjusting the effective width of a logic rod assembly to account for similar additions to the length of the crossing rods) yields an estimated volume $\sim 16 \mathrm{~nm}^{3}$ per interlock.

b. Energy per switching cycle. For a mobile rod with a switching time of $0.1 \mathrm{~ns}$, the estimated energy loss in a switching cycle (including reset) is $\sim 2 \mathrm{maJ}$. This amounts to $\sim 0.013 \mathrm{maJ}$ per interlock per switching cycle, or $\sim 0.031 k T_{300}$. This low dissipation is possible because the rod displacements in combinational rod logic systems in effect store each input and intermediate result, rendering all computations logically reversible. Note that in the limit of slow motion all of the identified energy dissipation mechanisms in combinational rod logic systems approach zero. It can be seen by inspection that the energy barriers responsible for ensuring reliable operation (Section 12.3.7) are essentially unrelated to the energy dissipated in switching (Section 12.3.4), hence there is no need to dissipate energy to ensure reliability. This is consistent with results in the extensive literature on thermodynamically reversible computation (e.g., Landauer, 1961; Toffoli, 1981; Bennett, 1982; Fredkin and Toffoli, 1982; Feynman, 1985), but inconsistent with statements in some older textbooks (e.g., Mead and Conway, 1980). Several reversible computation schemes, both electronic (based on transistors) and mechanical (based on buckling structural elements), have recently been described by Merkle (1992c, 1992d).

c. Comparison to transistors. Like transistors, interlocks are switching devices with the essential properties of a "good computer device" as defined by Keyes (1985): they support fan-out and fan-in, make reliable binary decisions, switch rapidly, pack densely, work with interconnections on their own scale, restore signals to a reference level at each step, and display high gain (in the form of a large change in output rod displacement when the gate displacement passes a threshold). In meeting these conditions, they are superior to the numerous failed device technologies described by Keyes (1989), although they suffer from the practical disadvantage of lacking an extant manufacturing technology.

In speed, interlocks are inferior to present experimental transistors, having switching times of $\sim 100$ ps rather than $\sim 10$ ps. Transistors continue to improve, while the exemplar system may be within a modest factor of real physical limits. Accordingly, there is every reason to expect that the fastest devices in the future will exploit electronic rather than mechanical phenomena; electronic devices will, of course, benefit from the precise control possible with molecular manufacturing.

In density, interlocks are greatly superior to present transistors. The area occupied by an exemplar interlock $\left(\sim 4 \mathrm{~nm}^{2}\right)$ is orders of magnitude smaller than the area occupied by a modern transistor $\left(\sim 10^{6} \mathrm{~nm}^{2}\right)$. Further, there is no obstacle to stacking interlocks with a vertical spacing of $\sim 3 \mathrm{~nm}$, while planar semiconductor processing, together with packaging, results in vertical transistor spacings $>10^{6} \mathrm{~nm}$. The overall improvement in volumetric packing density is thus $>10^{11}$.

In energy dissipation, interlocks are greatly superior to present experimental transistors. These have a switching energy of $\sim 100 \mathrm{aJ},>10^{6}$ times the calculated switching energy of the exemplar interlock. Relative to present commercial CMOS systems, the advantage in energy dissipation is $\sim 10^{9}$. To a first approximation, this advantage in switching energy translates into a $\sim 10^{9}$ increase in the quantity of computation that can be performed in a box of a certain size within given cooling limitations. (Systems like those discussed in Section 11.5 can substantially expand cooling capacity as well.)

### 12.4. Registers

Logic rods suffice to implement combinational logic systems of arbitrary depth and complexity. Without other components, however, the resulting state is destroyed when the rods are reset. To implement systems capable of iterative computation requires devices able to record the output of one computational cycle and present it as an input for a later cycle. Registers serve this function.

### 12.4.1. Kinematics of an efficient class of register

Figures 12.4 and 12.5 illustrate the structure and kinematics of an efficient class of register that abstractly parallels previous proposals based on a particle in a system with time-varying potential wells (e.g., Landauer, 1961; Bennett, 1982). The present description is based on a bounded continuum model; accordingly, the rod widths in Figure 12.4 are taken to be $\sim 1 \mathrm{~nm}$. The four components are as follows:

1. The input rod to the register is part of the output segment of a logic rod; it sets the state of the register.
2. The state rod stores the state of the register; it functions as an indicator in a measurement system (Section 11.2.1).
3. The spring rod provides a clocked bias force, helping to set the state of the register without determining the result.
4. The latching rod provides a clocked latching force, blocking movement of the state rod after the input rod is reset.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-48.jpg?height=526&width=1032&top_left_y=75&top_left_x=381)

Figure 12.4. An exploded diagram of the moving parts of a thermodynamically efficient class of register, with molecular detail suppressed in accord with the bounded continuum approximation and the housing structure omitted for clarity. Rod widths are $\sim 1 \mathrm{~nm}$; sensing and latching knobs are assumed to be single protruding atoms (to minimize van der Waals interaction energies in sensing, and to minimize knob length in latching). The rod ends marked with dots represent truncated surfaces of longer structures. See Section 12.4 for a description.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-48.jpg?height=1203&width=897&top_left_y=923&top_left_x=437)

Figure 12.5. Steps in the write-erase cycle of a thermodynamically efficient register, illustrated as in Figure 12.4. A housing structure (not shown) constrains rods to move along their axes. Black arrows show motion; white arrows show displacement.

The interaction of these components is diagrammed in Figure 12.5 and described in the following sections.

a. Compression. In frame (a) of Figure 12.5, both the spring rod and the latching rod are retracted. This leaves the state rod subject to thermal motion, traversing a range that carries the output knob through both its blocking and nonblocking positions (relative to a probe knob on a logic rod to which the state of the register cell is an input). In the transition to frame (b), the spring rod advances, pressing a small, compliant knob against the spring surface of the state rod, which is thereby forced toward the right, compressing its range of motion into the nonblocking 0 position.

b. Input. In the transition from (b) to (c.1), the input rod moves to its 1 state, and the contact between the input knob and the sensing knob forces the state rod to the left, into its 1 position. In doing so, the input rod does $\sim 30 k T_{300} \approx$ $120 \mathrm{maJ}$ of work against the force applied by the spring knob; assuming a displacement of $0.5 \mathrm{~nm}$, the required force is $\sim 0.24 \mathrm{nN}$.

In the transition from (b) to (c. 0 ), the input rod remains in its 0 state, and no displacements occur. The state rod remains in its 0 position. (In either sequence, the state rod can now be read as an input to the next level of logic.)

c. Latching. In the transition from (c.0) to (d.0), the latching rod advances, pressing the latching knob further to the right and stabilizing the state rod in its 0 position. In the transition from (c.1) to (d.1), the latching probe presses the latching knob further to the left, stabilizing the state rod in its 1 position.

d. Input reset. In the transition from (d.0) to (e.0), the spring rod retracts, leaving the state rod latched in place. In the transition from (d.1) to (e.1), both the spring rod and the input rod retract, again leaving the state rod latched in place. These retractions need not be synchronized. In both instances, the resetting of the input rod (along with others controlled by the same clocking phase) can initiate a chain of resetting operations that returns a preregister combinational logic system to its initial state. Meanwhile, the latched state rod continues to serve as an input gate knob for a logic rod in the first stage of a postregister combinational logic system.

e. Expansion. After the postregister combinational logic system has completed its cycle and been reset, the latching rod can be retracted, returning the state rod to the condition represented by frame (a). The reexpansion of the range of motion of the state rod discards the stored information and increases entropy by $\ln (2) k$.

### 12.4.2. Device size and packing

State rods can have the same widths and separations as the exemplar logic rod ( $1 \mathrm{~nm}$; see Section 12.3.3a), making the registers geometrically compatible with densely packed arrays of logic rods. With the geometry shown in Figure 12.4, the length of the assembly is $\sim 4 \mathrm{~nm}$, and its height is $\sim 5 \mathrm{~nm}$ (including an allowance for housing structure), yielding a total volume of $\sim 40 \mathrm{~nm}^{3}$. This volume should prove conservative.

### 12.4.3. Energy dissipation estimates

Unlike logic rods in a purely combinational system, these registers undergo a logically and therefore thermodynamically irreversible cycle. Their energy dissipation mechanisms can be divided into frictional mechanisms (which in a good design can approach zero loss per cycle as speed approaches zero) and fundamental mechanisms (which impose a fixed loss per cycle, regardless of speed).

a. Vibrational, thermoelastic, and drag losses. Owing to small size and high modal frequencies, losses resulting from the excitation of vibrations can be made negligible compared to those in logic rods. Thermoelastic losses depend on the square of the stress, which is substantial only in the spring rod, and then only if one spring rod serves many register cells. With a cross-sectional area of $\sim 1 \mathrm{~nm}^{2}$, a spring rod serving 16 register cells has a mean-square tensile stress of $\sim 4 \mathrm{GPa}$. This yields an estimated thermoelastic loss of $\sim 0.04 \mathrm{maJ}$ per cell per cycle.

The speeds of sliding motions are uniformly equal to or less than those in the associated system of logic rods. Since the sliding interfaces are similar, the energy losses per unit area per cycle are similar. The sliding interface area of an interlock with the exemplar parameter is $\sim 12 \mathrm{~nm}^{2}$; for the register system, it is roughly twice that. Accordingly, drag losses can be estimated at $\sim 0.01 \mathrm{maJ}$.

b. Nonisothermal compression and expansion losses. Losses from nonisothermal compression and expansion can be estimated using the model of Section 7.5.1. With the stated dimensions and a density of $3500 \mathrm{~kg} / \mathrm{m}^{3}$ of (surfacecorrected) volume, the mass of the state rod is $\sim 6 \times 10^{-24} \mathrm{~kg}$, giving it a root mean square thermal velocity of $\sim 25 \mathrm{~m} / \mathrm{s}$ at $300 \mathrm{~K}$.

During the compression phase, the extension of the spring rod reduces the range of motion of the state rod from $\sim 0.5 \mathrm{~nm}$ to a small region (e.g., an effective width of $\sim 0.16 \mathrm{~nm}$, assuming that the stiffness of the final potential well is $\sim 1 \mathrm{~N} / \mathrm{m}$ ). If the compression operation is assumed to take $0.1 \mathrm{~ns}$, with an approximately linear motion over a distance of $0.5-0.16=0.34 \mathrm{~nm}$, then the speed is $3.4 \mathrm{~m} / \mathrm{s}$. Assuming that the input knob and the spring probe are built for reasonably efficient energy exchange with state knob thermal motions, Eq. (7.62) with an accommodation coefficient $\alpha=0.5$ should provide a reasonable estimate of the energy loss. With the above parameters, the result is $\sim 1.4 \mathrm{maJ}$.

During the expansion phase, the withdrawal of the latching rod allows expansion of the range of motion of the state rod from a small region to a $0.25 \mathrm{~nm}$ long region before free expansion occurs (assuming, for the moment, that barrier crossing is switched on instantaneously) with an estimated energy loss of $\sim 0.14 \mathrm{maJ}$.

Nonisothermal compression and expansion results in the largest speeddependent, nonfundamental losses identified here. These can be reduced by reducing speed (undesirable but direct and effective), reducing compression and expansion lengths (for which there is only modest scope), reducing state rod mass (substantially, in a good design), and improving the coupling of state rod motions to thermal modes (which will involve trade-offs between drag and nonisothermal compression losses).

c. Free expansion losses. As the latching probe withdraws, the barrier dividing the potential wells corresponding to 0 and 1 disappears; in good designs,
these potential wells have approximately equivalent free energies throughout the merging process. As discussed in Section 7.6.3, the merger of symmetrical potential wells leads to an increase in entropy of $\ln (2) k$, and hence to a loss of free energy of $\ln (2) k T$, or $\sim 2.87 \mathrm{maJ}$ at $300 \mathrm{~K}$. This loss is irreducible.

d. Summary of losses. Losses dependent on design and speed of operation are estimated to total $\sim 1.6 \mathrm{maJ}$. Thermodynamically irreducible losses resulting from register erasure are $\sim 2.87 \mathrm{maJ}$. Total losses are thus $\sim 4.5 \mathrm{maJ}$ per register cell per cycle.

### 12.4.4. Fluctuations in stored energy

The energy stored in a register cell during the input phase depends on the logic state: in writing a 1 , the input rod does work against the spring probe, causing a net transfer of energy (on spring-probe withdrawal) from the input-rod drive system to the spring-rod drive system. This energy transfer is on the order of $120 \mathrm{maJ}$, with the precise value depending on design details and the required reliability of the register.

### 12.5. Combinational logic and finite-state machines

Combinational logic systems compute sets of Boolean functions (mapping from bit vectors to bit vectors), and commonly are built using programmed logic arrays (a.k.a. programmable logic arrays, programmable array logic, PALs, and PLAs). PLAs can be combined with registers to build finite state machines and much of the control circuitry for a CPU (Mead and Conway, 1980). The following discussion of PLAs illustrates how logic rods and registers can be combined to build clocked computational systems.

### 12.5.1. Finite-state machine structure and kinematics

The PLA-based finite state machine illustrated in Figure 12.6 is nearly a devicefor-device translation of a design described in Mead and Conway (1980). The chief differences are (1) that the use of devices abstractly resembling CMOS rather than ${ }^{\circ} \mathrm{NMOS}$ transistors halves the number of device columns in the AND-plane, and (2) that state information transmitted from the output register to the input register passes through a simple PLA structure, providing a delay during which the rods in the main PLA are reset.

Computation proceeds as follows: First, the vertical rods to the left, set 1 of PLA (a), are tensioned; their mobility is determined by the bit vector latched into the register to the lower left, register (ba). After a switching time, the horizontal rods, set 2 of (a), are tensioned; their mobility is determined by the state of set 1. After another switching time, the vertical rods to the right, set 3 of (a), are tensioned; they move as determined by set 2 . Finally, the state of set 3 is latched into the register to the lower right, (ab), by tensioning the latching rod (L2). A similar process then starts with this register and propagates through the lower PLA (b) while the series of motions in the upper PLA is reversed.

### 12.5.2. Finite-state machine timing and alternatives

a. Two-register systems. The upper panel of Figure 12.7 presents a timing diagram for a two-stage finite state machine. Note that the time for a cycle (including two register-to-register transfers with intervening combinational logic)

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-52.jpg?height=1021&width=1071&top_left_y=177&top_left_x=340)

Figure 12.6. A PLA-based finite state machine translated from an NMOS design (Mead and Conway, 1980) to nanomechanical logic, shown in the notation of Figure 12.1, but omitting several drive and spring systems owing to the constraints of a flat representation. Rod labels correspond to those in the source. PLA (a) is above the L rods; a smaller PLA, (b), is below. Rows of circled Rs represent cells in two registers.

is $10 t_{\text {switch }}$, or $1 \mathrm{~ns}$ for the parameters used in the exemplar system. In this timing sequence, both the register compression processes (driven by the spring rod) and the latching processes (driven by the latching rod) take $t_{\text {switch }}$, as assumed in Section 12.4.3. Motion of the first set of rods in the postregister PLA, however, does not immediately follow the displacement of the last set of rods in the preregister PLA (as it could, based on purely local constraints); it is instead delayed by $2 t_{\text {switch }}$ in order to satisfy global timing constraints involving the requirement that a PLA and its input register be reset when the other PLA output is ready to be written. In the overall cycle, $4 t_{\text {switch }}$ out of the cycle time of $10 t_{\text {switch }}$ is consumed in these delays.

b. Four-register systems. These delays can be eliminated by moving to a different architecture. The lower panel of Figure 12.7 shows a timing diagram for a four-stage finite state machine, in which a cycle involves four register-to-register transfers with intervening combinational logic. If PLA (a) and (c) are the same as (a) in the above example, and if (b) and (d) are the same as (b) in the two-register example, then (aside from an alternation in which register contains the most current bit vector) the systems are equivalent, with one full four-stage cycle corresponding to two cycles of the two-stage system. If (a) $\neq$ (c) and
![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-53.jpg?height=1040&width=856&top_left_y=188&top_left_x=342)

Figure 12.7. Timing diagrams for two PLA-based systems, with time measured in units of the logic rod switching delay $t_{\text {switch }}$, and driver displacement represented on an arbitrary scale (tensioned is high, de-tensioned is low). Upper panel: with two PLAs, (a) and (b), two registers, (ab) and (ba). Lines (a1), (a2), (a3) represent the driver displacements for the sets of rods in PLA (a); lines (ab-S) and (ab-L) graph the displacements of the spring rod and the latching rod drivers (respectively); other labels are analogous. Lower panel: with four PLAs and registers, otherwise analogous to the upper panel.

(b) $\neq$ (d), then the four-stage system is equivalent to a more complex system of two-stage register-to-register PLAs.

The four-stage architecture performs register-to-register combinational logic operations at $5 / 3$ the frequency of the two-stage architecture, using twice the volume and device count to do so. The register compression process, moreover, can be allotted a time period of $3 t_{\text {switch }}$ to complete; the energy dissipation model for this process predicts that this change will divide energy dissipation by a factor of 3. The estimates in Sections 12.3.4 and 12.4.3 suggest that register compression is the largest nonirreducible energy loss mechanism. Accordingly, in systems where mass and volume are inexpensive, and where speed and low power dissipation are at a premium, it appears that a four-stage architecture is superior to a two-stage architecture.

c. Estimated instruction execution rate in a $\boldsymbol{C P U}$. The time required for register-to-register transfer through a PLA ( $t_{\mathrm{PLA}}$ ) can be used to estimate the clock rate in a CPU. A clock cycle in a well-designed RISC (reduced instruction
set computing) machine requires $2 t_{\mathrm{PLA}}$ to $3 t_{\mathrm{PLA}}$, with the latter being a conservative value for the present purposes (Knight, 1991). In a RISC machine operating with a typical mix of instructions, the rate of instruction execution can equal or (in a superscalar architecture) exceed the clock rate (Hennessy and Patterson, 1990). With a four-register architecture based on the exemplar parameters of previous sections, $4 t_{\mathrm{PLA}}=1.2 \mathrm{~ns}$; hence a conservatively designed rod logic technology should enable the implementation of RISC machines capable of $>1000$ MIPS. This is competitive with the speed of current microelectronics, but is presumably inferior to the speed of future electronic systems.

### 12.5.3. Fan-in, fan-out, and geometric issues

The exemplar logic rod described in Section 12.3 is straight and has a fan-in and fan-out of 16 . Real systems will seldom require a rod with exactly these properties.

a. Changes in fan-in. Reducing fan-in shortens the input segment and increases its stiffness, improving feasible switching speed and reducing the total volume and energy dissipation per rod. The overhead of the drive mechanism, alignment knob, and reset spring are spread over a smaller number of devices, however, increasing the volume and energy dissipation per device.

Fan-in can be increased by lengthening the input segment, but at the cost of decreasing the feasible switching speed. Alternatively, multiple input segments can be mounted in parallel (e.g., yoked together at the drive end and at the alignment knob), yielding a system with the same logical properties as a series connection, but with higher vibrational frequencies and hence a higher feasible switching speed. (Indeed, this strategy might be desirable for $n_{\text {in }} \leq 16$.)

b. Changes in fan-out. Reductions in fan-out parallel reductions in fan-in where stiffness, switching speed, energy dissipation, and volume are concerned. The resulting increases in stiffness also reduce error rates resulting from thermal noise; in optimized designs (where error rates are significant but acceptable), this shift will typically permit the use of either slimmer rods or lower values of $F_{\mathrm{al}}$.

Increasing fan-out increases both switching speed and error rates, but errors can be kept in check by proportional increases in $S_{\text {eff }}$ (and hence stiffness). Again, yoking a set of shorter output segments together in parallel (e.g., at the alignment knob and the reset spring) results in a system with the same logical properties but higher frequencies and switching speeds. This strategy reduces errors from thermal excitation and reduces the required magnitude of $F_{\mathrm{al}}$, on a per-rod basis. (And again, this strategy might be desirable for $n_{\text {in }} \leq 16$.)

c. Flexible rod geometries. Interlocks can be linked by flexible rods passing through curved housings. Flexible rods can be made from structures that are one atom thick in the direction of curvature, such as polyyne chains or strips having a graphitic structure. These can have a radius of curvature $\sim 1 \mathrm{~nm}$, and the potential energy functions for sliding motions in the housings can be smooth (see Sections 10.5 and 10.8). Curved linkages enable broad geometric flexibility in the design of rod logic systems, permitting (for example) the use of PLAs stacked face to face that share access to a register.

### 12.5.4. Signal propagation with acoustic transmission lines

In the exemplar system, the state of an output gate is switched in $0.1 \mathrm{~ns}$ over a distance of $64 \mathrm{~nm}$, yielding an effective signal propagation speed of only $640 \mathrm{~m} / \mathrm{s}$. In larger logic systems, it is desirable to transmit signals at the full acoustic speed, $\sim 17 \mathrm{~km} / \mathrm{s}$ in diamond. This can be accomplished using systems that launch acoustic pulses at one end of a rod and probe displacements at the other.

a. Kinematics and positional uncertainty. For concreteness, consider a rod $5 \mu$ in length, with $S_{\text {eff }}=3 \mathrm{~nm}^{2}$ and $E=10^{12} \mathrm{~N} / \mathrm{m}^{2}$. The one-way signal propagation time along this rod is $\sim 0.3 \mathrm{~ns}$. As with the exemplar logic rods, a drive system and drive spring apply forces to one end, and an input segment with one or more interlocks then either blocks or fails to block displacement of the rod. If the rod is in a mobile state, the force applied by the drive spring accelerates the rod. After $0.1 \mathrm{~ns}$, a force of $1.8 \mathrm{nN}\left(\approx 2 F_{\mathrm{al}}\right.$ in the exemplar system $)$ will have displaced the end of the rod by $1 \mathrm{~nm}$ and propagated a region of tensile stress $1.7 \mu$ along the rod. Ceasing to apply tension for a further $0.1 \mathrm{~ns}$, then applying a reverse force for $0.1 \mathrm{~ns}$ restores the rod end to its initial position, while launching a wave which, as it passes, displaces the rod by $1 \mathrm{~nm}$ for $0.1 \mathrm{~ns}$. At the far end, the displacement can be probed by a conventional interlock controlling a short, briefly displaced logic rod that writes into a register and is immediately reset.

The positional uncertainty at the receiving end of the rod is adequately constrained by positional control at the sending end. The energy associated with a $1 \mathrm{~nm}$ stretching deformation of the rod is $\sim 600 \mathrm{maJ}$, or $\sim 150 k T_{300}$. Nonthermal vibrational modes are a concern, but clocked damping can be introduced to remove energy from these modes between signal pulses, without dissipating energy from the signal pulses themselves.

b. Energy recovery. The energy of a wave of this sort is $\sim 3.6 \mathrm{aJ}$. The roundtrip signal propagation time is $\sim 0.6 \mathrm{~ns}$; hence a pulse can be launched and recovered in a single clock period. In systems with stable clocking at the correct speed, the energy delivered by the reflected pulse can be recovered by a suitably structured drive system. Since an outgoing pulse consisting of a rarefaction followed by a compression is reflected from a free end as a compression followed by a rarefaction, the return pulse resembles a time-reversed version of the outgoing pulse, and a simple reversal of drive shaft motion produces a sequence of cam displacements that couples the energy or the return pulse into the drive system with reasonable efficiency. Energy dissipation is larger than that in the exemplar rods, but the need to propagate signals over such a distance should be reasonably rare; a sphere of $5 \mu$ radius can contain $>10^{10}$ interlocks.

### 12.6. Survey of other devices and subsystems

Although registers and PLA-based combinational logic in principle suffice to implement general-purpose computational systems, devices of several further classes are of considerable practical importance. The following sections briefly survey gates suitable for non-PLA combinational logic, carry chains for efficient implementation of arithmetic logic units (ALUs), and both random-access and tape-based memory systems; it closes with a discussion of devices for interfacing to macroscale systems.

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-56.jpg?height=477&width=975&top_left_y=198&top_left_x=417)

Figure 12.8. Schematic diagram of an OR gate operating within a single rod displacement cycle.

### 12.6.1. Gates for non-PLA combinational logic

A PLA system requires three successive rod displacement cycles to compute a set of Boolean functions. The functions AND, OR, and NOT can, however, be computed in a single displacement cycle by what is here termed direct logic.

The direct logical OR of a set of inputs can be computed by a linkage in which any input rod can displace the output rod without displacing any other input rod. This can be done by a mechanism like that in Figure 12.8. The direct logical AND of a pair of inputs can be computed by a mechanism like that in Figure 12.9 (note that the inputs need not be synchronous). If 1 and 0 states are defined by the direction of rod displacement, then a direct logical NOT can be computed by a lever having input and output rods attached on opposite sides of the fulcrum.

Direct gates add length and compliance, thereby increasing the minimal switching time relative to a connection not passing through a gate. This effect is small, however: several layers of direct combinational logic can be performed within the $0.1 \mathrm{~ns}$ switching time of a rod with the exemplar parameters. Regular recourse to clocked, interlock-based logic can provide the power and logic-level restoration required for complex computations.
![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-56.jpg?height=516&width=1016&top_left_y=1604&top_left_x=417)

Figure 12.9. Schematic diagram of an AND gate operating within a single rod displacement cycle.

### 12.6.2. Carry chains

Carry chains play an essential role in ALUs. A familiar example is the propagation of a carry bit when $00000001_{\text {binary }}$ is added to $01111111_{\text {binary }}$ to yield $10000000_{\text {binary }}$ (note that the left-most bit of the output can in general depend on the state of any bit in either input). In a carry chain, one cell represents each bit in a binary number, and a series of operations propagates carry information along the series of cells. In a fast carry chain, propagation does not require a ripple of switching operations moving from the low bit to the high. For example, a transistor-based Manchester carry chain (see Mead and Conway, 1980) forms a set of conducting paths through the cells by switching transistors to a conductive state where a carry signal should propagate to the next cell, and switching transistors to a nonconductive state where a carry signal should be blocked. This occurs in one step; a subsequent step applies carry-determining signals that propagate through the cells without switching delays.

An analogous scheme can be used in a nanomechanical ALU. Special-purpose rod segments (sliding in parallel grooves set at a shallow angle to the axis of the carry chain) can be coupled or decoupled by pins that are displaced by input rods. These specialized rod segments can then be driven by a set of carry-determining input rods; the carry signals then propagate through sets of precoupled segments. For a 32-bit word size, the length of a carry chain is about the same as the length of the exemplar rods (Section 12.3.3a). The compliance of the junctions between segments decreases the mean stiffness of the rod, reducing the low-frequency acoustic speed by about $1 / 2$. Carry signal propagation in a 32 -bit system is accordingly estimated to take about twice the switching time for an exemplar rod, or $\sim 0.2 \mathrm{~ns}$.

### 12.6.3. Random-access memory

Rod logic systems can be used to transmit and decode requests to a RAM and to carry the information read or written. As with registers and carry chains, however, the RAM itself requires specialized mechanisms.

To read (or write) one of many different words from a strip of RAM using a single set of read/write rods, an address signal must be able to engage the correct row of bit cells with the rods while other similar rows are left disengaged. One design approach that achieves this has features in common with register cells (Section 12.4), moving entire rows of cells as a unit to engage and disengage them. The size, speed, and energy dissipation of a RAM cell should be similar to that of a register cell.

### 12.6.4. Mass storage systems

RAM permits fast access and good energy efficiency, but at the cost of considerable bulk per bit stored. Denser information storage can be provided by a tape memory system based on polymer chains with side groups of two distinct kinds.

For example, a partially fluorinated polyethylene molecule can store two bits per carbon atom by representing 1 with an $\mathrm{F}$ atom and a 0 with an $\mathrm{H}$ atom. $\mathrm{A}$ chain of this sort can be read by a measurement system (Section 11.2) and written by a mechanochemical device able to perform abstraction and deposition reactions. The design of the reading mechanism can be simplified if one surface
of the molecule has a uniform structure (all $\mathrm{H})$; the design of the writing system can be simplified if each carbon on the other surface has exactly one $F$ (writing can then proceed exclusively by removing an $\mathrm{H}$ and then depositing an $\mathrm{H}$ on the proper face of the resulting pi radical). With these restrictions, the storage density for the tape itself is one bit per two carbon atoms, or $\sim 15 \mathrm{bits} / \mathrm{nm}^{3}$. Alloting twice the tape volume for other functions (to accommodate reels, packing inefficiency, drive systems, read-write mechanisms, and so forth) decreases the mean storage density to $\sim 5 \mathrm{bits} / \mathrm{nm}^{3}$, or $5 \times 10^{21} \mathrm{bits} / \mathrm{cm}^{3}$.

A volume of $10^{4} \mathrm{~nm}^{3}$ appears ample for a read-write mechanism. If 10 times this volume is allocated to the corresponding tape (and reels, etc.), then the tape-unit capacity is $\sim 5 \times 10^{5}$ bits. At $10^{9}$ bits/s, reading the entire tape takes $500 \mu \mathrm{s}$. At a seek speed of $10 \mathrm{~m} / \mathrm{s}$, traversing the length of the tape takes $\sim 15 \mu \mathrm{s}$. Accordingly, the expected access times of molecular tape storage systems are substantially less than those of macroscale disk storage systems.

### 12.6.5. Interfaces to macroscale systems

Demonstrating the feasibility of interfacing nanomechanical computational devices to conventional microelectronics shows how nanomechanical systems can be interfaced to systems that are in turn interfaced to the macroscale world. This can be accomplished using electromechanical devices (Section 11.6).

a. Input. Electrostatic actuators of the sort described in Section 11.6.4 can be used to transmit data from a $5 \mathrm{~V}$ microelectronic system to a rod logic system; doubling the plate area (and hence the force) enables the actuator to replace the input segment of an exemplar logic rod. Electrostatic forces of the stated magnitude can move a plate with a mass equaling that of a $1 \mathrm{~nm}$ thick slab of diamond by $1 \mathrm{~nm}$ in $\sim 0.03 \mathrm{~ns}$. Data input rates can accordingly be consistent with the rod logic speeds calculated in Section 12.5.

b. Output. Modulated tunneling junctions like those described in Section 11.6.3 can convert logic rod displacements into electrical signals that can be detected by microelectronic systems. At a junction potential of $1 \mathrm{mV}$ and resistance of $10^{4} \Omega$ (Section 11.6.2), the current is $1 \mu \mathrm{A}$ and the resistive power loss is $10 \mathrm{nW}$. Existing transistors can switch with $\sim 10^{-15} \mathrm{C}$ of charge, requiring $\sim 10^{-9} \mathrm{~s}$ of current flow at this rate; accordingly, data can be output at a clock rate like that estimated in Section 11.5.2. The energy dissipated in the junction per bit communicated is $\sim 10$ aJ. Sliding-contact switches (e.g., based on conductors terminated by graphitic planes) might reduce resistance and reduce power requirements.

c. System context. In typical systems containing many nanocomputers, nanoscale systems will communicate chiefly with other nanoscale systems, and little of the communications traffic will be with macroscale systems. Accordingly, the energy dissipated per bit in communicating with the macroscale world is relatively unimportant. Finally, since molecular manufacturing techniques can produce large devices, communication between nanoscale and macroscale systems need not proceed through conventional microelectronics (even if this were still in use), but could instead be mediated by a chain of amplifiers better matched to the problem.

### 12.7. CPU-scale systems: clocking and power supply

In electronic digital logic, clocking systems with two, four, or eight phases are not uncommon. What were termed two- and four-stage architectures in Section 12.5.2 might seem similar, but are in fact substantially different: each stage includes three levels of logic and a register with two control rods; this requires a total of twenty distinctly clocked inputs in a four-stage system. Further, the clocking signals in electronic digital logic are used to modulate power distributed by a DC system, while rod logic systems use the clocking signals as a power supply. The architecture of the clocking and power supply system is accordingly quite different.

To estimate clocking and power-distribution parameters appropriate for CPU-scale systems requires a model describing the size and contents of a CPU. The following will assume that a CPU-scale system contains $10^{6}$ interlocks, $10^{5}$ logic rods, and $10^{4}$ register cells, which (together with interconnects, power supply mechanisms, wasted space, etc.) occupy a cube $400 \mathrm{~nm}$ on a side. (Assuming a mean density of $2000 \mathrm{~kg} / \mathrm{m}^{3}$ implies a mass of $1.6 \times 10^{-17} \mathrm{~kg}$ and hence a halflife against radiation damage in Earth ambient background radiation of $\sim 100$ years; see Figure 6.13.)

### 12.7.1. Clocking based on oscillating drive rods

Consider the timing diagram for a two-stage system (shown in the upper panel of Figure 12.7). The tensioning and de-tensioning of each set of rods can be characterized by the duration of the tensioned and de-tensioned intervals and by the time marking the middle of the tensioned interval; this time can be taken to define the phase of the clock for that set of rods. Inspection of this diagram shows four phases: one for the logic rods of PLA (a) and the spring rod of register (ab), another for the latching rod of register (ab), and another two phases for PLA (b) and register (ba).

As illustrated in Figure 12.10, a sinusoidally oscillating cam surface on a drive rod can generate clocked drive-system impulses having intervals determined by the position of the follower with respect to the mean position of the ramp on the cam surface. The drive system for a set of rods could use several follower-and-ramp sets on the same drive rod; these can move in synchrony. A single drive rod (or system of drive rods sharing single phase) can power several drive systems having different intervals of tensioning. Further, since a ramp can slope in either direction, sets of rods differing in phase by $2 \pi$ can likewise be driven by a set of drive rods sharing a single phase. Accordingly, the ten different patterns of clocked impulses required for the two-stage system in Figure 12.7 can be generated by drive rods having only two distinct phases; the four-stage system similarly requires only four driver phases.

### 12.7.2. A CPU-scale drive system architecture

A drive system requires a mechanism for linking drive rods so that different sets have the correct relative phases, a mechanism for buffering energy to compensate for fluctuations in the energy stored in the logic system in different logic states, and a source of motive power to compensate for energy losses. The source

![](https://nanosystems.contact.ms/cropped/2024_03_29_1c4538e301c65fe5bda2g-60.jpg?height=550&width=1110&top_left_y=180&top_left_x=340)

Figure 12.10. Diagrams and text illustrating the generation of clocked drive-system impulses of varying intervals from the sinusoidal motion of a cam surface (only one ramp and one follower are shown).

of motive power can be a DC electrostatic motor (Section 11.7). The mechanism for buffering energy can be a flywheel rotating at the frequency of the system clock. The linking mechanism can be a crankshaft able to convert a single rotary motion into an indefinitely large number of linear, approximately sinusoidal motions of differing relative phases. (Note that subsidiary crankshaft mechanisms can be used at remote locations to couple drive subsystems of differing phase, permitting energy transfer between them and increasing the resistance to local desynchronization. These subsidiary crankshafts also provide one of several mechanisms for transmitting drive power around corners.)

The dynamics of this clocking system differ from the dynamics of clocking systems in integrated circuits, which are dominated by damping, leading to the diffusive spread of a clock signal along the conducting paths. The mechanical system, in contrast, is dominated by inertia, leading to resonant behavior in which all parts of the system could (in the absence of load) share a single phase. In real systems, however, loads will cause clock skew.

### 12.7.3. Energy flows and clock skew

During a clock cycle, a drive rod executes an oscillation, forcing movement in a set of logic, spring, or latching rods. If the energy stored in these rods as a function of time were invariant from cycle to cycle, and if there were no energy dissipation, then the potential energy of the drive rod as a function of position could be adjusted to allow it to move as a harmonic oscillator, executing sinusoidal oscillations with no external energy input or constraining force. In practice, variations in the energy stored in rods from cycle to cycle cause fluctuating forces and displacements in the drive system, and energy must on the average flow into the drive rod from an external source to compensate for energy losses.

a. Energy fluctuations. Fluctuations in stored energy are $>100$ times greater than fluctuations in dissipated energy (per clock cycle), and hence dominate the
cycle-to-cycle fluctuations in drive-system dynamics. Further, fluctuations in the energy stored in logic rods are $\sim 10$ times greater than comparable fluctuations in register cells. An energy-based analysis focusing on logic rod states can provide an estimate of the magnitude of the drive system stiffness and inertia required to ensure that these fluctuations do not cause excessive disturbances in local clock phase.

An examination of the timing diagrams in Figure 12.7 shows that no more than $1 / 3$ of the 6 sets of logic rods in the two-stage system are tensioned simultaneously, as are no more than 5/12 of the sets in the four-stage system. Accordingly, the estimated $1.2 \mathrm{aJ} \Delta \mathscr{E}_{\text {state }}$ derived for logic rods with the exemplar system parameters (Section 12.3), together with the assumed $10^{5}$ rods for a CPU-scale system, yields an estimated maximum variation in stored energy (relative to the mid-range value) of $\Delta \mathscr{E}_{\max }=1 / 2 \times 5 / 12 \times 10^{5} \times 1.2 \mathrm{aJ}=2.5 \times 10^{-14} \mathrm{~J}$.

(Note, however, that a logic system could be built in which every logic rod set to a 1 state is mirrored by a rod set to a 0 state, thus cancelling the major contributions to $\Delta \mathscr{E}_{\text {max }}$; this approach would approximately double system volume and energy dissipation. This scheme has electronic parallels.)

b. Acceptable clock skew and required drive-system stiffness. In a system with the exemplar rod parameters, switching causes a $1 \mathrm{~nm}$ displacement in the gate knobs, and a comparable displacement in the probe knobs. An interlock switching from a nonblocking to a blocking state can produce an error if substantial probe knob displacements precede substantial gate knob displacements; significant added energy dissipation and an increased probability of error can occur if the motion periods overlap more than slightly.

A system that undergoes a premature probe-knob displacement of $\leq 0.05 \mathrm{~nm}$ in the worst-case logic state will suffer negligible degradation of reliability or energy dissipation. With the exemplar parameters, this displacement corresponds to a clock skew of $\sim 0.014 \mathrm{~ns}$. At a drive-rod speed of $\sim 38 \mathrm{~m} / \mathrm{s}$, (Section 12.3.4d) this skew corresponds to a displacement of $\sim 0.53 \mathrm{~nm}$ relative to the optimal drive-rod position (a phase-angle error $\Delta \phi \approx 0.073 \mathrm{rad}$ ). If the energy occurring in a maximal fluctuation, $\Delta \mathscr{E}_{\max }=2.5 \times 10^{-14} \mathrm{~J}$, were delivered in a single period $t_{\text {switch }}=0.1 \mathrm{~ns}$ over a stroke length $0.1 \mathrm{~ns} \times 38 \mathrm{~m} / \mathrm{s}=3.8 \mathrm{~nm}$, the mean (fluctuating-component) force applied to the drive system during this period would be $\sim 6.6 \times 10^{-6} \mathrm{~N}$.

To transmit this force while limiting the elastic displacement to $\sim 0.53 \mathrm{~nm}$ requires a system with a stiffness of $\sim 1.2 \times 10^{4} \mathrm{~N} / \mathrm{m}$. If this is to be achieved using drive mechanism components with a typical length of $200 \mathrm{~nm}(\sim 1 / 2$ the system diameter) and a modulus $E=10^{12} \mathrm{~N} / \mathrm{m}^{2}$, the required total cross sectional area of the rods is $\sim 2500 \mathrm{~nm}^{2}$, and their volume is $\sim 0.0078$ that of the reference CPUscale system. Accordingly, a drive system stiff enough to limit clock skew to an acceptable value need occupy only a small fraction of the total system volume.

Clock signal distribution will likely have to differ in larger-scale synchronous systems. Control of local phase using optical or electrical signals offers one approach. As M. Miller observes, propagation of acoustic pulses at known speeds over known distances (e.g., with propagation times that are an integral number of clock periods) can also serve as a basis for large-scale synchronization. At some scale, designers of computer systems typically abandon synchronization.

### 12.7.4. Power requirements

The total power dissipation for the model CPU-scale system can be estimated from the component energy dissipations and the clock rate. Assuming a $1.2 \mathrm{~ns}$ clock with $0.03 \mathrm{maJ}$ per switching operation per interlock (Section 12.3.4), $4.4 \mathrm{maJ}$ per register-cell storage cycle (Section 12.4.3), and operation of every device on every clock cycle yields an estimated power dissipation of $74 \mathrm{aJ}$ per clock cycle, or $\sim 60 \mathrm{nW}$. This is less than $1 / 100$ the magnitude of the power flows corresponding to fluctuations in stored energy.

### 12.7.5. Power supply and energy buffering

a. Flywheels for energy buffering. A cylindrical flywheel of radius $r=$ $195 \mathrm{~nm}$ and height $h=20 \mathrm{~nm}$ can be placed within a $400 \mathrm{~nm}$ CPU-scale package. Its kinetic energy is

$$
\begin{equation*}
\mathscr{E}_{\mathrm{f}}=\frac{1}{2} I_{\mathrm{f}} \omega_{\mathrm{f}}^{2}=\pi^{2} r^{4} \rho h / t_{\text {clock }}^{2} \tag{12.26}
\end{equation*}
$$

With $\rho=3500 \mathrm{~kg} / \mathrm{m}^{3}, t_{\text {clock }}=1.2 \mathrm{~ns}$, and the above geometric parameters, $\mathscr{E}_{\mathrm{f}} \approx$ $6.9 \times 10^{-13} \mathrm{~J}$. Since $\Delta \mathscr{E}_{\mathrm{f}} / \mathscr{E}_{\mathrm{f}} \approx 2 \Delta \omega_{\mathrm{f}} / \omega_{\mathrm{f}}\left(\right.$ when $\left.\Delta \mathscr{E}_{\mathrm{f}} / \mathscr{E}_{\mathrm{f}} \ll 1\right), \Delta \mathscr{E}_{\max }=2.5 \times 10^{-14} \mathrm{~J}$ implies $\Delta \omega_{\mathrm{f}} / \omega_{\mathrm{f}} \approx 0.018$.

Note that the rim velocity, $\sim 1000 \mathrm{~m} / \mathrm{s}$, is well below the bursting speed for a diamond hoop, and that the presence of a significant vacuum gap avoids frictional drag.

b. Integration of motor and flywheel. The rotor of a motor with the exemplar parameters described in Section 11.7.3 can serve as a flywheel like that just described. The motor can deliver more power $(\sim 1.1 \mu \mathrm{W})$ than is needed to operate a CPU-scale system $(\sim 0.06 \mu \mathrm{W})$.

c. Start-up. Save for acoustic transmission lines, all of the computational mechanisms can work at low frequencies and dissipate less energy per operation as they do so. Static friction can be made effectively nil, with barriers $\ll k T_{300}$. Accordingly, a motor torque that can power a system at full speed is more than adequate to start it. Acoustic transmission lines operating with energy recovery are more dissipative just below their design frequency, but can be locked during start-up.

### 12.8. Cooling and computational capacity

In nanomechanical systems of sufficiently large scale, the $\sim 10^{12} \mathrm{~W} / \mathrm{m}^{3}$ power dissipation density of $\sim 1 \mathrm{GHz}$ nanomechanical logic systems described here exceeds any possible means of cooling. On a sufficiently small scale, however, cooling poses no problem. For example, the equilibrium $\Delta T$ of an isolated $100 \mathrm{nW}$ system of $400 \mathrm{~nm}$ dimensions is $<0.01 \mathrm{~K}$ in a medium with a thermal conductivity of $10 \mathrm{~W} / \mathrm{m} \cdot \mathrm{K}$.

On an intermediate scale, convective cooling is appropriate. Section 11.5 outlines a cooling technology based on branched channels, inhomogeneous phase-changing coolants, and high pressures capable of removing $\sim 10^{5} \mathrm{~W}$ of thermal energy from a $1 \mathrm{~cm}^{3}$ volume at $\sim 273 \mathrm{~K}$. This is sufficient to cool $\sim 10^{12}$ CPU-scale systems with an aggregate instruction-execution rate of $\sim 10^{21}$ per second. A more modest $10 \mathrm{~W}$ system can deliver $\sim 10^{11}$ MIPS.

Present techniques in software engineering could be used to apply parallel systems of this scale to a wide range of problems (e.g., fluid dynamics and many other physical simulations), but many other problems are less simple and uniform. To exploit growing computational resources, software engineering has developed techniques (e.g., object-oriented programming) that reduce the need for detailed, centralized planning. An analysis suggests that using market mechanisms to organize complex, decentralized processes has fundamental advantages in computation, particularly in large-scale parallel systems (Miller and Drexler, 1988a; 1988b; Drexler and Miller, 1988). This approach can be viewed as a further step in the direction taken by modern software engineering.

### 12.9. Conclusions

Nanomechanical computational systems can be implemented using logic systems based on sliding rods having switching times of $\sim 0.1 \mathrm{~ns}$, with energy dissipation $\ll k T_{300}$ per gate. Register cells can be constructed that approach the theoretical minimum energy dissipation of $\ln (2) k T$. Logic rods and registers can be joined to build register-to-register combinational logic systems that achieve four register-to-register transfers in $\sim 1.2 \mathrm{~ns}$; this performance (together with comparisons to existing microelectronic practice) suggests that nanomechanical RISC machines can achieve clock speeds of $\sim 1 \mathrm{GHz}$, executing instructions at $\sim 1000$ MIPS. Fast carry chains, RAM, tape, and I/O systems all appear feasible.

A CPU-scale system containing $10^{6}$ transistor-like interlocks (constructed with the parameters used in previous example calculations) can fit within a $400 \mathrm{~nm}$ cube. Compatible systems for clocking, power supply, and cooling have been described and analyzed. The power consumption for a $1 \mathrm{GHz}, \mathrm{CPU}$-scale system is estimated to be $\sim 60 \mathrm{nW}$, performing $>10^{16}$ instructions per second per watt.

Some open problems. The design calculations in this chapter are based on bounded continuum models; an open and accessible problem is the design and modeling of nanomechanical logic components (gates, registers, carry chains, RAM cells) in atomic detail. With good designs, substantially improved performance should be possible. At a higher level, the design of general-purpose computers that minimize irreversible operations (e.g., register erasure) is of substantial interest, as is the design of systems that reduce nonessential dissipation from logically reversible processes. The ongoing work in molecular and quantum electronics is of considerable interest. The anticipated fabrication capabilities of molecular manufacturing, however, may encourage consideration of a wider range of physical structures. For all but the highest-speed (as distinct from highest-throughput) computers, R. Merkle emphasizes that good switching technologies must eventually enable the use of nearly reversible operations to limit power dissipation; this may deserve greater attention in molecular and quantum electronics research.