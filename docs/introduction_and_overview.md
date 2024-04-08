# Introduction and Overview


### 1.1. Why molecular manufacturing?

The following devices and capabilities appear to be both physically possible and practically realizable:

- Programmable positioning of reactive molecules with $\sim 0.1 \mathrm{~nm}$ precision
- Mechanosynthesis at $>10^{6}$ operations/device $\cdot$ second
- Mechanosynthetic assembly of $1 \mathrm{~kg}$ objects in $<10^{4} \mathrm{~s}$
- Nanomechanical systems operating at $\sim 10^{9} \mathrm{~Hz}$
- Logic gates that occupy $\sim 10^{-26} \mathrm{~m}^{3}\left(\sim 10^{-8} \mu^{3}\right)$
- Logic gates that switch in $\sim 0.1 \mathrm{~ns}$ and dissipate $<10^{-21} \mathrm{~J}$
- Computers that perform $10^{16}$ instructions per second per watt
- Cooling of cubic-centimeter, $\sim 10^{5} \mathrm{~W}$ systems at $300 \mathrm{~K}$
- Compact $10^{15}$ MIPS parallel computing systems
- Mechanochemical power conversion at $>10^{9} \mathrm{~W} / \mathrm{m}^{3}$
- Electromechanical power conversion at $>10^{15} \mathrm{~W} / \mathrm{m}^{3}$
- Macroscopic components with tensile strengths $>5 \times 10^{10} \quad \mathrm{~Pa}$
- Production systems that can double capital stocks in $<10^{4} \mathrm{~s}$

Of these capabilities, several are qualitatively novel and others improve on present engineering practice by one or more orders of magnitude. Each is an aspect or a consequence of molecular manufacturing.

### 1.2. What is molecular manufacturing?

This volume describes the fundamental principles of molecular machinery and applies them to nanomechanical devices and systems, including molecular manufacturing systems and computers. At present, however, these are unfamiliar topics. New fields often need new terms to describe their characteristic features, and so it may be excusable to begin with a few definitions: *Molecular manufacturing* is the construction of objects to complex, atomic specifications using sequences of chemical reactions directed by nonbiological molecular machinery. *Molecular nanotechnology* comprises molecular manufacturing together with its techniques, its products, and their design and analysis; it describes the field as a whole. *Mechanosynthesis*-mechanically guided chemical synthesis-is fundamental to molecular manufacturing: it guides chemical reactions on an atomic scale by means other than the local ${ }^{\circ}$ steric[^0] and electronic properties of the ${ }^{\circ}$ reagents; it is thus distinct from (for example) enzymatic processes and present techniques for organic synthesis. [^52]

At the time of this writing, positional chemical synthesis is at the threshold of realization: precise placement of atoms and molecules has been demonstrated (for example, see Eigler and Schweizer, 1990), but flexible, extensible techniques remain in the domain of design and theoretical study (Part III), as does the longer-term goal of molecular manufacturing (Chapter 14). Accordingly, the implementation of molecular nanotechnologies like those analyzed in Part II awaits the development of new tools. This volume is addressed both to those concerned with identifying promising directions for current research, and to those concerned with understanding and preparing for future technologies.

The following chapters form three parts: Part I describes the chief physical principles and phenomena of importance in molecular machinery and manufacturing. Part II applies the results of Part I to the design and analysis of components and systems (yielding the conclusions summarized in Section 1.1). Part III then describes implementation pathways leading from our current technology base to systems like those described in Part II.

The rest of the present section attempts to clarify the nature of the topic by discussing an example of a nanomechanical device and by presenting a chemical perspective on molecular manufacturing. Sections 1.3 to 1.5 present a set of comparisons between this and other fields (mechanical engineering, microtechnology, chemistry, and molecular biology), a discussion of overall approach (including objectives, level, scope, and assumptions), and an overview of the later chapters and how they fit together. Table 1.1 lists some of the known problems and constraints that are addressed elsewhere in this volume.

### 1.2.1. Example: a nanomechanical bearing

As discussed in Section 1.3, the mechanical branch of molecular nanotechnology forms a field related to, yet distinct from, mechanical engineering, microtechnology, chemistry, and molecular biology. An example may serve as a better introduction than would an attempt at a written definition.

Figure 1.1 shows several views of one design for a nanomechanical bearing like those discussed in greater depth in Chapter 10. (Figure 1.2 describes some conventions used in illustrations like Figure 1.1) In a functional context, many of the bonds shown as hydrogen terminated would instead link to other moving parts or to a structural matrix. Several characteristics are worthy of note:
- The components are ${ }^{\circ}$ polycyclic, more nearly resembling the fused-ring structures of diamond than the open-chain structures of biomolecules such as ${ }^{\circ}$ proteins.

Table 1.1. Some known issues, problems, and constraints.

> Thermal excitation<br/>
Thermal and quantal positional uncertainty<br/>
Quantum-mechanical tunneling<br/>
Bond energies, strengths, and stiffnesses<br/>
Feasible chemical transformations<br/>
Electric field effects<br/>
Contact electrification<br/>
Ionizing radiation damage<br/>
Photochemical damage<br/>
Thermomechanical damage<br/>
Stray reactive molecules<br/>
Device operational reliabilities<br/>
Device operational lifetimes<br/>
Energy dissipation mechanisms<br/>
Inaccuracies in molecular mechanics models<br/>
Limited scope of molecular mechanics models<br/>
Limited scale of accurate quantal calculations<br/>
Inaccuracy of semiempirical models<br/>
Providing ample safety margins for modeling errors

- Accordingly, each component is relatively stiff, lacking the numerous opportunities for internal rotation about bonds that make ${ }^{\circ}$ conformational analysis difficult in typical biomolecules.
- Repulsive, nonbonded interactions strongly resist both rotations of the shaft away from its axial alignment with the ring, and displacement along that axis or perpendicular to it.
- Rotation of the shaft about its axis within the ring encounters negligible energy barriers, indicating a nearly complete absence of static friction.
- The combination of ${ }^{\circ}$ stiffness in five degrees of freedom with facile rotation in the sixth makes the structure act as a good bearing, in the conventional mechanical engineering sense of the term.
- The absence of significant static friction in a system that places bumpy surfaces in firm contact with no intervening lubricant is surprising by conventional mechanical engineering standards.
- No solvent is illustrated, and there is no reason to think that the bearing structure shown would in fact be soluble.
- Neither of the components of the bearing is a plausible target for synthesis using reagents diffusing in solution; barring unprecedented chemical cleverness, their construction requires mechanosynthetic control.

How typical are these characteristics? Stiff, polycyclic structures are ubiquitous in the designs presented in Part II. Many components are designed to combine stiff constraints in some degrees of freedom with nearly free motion in others, thereby fulfilling roles familiar in mechanical engineering; nonetheless,
![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-25.jpg?height=1544&width=1024&top_left_y=246&top_left_x=364)

Figure 1.1. End views and exploded views of a sample overlap-repulsion bearing design (shown in both ball-and-stick and space-filling representations). Geometries represent energy minima determined by the MM2/CSC molecular mechanics software. Note the six-fold symmetry of the shaft and fourteen-fold symmetry of the surrounding ring; with a least common multiple of 42 , this combination yields low energy barriers to rotation of the shaft within the ring. Bearing structures are discussed further in Chapter 10. (MM2/CSC denotes the Chem3D Plus implementation of the MM2 molecular mechanics force field. The MM2 model is discussed in Section 3.3.2; Chem3D Plus is a product of Cambridge Scientific Computing, Cambridge, Massachusetts.)

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-26.jpg?height=499&width=1205&top_left_y=199&top_left_x=145)

Figure 1.2. Conventions for atom representation using shading and relative sizes. The "H (fixed)" atom represents a hydrogen atom held at fixed spatial coordinates; these are used to model some mechanical constraints applied by a larger structure (e.g., in stiffness calculations). All radii are set equal to the values for $0.1 \mathrm{nN}$ compressive contacts given by Eq. (3.20).

a detailed understanding of how those roles are fulfilled requires analyses based on uniquely molecular phenomena. The operating environment assumed for the nanomechanical and mechanosynthetic systems discussed in Part II is high vacuum, rather than a solvent. Finally, the designs in Part II (unlike those described in Part III) are consistently of a scale and complexity that precludes synthesis using present techniques.

The bearing shown in Figure 1.1 suggests the nature of other systems described in Part II. For example, the combination of a bearing and shaft suggests the possibility of extended systems of power-driven machinery. The outer surface of the bearing suggests the possibility of a molecular-scale gear. The controlled rotary motion of the shaft within the ring, together with the concept of extended systems of machinery, suggests the possibility of controlled molecular transport and positioning, which is necessary for advanced mechanosynthesis.

### 1.2.2. A chemical perspective on molecular manufacturing

Chemistry today (and chemical synthesis in particular) focuses chiefly on the behavior of molecules diffusing and colliding in solution. Reaction rates in solution-phase chemistry are determined by multiple influences, including concentration-dependent collision frequencies, and steric and electronic effects local to the reacting molecules.

Although based on the same principles of physics, mechanosynthesis performed by molecular machinery in vacuum differs greatly from conventional chemistry. Concepts developed to describe diffusing molecules in a gas or liquid (or immobile molecules in a solid) often must be modified in describing systems characterized by nondiffusive mobility. The concept of "concentration," for example, in the familiar sense of "number of molecules of a particular type per unit of macroscopic volume" becomes inapplicable to calculations of reaction rates. Local steric and electronic effects remain important, but the decisive influence on reaction rates becomes mechanical positioning aided by applied force.

a. Machine-phase systems. To emphasize differences from solid-, liquid-, and gas-phase systems, it can be useful to speak of machine-phase systems and chemistry:

- A machine-phase system is one in which all atoms follow controlled trajectories (within a range determined in part by thermal excitation).
- Machine-phase chemistry describes the chemical behavior of machine-phase systems, in which all potentially reactive moieties follow controlled trajectories.

The useful distinction between liquid phase and gas is blurred by the existence of supercritical fluids; the useful distinction between solid and liquid is blurred by the existence of glasses, liquid crystals, and gels. Where machinephase chemistry is concerned, the definitional ambiguities are chiefly associated with the words all and controlled. In a conventional chemical reaction or an enzymatic active site, a moderate number of atoms in a small region can be said to follow somewhat-controlled trajectories, but these examples fall outside the intended bounds of the definition. In a good example of a machine-phase system, large numbers of atoms follow paths that seldom deviate from a nominal trajectory by more than an atomic diameter while executing complex motions in an extended region from which freely-diffusing molecules are rigorously excluded. Machine-phase conditions can be termed "eutactic ("well arranged," from the Greek eus, "good," and taktikos, "of order or arrangement"). Eutactic conditions are quite unlike those of solution-phase chemistry.[^1]

Mechanosynthesis of the sort discussed in Chapters 8 and 13 is a machinephase process (Part III discusses mechanosynthesis in a solvent environment). Eutactic mechanosynthesis offers novel chemical capabilities, such as positionbased discrimination among chemically equivalent sites, strong suppression of side reactions, and new sources of ${ }^{\circ}$ activation energy.

Chemistry in the machine phase shares characteristics of gas-, solution-, and solid-phase chemistry, and yet displays unique characteristics; these similarities and differences are discussed further in Sections 6.4.2 and 8.3. Since experience shows that habits of thought developed in the study of liquid- and gas-phase systems can yield misleading conclusions if hastily applied to machine-phase systems, frequent recourse to fundamental principles is necessary. The Index of this volume includes an entry (Chemistry: contrasts between machine and solution phase) that cites discussions of this issue. Table 1.2 provides a compact summary.

### 1.2.3. Exposition vs. implementation sequence

The implementation sequence for molecular manufacturing might proceed as follows: The ability to make complex molecular objects in solution is extended to objects of greater size and complexity. These molecular objects are used as components in molecular machines capable of directing the mechanosynthesis of yet larger and more complex machines. Through a series of steps, solution-

Table 1.2. Contrasts between solution-phase and mechanosynthetic chemistry (a more detailed comparison appears in Table 8.1).

| Characteristic | Solution-phase chemistry | Mechanosynthetic chemistry |
| :---: | :---: | :---: |
| Reagent transport | Diffusion | Mechanical conveyance |
| Reaction site selectivity | Structural influences | Direct positional control |
| Reaction environment | Solution | Mechanisms in vacuum |
| Control of <br/> reaction environment | Relatively little | Relatively great |
| Intermolecular <br/> reactions | Ubiquitous <br/> opportunities | Strictly controlled <br/> opportunities |
| Unwanted reactions | Inter- and <br/> intramolecular | Chiefly intramolecular |
| Sensitivity to <br/> energy differences | $10 \mathrm{maJ}$ is large | $10 \mathrm{maJ}$ is (often) small |
| Typical product size | 10 to 100 atoms | $>10^{10}$ atoms |

based mechanosynthetic methods are replaced by methods that require an inert environment, then polymeric building materials are replaced by diamondoid materials. Further increases in scale and capability yield advanced molecular manufacturing systems under computer control. (Each of these steps is discussed in Chapter 16.)

The expository sequence of this volume is quite different. It begins by describing fundamental principles of broad applicability (Part I), then applies them to the design and analysis of advanced systems (Part II). Finally, having described principles and objectives, it turns to implementation pathways (Part III). Thus, the means considered are guided by the objectives pursued.

### 1.3. Comparisons

Molecular nanotechnology resembles and overlaps with other fields, yet differs substantially. A discussion of resemblances can illustrate the applicability of existing knowledge and emerging developments; a discussion of differences can warn of false analogies and consequent misunderstandings.

Table 1.3 compares several existing production processes-conventional fabrication, microfabrication, solution-phase chemistry, and biochemistry-with molecular manufacturing. The following sections provide a more detailed comparison of molecular manufacturing and molecular nanotechnology with these other processes and their products. Appendix B focuses on areas of these fields having special relevance molecular manufacturing; the present section makes broad comparisons to the mainstream.

### 1.3.1. Conventional fabrication and mechanical engineering

a. Similarities: components, systems, controlled motion, manufacturing. Many mechanical engineering concepts apply directly to nanomechanical systems. As shown in Chapters 3 to 6, methods based on classical mechanics suffice for much of the required analysis. As shown in Chapters 9 to 11, beams, shafts, bearings, gears, motors, and the like can all be constructed on a nanometer scale to serve familiar mechanical functions. As a consequence, macromechanical

Table 1.3. Typical characteristics of conventional machining, micromachining, solution-phase chemistry, biochemistry, and molecular manufacturing. [^57]

| Characteristic | Conventional <br/> fabrication | Micro- <br/> fabrication | Solution <br/> chemistry | Bio- <br/> chemistry | Molecular <br/> manufacturing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Molecular <br/> precision? | no | no | yes | yes | yes |
| Positional <br/> control? | yes | yes | no | partial | yes |
| Typical <br/> feature scale | $1 \mathrm{~mm}$ | $1 \mu$ | $0.3 \mathrm{~nm}$ | $0.3 \mathrm{~nm}$ | $0.3 \mathrm{~nm}$ |
| Typical <br/> product scale | $1 \mathrm{~m}$ | $10 \mathrm{~mm}$ | $1 \mathrm{~nm}$ | $10 \mathrm{~nm}$ | $100 \mathrm{~nm}+$ |
| Typical <br/> defect rate[^58] | $10^{-4}$ | $10^{-7}$ | $10^{-2}$ | $10^{-11}$ | $10^{-15}$ |
| Typical <br/> cycle times | $1 \mathrm{~s}$ | $100 \mathrm{~s}$ | $1000 \mathrm{~s}$ | $10^{-3} \mathrm{~s}$ | $10^{-6} \mathrm{~s}$ |
| Products <br/> described by | materials | materials | atoms | monomer | atoms |

engineering and nanomechanical engineering share many design issues and analytical techniques.

Both molecular and conventional manufacturing systems use machines to perform planned patterns of motion: they shape, move, and join components to build complex three-dimensional structures. Systems of both kinds can manufacture machines, including machines used for manufacturing (Chapter 14).

b. Differences: scale, molecular phenomena. Despite these similarities, nanomechanical engineering forms a distinct field. The familiar model of objects as made of homogeneous materials, though still useful (Chapter 9), often must be replaced by models that treat objects as sets of bonded atoms (Chapters 2 and 3). Thermally excited vibrations are of major importance, and quantum effects are sometimes significant (Chapters 5, 6, and 7). Further, nanomachines suffer from molecular damage mechanisms (Chapter 6); molecular phenomena permit (and demand) novel bearings (Chapter 10); scaling laws favor electrostatic over electromagnetic motors (Chapters 2 and 11); and the basic operations of manufacturing on a molecular scale are chemical transformations (Chapters 8 and 13). These transformations typically move the system between discrete states, leading to structures that are either exactly right or clearly wrong; this resembles digital logic more closely than it does metalworking.

### 1.3.2. Microfabrication and microtechnology

a. Similarities: small scale, electronic quantum effects. Microtechnology has enabled the fabrication of micron-scale mechanical devices. These share basic scaling properties with nanomechanical devices-and so, for example, electrostatic motors are preferred over electromagnetic motors in both micro- and nanotechnology (Section 2.4.3). Further, quantum electronic devices of kinds now being explored with microfabrication technologies may become targets for molecular manufacturing.

b. Differences: fabrication technology, scale, molecular phenomena. Microfabrication relies on technologies (photolithographic pattern definition, etching, deposition, diffusion) essentially unrelated to those of molecular manufacturing. In a sense these two fields are moving in opposite directions: microfabrication attempts to make bulk-material structures smaller despite fabrication irregularities; molecular manufacturing will emerge from attempts to make molecular structures larger without losing the atomic precision characteristic of stereospecific chemical synthesis. Making structures consisting of a few dozen preciselyarranged atoms seems unachievable using microfabrication, but is routine in chemical synthesis. The gears, bearings, and motors described in Chapters 10 and 11 differ in volume from their closest microfabricated counterparts by a factor of $\sim 10^{9}$, and rely on molecular structures and phenomena in their operation.[^2]

### 1.3.3. Solution-phase chemistry

a. Similarities: molecular structure, processes, fabrication. Chemical principles describe the basic steps of molecular manufacturing, since each consists of a chemical transformation. Chemical knowledge can help in evaluating the stability of products, and chemical research has produced the most useful models of the mechanical behavior of molecular objects. Organic chemistry is particularly relevant owing to the superiority of carbon-based structures for most mechanical applications. Fundamental chemical concepts such as ${ }^{\circ}$ bonding, ${ }^{\circ}$ strain, ${ }^{\circ}$ reaction rates, ${ }^{\circ}$ transition states, ${ }^{\circ}$ orbital symmetry, and ${ }^{\circ}$ steric hindrance are all applicable; familiar chemical entities such as ${ }^{\circ}$ alkanes, ${ }^{\circ}$ alkenes, ${ }^{\circ}$ aromatic rings, ${ }^{\circ}$ radicals, and ${ }^{\circ}$ carbenes are all useful. [^53] Solution-based organic synthesis can make precisely structured molecular objects; it has even been used to make molecular gears (Mislow, 1989), although of a sort having no obvious utility for nanomechanical engineering.

b. Differences: machine-phase systems, mechanosynthesis. The chief differences between the present subject and conventional chemistry stem from the properties of machine-phase systems and of mechanosynthesis. These have been summarized in Section 1.1.2 and are discussed at length in Chapter 8.

### 1.3.4. Biochemistry and molecular biology

a. Similarities: molecular machines, molecular systems. Molecular biology, like molecular nanotechnology, embraces the study of molecular machines and molecular machine systems. Ribosomes-like mechanisms in flexible molecular manufacturing systems-can be viewed as numerically controlled machine tools following a series of instructions to produce a complex product. Molecular biology and biochemistry stimulated the train of thought that led to the concept of molecular manufacturing (Drexler, 1981), and their techniques offer paths to the development of molecular manufacturing systems (Section 15.2).

b. Differences: materials, machine phase, general mechanosynthesis. Biology is a product of evolution rather than design, and molecular biologists study systems that differ greatly from the eutactic systems described here. Unlike molecular manufacturing systems, the molecular machines found in cells can synthesize only relatively small molecules and a stereotyped set of polymers; they cannot synthesize a broad class of ${ }^{\circ}$ diamondoid structures. Larger biological structures typically acquire their shapes through the action of weak forces ('hydrogen bonds, ${ }^{\circ}$ salt bridges, ${ }^{\circ}$ van der Waals attraction, ${ }^{\circ}$ hydrophobic forces). As a consequence of stronger bonding, the strength and ${ }^{\circ}$ modulus of diamondoid components can exceed those of biological structures by orders of magnitude. The bearings, gears, motors, and computers discussed in Part II are accordingly quite different from the bacterial flagellar motor, the actin-myosin system, systems of neurons, and so forth. Biological and nanomechanical systems are organized in fundamentally different ways. For example, cells rely on diffusion in a liquid phase-although they contain molecular machines, they are not machine-phase systems.[^3]

### 1.4. The approach in this volume

### 1.4.1. Disciplinary range, level, and presentation

As Section 1.2 indicates, the study of molecular nanotechnology spans multiple disciplines. This circumstance has hampered both evaluation of the existing concepts and research aimed at extending and superseding them. One purpose of the present volume is to assemble a large portion of the necessary core knowledge in a form that requires no specialized knowledge of the component disciplines. An effort has been made (and a glossary provided) to make key chemical concepts accessible to nonchemists, solid-state physics concepts accessible to nonphysicists, and so forth, assuming only a basic background in both chemistry and physics (and a willingness to skip past the occasional obscure observation aimed at a reader in a different discipline). The intended contribution of this work consists not in extending the frontiers of existing fields, but in combining their basic results to lay the foundations of a new field.

To facilitate understanding, several mathematical results in Part I are derived from fundamental principles. Many of these results appear in existing textbooks; others (so far as is known) are novel, being motivated by new questions. The exposition of these mathematical models includes an unusually large number of graphs that illustrate equations in the text; these are provided to facilitate design, which is a synthetic as well as an analytic process. In the analysis of a given system, a calculation based on an equation with a single set of parameter values frequently suffices. In synthesis, however, the designer usually wishes to understand how system properties will vary as controllable parameters are changed; for this, a graph can be more useful than a bare equation.

Different fields have applied different energy units to molecular-scale phenomena, including the kilocalorie per gram-mole of items $\left(\approx 6.95 \times 10^{-21} \mathrm{~J}\right.$ per single item) and the kilojoule per gram-mole of items $\left(\approx 1.66 \times 10^{-21} \mathrm{~J}\right.$ per single item) of chemistry, and the electron-volt $\left(=\mathrm{eV} \approx 160 \times 10^{-21} \mathrm{~J}\right)$ of physics. The standard SI unit of energy, of course, is the joule itself. To avoid allusions to hypothetical moles of identical systems or to electrons not involved in the problem, and (more important) to enable mechanical calculations involving force, work, kinetic energy, and so forth to proceed without frequent unit conversions, this volume adheres to the joule as the unit of energy. The attojoule $\left(=\mathrm{aJ}=10^{-18} \mathrm{~J}\right)$ and milli-attojoule $\left(=\mathrm{maJ}=10^{-21} \mathrm{~J}\right.$ ) are convenient fractional units.

### 1.4.2. Levels of abstraction and approximation

In an ideal world, chemists would be able to predict the behavior of molecules by applying quantum electrodynamics (QED) to suitably defined assemblages of nuclei and electrons, and engineers would be able to predict automotive performance in the same manner. In this regard, the world is far from ideal. Although no experiment has yet shown an imperfection in QED as a description of the properties of ordinary matter (setting nuclear and gravitational interactions aside), it is computationally intractable as a description even of small molecules. In the real world, chemists and engineers describe systems using a hierarchy of levels of abstraction and approximation (Table 1.4). It is worth surveying this hierarchy because it provides a framework for practical analysis.

As discussed in Chapter 3, the most rigorous models ordinarily used by chemists apply $a b$ initio molecular orbital methods; these approximate the Schrödinger equation, which approximates the Dirac equation, which approximates QED, which approximates the unknown exact, universal laws of physics. In describing the mechanical properties of large molecular structures, however, chemists abandon molecular orbital methods in favor of molecular mechanics

Table 1.4. Levels of abstraction and approximation in molecular systems engineering.

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-33.jpg?height=700&width=712&top_left_y=253&top_left_x=517)

methods of more limited applicability but lower computational cost; these too are discussed in Chapter 3.

At the upper levels of the hierarchy, engineers set objectives in terms of system behavior and use these objectives to determine requirements for subsystem behavior (this can proceed through several layers of subsystems). Systems are commonly analyzed in terms of subsystem capabilities, which are analyzed in terms of lumped-component models, which in turn are analyzed in terms of continuum models. For example, a modern computer is described by its subsystems-processor, memory, disk, bus, cooling, power supply, and so forth. A processor (give or take some intermediate levels) is described as an interconnected network of discrete transistors and other lumped components. Transistors are described by continuum models that consider gate geometries, dopant distributions, electron transport, and so forth. Individual atoms and electrons are neglected in describing transistors, and one never describes a computer by describing electron transport within transistors.

Nanomechanical systems are subject to a similar analysis, describing systemlevel objectives served by subsystem capabilities implemented using lumped components. Continuum models, however, become problematic on the nanometer scale. Chapter 9 develops bounded continuum models that take sufficient account of surface effects to enable the analysis of a broad range of nanomechanical designs in less than atomic detail. To design the smallest devices, however, detailed molecular mechanics models are necessary, and to provide a firstprinciples analysis of a mechanochemical process, there is no substitute for molecular orbital methods.

### 1.4.3. Scope and assumptions

The present volume adheres to design constraints that may not limit future engineering practice. Each constraint excludes possibilities that are presently difficult to analyze, but that may prove both feasible and desirable. The following

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-34.jpg?height=463&width=649&top_left_y=203&top_left_x=438)

Figure 133. Diamondoid structures are a subset of covalently bonded structures, which are a subset of the broad range of solid structures.

assumptions and limitations are thus conservative, resulting in what are likely to be underestimates of future capabilities:

a. A narrow range of structures. From the broad range of materials (metals, ionic crystals, molecular crystals, polymers, etc.), the present work selects the class of diamondoid ${ }^{\circ}$ covalent solids as its focus (Section 9.3.1f). These structures form a small subset of those that are possible (Figure 1.3), and contain atoms drawn chiefly from the shaded region of Figure 1.4. Diamond itself is the strongest and stiffest structure presently known at ordinary pressures (Kelly, 1973), making it and similar materials attractive on engineering grounds. Since many components can be regarded as polycyclic organic molecules, much of the vast base of knowledge developed by organic chemists is immediately applicable. Small components are subject to large surface effects, but typical organic molecules are, in effect, all surface; accordingly, surface effects are an integral part of molecular models.

![](https://nanosystems.contact.ms/cropped/2024_03_29_5078c09f4e8b2d767097g-34.jpg?height=451&width=950&top_left_y=1516&top_left_x=287)

Figure 1.4. Periodic table of the atoms, with cells shaded to indicate those of greatest importance to nanomechanical design: hydrogen $(\mathrm{H})$, carbon $(\mathrm{C})$, nitrogen $(\mathrm{N})$, oxygen $(\mathrm{O})$, fluorine $(\mathrm{F})$, silicon $(\mathrm{Si})$, phosphorus $(\mathrm{P})$, sulfur $(\mathrm{S})$, and chlorine $(\mathrm{Cl})$. Other elements have applications, but few of the structures discussed in the following chapters contain them. [H is more often placed above lithium ( $\mathrm{Li})$ than above $\mathrm{F}$, but hydrocarbons resemble the stable fluorocarbons far more than they do the reactive lithiocarbons. Like F, H is only one electron short of a closed-shell configuration.]

b. No nanoelectronic devices. On a macroscale, mechanical systems are quite distinct from electronic systems: they involve the motion of materials, rather than of electrons and electromagnetic fields. On a nanoscale, mechanical motions are identified with the displacements of nuclei, but electronic activity can cause such motions. Nevertheless, many systems (e.g., the bearing in Figure 1.1) can be described by molecular mechanics models that take no explicit account of electronic degrees of freedom, instead subsuming them into a potential energy function (Chapter 3) defined in terms of the positions of nuclei. This volume focuses on mechanical systems of this sort.

Some systems are strongly electronic in character, relying on changes of electronic state to change other electronic states, with the associated nuclear motions being of small amplitude. Molecular nanotechnologies will surely include nanometer-scale electronic devices exploiting quantum phenomena to achieve (for example) switching and computation. Research relevant to this class of devices is already in progress.

Although nanoelectronic devices are likely to be important products of molecular manufacturing, they fall beyond the scope of the present work. There are several reasons for this. First, the analytical methods required for quantum electronics differ from those required for molecular machinery; including them would have made this volume larger and later. Second, these analytical methods require approximations that frequently render the results dubious, reducing their value as a premise for further reasoning (the existence in 1992 of at least three competing classes of theories to explain high-temperature superconductivity, observed and studied in cuprates since 1987, suggests the magnitude of the difficulties). Finally, while nanomechanical devices can build nanoelectronic devices, the latter cannot return the favor; thus, nanomechanical devices are in a technological sense more fundamental. Accordingly, the nanocomputers discussed in Chapter 12 are based on mechanical devices, although electronic devices will surely permit greater speed.

Chapter 11 briefly discusses nanoscale electromechanical systems. These use conductors, insulators, and tunneling junctions as components of motors, actuators, and switches. Quantum phenomena are important in nanoscale electromechanical systems, but the gross results (switching, interconversion of electrical and mechanical energy) do not rely on subtle quantum effects. Finally, despite their likely utility, machine-phase electrochemical processes are mentioned only in passing.

c. Machine-phase chemistry. Because it can guide reactions (and can avoid most competing reactions) by tightly constraining molecular motions, machinephase chemistry can be simpler, in some respects, than is solution-phase chemistry. Mechanosynthesis and other operations can be conducted by systems of molecular machines immersed in a solution environment, and there are sometimes advantages to doing so. These less controlled, more complex chemical systems fall beyond the scope of the present work, save for the discussion of implementation strategies in Part III.

d. Room temperature processes. Reduced temperatures decrease thermally excited displacements (Chapter 5), thermal damage rates (Chapter 6), and phonon-mediated drag (Chapter 7). The opportunities and problems presented by low-temperature systems are nonetheless not explored in the present work. Operation at high temperatures is desirable in some circumstances, and can facilitate both desired and undesired chemical reactions, but discussions of the associated technological opportunities and problems are likewise omitted.

e. No photochemistry. Photochemical damage mechanisms are discussed in Section 6.5. Design of molecular machines for photochemical damage resistance is an important challenge, but for simplicity the following will instead assume that devices operate in optically shielded environments. Deliberate use of photochemistry is mentioned only in passing.

f. The single-point failure assumption. The design of small components that can tolerate atomic-scale damage and defects is worthy of attention, but the following will instead assume that any such flaw causes component-level (and usually subsystem-level) failure, unless the components are relatively large. The use of redundant systems to achieve damage tolerance is proposed and analyzed only at higher levels of system organization. Diverse damage mechanisms are reviewed and modeled in Chapter 6.

### 1.4.4. Objectives and nonobjectives

Because this volume is a work of theoretical applied science (Appendix A), some objectives appropriate to pure and applied experimental studies, or to pure theoretical studies, are inappropriate here. The following paragraphs outline both familiar objectives that are neglected and less-familiar objectives that are pursued. Appendix A describes these issues in more depth.

a. **Not describing new principles and natural phenomena.** An enormous literature describes new natural phenomena, but this volume describes the implications of known phenomena for new technologies.

b. **Seldom formulating exact physical models.** In analyzing functional systems, estimates should be accurate or conservative, but need not be exact. The goal is to gain a quantitative understanding of the relationship between structure and function, not to formulate exact physical models for their own sakes.

c. **Seldom describing immediate objectives.** Most of the scientific literature discusses either past achievements or objectives achievable using existing techniques. Few publications examine objectives that require substantial preparatory development (space science and high-energy physics produce many of the exceptions). Constructing the physical systems discussed in Chapters 8-14 and 16 , however, is well beyond current capabilities. In this volume, only Chapter 15 describes objectives suited to the constraints of present laboratory technique. Our ability to model has outstripped our ability to make, and these studies exploit that fact to analyze ambitious objectives.

d. **Not portraying specific future developments.** This volume describes systems that can deliver performance orders of magnitude beyond that possible with current technology. Nonetheless, as research in this area expands, better designs will in most instances supersede these systems prior to their realization. Accordingly, they should be regarded not as portrayals of specific future developments, but merely as examples of what can be done.

e. **Seldom seeking an optimal design in the conventional sense.** In mature fields of technology, competitive pressures encourage a search for designs that are nearly optimal. In the exploratory phase of design, however, the more modest goal of workability suffices. A design can depart from optimality either (1) by being overdesigned and inefficient, or (2) by being underdesigned and unreliable. Here, (1) is acceptable, (2) is not.

f. **Seldom specifying complete detail in complex systems.** Given an established technology base, a designer can often describe a system at a high level of abstraction (Section 1.4.2) with confidence that compatible sets of components can be specified before placing the unit into production. This is easier if the product can be overdesigned and inefficient, because margins of safety in the initial design can then compensate for uncertainties in component performance. The approach pursued in this volume amounts to the analytical (as distinct from physical) development of a technology base with capabilities known within some error margins. The later chapters describe systems at various levels of abstraction, likewise using margins of safety to compensate for uncertainties in component performance.g. Favoring false-negative over false-positive errors in analysis. In modeling and analyzing proposed designs, one would ideally distinguish workable from unworkable designs with perfect accuracy. But since models are never exact and accurate, errors of some sort are inevitable. These errors can be of two kinds: False-positive evaluations wrongly accept an unworkable design; falsenegative evaluations wrongly reject a workable design. In exploring a new domain of technology, conclusions regarding the feasibility of systems rest on conclusions regarding the feasibility of subsystems, forming a hierarchical structure of analysis that can have several layers. A substantial rate of false-positive assessments at a subsystem level would make false-positive assessments at the system level quite likely: designs that rely on unworkable subsystems will not work, and may be beyond repair. False-negative assessments, in contrast, are relatively benign. Correcting a false-negative assessment of a rejected subsystem cannot invalidate the analysis of a system whose design omits that subsystem; indeed, correcting this error merely expands the list of workable designs. It is desirable to minimize errors of both kinds, but where uncertainties remain, it is better to bias analytical models and criteria toward safe, false-negative conclusions. This strategy guides the following chapters.

h. **Describing technological systems of novel kinds and capabilities.** The objective of this volume, then, is to provide an analytical framework adequate for designing nanomechanical systems (Chapters 3 to 10), and to begin to exploit that framework by designing systems capable of processing both information (mechanical nanocomputers) and matter (molecular manufacturing systems). A further objective is to show how these systems can be implemented, starting from our present technology base (Chapters 15 and 16). Achieving these objectives can define fruitful goals for experimentation, simulation, and software development, and can provide a better basis for understanding human capabilities and choices in the coming years.

### 1.5. Overview of following chapters

In a work of this length in a new field, the relationship among topics can easily become lost in a mass of detail. This section provides a chapter-by-chapter overview, describing relationships and indicating areas where a detailed analysis merely shows that a simpler analysis is sufficient.

### 1.5.1. Overview of Part I

**Chapter 2** summarizes classical scaling laws for mechanical, electrical, and thermal systems, describing the magnitudes they imply for various physical parameters, and describing where and how these laws break down (requiring the substitution of molecular and quantum mechanical models). These relationships are provided for perspective and as an aid in making preliminary estimates of physical quantities. They are seldom used in later chapters, where most calculations proceed directly from physical principles, rather than from a scaling analysis.

**Chapter 3** provides an overview of molecular and intersurface potential energy functions, describing in some detail the molecular mechanics models that later chapters apply to the description of molecular machines. The concepts developed in this chapter are fundamental to much of what follows, since the potential energy function of a molecular system provides the basis for an essentially complete description of its mechanical properties. Its chief conclusion is that the limitations and inaccuracies of molecular mechanics models, although a serious handicap in solution-phase chemistry, are compatible with the use of these models in designing certain classes of molecular machinery.

**Chapter 4** provides an overview of various models of molecular dynamics and describes the basis for the choice of models made in later chapters. Its chief conclusion is that classical mechanics and classical statistical mechanics, with occasional quantum mechanical corrections, provide an adequate basis for analyzing most molecular mechanical systems operating at ordinary temperatures.

**Chapter 5** examines several classes of mechanical structures and derives relationships that describe the positional uncertainties resulting from the combined effects of quantum mechanics and thermal excitation; later chapters use these results to calculate error rates. This is the most heavily mathematical chapter in the book, but it chiefly concludes that classical statistical mechanics adequately describes the positional uncertainties of nanometer-scale mechanical systems at ordinary temperatures. Only Eq. (5.4) is directly applied in later chapters.

**Chapter 6** examines various processes that cause transitions among ${ }^{\circ}$ potential wells in a nanomechanical system, including transitions that cause errors and structural damage. It describes standard theoretical models used to calculate chemical reaction rates based on potential energy functions; these are applied later in analyzing molecular manufacturing processes. Regarding damaging transitions, the chapter concludes that systems at room temperature can be designed to limit rates of damage caused by thermal, mechanical, and photochemical effects to low enough levels that the overall rate of damage is chiefly determined by the background level of ionizing radiation. Damage caused by radiation imposes major constraints on the design of large systems.

**Chapter 7** examines various processes that degrade mechanical energy into heat, causing frictional losses; among these are acoustic radiation, phonon scattering, shear-reflection drag, phonon viscosity, thermoelastic damping, nonisothermal compression of mobile components, and transitions among potential wells that vary with time. It develops a set of analytical models applied in later chapters to estimate the power dissipated by various nanomechanical devices.

**Chapter 8** compares and contrasts the established capabilities of solution chemistry to those expected from mechanochemical systems, considering speed, efficiency, versatility, and reliability; it also examines an illustrative set of mechanochemical processes in detail. It concludes that a large set of mechanochemical reactions can be made extremely reliable, with error rates $<10^{-15}$. (Although not strictly necessary, this degree of reliability substantially simplifies molecular manufacturing.) It also concludes that mechanochemical processes can be used to construct a wide range of diamondoid structures; this motivates the consideration of diamondoid components in Part II.

- Overall, Part I expends substantial effort in describing physical effects that are of negligible importance in nanomechanical design. In established fields of engineering, training and experience focus attention on the important physical effects; most trivial effects are automatically ignored. In surveying a new field, however, insignificant effects must often be examined before they can be recognized as insignificant.


### 1.5.2. Overview of Part II

**Chapter 9** discusses nanoscale structural components and relates molecular mechanics models to descriptions based on bulk material properties. It develops the concept of a bounded continuum model that omits atomic detail while treating surfaces in a way that takes account of interatomic potentials. It concludes that diamondoid structures are desirable nanoscale components, that bounded continuum models can provide useful preliminary descriptions of component properties, and that a wide range of shapes can be constructed on a nanometer scale, despite the discrete nature of atoms and bonds.

**Chapter 10** uses molecular mechanics models and analytical models developed in Part I to describe the mechanical properties and performance characteristics of active devices such as gears, bearings, and drive mechanisms. It concludes that structures on a several-nanometer scale can serve as mechanical devices of most classes familiar on the macroscopic scale, and that these nanomechanical devices can in many instances move with negligible static friction. Models from Chapter 7 are applied to describe energy dissipation from dynamic friction. The conditions for low-friction motion derived in this chapter are assumed as background in Chapters 11 to 14.

**Chapter 11** describes various subsystems of intermediate size and complexity. These include devices capable of measuring and distinguishing molecular features, stiff drive mechanisms, fluid handling systems (including walls, seals, and vacuum pumps), cooling systems, and electromechanical devices such as motors and actuators. These subsystems and their capabilities are applied or assumed as background in Chapters 12 to 14.

**Chapter 12** describes nanomechanical computer systems. It starts with mechanical digital logic systems, including logic gates, signal transmission channels, registers, and their integration into finite-state machines (with an analysis of thermally induced error rates). It then discusses carry chains, random access memory, tape-based storage, power supplies, clock distribution, information input and output to macroscopic systems, and overall system performance (volume, speed, and power dissipation). Its chief conclusion is that a 1000 MIPS computer can occupy less than one cubic micron and consume less than 0.1 microwatt of power.

**Chapter 13** describes systems for converting impure feedstock solutions into diamondoid molecular objects, using molecular concentration and purification systems, followed by special-purpose mechanochemical systems (molecular mills) capable of performing repetitive operations efficiently, and by generalpurpose mechanochemical systems (i.e., molecular manipulators) capable of performing a complex series of operations under programmable control. A key conclusion is that, after an initial purification and ordering process, molecular assembly can be sufficiently reliable that cycles of inspection and rework to correct failures can be avoided. The conclusions of this chapter are directly exploited in the next.

**Chapter 14** describes molecular manufacturing systems that use purification systems, mills, and manipulators to transform an impure feedstock solution into any one of a large set of macroscopic (kilogram-scale) products within a few thousand seconds. It focuses on systems integration and overall performance, and discusses a range of issues including design complexity and product cost.

- Part II describes diamondoid nanomechanical systems of increasing complexity, ending with a description of molecular manufacturing systems that can build complex diamondoid nanomechanical systems. This supports the nontrivial proposition that molecular manufacturing systems are feasible, given molecular manufacturing systems with which to build them. Part III discusses the implementation of molecular manufacturing systems in the absence of preexisting systems of the same kind. It begins from our present technology base.


### 1.5.3. Overview of Part III

**Chapter 15** describes current capabilities for the design and fabrication of multinanometer scale molecular objects (by chemical and biochemical means) and discusses approaches for combining and extending these capabilities to enable the construction of larger and more complex systems. The major approaches considered are (1) protein engineering, (2) the engineering of proteinlike molecules designed to fold more predictably and stably, and (3) the development of mechanosynthetic systems that make use of atomic force microscope (AFM) technologies. The first two approaches would construct large molecular systems by ${ }^{\circ}$ Brownian assembly (self assembly) of smaller units; the AFM approach would construct them directly from small monomers. This chapter concludes that means can be developed for constructing molecular mechanical systems containing $10^{5}$ monomers, operating in a solution environment.

**Chapter 16** describes a development pathway leading from small molecular mechanical systems operating in solution, through larger and better-isolated systems, to $\sim 100 \mathrm{~nm}$ scale mechanisms able make complex diamondoid structures by means of mechanosynthesis. It proposes the use of externally generated pressure fluctuations to provide power and control to these intermediatetechnology devices, and the use of optically probed, environmentally modulated fluorescent molecules to enable prompt sensing of the results of attempted mechanosynthetic operations. This chapter concludes that accessible (though not necessarily easy) development paths lead from present capabilities to advanced molecular manufacturing.

- Part II begins and ends with long-term technologies, but Part III begins with current technologies. Readers more interested in short-term developments and practical foundations may wish to start with Part III. It is relatively independent of the rest, although it occasionally cites results from previous chapters.


### 1.5.4. Overview of Appendices

**Appendix A** discusses methodologies appropriate to the study of technological possibilities, comparing and contrasting them to the methodologies appropriate to the study of natural phenomena (i.e., standard scientific problems) and to the design of products for immediate implementation (i.e., standard engineering problems).

**Appendix B** discusses related work by other researchers. It returns to the fields of mechanical engineering, microtechnology, chemistry, and molecular biology (adding protein engineering and proximal probe technology), focusing on the work in these fields that has advanced furthest toward engineering complex molecular systems.

### 1.5.5. Open problems

Many chapters end with a discussion of open problems. These range from developing specific examples and analyses to developing major software systems and laboratory research programs. The discussions are not exhaustive, but are intended to highlight useful directions for research.

[^0]: Words appearing in the Glossary are sometimes prefixed with a small circle, e.g., ${ }^{\circ}$ steric.
[^52]: Considering the words in isolation, the terms molecular nanotechnology and molecular manufacturing could instead be interpreted to include much of chemistry, and mechanosynthesis could be interpreted to include substantial portions of enzymology and molecular biology. These established fields, however, are already named; the above terms will serve best if reserved for the fields they have been coined to describe, or for borderline cases that emerge as these fields are developed.
[^1]: D. Cram has introduced the concept of an inner phase to describe the interior of container molecules in which (for example) single, isolated molecules of cyclobutadiene are stable at room temperature because the container walls block intermolecular collisions (Cram et al., 1991). Inner-phase systems prevent collisions; machine-phase systems control them.
[^57]: Product scale, defect rates, and cycle times vary widely from process to process within most of these families; feature scale varies widely within the first two.
[^58]: The defect rate listed for biochemistry corresponds to high-reliability DNA replication processes that include kinetic proofreading (Watson et al., 1987); most biochemical defect rates are higher. All rates are on a per-component basis.
[^2]: The term nanotechnology, first widely used to refer to what is here termed molecular nanotechnology, has since been applied to many small-scale technologies, including conventional microfabrication techniques working in the submicron size range. Accordingly, discussions of the history, status, and prospects of so-called nanotechnology often confuse essentially dissimilar concepts, as if the term ornithology were used to describe the study of flying things, thereby stirring together birds, bats, spacecraft, balloons, and bombers into a single conceptual muddle.
[^3]: It is sometimes suggested that artificial molecular machine systems cannot improve on biological systems because the latter have been shaped by billions of years of evolution. In specific engineering parameters, however, the products of evolution have already been surpassed: graphite composites are stronger than bone, copper is more conductive than axonal cytoplasm, and so forth. Biological systems do, however, excel in their capacity to evolve, and it can be shown that several of their characteristic differences from eutactic nanomechanical systems (including the use of diffusive transport rather than mechanical conveyance) are important to this capacity (Drexler, 1989a).