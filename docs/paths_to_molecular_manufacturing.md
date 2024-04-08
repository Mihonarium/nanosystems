# Paths to Molecular Manufacturing


### 16.1. Overview

Chapter 15 describes extensions of present capabilities that would facilitate the construction of complex macromolecular structures, working in a solution environment. The chapters of Part II describe systems able to perform high-speed, high-efficiency, high-reliability mechanosynthesis of macroscopic objects, working in a vacuum environment. The present chapter attempts to describe how the gap between these technologies could be bridged by the development of a series of small mechanosynthetic devices. Section 16.2 describes the overall strategy. Sections 16.3 and 16.4 describe intermediate technologies, planning backward from advanced objectives toward present capabilities. Section 16.5 discusses factors affecting the pace of development.

The author apologizes in advance to experimentalists who may be offended by so quick a summary of so large a set of objectives. The work outlined here could readily absorb researcher-centuries of effort: many of the steps described will, if attempted, spawn a host of subproblems, each demanding long, hard, and creative work. It would, however, become burdensome to point this out at every turn. Developments that will one day make molecular manufacturing fast and easy will result from efforts that are slow and difficult.

### 16.2. Backward chaining to identify strategies

### 16.2.1. Forward vs. backward chaining

In a forward chaining search (as the term is used in computer science), one pursues a goal by taking steps that may lead toward it, sometimes exploring blind alleys. If, however, all possible destinations are considered equally good, then there is no real goal, hence (by this loose standard) forward chaining never fails. In science, it is common to pursue experimental programs opportunistically, choosing next steps based on immediate prospects and a sense of what is interesting, important, and fundable. This process resembles forward chaining with abundant, unranked goals, and it routinely produces incremental advances in knowledge and capabilities.

In backward chaining, one first describes a goal, then searches for intermediate situations one step removed from the goal, then for situations one step removed from those, and so forth, planning backward toward situations that are immediately accessible-that is, toward potential first steps on an implementation pathway. If there are many potential first steps, then backward chaining can be particularly attractive. In technology, it is common to select a goal based on its near-term feasibility and economic attractiveness and then plan backward to select the necessary parts and procedures. The enormous range of modern technological capabilities often provides many possibilities, hence engineers are more often concerned with cost and performance than with feasibility alone.

### 16.2.2. Evaluating paths to molecular manufacturing

Molecular manufacturing is a technological goal (presenting many scientific challenges), but it cannot be achieved in a few steps or a few years. Accordingly, one cannot expect to succeed by combining just existing parts and procedures. Backward chaining is still appropriate, but the links in the chain are intermediate technologies, not mere parts and assembly procedures.

Opportunistic, forward-chaining research strategies have moved toward increasing molecular control, and continued progress will eventually encompass the methods of molecular manufacturing (unless other methods can deliver equivalent capabilities). These opportunistic steps have been guided by perceived short-term rewards, but molecular manufacturing can be achieved more directly if long-term strategies and rewards guide short-term decisions. In a society that heavily discounts its future, however, long-term research directions must deliver short-term rewards. Early steps are described in Chapter 15, and some mention has been made of their immediate applications.

Short-term rewards aside, the chief criteria for development paths are directness and reliability. A path with fewer sequential steps can likely be traversed more rapidly. A path (or family of paths) that offers many choices at each step is more reliable, since it is unlikely that any single problem can block all choices. Assuming adequate short-term rewards, the total cost of following a development path is of little significance. Since 1950, the total cost of developing computers has been enormous, but the industry has earned steady returns. The present case seems similar.

### 16.2.3. Overview of the backward chain

Table 16.1 summarizes the characteristics of several technologies (Stages 1-3) that might be developed on the way to advanced molecular manufacturing systems (Stage 4). The descriptions of Stages 2 and 3 assume that the first molecular machine systems work in a liquid medium. The description of Stage 1 assumes that the process begins with AFM-based mechanosynthesis.

This table omits many alternatives. Sections 15.2 and 15.3 have described (Brownian) self-assembly strategies that could replace Stage 1 as a basis for developing Stage 2. R. Merkle has suggested vacuum-based mechanosynthesis systems; the most likely subsequent steps would differ greatly from Stages 2 and 3 as described here.

The following sections trace a path backward through the stages of Table 16.1. Section 16.3 attempts to describe the simplest molecular manufacturing

Table 16.1. Differences between proposed generations of mechanosynthetic assembly systems, taking Stage 1 as AFM-based molecular manipulation (Section 15.4, but see also Section 15.2 and 15.3); Stage 4 embraces a range of systems, including those described in Chapter 14.

| Characteristic | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
| :---: | :---: | :---: | :---: | :---: |
| System size | macroscopic | submicron | submicron | up to macro |
| Initial production | present tech. | Stage 1 syst. | Stage 2 syst. | Stage 3 syst. |
| Molecular parts | $\sim 10^{1}$ to $10^{2}$ | $\sim 10^{5}$ to $10^{6}$ | $\sim 10^{7}$ to $10^{8}$ | $\sim 10^{8}$ to $10^{9}+$ |
| System assembly | surface <br/> chemistry | folding <br/> block-chain | positional <br/> assembly | positional <br/> assembly |
| Structural <br/> materials | folded <br/> polymers | crosslinked <br/> polymers | crosslinked <br/> polymers | diamondoid <br/> solids |
| Instructions | external | external | external | internal |
| Internal comp. | no | no | no | yes |
| Cycle times | $\sim 1 \mathrm{~s}$ | $\sim 100 \mathrm{~ms}$ | $\sim 10 \mathrm{~ms}$ | $\sim 1 \mu \mathrm{s}$ |
| Error rates | $\sim 10^{-6}$ | $\sim 10^{-9}$ | $\sim 10^{-12}$ | $\sim 10^{-15}$ |
| Working <br/> medium | solution | pure liquid | pure liquid <br/> or vacuum | vacuum |
| Reagent <br/> transport | diffusion | $\underset{\text { conveyance }}{\operatorname{minimal}}$ | simple <br/> conveyance | conveyance |
| Stray molecules | solvent, <br/> reagents | solvent, <br/> contaminants | solvent, <br/> contaminants | rare |
| Feedstocks | complex | complex | complex | simple |
| Reagent <br/> processing | none | reactive <br/> $\quad$ activation? | reactive <br/> $\quad$ activation? | extensive |
| Reagents | moderate <br/> reactivity | high <br/> reactivity | high <br/> reactivity | extreme <br/> reactivity |
| Applied forces | small | moderate | moderate | large |
| Energy efficiency | negligible | low | low | good |

systems able to use highly active reagents (Chapter 8 ) to produce diamondoid materials (Part II). Section 16.4 then describes how systems of this sort could themselves be built by systems working with more conventional reagents in a liquid medium, and then how those systems could be built by smaller and simpler systems working in the same medium. These, in turn, could be built using one of the macromolecular engineering approaches described in Chapter 15.

### 16.3. Smaller, simpler systems (stages 3-4)

### 16.3.1. Macroscopic via microscopic manufacturing systems

With suitable instructions, the exemplar manufacturing system described in Chapter 14 could build a similar system of its own size, or larger. Conversely, it could be built by a similar system smaller than itself. What is the smallest, simplest system of this kind, able to build similar systems that are larger and more complex? Since both CPUs and manipulators can be of submicron size, an initial system can evidently be of microscopic dimensions, but more radical simplifications are possible.

One strategy for simplifying early nanoscale systems is to transfer complexity to the macroscopic world. Section 16.3.2 describes how onboard computing, information storage, and power supply systems can be replaced by transducers that respond to externally imposed acoustic signals. Section 16.3.5 describes how feedstocks consisting of pure solutions of large molecules can enable onestep mechanisms to replace complex molecule acquisition and purification systems. Sections 16.3.3 and 16.3.4 describe tactics for building simpler manipulators and for achieving the most important benefits of vacuum operation in a fluid medium. Combining these features, Section 16.3.6. describes a small mechanosynthetic device.

### 16.3.2. Acoustic power and control

a. Broadcast instructions. Replacing computers and stored instructions with broadcast instructions can simplify molecular manufacturing systems. If all operations are sufficiently reliable, then sensors and logic for directing conditional operations can be omitted. (Reliability will result from some combination of computational modeling, model-error-tolerant design, experiment, and redesign.) Broadcast instructions can enable system replication without internally stored instructions.

Signals can be broadcast to molecular mechanical systems in several ways (e.g., by light via photochemical isomerization), but signaling by modulated pressure via mechanical transducers is both simple and adequate. It is thus of interest to consider pressures and pressure histories that can be produced by the application of present technologies. The discussion that follows is generic, but some of the specific parameters and conclusions developed are used in later sections.

b. External control of the pressure history. The pressure on a device can vary over (at least) the range in which the surrounding solution remains liquid. At $\sim 300 \mathrm{~K}$, the solidification pressures of several pure solvents are $>2 \mathrm{GPa}$ (for example, $>3 \mathrm{GPa}$ for methanol); using mixed solvents can expand the available range. The following calculations assume that pressure can vary over the range $0 \leq p \leq 2 \mathrm{GPa}$.

Available laboratory equipment can subject $50 \mathrm{~cm}^{3}$ of solution to static pressures of up to $2 \mathrm{GPa}$ (Isaacs and George, 1987). Broadcasting of instructions, however, requires varying the pressure. At low frequencies, suitable designs include small cells modulated by pistons driven by relatively large actuators. If the diameter of the cell and piston are $\sim 10^{-3} \mathrm{~m}$ (permitting volumes $>10^{9} \mu^{3}$ ), then the maximum required force is $\sim 2 \times 10^{3} \mathrm{~N}$, and electromechanical actuator dimensions $<5 \mathrm{~cm}$ appear reasonable. It appears feasible to sweep the ambient pressure in a cell through its full range in $\sim 1 \mathrm{~ms}$. The approach outlined below uses the ambient pressure in the cell to select transducers of a particular class, and acoustic pressure fluctuations of lesser magnitude $( \pm 1$ to $100 \mathrm{MPa})$ and greater frequency ( $\sim 10^{6}$ to $10^{7} \mathrm{~Hz}$ ) to drive them. (Acoustic wave amplitudes can be increased by focusing.)

At pressures up to $2 \mathrm{GPa}$, the speed of sound in organic liquids is $\sim 1000$ to $2000 \mathrm{~m} / \mathrm{s}$, with negligible dispersion of phase velocities at megahertz frequencies

(Gray, 1972). The amplitude of acoustic plane waves in a liquid decays exponentially with distance, and is usually well described by the expression

$$
\begin{equation*}
A=A_{0} \exp \left(-C_{\text {atten }} f^{2} x\right) \tag{16.1}
\end{equation*}
$$

where $A$ is the amplitude, $A_{0}$ the initial amplitude, $f$ the frequency $(\mathrm{Hz}), x$ the propagation distance $(\mathrm{m})$, and $C_{\text {atten }}$ a measure of the attenuation $\left(\mathrm{s}^{2} / \mathrm{m}\right)$. For organic liquids at $\sim 300 \mathrm{~K}$ and low pressures, the value of $C_{\text {atten }}$ ranges from $\sim 3 \times 10^{-14}$ to $\sim 6 \times 10^{-12} \mathrm{~s}^{2} / \mathrm{m}$, declining with increasing pressure (Gray, 1972). For a typical value, $C_{\text {atten }}=10^{-13} \mathrm{~s}^{2} / \mathrm{m}$, a $10 \mathrm{MHz}$ signal can propagate $\sim 1 \mathrm{~cm}$ with $\sim 10 \%$ attenuation; sizes and frequencies in this range are compatible.

A final concern is conversion of high-amplitude sound waves to shock waves by nonlinear properties of the fluid. Shock-wave formation, however, requires a substantial propagation distance and does not occur in systems having sizes, frequencies, and amplitudes in the range considered here.

At $10 \mathrm{MHz}$, a 100 -pulse train lasts $10^{-5} \mathrm{~s}$, during which the ambient pressure (if modulated over its full range in $1 \mathrm{~ms}$ ) changes by only $\sim 1 \%$ of its peak value. It will here be assumed that, at a particular point in the cell, the pressure can be varied over a $2 \mathrm{GPa}$ range in $1 \mathrm{~ms}$, and that acoustic pulse trains with frequencies of up to $10 \mathrm{MHz}$ can be superimposed. For comparison, pulse-echo diagnostic ultrasound systems used in medicine can produce peak-to-trough pressure differentials of $\sim 10 \mathrm{MPa}$, with frequencies of 1 to $20 \mathrm{MHz}$ and pulse lengths measured in microseconds (ter Haar, 1988).

c. Pressure-threshold actuators. To convert a pattern of pressure fluctuations directly into a series of mechanical operations requires transducers that function as pressure-driven actuators. Devices like that abstractly represented in Figure 16.1 prove convenient. Each actuator of this kind is characterized by a pressure threshold $p_{\text {thresh }}$, a volumetric change $\Delta V$, and a corresponding length change $\Delta \ell$. The Gibbs free energy difference between the extended and retracted configurations is

$$
\begin{equation*}
\Delta \mathcal{G}_{\text {extend }}=\left(p-p_{\text {thresh }}\right) \Delta V \tag{16.2}
\end{equation*}
$$

and the outward force applied by the actuator at lengths between its limiting values is

$$
\begin{equation*}
F_{\text {extend }}=-\left(p-p_{\text {thresh }}\right) \Delta V / \Delta \ell \tag{16.3}
\end{equation*}
$$

![](https://nanosystems.contact.ms/cropped/2024_03_29_927bccd89a95a64e68a3g-83.jpg?height=434&width=506&top_left_y=1761&top_left_x=227)

below threshold pressure above threshold pressure
Figure 16.1. Schematic diagram of a pressure-threshold actuator, here illustrated with a constant-force spring (Section 10.5.3) and a piston moving between two limit stops. Actuators of this abstract class can be constructed with widely varying structures.

neglecting the effects of compliance. By adding a mechanism such as a lever, the effective value of $\Delta \ell$ can be changed without varying other parameters. The discussions that follow will use one of two sample sets of parameters:

1. High-pressure actuator parameters. With $\Delta p=p-p_{\text {thresh }}=-0.1 \mathrm{GPa}$ and $\Delta V=5 \mathrm{~nm}^{3}, \Delta \mathcal{G}_{\text {extend }}=-500 \mathrm{maJ}$, providing reliable avoidance of the disfavored position despite thermal excitation. With $\Delta \ell=1 \mathrm{~nm}$, the maximum force delivered at $\Delta p=-0.1 \mathrm{GPa}$ is $0.5 \mathrm{nN}$.
2. Low-pressure actuator parameters. With $\Delta p=-0.001 \mathrm{GPa}, \Delta V=500 \mathrm{~nm}^{3}$, $\Delta \mathscr{G}_{\text {extend }}$ is again $-500 \mathrm{maJ} / \mathrm{nm}^{3}$, and with a suitable geometry and mechanical advantage, the delivered force can again be $0.5 \mathrm{nN}$.

In a system described by the high-pressure parameters, a $2 \mathrm{GPa}$ pressure range permits use of actuators divided into 20 distinct classes, with $p_{\text {thresh }}=0.1$, $0.2,0.3, \ldots, 1.9,2.0 \mathrm{GPa}$. With the low-pressure parameters, 20 classes can be accommodated in a pressure range of $20 \mathrm{MPa}$, or 2000 in a pressure range of $2 \mathrm{GPa}$. (This is conservative; closer analysis of the mechanism described in Section 16.3.2d indicates that thresholds can be spaced at intervals less than $\Delta p$.)

Actuators in any one pressure class can be cycled through a reliable length transition repeatedly without activating those of other pressure classes. Shifting the ambient pressure monotonically from the value of $p_{\text {thresh }}$ for one class to that of another class, then back again, will cycle all actuators of intermediate $p_{\text {thresh }}$ exactly once. If the pressure is swept over the range only once, each set of actuators becomes active only once, each in a fixed sequence but with an independently controllable number of cycles including at least one more extension than retraction.

d. Control via acoustic signals. Two actuators with different thresholds could provide clock and data signals, permitting the input of strings of bits to a nanomechanical controller with data rates on the order of $10^{7}$ bits per second. The present application, however, requires control of the motion of several different parts, which would require mechanisms to decode the instructions and then apply the results at different locations.

A more direct approach can reduce complexity. Figure 16.2 illustrates how pressure-threshold actuators can drive a ratchet mechanism that moves a rod. When the latching pawl is engaged, the rod will not move left or right spontaneously, but can readily be driven to the right by an applied force. The driving pawl provides this force: every downward pressure transition from $p_{\text {thresh }}$ to $p_{\text {thresh }}$ $-\Delta p$ pushes the rod one increment to the right. (A reasonable spacing for the ratchet teeth is $\sim 1 \mathrm{~nm}$.) When both ratchets are disengaged, a small bias force retracts the rod leftward to a fixed position. For a mechanism of this kind to work reliably, the ratchet barrier heights must be adequate (e.g., $250 \mathrm{maJ}$ ); actuators with $\Delta \mathscr{G}_{\text {extend }}$ on the order of $500 \mathrm{maJ}$ are more than adequate to surmount these barriers. Incrementing a ratchet dissipates substantial energy, but efficiency here is not a concern.

A typical operational cycle (Figure 16.2) would begin at high pressure, with both ratchets disengaged and the rod to the left. Lowering the pressure through the first range engages the latching ratchet with a force that is essentially constant at all lower pressures, owing to the limit stop. After lowering the pressure further (possibly much further), the driving rachet extends and moves the rod to
![](https://nanosystems.contact.ms/cropped/2024_03_29_0e0656d74dae9ab2ac34g-02.jpg?height=1214&width=760&top_left_y=197&top_left_x=339)

non-bar mechanisms $\sim 100,000$ atoms

Figure 16.2. A ratchet mechanism driven by a pair of pressure-threshold actuators. At high pressures (1), both pawls are retracted. As the pressure falls, the latching pawl and the driving pawl extend and engage (2). As the pressure drops through the active range of the driving pawl, it extends, forcing the rod to the right and momentarily lifting the latching pawl against the force of a spring, leading to state (3). An increase in pressure crossing the active range of the driving pawl resets it, preparing to move the rod a further step during the next downward pressure transition. Raising the pressure to the level in state (1) retracts both pawls again, allowing a bias force to reset the rod position to the left. Springs outside the two actuator cylinders represent mechanical compliances not directly involved in actuation.

the right. The pressure then can be lowered further with no effect on this mechanism, or it can be cycled up and down across the active range of the driving ratchet, moving the rod by further increments. After an operation has been performed, a return to high pressure resets the rod to its initial position. All latching ratchets can have actuators of a single pressure class, hence a system with $N$ distinct classes can directly control $N-1$ distinct motions.

Simple ratchet-driven rods of this sort would, however, provide inadequate positional resolution ( $\sim 1 \mathrm{~nm}$ ) for mechanosynthesis of diamondoid structures, if

![](https://nanosystems.contact.ms/cropped/2024_03_29_0e0656d74dae9ab2ac34g-03.jpg?height=560&width=869&top_left_y=193&top_left_x=441)

Figure 16.3. A vernier ratchet mechanism driven by four pressure-threshold actuators. Ratchets with differing tooth spacings can provide positional resolution equal to the difference in spacing (Section 16.3.2d). This schematic illustration places both sets of actuators in the same plane, suggesting a mechanical interference that need not occur in a noncoplanar geometry. Note that the two latching pawls can be driven by actuators of the same pressure threshold.

their displacements were applied in a 1:1 ratio. Use of levers, screws, or gears to provide mechanical advantage is one option; use of additional vernier displacements of a slightly different increment size (Figure 16.3) is another (for example, a total displacement can be the sum of $1 \mathrm{~nm}$ displacements at one interface and $1.1 \mathrm{~nm}$ displacements at another, yielding $0.1 \mathrm{~nm}$ resolution).

e. Power via acoustic signals. A single actuator described by either of the sets of parameters described in Section 16.3.2c can yield $\sim 5 \times 10^{-12} \mathrm{~W}$ of mechanical power when cycled at $10 \mathrm{MHz}$. This power level could support $10^{6} \mathrm{op}-$ erations per second at $5 \mathrm{aJ} /$ operation (far larger than the comparable value estimated for the exemplar system in Chapter 14).

In systems of the sort considered here, control and power supply are inseparable. The power supplied by an actuator is sufficient so long as the forces it applies are sufficient to drive component motions. A force of $\sim 0.5 \mathrm{nN}$ (Section 16.3.2c) is ample to overcome both the inertial and viscous drag forces caused by displacing a $10 \mathrm{~nm}$ diameter, $100 \mathrm{~nm}$ long rod by $1 \mathrm{~nm}$ in $10^{-7} \mathrm{~s}$; these values are chosen to roughly model the struts of a molecular manipulator like that discussed in Section 16.3.6d.

### 16.3.3. Simpler manipulators

The manipulator described in Section 13.4 requires stiff materials and intricate parts, making it difficult to implement. An alternative design (Figure 16.4) uses a Stewart platform, widely used in aircraft flight simulators and occasionally in robotics (its use in this context was suggested by Professor D. Taylor of Cornell). The Stewart platform has a roughly octahedral geometry, with a fixed triangular base linked to a mobile triangular platform by six struts of adjustable length. Figure 16.5 shows a two-dimensional analogue with three struts and indicates a portion of the available range of motion. Strut lengths can be altered with

![](https://nanosystems.contact.ms/cropped/2024_03_29_0e0656d74dae9ab2ac34g-04.jpg?height=741&width=899&top_left_y=199&top_left_x=303)

Figure 16.4. A positioning mechanism based on the Stewart platform (schematic). Each strut has a joint at each end, shown for simplicity as ball-and-socket joints at the base and as flexible point attachments at the top. Each strut has a set of actuators able to adjust its length. See Figure 16.5.

$\sim 0.1 \mathrm{~nm}$ accuracy by means of pressure-actuated vernier ratchet mechanisms like those described in Section 16.3.2d.

A manipulator can replace many other control mechanisms. With a "hand" in the workspace, various devices can be "hand operated"-for example, a manipulator could push any one of a dozen levers to select and move a particular transport mechanism, or it could move a partially finished part from a clamp to a
![](https://nanosystems.contact.ms/cropped/2024_03_29_0e0656d74dae9ab2ac34g-04.jpg?height=572&width=1128&top_left_y=1475&top_left_x=192)

Figure 16.5. A two-dimensional schematic of a positioning mechanism based on the Stewart platform (a); the kinematics of this structure correspond to three of the six degrees of freedom of a three-dimensional platform (Figure 16.4). Panel (b) illustrates a portion of the available range of motion. Note that the lateral range exceeds the length of the arm in a retracted position.

special jig for a series of operations, and then to its destination. To minimize parts and physical complexity, it may be desirable to use a manipulator for many purposes beyond the narrowly mechanochemical.

### 16.3.4. Inert internal environment

The previous chapters describe nanomechanical systems working in vacuum. This environment has three basic advantages (aside from analytical simplicity):

- No viscous drag
- No mechanical interference
- No chemical reactivity

Viscous drag is acceptable here because energy dissipation is of negligible concern. Mechanical interference (i.e., jamming) could pose problems, but only if a motion (e.g., of gears meshing) creates an enclosed pocket of molecular size or larger and then attempts to compress it to a substantially smaller volume; mechanisms can be designed so as to avoid this. Chemical reactivity is a concern in many media (particularly with highly active reagents), but not in a nearly inert medium such as helium.

A helium-filled structure can equalize interior and exterior pressures to minimize wall flexure. More precisely, an enclosure can include an expansion bellows, thereby concentrating flexure in a region designed to accept it. Evacuated regions would be needed (if at all) only inside actuators, and these could be pumped: the presence of a few molecules would be inconsequential. Adopting the low-pressure actuator parameters (Section 16.3.2c), a pressure range of $0.02 \mathrm{GPa}$ is adequate to control many distinct devices. If the total mean pressure is $0.2 \mathrm{GPa}$, the pressure (and gas-filled volume) fluctuations are then $\sim 10 \%$. Helium can be admitted (and large molecules excluded) by helium-permeable pores. A suitable internal helium pressure will result if the surrounding liquid is in contact with gaseous helium, and if the mean fluid pressure does not vary too widely or too fast.

If the interior volume is $\sim(100 \mathrm{~nm})^{3}$, then so long as the contained helium in a set of devices has a mean mole-fraction impurity concentration $<10^{-9}$, the probability of the presence of a stray nonhelium molecule in any one device is $<.1$, hence most lack any contamination. Many reactive contaminants could be neutralized by gettering, that is, by providing sacrificial reactive surfaces with which they can combine without harmful effect. One such contaminant is hydrogen, the molecule most likely to enter through helium-permeable pores.

### 16.3.5. Sorting and ordering molecules

To simplify cost estimation (and to reduce estimated production costs), Chapter 14 describes molecular manufacturing systems able to use low-purity solutions of small-molecule feedstocks. The present objectives differ; to simplify the systems themselves (and to reduce estimated development costs), it is better to assume larger-molecule feedstocks of high purity.

Large feedstock molecules of several kinds can differ greatly both from solvent molecules and from one another. Reliable acquisition of a large molecule of a particular kind can then be straightforward, in part because larger molecules can have enormous binding affinities. For example, a 31-atom molecule (biotin) binds to a protein (avidin) in water with a dissociation constant $K_{\mathrm{d}}$ of
$\sim 10^{-15} \mathrm{~nm}^{-3}$. Assuming solute concentrations of $\sim 1 \mathrm{~nm}^{-3}$, a dissociation constant this low provides more than adequate sorting and ordering in a single step, assuming that no closely similar molecules are present to compete for the receptor. This can be ensured by careful purification of the large-molecule components of the feedstock solution (e.g., by repeated affinity chromatography). Accordingly, it seems that a judicious choice of high-purity feedstock components can enable a manufacturing device to acquire feedstock molecules of one kind with good reliability in a single step. A mechanism with a single receptor could then replace complex systems like those shown in Figures 13.4 and 13.5.

### 16.3.6. Minimal diamondoid-material systems

Any attempt to describe a "minimal" system must be considered speculative. On one hand, a general description may overlook some minor but complex and necessary feature; on the other hand, clever designs may result in smaller, simpler systems overall. The mechanosynthetic system described here has passed through several cycles of simplification, and there is no reason to regard it as ideal or final. This sketch, like those that follow for other stages, is offered only to provide a stimulus and point of reference for further work.

a. Preparing and applying reagents. Chapter 14 describes systems using specialized mill mechanisms to prepare reagents and to perform several stages of subsequent assembly; this specialization improves throughput and energy efficiency. Parts count can be reduced, however, by applying manipulator mechanisms more directly to feedstock molecules.

Conventional chemical synthesis can prepare feedstock molecules of several kinds, each having a reagent-precursor moiety at one end and a distinctive "handle" of several dozen atoms at the other. Differences between handles can enable the selective binding assumed in Section 16.3.5. Forces applied by a manipulator can drive the rotation of a receptor from the exterior to the interior of the enclosure, and can force the release of a bound feedstock molecule; the handle can then bind to a larger block with a standardized, grippable surface.

A pair of manipulators (one can be an immobile gripper) can be situated so that their tips can interact. Bound feedstock molecules can then be moved, placed, and made to interact with flexible control of encounter sequence and geometry. The resulting mechanochemical transformations can generate a wide range of reagent moieties and subassemblies from a smaller range of feedstock molecules. In particular, relatively unreactive precursors (stable in solution) can be transformed into highly active reagents in the inert environment within the enclosure.

Once prepared, reagents can be applied, transferring groups to (or abstracting atoms from) a workpiece. The degree of control available is essentially that described in Chapter 8.

b. Waste disposal. The preparation and application of reagent moieties will generate wastes in the form of discarded handle structures. These will typically have a volume greater than that of the product structure, and must be cleared from the workspace. The manipulator can deliver them to a relatively unselective positive-displacement pumping mechanism for expulsion into the surrounding solution.

Spent handles might resemble feedstock molecules enough to compete for receptors. This problem can be avoided by either (1) ensuring that their use modifies structures important to binding, (2) ensuring that their concentration in solution remains very small, or (3) trapping them in an expandable external compartment (e.g., a bag).

c. Wall design and product delivery. Pressure equalization minimizes loads on walls, enabling the use of a flat-walled enclosure scheme like that illustrated in Figure 14.6. This geometry relies on a sliding interface to provide a seal between the enclosing wall of the manufacturing system and the emerging wall of the (possibly larger) product structure. Section 11.4.2 describes suitable seals.

d. Estimated size, complexity, and replication time. A system of the sort described in this section could be packaged in a volume $\sim(100 \mathrm{~nm})^{3}$ (although not equidimensional). The structural components of a Stewart-platform manipulator (Section 16.3.3) having 6 struts $\sim 100 \mathrm{~nm}$ long and $\sim 5 \mathrm{~nm}$ wide contribute $\sim 2 \times 10^{4} \mathrm{~nm}^{3}$ of solid structure. Each strut has 4 actuators, including verniers. If an additional 4 actuators are provided to control operations at the manipulator tip, 8 to control a second, more rudimentary arm (Section 16.3.6a), 4 to control overall movement of the product structure, and 2 to drive a waste-expulsion pump, then the total is 42 . If each actuator is approximated as a box $10 \mathrm{~nm}$ on a side with walls $1 \mathrm{~nm}$ thick, actuators contribute $\sim 2.5 \times 10^{4} \mathrm{~nm}^{3}$ of solid structure (actuators this large permit operation in the low-pressure regime described in Section 16.3.2c). Allowing for 10 reagent-acquisition mechanisms, each $\sim 5 \mathrm{~nm}$ wide and $\sim 10 \mathrm{~nm}$ tall, adds a negligible $0.25 \times 10^{4} \mathrm{~nm}^{3}$. Walls $1 \mathrm{~nm}$ thick contribute $\sim 6 \times 10^{4} \mathrm{~nm}^{3}$. The total volume, including a $50 \%$ allowance for additional components and structures, is then $\sim 1.6 \times 10^{5} \mathrm{~nm}^{3}$, or $\sim 2 \times 10^{7}$ atoms. The estimated number of moving parts is, according to this estimate, $\sim 100$.

With the parameters assumed here, motion frequencies are limited by the frequency at which the pressure in the cell is swept over its full range. At $\sim 1 \mathrm{~ms}$ per sweep and 5 motion cycles per reagent application cycle, reagent application operations can be performed at $\sim 200 \mathrm{~s}^{-1}$. If the mean number of atoms transferred per operation is $\sim 1$, then the replication time for the system is $\sim 10^{5} \mathrm{~s}$, or $\sim 1$ day. Since there is reason to regard the atom count as generous and the motion frequencies as conservative, this time estimate seems likely to be generous. (Note that the acceptable mean error rate per operation can be larger than the goal discussed in Chapter $8, \sim 10^{-8}$ rather than $\sim 10^{-15}$.)

e. Instrumentation. Techniques for probing product structures will be central to experimentation and process development. One approach would exploit modulation of the fluorescence yield, lifetime, and spectrum of a chromophore by changes in its mechanical and electronic environment. In the solution phase, changes in solvent polarity can produce dramatic shifts in fluorescence spectra (Wayne, 1988). Changes in the distribution of charge near a bound chromophore or direct mechanical deformation of a conjugated structure can produce changes of similar magnitude.

Existing instrumentation using subnanosecond excitation pulses and spectrally filtered, nanosecond time-gated detection to suppress background photons permits the detection of single molecules (each with a single chromophore)
by their fluorescence in a $\sim 10 \mathrm{~ms}$ interval (Shera et al., 1990). With accessible improvements (e.g., reduction of photobleaching by tailoring the molecular environment) more photons can be collected, and changes in the properties of the chromophore should be readily detectable. This can enable readout of data from an individual mechanosynthetic device. A chromophore can be manipulated like a feedstock molecule, and its fluorescent properties (frequency, quantum yield) can be modulated by direct contact with the structure being probed, causing electrostatic or mechanical perturbation of the chromophore. Since the chromophore is a proximal probe, repeated positioning at different locations can be used to build up an image of a workpiece structure, as in AFM and STM. If measurements can be performed in $\sim 10 \mathrm{~ms}$ or less, atomic-resolution images can be acquired at $\sim 1 \mathrm{~nm}^{2} / \mathrm{s}$.

Unless their photostability is excellent, probe chromophores will require regular replacement. This can be accomplished by mechanisms like those used to provide reagent moieties. To avoid interference from unbound chromophores, however, the feedstock molecules must initially have negligible fluorescence at the signal wavelengths, and must be activated after binding to the mechanism. Alternatively, the mechanosynthetic device could be tethered to a surface and fluid flow could be used to purge the surrounding volume before gathering data from a proximal fluorescent probe.

f. Summary. An inert workspace environment in which highly active reagent moieties can be positioned relative to workpieces with high precision and reliability (the essential requirements of qualitatively advanced molecular manufacturing) can be provided by a mechanism with $\sim 10^{2}$ moving parts and $\sim 2 \times 10^{7}$ atoms. Pressure-threshold actuators enable substantially independent control of several tens of mechanisms within a single manufacturing system; an indefinitely large number of identical systems can be driven through the same sequence of operations at the same time. Using a manipulator mechanism able to reach a large portion of the interior space, complex behaviors can be implemented by complex control sequences, rather than by complex hardware. With $10^{7} \mathrm{~Hz}$ actuator stepping rates, manufacturing can proceed at $\sim 200$ operations per second, enabling a system to build an object of its own complexity in about a day. Molecular probes can be used to determine the outcome of operations within a single device, facilitating experimentation and the development of new operations.

These system characteristics assume the use of diamondoid materials, and are chosen to permit the fabrication of diamondoid materials. The following steps in the backward-chaining analysis will move away from these materials and conditions toward more familiar polymeric structures and solution-based chemistry.

### 16.4. Softer, smaller, solution-phase systems (stages 2-3)

### 16.4.1. Diamondoid via nondiamondoid systems

Diamondoid materials with diamondlike stiffness and atom number density are challenging targets for synthesis (Section 8.6.1), and are here assumed to require the use of highly active reagents. These, in turn, are assumed to be incompatible with solution-phase synthesis conditions, owing to the potential for reaction
with solvents. (If either of these assumptions proves incorrect, development will be easier.[^43]) Along development paths that start with solution-phase chemistry, diamondoid structures must be built by nondiamondoid systems.

A nondiamondoid system can build diamondoid structures if it can execute suitable motions with adequate stiffness in an environment compatible with highly active reagents. A mechanism resembling that described in Section 16.3.3 will suffice, using thicker struts to compensate for lower modulus. Highly oriented polymers can exhibit a Young's modulus $>100 \mathrm{GPa}$; examples include polyethylene and Kevlar 49. Similar materials can be made by solution-phase mechanosynthesis. A strut $\sim 10 \mathrm{~nm}$ in diameter and $\sim 100 \mathrm{~nm}$ long would then have a stretching stiffness $k_{\mathrm{s}} \approx 100 \mathrm{~N} / \mathrm{m}$.

Highly crosslinked organic structures of good stiffness can presumably be made by positioning multifunctional monomers of conventional reactivity; extensive use of cycloaddition reactions, for example, can enable the formation of relatively dense bond networks. The number of atoms required for a given functional capability will usually be larger for such structures than it would be for more diamondlike structures, but the number of (relatively large) monomers placed, and hence the number of mechanosynthetic operations, should typically be lower.

These crosslinked organic structures can be built by mechanosynthetic systems of still lower stiffness. Required manipulator stiffness varies as the inverse square of the site separation. The large size of multifunctional monomers in comparison to simple radicals and alkynes tends to increase the separation between reactive sites; the alignment requirements of cycloaddition reactions can further widen the separation in configuration space (Section 8.3.3f).

The picture that emerges from these considerations is of a progression from relatively compliant mechanosynthetic systems that position large monomers in solution to relatively stiff systems that position small, highly active moieties in an inert environment. Monomer-based structures built by compliant mechanisms using solvent-compatible chemistry can themselves be stiff enough to build diamondoid structures.

### 16.4.2. Inert environments from solvent-based systems

The transition from solvent to an inert environment can be achieved by a manufacturing system that (1) tolerates but does not require an internal solvent, and

(2) can replicate while maintaining a barrier against solvent entry. Consider a system meeting this specification that initially contains $10^{9}$ molecules of solvent. After one replication cycle, the mean number of solvent molecules in each of the resulting pair of systems is $10^{9} / 2$. After 40 replication cycles, the mean number is $10^{9} / 2^{40} \approx 10^{-3}$; hence most systems are solvent-free by virtue of extreme dilution.

If all solvent molecules were sufficiently mobile, then replication-based dilution could be replaced by simple pumping. Problems that might be caused by operating in the presence of a helium-solvent phase boundary can be avoided by pumping out all mobile solvent molecules, then using replication cycles to produce solvent-free mechanisms by dilution.

If enclosures made of polymeric materials are permeable to small reactive contaminant molecules (e.g., hydrogen), then either the external concentration of such contaminants must be kept low (by avoiding sources or providing sinks) or the internal mechanisms must tolerate their presence. Note that dangerously reactive contaminants should be susceptible to chemical scavenging.

### 16.4.3. Solution-synthesized pressure-threshold actuators

Relatively advanced solution-phase mechanosynthesis systems can presumably make (and use) pressure-threshold actuators based on piston mechanisms like the one illustrated in Figure 16.1. An alternative approach, presenting less synthetic difficulty, exploits pressure-driven changes in volume analogous to solidstate phase transitions in bulk materials.[^44] Various salts and organic crystals exhibit phase changes at pressures between 0.05 and $2 \mathrm{GPa}$ with fractional volumetric changes of $\sim 0.05$ to 0.1 (Gray, 1972). A block of material with this behavior can serve as a pressure-threshold actuator: the nature of the relationship among force, displacement, and pressure is identical. The chief disadvantage is the smaller value of $\Delta V / V$; this can be accommodated by roughly doubling the linear dimensions of the device.

### 16.4.4. Smaller liquid-based mechanisms

Sections 16.3.6 and 16.4.2 assume that synthesis occurs inside a $\sim 100 \mathrm{~nm}$ scale enclosure, with each moiety (or monomer) emplaced by a manipulator of comparable size. The enclosure must surround the system, and the manipulator (to enable replication) must span its diameter. A rough estimate (Section 16.3.6d) places most of the system mass in these components. To add a further link in the backward chain from advanced manufacturing systems, it is desirable to keep the chief benefits of enclosures (exclusion of stray reagent molecules) and of manipulators (use of positional control to build complex structures) while eliminating most of their mass. The result is an easier target for construction.

a. Stray reagent exclusion without a wall. If reagent monomers contain dozens of atoms (or have discardable handles), then it is not a severe constraint to require that they carry enough polar or charged groups to make them substantially soluble only in a polar medium. If the workspace is located within a droplet of an unreactive, nonpolar solvent (e.g., an aliphatic hydrocarbon), then reagent monomers carried by an external polar solvent will be largely excluded from the interior. Droplets can be stabilized against coalescence by polymeric surfactant structures of low mass and complexity; their equilibrium size can be fixed (for example) by the colligative properties of their contents, or by the surfactant structures. Reagent monomers can be transported into the workspace by mechanically rotatable receptors like those discussed in Section 16.3.5.

b. Folding-assisted assembly. Biological molecular machines are manufactured by devices capable of controlling only the sequence of a chain of small monomers. A manipulator-based assembly system with even a small range of motion (e.g., $5 \mathrm{~nm}$ ) could build relatively rigid, highly crosslinked molecular objects of substantial size-more like a protein than like an amino acid residue. A chain of these objects could be designed to undergo a specific, predictable folding sequence as it exited the assembly system, guided by the binding of complementary surfaces with areas of several square nanometers. Note that identical pairs of complementary surfaces can be used repeatedly, so long as only one of any particular kind is ever exposed within reach of a tethered complementary structure.

Accordingly, a manipulator with a range of motion $\sim 1 / 20$ that of the device described in Section 16.3.6d can build structures far larger than itself, including larger manipulators. A single ratchet-driven bar can be used to move any of several reagent receptor mechanisms within reach. As in the proposed AFM-based mechanism (Section 15.4), the workpiece can be mounted on the manipulator, enabling monomers to be bound to it directly from a receptor. The comments in Section 16.3.6e regarding chromophores as probes are applicable here as well.

The advantages over an AFM-based mechanism include (1) isolation of the workpiece from stray reagent monomers, (2) motion control in six degrees of freedom, (3) a "substrate" that can include mechanisms for product clamping and release, (4) reagent receptors in known locations that need not be mapped, and (5) the feasibility of directing a replication process that generates large numbers of low-cost mechanosynthetic devices. The disadvantages include (1) inability to correct for reaction failures-at least when many devices are sharing one stream of broadcast signals-and (2) the requirement for much more complex nanomechanisms.

c. Estimated size. To minimize the scale of the pressure-threshold actuators, pressures and sizes can be chosen in the range suggested by the high-pressure actuator parameters in Section 16.3.2c. With $\Delta V=5 \mathrm{~nm}^{3}$, the required volume per actuator is $\sim 50 \mathrm{~nm}^{3}$, and a set of $\sim 40$ actuators (of $\sim 20$ different pressure classes) requires $\sim 2000 \mathrm{~nm}^{3}$ of material. The size of the struts is negligible in comparison, and the wall is nonexistent. In systems with large pressure swings, structural deformations resulting from ordinary compressibility (rather than discrete phase changes) will be an important consideration in design.

Based on these estimates, a total structural volume of $\sim 4000 \mathrm{~nm}^{3}$ appears ample, suggesting an atom count of $\sim 4 \times 10^{5}$. Assuming $\sim 20$ atoms per monomer, the number of synthetic operations required for construction is $\sim 2 \times 10^{4}$. This is within the $>10^{5}$ operations estimated to be feasible using AFM-directed mechanosynthesis (Section 15.4); alternatively, a self-assembled structure might be made from a set of $\sim 400$ molecular objects each consisting of $\sim 50$ monomers. Once fully operational, a device of this sort could build another device of comparable size and complexity in $\sim 1$ hour, working at only 5 operations per second.

### 16.5. Development time: some considerations

The preceding sections outline an ambitious effort. Reaching the first stage described in this chapter (Stage 2, Section 16.4.4) will require the construction of precise molecular structures $\sim 10^{2}$ to $10^{3}$ times larger than those previously achieved. Subsequent steps, building on this base, will move still farther from present laboratory experience.

Naive assessments of feasibility often implicitly assume that future developments will be limited (in scope and pace) by today's tools, instruments, and techniques. This mistake is natural, because only today's capabilities are widely and concretely known. Where the developments under consideration involve several stages of tool development, however, this static picture can be quite misleading. To formulate a more accurate understanding, one must instead consider each step in light of the capabilities provided by previous steps. The balance of this section makes a preliminary effort in this direction, beginning with a conceptual framework of more general applicability.

### 16.5.1. Determinants of the development time

a. The cycle of experimentation. Development of new technologies involves experimentation leading to the accumulation of reliable systems and tested capabilities. The cycle of experimentation has several stages: (1) choosing an objective, (2) choosing an approach, (3) trying the approach, and (4) evaluating the result. So long as the result is unsatisfactory, stages (2) through (4) are repeated until success is achieved or the objective is altered or abandoned.

b. The number of sequential experimental steps. The time required to develop a system equals the sum of the durations of the required sequential steps. Good strategy can reduce the number of steps (and their difficulty); there is no reason to believe that the best strategy for developing molecular manufacturing has yet been identified. Further, many steps can be taken in parallel. For example, multiple teams can work with similar mechanosynthetic systems, each doing experiments that add to the repertoire of reproducible synthetic operations. Low instrument and materials costs can enable more teams to work, increasing parallelism. Concurrent development of a system and of plans for using it (via computational modeling) can further increase parallelism.

c. The number of teams working on a step. Even without cooperation, work by multiple teams can speed completion of a single step, because this happens as soon as the fastest (or luckiest) group succeeds. The number of teams funded to work on a problem will depend in part on the perceived importance of solving it.

d. Computational modeling. If computational modeling were perfect (fast, inexpensive, and accurate), then it would enable all correctly executed experiments to succeed on the first try. In reality, it does far less, yet modeling can help researchers avoid unworkable approaches without rejecting too many workable approaches. This tends to increase the fraction of experiments that can, after repeated tries, be made to work, thereby decreasing the mean delay in achieving an objective.

Computational modeling is more useful in planning mechanosynthesis than it has been in solution synthesis. Mechanosynthesis can impose a particular interaction geometry on a pair of reagents, thereby defining the system to be modeled and rendering small errors in transition-state energy relatively unimportant (Section 4.4.3). Further, relatively rigid, crosslinked structures are less sensitive to modeling errors than are conformationally flexible peptides and typical products of organic synthesis. As inexpensive computers become faster and software becomes more sophisticated, the utility of computational modeling will increase.

e. Time for synthesis. If the cycle of experimentation is to be short, the time required to synthesize a structure must be short. This consideration favors active reagents, high effective concentrations, and the use of software control to direct long sequences of operations.

f. Time for evaluation. Short experimental cycles likewise demand short evaluation times. This tends to favor intermediate technologies that combine sensors and manipulators in a single package.

g. Willingness to limit evaluation and abandon subgoals. In routine science, an unexpected result often provides a problem to study. In building novel systems, however, an unexpected result often gives reason to seek a more predictable system. To evaluate a result, success and failure must be distinguished, but the nature of a failure need not always be understood-an attempt to study it in detail seldom yields fundamental knowledge, and may merely yield detailed knowledge of something useless. Even a consistent pattern of failures may motivate, not a prolonged halt for study, but instead a redesign that avoids the difficulty entirely. Analyzing unexpected failures can be of great value, producing rules to guide future design; but quickly trying a different approach can sometimes speed development. (Note that evolution developed sophisticated molecular machine systems without analyzing failures.)

### 16.5.2. Stage 1a: Brownian assembly of medium-scale blocks

Building a solution-phase mechanosynthesis system of the sort described in 16.4.4 $\mathrm{c}$ by Brownian assembly (rather than by AFM-directed mechanosynthesis) might involve developing $\sim 400$ self-assembling building blocks of $\sim 50$ monomers apiece (Section 15.3). Monomers can be developed in parallel with one another. With good CAD software to define their functions and interfaces, building blocks can also be developed in parallel with one another. Further, design of building blocks can be overlapped with the design and synthesis of monomers.

Designing $\sim 400$ building blocks need not require the design of a similar number of unique complementary interfaces. If building blocks are added to solution sequentially (and removed afterward), each will have a unique destination so long as the assembly sequence exposes only one interface of each kind at any one time; supramolecular variants of protective-group strategies may be useful here. The quality of the tools available for computer-aided design of folded structures that meet geometrical and functional specifications appears critical to the pace of development along this pathway.

Blocks of $\geq 150$ monomers can be characterized by NMR spectroscopy (Kay et al., 1990). Interpretation of NMR data is simpler if the desired fold is known,
and if structures that differ widely from the objective are discarded without detailed study. Molecular-tip AFM techniques could aid in evaluating both building blocks and assembled structures.

In past protein design efforts, the time required for synthesis and characterization has often been measured in months or more, and success rates per trial have been moderate. Augmented proteins, designed to make design and synthesis easier, will presumably permit somewhat faster cycles.

### 16.5.3. Stage 1b: Mechanosynthetic assembly of small building blocks

AFM-directed mechanosynthesis can sidestep the problem of designing folding polymer structures and enable immediate characterization of product structures using the AFM mechanism itself. The required monomers are likely to be complex (bearing multiple functional groups) but can be designed to permit synthesis by conventional means. Monomers can be developed in parallel, and to avoid investing synthetic effort in chemical blind alleys, they are best developed in parallel with designs intended to use them.

Effective exploitation of AFM-directed mechanosynthesis systems will require substantial software development: image interpretation software able to determine the types, positions, and orientations of specific sets of reagent binding molecules; control software to automate reagent positioning and sensing, thereby automating the execution of long sequences of reactions; and computeraided design software to plan both what to build and how to build it.

The cost of an AFM-based mechanosynthesis system can be estimated today: it will likely be less than the price of an AFM system in the early 1990s, $\sim \textdollar 10^{5}$. Reasonably low prices will enable many teams to enter the field, some working in parallel to develop and expand a set of reliable synthetic operations. With suitable reagents, reaction times can be $\sim 1 \mathrm{~s}$, enabling the construction of moderately complex objects in minutes and of objects containing $\sim 10^{5}$ monomers in about a day. Once good tools are in hand, the time required to develop mechanical systems with $\sim 10^{2}$ moving parts (as many as in the system in Section 16.3.6d) consisting of $\sim 2 \times 10^{4}$ monomers (estimated to be sufficient to build a minimal solution-based molecular manufacturing system, Section $16.4 .4 \mathrm{c}$ ) could be a fraction of a decade.

### 16.5.4. Stage 2: First-generation solution-based systems

Stage 2 manufacturing systems as described in Section 16.4.4 have capabilities resembling those of AFM-based mechanosynthetic systems, hence they can use identical or similar monomers, and their applications can be planned using similar CAD software. Since these systems are precisely constructed, they create no requirement for image-interpretation software to locate and discriminate among reagent receptors. Evaluation of the results of an operation (including imaging) can be achieved as described in Section 16.3.6e.

The estimated time required for a system of this kind to build a copy of itself (a key threshold in development) is several hours. If the replication time is $\sim 1$ hour (Section 16.4.4c), then the time required to produce a macroscopic quantity of systems is several days. Subsequent production of other devices can supply relatively low-cost, disposable laboratories for mechanosynthesis. The cost of required reagents is negligible on a per-device basis. For example, a cost
of $10^{4} \textdollar / \mathrm{gm}$ amounts to $\sim \textdollar 10^{-12}$ per complex device. New reagents, operations, and devices can be developed in parallel in many laboratories. From this technology base, the direction of advance is toward enclosed systems with larger manipulators, then toward inert interiors, then toward more active reagents. Experimental cycle times can remain short throughout this process.

### 16.5.5. Stage 3: Inert environments, diamondoid materials

After the transitions enabling the use of highly active reagent moieties and the construction of devices made from diamondoid materials, development can proceed more or less directly to advanced molecular manufacturing systems. CAD systems for diamondoid materials will differ from those used with larger monomers, but will be in some respects simpler. The frequency of synthetic operations can be increased, in part by the use of more active reagents and in part by the construction and use of decoding subsystems that more fully exploit the capacity of information input channels. Further, once systems are built with internal control and data storage devices, brief instructions can activate complex subroutines, greatly relaxing constraints associated with data transmission rates. A single manufacturing system can then contain multiple production lines, each working at high frequency. Construction of molecule sorting and preparation subsystems can enable the use of simpler, less pure, less expensive reagents, reducing product costs. With scale-up, integration, and suitable software for design and control, these features provide the basic capabilities described in Chapter 15.

### 16.6. Conclusions

A backward-chaining analysis indicates that feasible developmental pathways link our present technology base to the technology base described in Part II. Alternative pathways are known, and others can be devised.

To reach the first stage discussed in this chapter requires the assembly of molecular machine systems from $\sim 10^{4}$ to $10^{5}$ monomers. Chapter 14 describes several ways to achieve this ability, via Brownian assembly or the development of AFM-directed mechanosynthesis systems. Once assembled, small mechanosynthetic devices can be made to execute complex patterns of motion powered and controlled by imposed pressure fluctuations. Relatively small and simple devices can be used to construct larger and more complex devices. A series of steps can enable a relatively smooth transition from solution-phase assembly of monomers with conventional reactivity to the assembly of diamondoid mechanisms in an inert (eventually, vacuum) environment using highly active reagents.

Each step along this pathway will present great practical challenges, but each step will also bring valuable new capabilities. The long-term rewards, measured in terms of scientific and technological capabilities, appear large.

[^43]: J. Bonaventura has suggested the use of liquid xenon (e.g., at $16 \mathrm{C}, 58 \mathrm{~atm}$ ) as a solvent (Rentzepis and Douglass, 1981); this may avoid some of these constraints. Xenon has little interaction with (e.g.) reactive organic radicals (Cook and Roberts, 1983).
[^44]: Martensitic transitions have desirable properties: they transform one solid structure into another, are cooperative, occur through local structural displacements, require no diffusion, cause little change in entropy, and can propagate at speeds near that of sound.