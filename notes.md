# Vorlesungsnotizen

## Fr, 06.03., 15:00 - Führung durchs Stadtarchiv, Bibliothek Bielefeld
- Herr Tieli verkauft Grundstück, erste Eintragung im Archiv
- 1782 wird Philipp Gehring als Räuber gerichtet und erhängt
- zeit.nrw:Archiv-Suche mit Volltext-Suche
- Jakob Dietrich Kohlbaum, 2 mal Bürgermeister in Bielefeld, falsch eingeschätzt



## Mi, 14.01., 08:15 - Grundlagen der Genomforschung (V)

- Kegg Pathway Database
- Metabolome, pmdb.org.cn, chin. DB, Gifte
- Digitoxin, senkt d. Blutdruck, beruhigt d. Herz
- Enzyme, Genome, DNA, Chromosome
- Proteine werden gebunden
- Systembiologie, Enzymatische Reaktionen
- Wie viele "3-Phospat" i. d. Zellkultur? mol/l, Mole
- Moleküle, Graphen



## Di, 18.11., 15:45 - Automatisierungstechnik (V)

- Autonome deterministische Automaten
- Matrixmultiplikation für Zustandssimulation
- Beschreibung durch boolesche Funktion



## Mo, 17.11., 15:30 - Rechnerarchitektur (V)

- Prinzipielle Struktur des Bussystems und Busse
- Bustaktung, Quelle: Tanenbaum 2004
- Synchroner Bus und Speicherzugriff



## Fr, 24.10., 12:15 - Parallel and Distributed Computing (V)

- Was ist ein Parallelrechner, was ist ein Vektorrechner?
- **Cray-1**: brach alle Geschwindigkeitsrekorde, gewann Schachweltmeisterschaften, Nachfolger Cray-2
- **64 Bit Rechner**: Acht 8 Bit Operationen werden gleichzeitig ausgeführt, mit 8 Bit CPU
- **Pipelining**: instruction pipelining, d.h., CPU führt eine Operation pro Takt aus
  - Genauer: ein Maschinenbefehl (12 ADD $64 [REG]) braucht mehrere Prozessoroperationen/-zyklen:
    - Fetch (Befehl lesen)
    - Decode
    - Execute
    - Write (Ergebnis ins Register)
- **Idee**: Parallelisiere diese Operationen, beachte Probleme



## Fr, 24.10., 10:15 - Mathematik für Wirtschaftswissenschaften (V)

- Aussagenlogik
- Beweis von de Morgan: Negation, Äquivalenz
- Umformungsregeln, Implikation, Äquivalenz
- Distributivgesetz, Kontraposition



## Do, 23.10., 16:15 - Einführung in die Informatik (V)

- Binärzahlen, 11111
- Mit 5 Stellen lassen sich 32 Zahlen darstellen aber die höchste Zahl ist 31
- Substraktionsmethode, Divisionsmethode, erstere ist natürlich



## Do, 23.10., 12:30 - Entwurf mikroelektronischer Systeme (Ü)

- Zu zweit am Rechner
- Netboot, Fernsteuerung von zu Hause
- Aufgaben sind im Lernraum
- Wie ist der Weg zum eigenen Chip?
- Rekonfigurierbare und parallele Rechnersysteme (VHDL)
- Xilinx Vivado
- `.xdc-file` is Xilinx design constraints



## Do, 23.10., 10:15 - Entwurf mikroelektronischer Systeme (V)

- Intel startete als Speicher-, nicht CPU-Chip Hersteller
- **Moore's Law** scheint geheuchelt, unglaubwürdig, dass dieser komplexe Herstellungsprozess in seinem Potenzial so noch nicht absehbar war
- **Transistorgrößen-Entwicklung**:
  - 1971: 10μm
  - 1974: 6μm
  - 1978: 3μm
  - 1982: 1,5μm
  - 1999: 250nm
  - 2008: 45nm (Core i7, Bloomfield)
  - 2017: 14nm (Skylake)
- ASICs Entwurf konservativ, never change running ASIC
- HDL beschreibt, welche Bauteile und PINs der HW wie genutzt werden
- 100% Coverage schwierig bei HDL-Verhalten
- Theorie der Coverage, Testklassen
- Teilnahme V, Ü: jhagemey@cit-ec.uni-bielefeld.de



## Mi, 22.10., 10:15-11:00 - Random Graphs (V)

- Graphs, vertices, edges, degree of vertices
- Graphs and their degree and connectivity structure
- Friends in a random friendship



## Mi, 22.10., 8:45 - Daten & Zufall (V)

- Experiment: Augensumme
- Elementares Ereignis aus Omega
- Verwende die Gleichverteilung, wenn Symmetrieeigenschafte(n) vorliegen



## Di, 21.10., 14:45 - Formale Logik (V)

- Characteristics of simple logic formulas
- Replacement theorem, proof of
- We can proof by structural logic induction
- Normal forms, conjunctive normal forms
- CNF, DNF, truth tables, examples



## Di, 21.10., 10:15 - Introduction to Natural Language Processing (V)

- **Aim of Machine Learning (ML)**: Increase efficient solvability of complex tasks
- **ML Pipeline phases**: Data acquisition, training, deployment, action
- **Fitting**: Underfit, best fit, overfit for limited training data
  - Best fit: keep a little error deviation for generic answers
- **Classification** (yes/no) vs. **regression** (%)



## Di, 21.10., 08:30 - Autonome Robotermanipulation (V)

- Lage im Raum durch lineare Abbildung
- **Passive View**: Nur ein Punkt p
- **Active View**: Zwei Punkte bei Verschiebung in anderes Koordinatensystem
- Transformation durch Matrizen, Determinanten und Inverse von Matrizen
- Nutze drei Eulerwinkel und drei Achsen x, y, z
- Eule, Euler und R, Matrix R, Rotation, Drehung



## Mo, 20.10., 16:15 - Grundlagen des Software Engineering, 5LP (Ü)

### Tools
- **Android Studio**: Google IDE für Android (IntelliJ IDEA Community Edition)
- **Artemis**: Bewertung von Programmier-, Text- und Modellierungsaufgaben, Apollon für UML
- **Python**: Visual Studio Code oder PyCharm Community Edition

### IT-Infrastruktur & Orga
- Git push mit Syntax-Fehler nicht erlaubt
- Für jeden Meilenstein ein neues Repository
- Keine durchgängige MacBook-Unterstützung
- Pro Woche 5 bis 6 Stunden, mit Übungen mehr, mehr als 5 LP



## Fr, 17.10., 14:00 - Funktionentheorie (V)

- Komplexe Differenzierbarkeit
- Stetigkeit, offene Urmengen und Abbildungen
- Urmengen sind wichtig für andere Definitionen
- Es werden Definitionen definiert für andere Definitionen im Kontext der anderen Definitionen
- Allgemein betrachtet können solche Definitionen dadurch Schwächen haben
- Abbildungen, Urbilder, Bilder in der Algebra, aber Funktionen, Differenzierbarkeit in der Analysis



## Fr, 17.10. - Daten & Zahlen (V)

- Ereignisse, Wahrscheinlichkeitsraum
- Omega ist endlich od. abzählbar unendlich
- Wurf eines Würfels, Betrachte d. Augensumme
- Elementarereignisse
- Schnitt und Vereinigung von Ereignissen



## Fr, 17.10., 08:35-09:05 - Stochastic Analysis II (V)

- Mehr informal, präziser als Wald v. Definitionen
- Theoretiker wetteifern in der Theorie in dahingegebener Weise, besonders China
- Kolmogov Kontinuitätskriterium



## Do, 16.10., 16:15 - Einführung in die Informatik I (V)

- Einführung für Medienwissenschaft
- Klausur kann beliebig oft wiederholt werden, Studierende haben dafür gekämpft
- Daten, Informationen, Wissen
- Digitalisierung von analogen Signalen, Membran
- Idee: Verwende Trommelfell von der Katze



## Do, 16.10., 14:15-15:15 - Kollaborative Robotik (V)

- Wie kollaboriere ich mit Robotern?
- Robot vs. Cobot nach VDI
- Kognitive Roboter
- Wir müssen mathematisch beweisen können, dass keine Probleme bei AI Robotern auftreten?!
- Geschichte der kollaborativen Roboter



## Do, 16.10., 10:30-11:15 - Grundlagen der Statistik (V)

- Satz der totalen Wahrscheinlichkeit
- Satz von Bayes
- **Beispiel Brustkrebs**: 10% der Frauen haben nur Brustkrebs, wenn die Diagnose Brustkrebs ist, bei 1% Brustkrebs aller Frauen (Testsicherheit, TS). Wenn mehr als 1% der Frauen Brustkrebs haben, dann soll die TS steigen?
- Zufallsvariablen im Wahrscheinlichkeitsraum
- Diskrete und Kontinuierliche Zufallsvariable



## Do, 16.10., 8:30-09:45 - Statistische Datenanalyse mit R (V + Ü)

- Länge, Variationsbreite, Arithmetische Mittelwert mittelt über alle Werte
- Median mittelt über die Verteilung der Werte (50% d. Werte links und 50% d. Werte rechts), Median liegt bei 29
- Leerzeichen in R beachten
- Anwendungsdomäne ist Statistik, z.B. für `hist`
- Relative und Kumulative Wahrscheinlichkeit
- Mittelwert über Gruppen wird gewichtet
- R ist objektorientiert, auch Zahlen sind Objekte
- Hilfe mit `help(...)`



## Di, 14.10., 10:28-11:15 - Data Science in der Biologie (Ü + S)

- Python oder R, Python hat sich durchgesetzt
- Python wird interpretiert, R auch
- In der Wissenschaft/Biologie werden Python und R zusammen und isoliert verwendet
  - Python liefert Tabellen für R
  - R verwendet Tabellen für Statistik
- JupyterLab für Python
- Befehl: `whos` zeigt Übersicht der Variablen an



## Mo, 13.10., 12:45 - Algebraische Graphentheorie (V)

- Definition of a graph, Isomorphism
- **Problem**: Check whether two graphs are isomorph
- **Idee**: Lineare Laufzeit in V: Knotenzahl gleich?
  - Ja, dann finde die Strukturüberdeckung, wo der Knotengrad am besten passt
  - Prüfe die Strukturbeziehung: (a) kleiner, (b) gleich, (c) größer
  - Es kann bei gleicher Knotenanzahl nicht mehr Strukturbeziehungen geben als (a), (b), (c)
  - Bei ungleicher Knotenanzahl gibt es keine Strukturbeziehung



## Mo, 13.10., 12:15 - Data Mining (V)

- **Idea**: Observable data vs latent/hidden pattern
  - Beispiel: sound wave from .mp3 vs music sheet author
  - Beispiel: projected tree image vs tree from photo
- **Autoencoder perspective**:
  - From a photo with a tree, compress the photo with "algorithms" (encoding)
  - Get compressed data
  - Project photo again with the compressed data (decode)
  - Obtain tree image with less quality but with en- and decoding, i.e., autoencoding



## Mo, 13.10., 10:00 - Advanced Statistics in R (V + Ü)

**Statistics is learning from data**

### Steps:
1. Data collection
2. Model fitting for data
3. Interprete the model

### Models:
- Uniform distribution in R
- Normal distribution in R
- Poisson distribution in R
- Binomial distribution in R
- Geometric distribution as shown above

### Tools:
- R-Markdown, Plot PDF, R-Studio
- S before R, R implemented in C
- Foto: 11:08 Uhr, Randomized Algorithms in P, "66"



## Fr, 18.07., 14:00 - Mathematische Biologie (V)

- Statistik- und Hypothesentest
- **Stochastik**: das Beschäftigen mit Zufallsexperimenten
  - A) W'keitstheorie
  - B) Statistik

### A) Wahrscheinlichkeitstheorie
- Zufallsvariable, suchen Verteilung, Parameter gegeben (W'keit, ein Baum ist krank, p)
- Also geometrische Verteilung: `(1-p)^{k-1}p`

### B) Statistik
- Hier: Verteilung gegeben, suchen Parameter (W'keiten), an Hand von Schätzverfahren oder Hypothesentests

### Beispiele:
- **a) Bäume**: Die W'keit, dass wir k gesunde Bäume sehen bis wir den ersten kranken Baum sehen, sie nimmt ab je größer k wird
- **b) Tasks**: Die W'keit, dass wir k gesunde Tasks sehen bis wir die erste kranke Task sehen, sie nimmt ab je größer k wird
  - Falls p=0.1, dann ist:
    - k=1: p=0.1
    - k=2: p=0.09
    - k=3: p=0.0081
  - Der Erwartungswert E ist E=1/p, also 10
  - Das heißt erst 10 gesunde Tasks und erst die 11. Task blockiert



## Fr, 27.06., 14:00 - Algorithmic Cheminformatics (V)

- **Wiener Index** löst das Problem paarweise, die kürzesten Pfade finden
- Ist der Wiener Index hoch (Summe der oberen Dreiecksmatrix), ist auch der Siedepunkt hoch
- **Hoher Siedepunkt** bedeutet: es braucht viel Energie, um die Moleküle voneinander zu trennen
- **Siedepunkt** (auch Siedetemperatur): die Temperatur, bei der eine Flüssigkeit in den gasförmigen Zustand übergeht, also siedet
