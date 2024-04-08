# Nanoscale Structural Components


### 9.1. Overview

Nanomachines (like macromachines) are made from components, and their strength, stiffness, shape, and surface properties largely determine what those components can do. Chapter 10 discusses components as moving parts, focusing on sliding and rolling interfaces. The present chapter discusses components (including fixed housings) from a structural perspective, developing approximations and rules for analyzing designs specified in less than atomic detail.

Section 9.2 discusses some general issues in nanomechanical design. Section 9.3 considers components as pieces of material and discusses the relationship between material-based continuum models and atom-based molecular models. Section 9.4 examines component properties, emphasizing surface corrections to bulk quantities. Sections 9.5 and 9.6 discuss the control of shape in designing irregular and symmetric objects. Finally, Section 9.7 adds a discussion of adhesive interfaces for joining components to form larger structures.

### 9.2. Components in context

Nanomechanical systems differ from systems of biological molecular machinery in their basic architecture: nanomechanical components are supported and constrained by stiff housings, while biological components often can move freely with respect to one another.[^23] It is natural to focus on moving parts, but a typical system has much of its mass in the form of a stiff housing. Gears, bearings, springs, screws, sliding rods, motors-each should be pictured as anchored to or embedded in an extended diamondoid structure tailored to support it in a functional position with respect to other components (Chapter 10 describes conditions under which nonbonded interfaces form good bearings, enabling parts to move in their housings).

The analogy to macroscale engineering practice is clear: the components of macroscale machines and other systems are commonly mounted on an extended structure, whether this is termed a housing, chassis, casing, airframe, engine block, or framework. (The chief exceptions to this rule are devices that flexibly position an object in space-cranes, robotic arms, desk lamps-and even these constrain the motion of each part with respect to its neighbors.) A housing structure forms a unit, but it need not be monolithic. Macroscale housings can be made from pieces held together by fasteners, adhesives, or welding; nanomechanical housings can likewise be made from pieces held together by fasteners or adhesive interfaces (Section 9.7).

Moving parts typically occupy or sweep out only a modest fraction of the volume enclosed by a housing; the rest, save for small clearances, can be occupied by a solid structure with a diamondlike modulus. Accordingly, housings can often be quite stiff. Note that the thermal positional uncertainty of one region of a homogeneous three-dimensional structure with respect to another approaches a distance-independent constant at large separations. Since the stiffness of a housing can often be much greater than that of the moving parts, a housing can often be treated as rigid on a large scale, making corrections (when necessary) for local compliance.

### 9.3. Materials and models for nanoscale components

Macromechanical engineering treats components as being made from materials, neglecting the placement of specific atoms. Section 9.3.1 discusses various classes of materials from an engineering perspective, introducing nanomechanical concerns. Section 9.3.2 contrasts viewing a component as a specific molecular structure with viewing it as a piece of material. Section 9.3.3 outlines how the materials perspective can be extended to provide a useful description of many nanoscale mechanical components.

### 9.3.1. Classes of materials

a. Conventional metallic solids. In common metals (e.g., iron, aluminum, copper), atoms have 8 to 12 nearest neighbors with which they share weakly directional bonds. A simple model of ${ }^{\circ}$ valence electrons in a metal pictures them as forming a gas in which the ionic cores of the atoms are embedded; in this model, bonding is nondirectional.

Bonds of low directionality allow dislocations to move smoothly, enabling atomic layers to slide over one another with relatively little resistance. This nanoscale behavior permits macroscale ductility, making objects insensitive to cracks and able to undergo large plastic deformations. Brittle materials, in contrast, resist dislocation motion; this makes them stronger, but unable to deform plastically and highly sensitive to microscopic flaws. This sensitivity occurs because cracks under tensile loads concentrate the stress at their tip: ductile materials deform to blunt the tip and reduce the stress; brittle materials break, extending the crack and raising the tip stress, leading to catastrophic failure.

Because conventional manufacturing makes objects with a high density of microscopic flaws, strong-but-brittle materials have proved difficult to use, and weaker-but-ductile metals have dominated macroscale engineering practice.

Molecular manufacturing, however, can limit flaws to rare defects of atomic scale, enabling the wider use of brittle materials. (Other tactics, such as dividing materials into fibers, can also make brittle materials useful; see discussions in the extensive literature on fracture mechanics.) The atomic mobility permitted by metallic bonding sharply limits the usefulness of metals in a nanomechanical context at ordinary temperatures. Although some refractory metals and intermetallic compounds may in fact be useful, this volume assumes no use of metals as mechanical components.

b. Ionic solids. An ideal ionic solid consists of ions held together almost exclusively by electrostatic forces. Because an ion of one charge is strongly attracted to its oppositely charged nearest neighbors, but repelled by more distant neighbors, smooth sliding is difficult, and brittle behavior results. Since ionic solids have no great strength to compensate for their brittleness, they find no significant application in macromechanical engineering and are expected to find no significant application in nanomechanical engineering.

Some solids have mixed covalent and ionic bonding (e.g., alumina, silica) and high strength. These materials (ceramics and glasses) are sometimes regarded as ionic solids; for present purposes, they can be regarded as borderline covalent solids. They find use in macromechanical engineering (limited chiefly by their brittleness), and may find use in nanomechanical engineering (limited chiefly by the availability of covalent materials with better properties).

c. Molecular solids. Weak forces (e.g., van der Waals attraction) can bind inert gas atoms and neutral, covalently bound molecules to form a solid. Unless the molecules are large (Section 9.3.1d), molecular solids are weak and of no use as structural materials.

d. Polymeric solids. In a polymeric solid, weak forces provide effective cohesion between long molecules, and the covalent bonds within those molecules can dominate the bulk properties of the material. Polymeric solids with wellaligned molecules can be strong and stiff along the axis of alignment. Many polymeric solids are also tough and ductile; they find widespread use in macroscale engineering.

In nanomechanical engineering, even small-scale mobility of polymer chains must usually be suppressed. This can most directly be accomplished by providing covalent cross links between chains, but in the limiting case, a crosslinked polymer becomes a covalent solid.

e. Covalent solids. In a covalent solid, bonds form a dense, continuous network in which most atoms are bonded to three or more neighbors. Examples of covalent solids include diamond and graphite: brittle materials of great strength. Other examples include black phosphorus and germanium, which are of little interest as structural materials. In nanomechanical engineering, interest focuses on the more diamondlike covalent solids.

f. Diamondoid covalent solids. Used narrowly, diamondoid refers to materials consisting almost entirely of carbon with $s p^{3}$ bonding. As used here, diamondoid describes strong, stiff covalent solids with a dense, three-dimensional network of bonds. The diamondoid solids of most interest have compositions

Table 9.1. Properties of some strong solids. ${ }^{a}$ Many other refractory materials (metal carbides, borides, oxides, nitrides, and silicides) may also be of mechanical (or electrical) interest.

| Material | Young's modulus <br/> $(\mathrm{GPa})$ | Strength $^{\mathrm{b}}$ <br/> $(\mathrm{GPa})$ | Melting point <br/> $(\mathrm{K})$ | Density <br/> $\left(\mathbf{k g} / \mathbf{m}^{3}\right)$ |
| :--- | :---: | :---: | :---: | :---: |
| diamond | 1050 | 50 | $1800^{\mathrm{c}}$ | 3500 |
| graphite $^{\text {d }}$ | 686 | 20 | $3300^{\mathrm{c}}$ | 2200 |
| $\mathrm{H}-6$ carbon $^{\mathrm{e}}$ | $\sim 1500 ?$ | $?$ | $?^{\mathrm{c}}$ | $\sim 3200$ |
| $\mathrm{SiC}$ | 700 | 21 | $2570^{\mathrm{c}}$ | 3200 |
| $\mathrm{Si}$ | 182 | 7 | 1720 | 2300 |
| $\mathrm{Boron}$ | 440 | 13 | 2570 | 2300 |
| $\mathrm{Al}_{2} \mathrm{O}_{3}$ | 532 | 15 | 2345 | 4000 |
| $\mathrm{Si}_{3} \mathbf{N}_{4}$ | 385 | 14 | $2200^{\mathrm{c}}$ | 3100 |
| Tungsten | 350 | 4 | 3660 | 19300 |

a Most values in this table are from Kelly (1973).

b Strength values are inferred from measurements and may underestimate the values achievable in flaw-free structures.

c Material sublimes or decomposes rather than melting.

d Modulus and strength of graphite are in the bonded plane.

e The stability and properties of H-6 carbon metal are inferred from tight-binding semiempirical calculations (Tamor and Hass, 1990); the ratio of Young's modulus to bulk modulus is here assumed equal to that of diamond.

biased toward multivalent first-row elements that form good covalent bonds (boron, carbon, nitrogen, oxygen), but may make substantial use of the similar second-row elements (silicon, phosphorus, and sulfur), limited use of monovalent elements (hydrogen, fluorine, chlorine), and sparing use of other elements. Among structures fitting this description (which embraces diamond itself) are many that are strong, stiff, and highly stable. Table 9.1 surveys the properties of diamond and several diamondoid materials. Pure-carbon structures falling within this broad definition have been widely discussed (e.g., by Johnston and Hoffmann, 1989; Karfunkel and Dressler, 1992; Merz et al., 1987; Tamor and Hass, 1990).

In the present context, diamondoid structures have a further advantage. With some restrictions on the choice of atoms and bonding patterns, they are reasonably well described by molecular mechanics models (Section 3.3), enabling the computationally economical investigation of mechanical systems specified in atomic detail.

g. Mixed structures. The categories discussed in Sections 9.3.1(a-f), though useful, are not sharply bounded. Many materials have intermediate structures. Ceramics with bonding intermediate between ionic and covalent have been mentioned. Covalent-solid objects of small size can be described as molecules, and combinations of them can be viewed as molecular or ionic solids. Covalent bonding can coexist with metallic conductivity. Molecular objects built on the development pathways from solution chemistry to advanced mechanosynthesis are likely to include extensively crosslinked polymeric structures intermediate between conventional polymers and covalent solids (see Chapter 16).

### 9.3.2. Materials vs. molecular structures

In macromechanical engineering, components are described as regions occupied by a material (usually isotropic and homogeneous) having certain mechanical properties: strength, density, shear modulus, and Young's modulus. These and other material properties (e.g., fatigue life, thermal coefficient of expansion, damping coefficients, friction coefficients), together with shape, enable a detailed engineering analysis of the component.

From a molecular mechanics perspective, a diamondoid component is a network of bonded atoms. The smallest objects contain few atoms, and must be described in atomic detail, yet at some scale a description in terms of shape and continuum material properties becomes quite useful (especially in preliminary design). To what extent can continuum models be applied to small diamondoid structures?

### 9.3.3. The bounded continuum approach

In extending continuum models to nanostructures, one must consider both surface effects and the atomic graininess of matter. Surface effects in diamondoid structures can be approximately described by a bounded version of a continuum model, but atomic structure constitutes a fundamental limit to such models. Surface effects on the mechanical properties of metals are more pervasive because of the nonlocal nature of metallic bonding; these effects are not considered here.

a. Surface effects. A simple continuum model treats the mechanical properties of a material as continuous up to a sharp boundary, but this is physically unrealistic for nanoscale objects. Section 3.5 discusses models of interacting diamondoid surfaces that account for van der Waals attractions and overlap repulsions between their surface atoms, yet treat those atoms as forming a twodimensional continuum. This approach can be used to convert a standard continuum model into a bounded continuum model, treating the boundaries of an object in a physically realistic way.

To apply a continuum model to the interior of an object, however, a sharp boundary must be defined. The natural definition of a surface for mechanical purposes-as the boundary of the region from which other similarly defined objects are excluded-gives misleading results in calculations based on bulk density, modulus, and strength. At ordinary pressures, nonbonded-contact radii are approximately twice as large as covalent radii, hence surface atoms occupy more space than interior atoms. Accordingly, rules for defining surface locations that yield good values for mass (from density), for component stiffness (from modulus), or for component strength (from material strength) define surfaces that fall well within the boundaries of the excluded volume (see Figure 9.1). Section 9.4 discusses issues of component size and surface effects in more detail.

b. Graininess effects. The atomic structure of matter constrains the shapes possible for small objects. In macroscale engineering, one assumes that (save for machining geometry and minimum gauge limitations) a part can be made in any desired shape, within some size tolerance and surface roughness. Section 9.5.2 discusses the conditions under which similar assumptions can be applied to nanoscale objects, in effect treating diamondoid structures as materials to be shaped.

Surface roughness can increase friction. Chapter 10 discusses friction, yielding results that can be applied without specifying atomic coordinates; these results are thus applicable in preliminary designs based on analyses at the level of materials, rather than of molecular structures.

c. Anisotropies. The bounded continuum models used in this volume treat materials as isotropic. Although this is a good approximation for many structures, including the most diamondlike diamondoids, it is a poor approximation for others. Continuum models of anisotropic bulk materials (e.g., those developed to describe composite structures) can be useful in describing anisotropic diamondoid components.

### 9.4. Surface effects on component properties

Density, modulus, size, and shape are ambiguous in nanoscale systems. Size and shape are ambiguous because molecular surfaces are not sharply bounded, and this makes density and modulus ambiguous, despite the clear-cut meanings of mass and stiffness. Nonetheless, a model based on defined surfaces and (isotropic, homogeneous) properties can provide useful design-phase estimates of mass, stiffness, and strength. A conservative application of bounded-continuum estimates can be used to identify design conditions that limit elastic deformation to acceptable bounds, but may provide only a rough description of the residual displacements.

### 9.4.1. Materials and stiffness

To maximize strength and stiffness, nanoscale structural components are best made from diamondoid solids (Section 9.3.1f). In the systems analyzed in the following chapters, stiffness requirements are usually more constraining than are strength requirements. Stiffness can be directly estimated by computational experiments using molecular mechanics models. Examples of such calculations appear in Section 9.4.3, along with guidelines for estimating the stiffness of diamondoid components.

### 9.4.2. Assigning sizes

Ordinarily, one regards the region occupied by a component as the region from which other components are excluded. This measure of size varies with compressive loads, and with the shapes and chemical natures of the facing surfaces. A reasonable standard choice is the region occupied by the component atoms of

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-27.jpg?height=422&width=1203&top_left_y=1837&top_left_x=226)
the structure when each is assigned a summable $0.1 \mathrm{nN}$ radius (Section 3.3.3b); these radii are used in space-filling molecular representations throughout this volume.

Figures 9.2 and 9.3 suggest why this size estimate must be corrected when estimating stiffness. The polycyclic framework structure accounts for most of the stiffness, but the excluded volume extends well beyond this framework, because of both the separation between nonbonded atoms and (in some structures) the presence of monovalent surface atoms. To maximize stiffness for a given component size, it is best to avoid monovalent surface atoms, instead favoring structures like the one in Figure 9.3. The size correction $\delta_{\text {surf }}$ required to describe the structural volume is then approximately the difference between the covalent and nonbonded radii; using the $0.1 \mathrm{nN}$ nonbonded radii, $\delta_{\text {surf }} \approx 0.07 \mathrm{~nm}$ for both first- and second-row atoms. A larger correction ( $\delta_{\text {surf }}=0.1 \mathrm{~nm}$ is used in Chapter 11) yields a more conservative estimate of stiffness for a component of a given excluded-volume size. (For H-terminated diamond, a comparable correction is $\delta_{\text {surf }} \approx 0.14 \mathrm{~nm}$.)

(a)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=82&width=502&top_left_y=1006&top_left_x=481)

(b)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=100&width=502&top_left_y=1122&top_left_x=481)

(c)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=106&width=500&top_left_y=1257&top_left_x=481)

(d)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=136&width=504&top_left_y=1410&top_left_x=480)

(e)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=168&width=506&top_left_y=1578&top_left_x=478)

(f)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-28.jpg?height=200&width=524&top_left_y=1777&top_left_x=461)

Figure 9.2. A series of rod structures, most consisting of a hydrogen-terminated region of the diamond lattice. Rod (a) is a polyethylene chain;(b)-(f) can be described as additional chains linked side by side (the digits to the right indicate the number of such chains in the corresponding rod). The structure of rod (c) departs from the diamond pattern, adding bonds perpendicular to the rod axis to replace nonbonded $\mathrm{H} / \mathrm{H}$ contacts. Moduli are graphed in Figure 9.4(c).
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-29.jpg?height=298&width=562&top_left_y=222&top_left_x=537)

Figure 9.3. A segment of rod resembling Figure 9.2(f), but with $\mathrm{N}$ and $\mathrm{O}$ termination in place of $\mathrm{CH}$ and $\mathrm{CH}_{2}$. See Section 9.4.3 for discussion and Figure 9.4(a) for modulus.

A further correction can arise from differences in the stiffness contributions between the outermost framework atoms and those in the interior; with fewer constraints on their motions, they may be subject to greater relaxation under stress, reducing their stiffness contributions. This effect can be explored by examining the scaling of stiffness with cross-sectional area in a molecular mechanics model such as MM2.

(The structural volume is responsible for strength as well as stiffness, hence a similar correction applies. In the absence of monovalent surface atoms, the same can be said of mass. Calculations of bending stiffness may require a different correction to the effective cross section.)

### 9.4.3. Computational experiments on rod modulus

Molecular mechanics predictions for the linear modulus of a rod, $E_{\ell}$ (having the dimensions of force), can be obtained by computing the energy of a series of rods placed under differing strains. For an ideal measure of area $S_{\text {rod }}$, the product $S_{\text {rod }} E=E_{\ell}$, for some value of Young's modulus $E$.

Figure 9.2 shows a series of segments from rods with differing cross-sectional areas, most consisting of a hydrogen-terminated region of the diamond lattice. For these rods, a reasonable measure of cross-sectional area is $n_{\text {bonds }}$, the minimum number of framework bonds crossing a surface that divides the rod. In Figure 9.2(a), a strand of polyethylene, $n_{\text {bonds }}=1$; for the two joined strands of Figure 9.2(b), $n_{\text {bonds }}=2$; and so forth, through $n_{\text {bonds }}=9$. Calculating the effective area of these rods from their bond count and from the bond density for the equivalent orientation in diamond $\left(\sim 1.925 \times 10^{19} \mathrm{~m}^{-2}\right)$ avoids the issues of surface definition just discussed. For this family of rods

$$
\begin{equation*}
S_{\text {rod }} \approx 5.2 \times 10^{-20} n_{\text {bonds }}\left(\mathrm{m}^{2}\right) \tag{9.1}
\end{equation*}
$$

and, in the bulk-material limit,

$$
\begin{equation*}
E_{\ell} \approx 5.45 \times 10^{-8} n_{\text {bonds }}(\mathrm{N}) \tag{9.2}
\end{equation*}
$$

If relaxation were to reduce the stiffness contributions of surface atoms, then thinner rods would have a lower value of $E_{\ell}$.

Figure 9.4 summarizes the results of computational experiments on the structures in Figures 9.2,9.3, 9.5, and 9.6. As can be seen, on a per-bond basis, thinner rods have a slightly greater value of $E_{\ell}$ than thicker rods (presumably owing to contributions from nonbonded interactions involving hydrogen), but rods of all

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=695&width=1143&top_left_y=181&top_left_x=147)

Figure 9.4. Results of computational experiments measuring rod moduli in the MM2/CSC approximation. Structure (a) is the $\mathrm{N}$ - and O-terminated rod in Figure 9.3; set (b) consists of the structures in Figure 9.5; set (c), Figure 9.2; set (d), Figure 9.6. The dashed line labeled (e) passes through the origin and a point corresponding to a column of hexagonal diamond structure (with a compact cross-section) having $n_{\text {bonds }}=16$; as can be seen, it almost exactly corresponds to an extrapolation from a similar column with $n_{\text {bonds }}=3$. The dashed line (f) is analogous to (e), but for a structure like family (c) with $n_{\text {bonds }}=18$. The upper dashed line bounding the shaded region corresponds to the modulus of diamond rods oriented along the $<111>$ axis, extrapolating from the properties of bulk diamond; the lower dashed line corresponds to a similar extrapolation with the modulus halved.

(a)
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=130&width=618&top_left_y=1524&top_left_x=422)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=128&width=239&top_left_y=1673&top_left_x=421)
3

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=145&width=278&top_left_y=1664&top_left_x=763)

(c)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=145&width=243&top_left_y=1833&top_left_x=419)
4

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-30.jpg?height=166&width=297&top_left_y=1818&top_left_x=749)

Figure 9.5. A series of rods forming a family of structures suffering increasing strain per bond with increasing diameter; instances with $n_{\text {bond }}=2,3$, and 4 are shown. Moduli are graphed in Figure 9.4(b).

(a)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=94&width=280&top_left_y=238&top_left_x=516)

(b)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=98&width=280&top_left_y=390&top_left_x=516)

(c)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=111&width=299&top_left_y=545&top_left_x=499)

(d)

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=133&width=243&top_left_y=715&top_left_x=501)
3
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=432&width=292&top_left_y=240&top_left_x=864)
6

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-31.jpg?height=150&width=280&top_left_y=709&top_left_x=861)

Figure 9.6. A second series of rods forming a family of structures suffering increasing strain per bond with increasing diameter; instances with $n_{\text {bonds }}=3,4,5$, and 6 are shown. Moduli are graphed in Figure 9.4(d).

sizes have a value substantially lower than that of bulk diamond. Since this trend continues to structures with substantial stiffness contributions from interior atoms (e.g., the $n_{\text {bonds }}=18$ value indicated in Figure 9.4), it appears that this modulus deficit results from defects in the MM2 model (Section 3.3.2) rather than from surface relaxation. (Since the usual goal is to maximize stiffness, adopting MM2 values usually results in conservative assessments of designs.)

Figure 9.3 illustrates a structure like Figure 9.2(f), but with $\mathrm{N}$ and $\mathrm{O}$ termination, rather than $\mathrm{CH}$ and $\mathrm{CH}_{2}$. (Chains of $s p^{3}$ nitrogen atoms should be stable when each is bonded to carbon in a diamondoid solid of this kind.) For a given value of $n_{\text {bonds }}$, structures terminated in this manner are substantially more compact, and the MM2 model predicts substantially greater stiffness. This increase is a surface effect, but one which it is conservative to neglect. Figures 9.5 and 9.6 illustrate other rods having moduli plotted in Figure 9.4. The hexagonal column $\left(n_{\text {bonds }}=3\right)$ of Figure $9.5(\mathrm{~b})$ is the smallest structural unit that might plausibly exhibit the elastic properties of bulk hexagonal diamond along the corresponding axis; it falls almost precisely on a line drawn through the result for a compact column of hydrogen-terminated hexagonal diamond structure with $n_{\text {bonds }}=16$. Accordingly, surface relaxation effects on modulus appear negligible in this family of structures as well.

### 9.5. Shape control in irregular structures

Nanomechanical devices can be specified in complete atomic detail, permitting them to be described (with varying accuracy) by molecular modeling techniques. This is necessary for small structures, and for structures about to be built, but it is not always necessary for large structures during preliminary design and analysis. It will be useful to have some guidelines regarding the boundary between small and large for these purposes.

### 9.5.1. Control of shape and detail of specification

Nanomechanical engineering differs from macroscale engineering in that the number of possible component shapes can be significantly constrained by atomic sizes and feasible bonding patterns. In sufficiently small components, the set of possible shapes can be exhaustively described. For each type of mechanism, there is some minimum size below which components of the required shapes cannot be constructed (e.g., it is fruitless to attempt to build a gear having 50 teeth in a volume that can contain only 10 atoms; the limiting size for a 50-tooth gear is substantially larger). Near this minimum size, a design must be specified in complete molecular detail to gain any confidence in its validity.

Somewhat above this limit, however, complete atomic specification becomes unnecessary, just as in macroscale engineering and for the same reason: any one of many arrangements of atoms can serve the purpose. On this larger size scale, a specific molecular structure must be chosen before planning a mechanosynthesis, and before performing a fully detailed analysis, but this choice can be made after performing a reasonably accurate analysis describing size, shape, strength, stiffness, mass, dynamics, energy dissipation, and performance. Sections 9.5.2 to 9.5.4 discuss how the number of available diamondoid structures varies with volume and structural constraints, drawing conclusions regarding the scale at which molecular detail can be omitted and a bounded continuum model can be adopted. Designs based on these models often are relatively conservative, setting only lower bounds on the performance of nanomechanical systems.

### 9.5.2. Estimates of the number of diamondoid structures

a. Exponential scaling with volume. The number of distinct diamondoid structures $N_{\text {struct }}$ that can fit in a given volume of reasonable shape is an exponential function of the volume (neglecting surface corrections). This can be seen by considering a hypothetical atom-by-atom construction process: at each surface site in a partially completed structure there is some number of distinct options (with a geometric-mean value $N_{\text {opt }}$ which is not necessarily an integer) for how to proceed at the next step, that is, for what kind of atom to bond in what manner. The value of $N_{\mathrm{opt}}$ describes the effective number of choices made per atom added, correcting for patterns of choices that in the end produce the same structure. The number of choices defined in this way is proportional to the number of atoms in the final structure (which will, for some typical atomic number density $n_{\mathrm{v}}$, be proportional to the volume $V$ ), and each choice leads to a different structure (by the above definition of distinct choice). For a suitable definition of $N_{\text {opt }}$, the number in question is

$$
\begin{equation*}
N_{\text {struct }}=N_{\mathrm{opt}}^{\left(n_{\mathrm{v}} V\right)} \tag{9.3}
\end{equation*}
$$

The proper value of $N_{\mathrm{opt}}$ is not obvious, even if the atoms are restricted to a single type. It will depend on the range of permissible local structures, constrained by (for example) the magnitudes and patterns of bond strain permitted in the interior of a solid stable enough for practical use. Knowledge of these constraints would be necessary (yet not sufficient) to enable a simple computation.

b. Estimates from entropy of fusion. The entropy of fusion of a crystal is a measure of the increase in the available volume in configuration space (Section

4.3.3) that occurs with a transition from a single, regular structure to an ensemble of states which includes many different structures. If the potential wells in the liquid state were as narrow as those in the solid state, and if each of those potential wells were equally populated and corresponded to a stable amorphous structure (and vice-versa), then the entropy of fusion would be a direct measure of the increase in number of wells, and would thus provide a direct measure of the number of available structures. In practice, low-stiffness wells and the thermal population of unstable transition structures tend to make the entropy of fusion an overestimate; the negligible thermal population of high-strain states that would be kinetically stable in corresponding solids tends to make it an underestimate. The absence of a choice of atom types at various sites (in elemental crystals) introduces a strong bias toward underestimation, relative to the systems of interest here.

Measuring the entropy of fusion of carbon (melting point $\sim 3820 \mathrm{~K}$ ) presents technical difficulties; the values for silicon and germanium crystals, which share the diamond structure, are $4.6 \times 10^{-23}$ and $4.7 \times 10^{-23} \mathrm{~J} / \mathrm{K}$ per atom respectively. These values are both about $3.4 k$; if this increase in entropy were solely the result of the increased number of available potential wells per atom, that number would be $N_{\text {opt }} \approx 30$. An estimate of the number of distinct states in argon at liquid density (Stillinger and Weber, 1984) yields a value equivalent to $N_{\text {opt }} \approx 3$ wells per atom; this is compatible with an estimate based on the entropy of fusion.

c. Estimates including multiple elements. In the set of broadly diamondoid structures built up from C, Si, B, N, P, O, S, H, F, and $\mathrm{Cl}$ (with a bias toward the higher-valence and first-row members), $N_{\text {opt }}$ is increased as a result of the choice of atom type at each step; a factor of 5 is a plausible estimate of this increase, allowing for constraints and biases in the choices made. Taking the preceding silicon and germanium estimates as a base, this suggests that a reasonable estimate for diamondoid structures is $N_{\mathrm{opt}} \approx 150$, and that calculations based on $N_{\mathrm{opt}}=30$ are conservative. This conservatism is intended to compensate for various constraints, including structural stability and avoidance of unacceptable electric fields and potentials resulting from patterns of aligned dipoles.

A region with a structural volume of $1 \mathrm{~nm}^{3}, N_{\mathrm{opt}}=30$, and $n_{\mathrm{v}}=100 \mathrm{~nm}^{-3}$ has $N_{\text {struct }} \approx 10^{148}$. A similar cubical region with an excluded volume of $1 \mathrm{~nm}^{3}$ and $\delta_{\text {surf }}=0.1 \mathrm{~nm}$ has a structural volume of $\sim 0.51 \mathrm{~nm}^{3}$, and $N_{\text {struct }} \approx 10^{75}$.

### 9.5.3. Exclusion of structures by geometrical constraints

These enormous numbers imply that objects can be constructed with almost any specified shape, provided (1) that the specifications do not describe complex contours on a subnanometer scale, or sharp corners and the like, and (2) that the specifications allow adequate tolerances in the placement of surface atoms, relative to the ideal contours of the shape. Demanding that many surface atoms simultaneously meet tight tolerances can easily result in an overconstrained problem having no physically realizable solution.

For example, one might ask that each of the $\sim 100$ atoms on the surface of a $1 \mathrm{~nm}$ object be within a distance $\varepsilon$ of an ideal surface contour. A randomly chosen structure can be terminated so as to keep only those atoms within a certain
boundary, and that boundary can be chosen so that the surface atoms of the terminated structure are close to a preselected ideal surface contour (Section 10.3 discusses a similar picture in more detail). With $n_{\mathrm{v}}=100 \mathrm{~nm}^{-3}$, the positions of these surface atoms typically vary over a range of $\sim 0.2 \mathrm{~nm}$ about that contour. If we demand that each surface atom be within $\varepsilon=0.01 \mathrm{~nm}$ of this contour, then on the order of $(0.01 / 0.2)^{100} \approx 10^{-130}$ of a set of randomly chosen structures will meet this condition. Given $N_{\text {struct }} \approx 10^{75}$, the probability that some structure satisfies this condition is on the order of $10^{-55}$. If, however, one asks that 50 atoms forming particular surfaces be accurately placed within $\varepsilon=0.02 \mathrm{~nm}$, then on the order of $(0.02 / 0.2)^{50} \approx 10^{-50}$ of a set of randomly chosen structures will meet this condition, and the probability that a suitable structure does not exist is on the order of $10^{-25}$. (Brute-force search procedures would be inadequate to find acceptable structures, but various options exist for developing more sophisticated search procedures to solve problems of this general kind; doing so presents an interesting and important challenge for computer-aided design of molecules.)

Tight constraints on object shape arise chiefly in the working interfaces of moving parts, for example, where surfaces must slide smoothly. Chapter 10 develops several models for such interfaces; some are based on the choice of regular structures of high symmetry (to which the statistical analysis in this section does not apply); others describe the constraints on an irregular structure imposed by the requirement that it slide smoothly over a regular surface. Other working interfaces bind molecules; these are considered in the next section. Nonworking surfaces are exposed to free space and have few constraints.

### 9.5.4. Exclusion of structures by molecular binding requirements

Surfaces with ${ }^{\circ}$ binding sites (receptors) for specific molecules are useful, for example in acquiring and processing molecules from solution (Section 13.2). The principles of selective binding are familiar from molecular biology, and chiefly involve detailed surface complementarity between the molecule and its receptor: complementary surface shapes to provide strong van der Waals attraction, complementary patterns of charge and dipole orientation to provide electrostatic attraction, and so forth (in aqueous solutions, so-called hydrophobic forces can play a large role). These requirements for complementarity impose constraints on surface structure, again reducing the size of the set of acceptable structures by many orders of magnitude.

Mammalian immune systems provide an example in which structures capable of strong, selective binding are chosen from a set of structures of calculable size. Mammals can produce highly specific antibodies able to bind any one of a wide range of small molecules (when a molecule of a particular type is presented as an immunologically stimulating hapten); this includes molecules not found in nature. These antibodies are developed by a process of variation and selection chiefly within a space of possibilities defined by differing sequences of the 20 genetically encoded ${ }^{\circ}$ amino acid residues within the antibody hypervariable domains (variations at other sites are relatively rare). These domains contain $\sim 38$ amino acid residues; hence most antibodies are selected from a set of structures containing $\sim 20^{38} \approx 3 \times 10^{49}$ members. Equation (9.3) with $N_{\mathrm{opt}}=30$ suggests that comparable diversity can be provided by a set of structures each containing
$<35$ atoms, although the geometric and structural constraints of receptors often require larger structures. (Note that use of rigid structures for most machine components does not preclude the use of flexible structures, e.g., to enable a flap on a binding site to fold over a ligand.)

### 9.5.5. Kaehler brackets

T. Kaehler has proposed a systematic approach to designing irregular interfaces to meet particular geometrical constraints (Kaehler, 1990; Kaehler, 1992). First, one defines an anchoring surface [e.g., a hydrogenated diamond (111) surface]. Second, one defines a large family of brackets extending from this surface. (These can resemble the hexagonal column of Figure 9.5(b), but adding various modifications: substitution of $\mathrm{N}, \mathrm{B}, \mathrm{P}$, or $\mathrm{SiH}$ for $\mathrm{CH}$, replacement of a $\mathrm{C}-\mathrm{C}$ linkage or a $\mathrm{CH} \mid \mathrm{HC}$ contact with $\mathrm{C}-\mathrm{CH}_{2}-\mathrm{C}, \mathrm{C}-\mathrm{O}-\mathrm{C}$, or $\mathrm{C}-\mathrm{S}-\mathrm{C}$, etc., all subject to stiffness and stability constraints; see Figure 9.7. The size of the resulting family of structures increases exponentially with bracket length and soon reaches millions.) Third, one determines the geometry of each bracket and notes the positions and orientations of its terminal bonds. Finally, one compiles an index based on this data, organized to enable one to find the brackets with terminal bonds most nearly matching a desired position and orientation.

How might an indexed set of Kaehler brackets be used in design? The brackets define a relatively comprehensive set of slim diamondoid structures, indexed according to the geometrical relationship between their ends. These can be used
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-35.jpg?height=566&width=1008&top_left_y=1198&top_left_x=323)

Figure 9.7. Six short Kaehler brackets ( $\sim 0.9 \mathrm{~nm}$ between the top and bottom six-membered rings), illustrating a portion of the available range of structural variations and geometries. Bracket (a) is a simple column (a hydrogen-terminated fragment of hexagonal diamond; all column ends truncated). Bracket (b) is lengthened by substituting Si for $\mathrm{C}$ at six sites. Bracket (c) is shortened by substituting $\mathrm{C}-\mathrm{O}-\mathrm{C}$ for a $\mathrm{CH} \mid \mathrm{HC}$ contact at six sites. Bracket (d) is bent by one substitution of the sort in bracket (a) and three of the sort in (c). Bracket (e) has its top offset with respect to the bottom because of four substitutions like those in (c), the substitution of $\mathrm{Si}$ for $\mathrm{C}$ at two sites closer to the ends, and the substitution of $\mathrm{F}$ for $\mathrm{H}$ at two sites. Bracket ( $f$ ) has its top rotated with respect to the bottom because of three substitutions as in (c) and three substitutions of $\mathrm{HC}-\mathrm{CH}$ for $\mathrm{C}$. If brackets are anchored to a diamond structure with a choice of locations, the range of end displacements need only span a diamond lattice cell. (MM2/CSC)
to link structures that must be held in specific relative orientations; several such bridges can form a stiff connection. Further, the design-phase substitution of one Kaehler bracket for another bracket of similar end geometry is like moving a small robotic arm by a small distance (and perhaps changing its stiffness). One can imagine algorithms that in effect push and pull a flexible structure into a desired shape (e.g., to fine-tune a receptor design), choosing brackets of the shape necessary to apply the needed forces. Discrepancies between predicted and actual geometries could be rectified by further substitutions among brackets of similar end geometry, but perhaps quite dissimilar structure.

### 9.6. Components of high rotational symmetry

In building rotating machinery, components having high-order rotational symmetry are often desirable. Chapter 10 discusses applications of such components in bearings and gears. (Perturbations from an asymmetric environment always break perfect symmetry, but perfection is unnecessary.) Rotationally symmetric components divide roughly into two classes: strained-shell structures made (at least conceptually) by bending a straight slab into a hoop, and specialcase structures that are more intrinsically cylindrical. Members of an intermediate class of curved-shell structures resemble strained-shell structures, but with regular arrays of dislocation-like features that reduce the strains. These terms correspond to rough categories, not to precise distinctions.

### 9.6.1. Strained-shell structures

Figure 9.8 illustrates a relatively small strained shell having two distinct layers of cyclic structure. The thickness-to-radius ratio $(t / r)$ of strained shells is constrained by the net hoop stress and the permissible bond tensile strain at the outer surface. For diamondoid structures with negligible net hoop stress, permissible bond strains may be as large as $0.035 \mathrm{~nm}\left(\sim 1.23 r_{0} \approx 0.187 \mathrm{~nm}\right)$; assuming a Morse potential (Section 3.3.3a), a C-C bond with smaller strain has positive stiffness, tending to stabilize its length. In the presence of a strain gradient perpendicular to the axis of strain (as in a strained shell), even a layer somewhat beyond the positive-stiffness limit can be stabilized by restoring forces imposed by the less-strained layers closer to the shell axis (the layers are coupled by shear stiffness). Note that this situation differs from the single-bond, pure-tensile-

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-36.jpg?height=437&width=865&top_left_y=1726&top_left_x=301)

Figure 9.8. A strained shell structure with a relatively thin wall and small diameter.

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-37.jpg?height=700&width=1206&top_left_y=195&top_left_x=222)

Figure 9.9. A strained shell structure with a thin wall and small diameter (a); structure (b) adds a nonbonded polyyne chain along the axis.

load model used to derive bond failure rates in Section 6.4.4a. In general, the stability analysis for highly strained shells is complex, because of the possibility of concerted bond rupture and rearrangement; the designs in this volume assume considerably smaller bond strains.

If the material of the shell in Figure 9.8 had linear elastic properties, a $0.035 \mathrm{~nm}$ strain would occur with $t / r \approx 0.46$ (using a mid-thickness reference for $r$ ). The worst-case nonlinearity would prohibit bond compression entirely, resulting in a limit of $t / r \leq \sim 0.23$. Both these estimates neglect the favorable effects of angle-bending relaxation. The appropriate measure of thickness for these calculations is smaller than that of the structural volume discussed in Section 9.4.2; atomic centers at the edge of the framework structure provide a conservative marker for the surface.

R. Merkle (1991; 1992a) has developed computer-aided design (CAD) software able to generate a wide range of strained-shell structures based on the diamond lattice, providing flexible control of radius, thickness, crystallographic orientation, surface shape, and surface termination; precise arrays of thousands of atoms can be generated by supplying a few parameters. The structure in Figure 10.17 was generated using this CAD tool together with subsequent energy minimization using molecular mechanics software.

Figure 9.9 illustrates an example of a strained-shell structure with little bond stretching, consisting of a single layer of cyclic structure. It gains stiffness from the compressed nonbonded contacts in its interior; additional nonbonded contacts can be provided by placing a polyyne chain along its axis.

### 9.6.2. Curved-shell structures

Thick cylindrical structures have many applications. They can be made from diamondlike structures, relieving strain with arrays of dislocations. Merkle notes that the Lomer dislocation is stable and has useful geometrical properties for

![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-38.jpg?height=555&width=1203&top_left_y=210&top_left_x=127)

Figure 9.10. A curved shell structure containing an array of Lomer dislocations (structure courtesy of R. Merkle, Xerox PARC, and L. Balasubramaniam, MIT).

this purpose. Figure 9.10 illustrates a cylindrical structure incorporating several Lomer dislocations; preliminary work by R. Merkle and L. Balasubramaniam has produced software that aids in the design of tubular structures of this kind. Merkle suggests that computer-aided design tools able to automatically generate diamond lattices modified by (potentially dense) arrays of dislocations offer a promising approach to the generation of diamondoid structures of considerable diversity.

### 9.6.3. Special-case structures

Some cylindrical structures are not members of scalable families. The rods illustrated in Figures 9.5 and 9.6 are examples of small-radius structures having significant rotational symmetry. The cylindrical structure of Figure 9.11 provides
![](https://nanosystems.contact.ms/cropped/2024_03_29_ec553d027506296c17dbg-38.jpg?height=552&width=756&top_left_y=1574&top_left_x=360)

Figure 9.11. A cylindrical structure with $s p^{3}$ surface structure and an $s p^{2}$ inner structure (the ten-membered conjugated rings will exhibit ${ }^{\circ}$ aromatic stabilization).

an example of intermediate size; the outer ring of the bearing in Figure 1.1 provides a still larger example. The set of diamondoid structures of high rotational symmetry, small length, and diameter $\leq 1 \mathrm{~nm}$ is large, but may be small enough to permit the development of an exhaustive catalogue.

### 9.7. Adhesive interfaces

Large structures can be built directly from small reactive moieties and clusters, but there are substantial advantages to building indirectly via intermediate-scale blocks (Sections 8.6.6 and 14.2). These blocks can be joined by adhesive interfaces that can exploit any of the attractive forces responsible for the cohesion of solids. Designing a system to be assembled in this way imposes some constraints on its structure, but in many instances these need not be severe.

### 9.7.1. Van der Waals attraction and interlocking structures

The simplest adhesive interface consists of two surfaces of complementary shape, with no special provision for bonding. If the interface has suitable corrugations, the interface will resist shear. Van der Waals attraction provides tensile strength and (together with balancing overlap repulsions) interfacial stiffness. Figure 3.12 indicates that a simple contact between complementary diamondoid surfaces can have a tensile strength $\sim 1 \mathrm{GPa}$ and a stiffness per unit area of $>30 \mathrm{~N} / \mathrm{m} \cdot \mathrm{nm}^{2}$. The compliance of an interface with this stiffness is equal to that of a $\sim 30 \mathrm{~nm}$ thick slab of diamond.

Introducing a simple van der Waals interface thus degrades the strength of a diamondoid structure by about two orders of magnitude, and substantially degrades the stiffness of systems built on a $100 \mathrm{~nm}$ scale. Where strength is unimportant and stiffness is not at a premium, such interfaces may be of considerable use. Convoluted, interlocking interfaces (e.g., with knobs that snap into holes) can greatly increase strength and stiffness by making greater use of overlap repulsions.

### 9.7.2. Ionic and hydrogen bonding

Complementary patterns of charge or ${ }^{\circ} \mathrm{hydrogen}$ bonding capacity can increase interfacial strength and stiffness. The strength and stiffness of interfaces with extensive ionic bonding can be estimated from the properties of sodium chloride. Theoretical calculations of the breaking stress yield estimates around 2.7 GPa (Kelly, 1973), and modulus data indicates an interlayer stiffness per unit area of $\sim 170 \mathrm{~N} / \mathrm{m} \cdot \mathrm{nm}^{2}$.

### 9.7.3. Covalent interfacial bonding

The strongest and stiffest adhesive interfaces result from the formation of dense arrays of strong bonds; various reactive diamondoid surfaces can be designed to join in this way. Diamond (111) surfaces terminated with complementary patterns of $\mathrm{B}$ and $\mathrm{N}$ atoms can join by forming an array of ${ }^{\circ}$ dipolar bonds. Arrays of dienes and dienophiles can join through Diels-Alder reactions to form an array of $\mathrm{C}-\mathrm{C}$ bonds. Hexagonal diamond surfaces like that illustrated in Figure 8.24 can apparently bond to form continuous hexagonal diamond (bonding two planar surfaces is electronically analogous to bonding a hexagonal column to a surface); a pair of diamond (110) surfaces can apparently bond to form continuous
cubic diamond. In these instances, adhesive surfaces can unite blocks of the strongest, stiffest materials known to experimental science without leaving a distinct interface, and hence without loss of strength or stiffness.

A potential difficulty in forming strong interfaces is avoiding the sudden release of unacceptable amounts of mechanical energy: the energy of a diamond (111) surface is $\sim 5.4 \mathrm{~J} / \mathrm{m}^{2}$, which if suddenly thermalized would be enough to raise the temperature of a $1 \mathrm{~nm}$ thick slab by $\sim 10^{3} \mathrm{~K}$. Adhesion, however, can be viewed as the inverse of crack formation. The gradual application of inhomogeneous stress distributions can cause controlled crack growth; the relaxation of similar stress distributions can enable controlled joining. Alternatively, interposed structures could force joining to proceed at a controlled rate, or surface structures might be chosen such that adhesion is slowed by steps with substantial thermal activation barriers. Section 14.2.2a notes the utility of alignment pegs in large interfaces.

### 9.8. Conclusions

Nanoscale structural components can serve either as housings or as moving parts. The best materials for nanoscale components are diamondoid in structure: these materials have unusual strength and stiffness, and lend themselves to design using molecular mechanics methods. Computational experiments indicate that bulk-material stiffnesses for diamond (and diamondoid solids) can be used to describe components of subnanometer dimensions, provided that the modulus is applied to a cross-sectional area that is descriptive of the structural framework (here termed the structural volume), omitting an outer layer of the excluded volume resulting from the relatively long range of overlap forces, and from any monovalent surface atoms. At a $\sim 1 \mathrm{~nm}$ size scale, the number of stable diamondoid structures becomes enormous, and essentially any shape can be built, provided that tight $(<0.02 \mathrm{~nm}$ ) tolerances are not applied too widely. (A discussion of the compatibility of irregular structures with smooth sliding motion is deferred to the next chapter.) Components of high rotational symmetry can be constructed in several ways; Chapter 10 describes the use of such structures in building bearings and gears.

Some open problems. Open problems in the field of nanoscale structural components divide into problems of design and problems of analysis. Regarding the latter, further research using molecular mechanics studies to improve bounded continuum models and explore their range of validity would be valuable. A challenging objective is to develop software that merges classical finite-element methods with bounded continuum models and molecular mechanics methods; this would enable a designer to control the level of detail in a structural description, keeping atomic detail where it is significant and omitting it elsewhere to improve computational efficiency.

In design, it would be useful to specify and characterize many small, regular structures useful as shafts, gears, and so forth; means for indexing and recovering designs are of comparable importance. Still more useful would be the development of software for designing irregular structures that meet particular boundary conditions. The Kaehler bracket approach is promising for a range of applications, as is Merkle's suggestion of dense dislocation networks; another
might be a simulated annealing process (using a potential function developed for the purpose) in which atom number and atom types are permitted to change.

In another area entirely, studies of the joining of diamond surfaces could resolve questions regarding the practicality of using the strongest adhesive interfaces in component assembly. Further, characterization of the properties of $\mathbf{B}-\mathbf{N}$ dipolar bonds (and other dipolar and coordination bonds) could yield descriptions of desirable adhesive interfaces, and might yield improved designs for interfaces suitable for use in nanomechanical gears (Section 10.7).

[^23]: E. Tribble has emphasized the importance of such supporting structures for separating degrees of freedom in a system and thereby simplifying design and analysis.