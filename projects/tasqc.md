# TASQC (Timing Authentication Secured by Quantum Correlations)

- Official page: OSTI software record https://www.osti.gov/biblio/1339958 ("TASQC Quantum Key Transfer Program", 2016-11-04, research org ORNL, sponsor USDOE) [KNOWN: OSTI records API, accessed 2026-10-24]
- Repo: https://github.com/ORNL/TASQC [KNOWN]
- Docs: the top README, `keyTransferClient/README.md` and a Maven site page `src/site/markdown/index.md` [KNOWN: repo tree]
- License: BSD-style 3-clause, copyright 2015 UT-Battelle (`LICENSE`; the same header is in each source file) [KNOWN]
- Status: unknown (last push 2019-05-21; not archived) [KNOWN: GitHub API, accessed 2026-10-24]

## Walkthrough
TASQC is the software half of a research idea: use quantum physics to make the power grid's clocks harder to fake. [KNOWN: repo title; OSTI description, paraphrased]
The problem: grid sensors stamp their readings with GPS time so operators can line them up. If an attacker spoofs the timing signal, the readings stop lining up and protection systems can make bad calls. Proving that a timing signal really came from the right sender needs shared secret keys. [INFERRED: standard background for grid timing; the OSTI record ties the work to secure timing for the grid]
What goes in: a file of secret key bits produced by quantum key distribution (QKD) hardware. QKD is a way for two sites to build a shared random key by sending single photons, and physics makes eavesdropping detectable. The default file is `SecretKey.log`, or one "0" or "1" per line in BitPerLine mode. [KNOWN: README "Properties"; QKD definition is standard background]
What happens: a small Java web server reads those bits into a queue and hands out the next key over HTTP at `/keys`. A C++ client library fetches keys for programs that need them, which the client README says are GNU Radio programs (software-defined radio). [KNOWN: `KeyResource.java`, `QuantumKeyContext.java`, client README]
What comes out: JSON with a key id and key value, plus a local record of handed-out keys in `keyDB.txt`. [KNOWN: `KeyTransLauncher.java`, `QuantumKeyContext.java`]
Where humans act: someone runs the QKD hardware, starts the server and points the radio software at it. [INFERRED]
What it is not: not the quantum hardware, and not the timing-authentication math itself. It's only the plumbing that moves quantum-made keys to the programs that use them. [KNOWN: repo contents]
Example: a GNU Radio program asks `http://localhost:8080/keys?authKey=...` for a key, gets `{"id": 7, "key": "0110..."}`, and uses it to sign a timing message. (The URL shape comes from the code; the JSON values are illustrative.)
Unknown: whether it was ever tested on a live grid link, and what the hardware setup was.

## What it is (plain English, 2-4 sentences)
A research prototype key server from 2015-2017. It takes the secret bits a quantum key distribution system produces and serves them to other software over a simple web API. It comes with a C++ client library meant for radio software. [KNOWN: README, client README, OSTI record]

## How it works (plain English, no jargon without definition)
1. Load keys: `QuantumKeyContext` reads the key file into an in-memory queue holding up to 1,024 keys by default (`queueSize` changes it). [KNOWN: `QuantumKeyContext.java` lines 74, 162-201]
2. Serve: Jersey (a Java library for web APIs) running on the Grizzly HTTP server answers `GET /keys` with the next key as JSON. A `keyId` parameter fetches a specific key instead. [KNOWN: `KeyResource.java` `@Path("keys")`, `getNextKey`]
3. "Authentication": the server only checks that an `authKey` parameter is present, not what its value is. Any value gets a key. [KNOWN: `KeyResource.java` line 111, `if (authKey != null)`]
4. Client: the C++ `KeyService` defaults to `localhost:8080`, sends placeholder credentials `"user"`/`"password"`, and has a flag that switches off TLS certificate checking. [KNOWN: `KeyService.cpp` lines 45, 85, 108; `LibcurlUtils.cpp` lines 86-90]
5. Extras: `cmwc.cpp` and `cmwc-streaming.cpp` are test programs for a complementary-multiply-with-carry random number generator, a fast non-quantum generator. [KNOWN: file names and code] Their role in the project is UNKNOWN.

For a security student, steps 3 and 4 are the lesson: this is lab plumbing, written to run on one trusted machine, not hardened for a network. [INFERRED from the defaults; no source calls it production]

## How the project is organized
- Layout: `gov.ornl.tasqc.keytrans/` (the Java server: 5 classes, 3 JUnit tests, `pom.xml`, `config.properties`, Eclipse project files) and `keyTransferClient/` (the C++ client: `libcurlUtil/` with `KeyService`, `LibcurlUtils`, an `HTTPInterface`, an error logger, its own `CMakeLists.txt` and a `tests/` folder with a fake HTTP layer). [KNOWN: repo tree]
- Languages and build: Java 7 with Maven (`mvn package shade:shade` builds a single runnable jar), and C++ with CMake and libcurl. [KNOWN: README]
- Tests: JUnit for the server; C++ tests with a fake curl layer for the client. No CI. [KNOWN: repo tree]
- Contributors: 4 counting anonymous authors, 2 accounts. Source headers name the authors; they aren't repeated here. [KNOWN: GitHub contributors API; headers]
- History: the first commit (2016-10-06) is a stub "Initial commit"; the second, on 2017-02-03, says the code was imported from an older repository with no history (corrected in a fact-check pass, 2026-10-29). The README's clone link points at ORNL's internal-looking GitLab host, which this team doesn't follow. [KNOWN: git log; README]
- Releases: none. [KNOWN]
- Why it was built this way: UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2015 | copyright year in license and headers | `LICENSE` | [KNOWN] |
| 2016-10-06 | GitHub repo created | GitHub API | [KNOWN] |
| 2016-11-04 | OSTI software record 1339958 | https://www.osti.gov/biblio/1339958 | [KNOWN] |
| 2017-02-03 | "Initial import from old repository. No history." | git log | [KNOWN] |
| 2017 | 11 commits | git log | [KNOWN] |
| 2019-05-21 | last push (2 commits in 2019) | GitHub API; git log | [KNOWN] |

## Who uses it / why it matters
No outside users or forks with new work found; 2 stars, 4 forks, 1 open issue. [KNOWN: GitHub API, 2026-10-24] It matters as an early public trace of ORNL's quantum networking work for the grid, a topic ORNL kept working on after this repo went quiet. [INFERRED: the later work isn't sourced in this brief; see connections/map.md]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| GNU Radio | intended client (outside project) | `keyTransferClient/README.md` | [KNOWN] |
| [GridKit](gridkit.md) / power grid | related topic (grid timing); map link 68 | https://github.com/ORNL/TASQC | [INFERRED] |
| CPAD (catalog entry, no brief) | related topic (cyber-physical security); map link 88 | OSTI 1396084 | [INFERRED] |

## What stands out
The "quantum" part lives entirely in hardware that isn't in the repo. What's public is ordinary web plumbing, and its security defaults (any auth value accepted, a switch to skip certificate checks, placeholder passwords) show it was a bench prototype. That's a fair, concrete example of the gap between a research demo and something you'd put on a grid network.

## Ten questions (GOAL.md)
1. Problem and audience: delivering quantum-made keys for authenticating grid timing signals, for researchers. [KNOWN: OSTI, README title]
2. Place in the tree: cyber and grid security with quantum communication. Which division owns it is UNKNOWN.
3. Who pays: OSTI says USDOE with no program office, so the specific program is UNKNOWN.
4. Code: a Java/Maven/Jersey server and a C++/CMake/libcurl client. [KNOWN]
5. Alive: no, nothing since 2019. [KNOWN]
6. Outside users: none found. [UNKNOWN]
7. Connections: upstream QKD hardware output files; downstream GNU Radio programs. [KNOWN]
8. What it teaches: ORNL published even small prototypes under BSD terms and registered them on OSTI. [KNOWN]
9. Student path: a good one for a security student. Build the server with an old JDK, feed it a fake key file and see the authKey check for yourself, on your own machine only. Java 7 is long out of support, so expect to bump the build. [INFERRED; not run]
10. Still unknown: the hardware, any field test and later versions. Searched without result: other public repos by this name.

## Known / Inferred / Unknown
- KNOWN: the OSTI record, license, layout, API behavior, client defaults and history.
- INFERRED: the grid-timing threat background and the prototype-not-production reading.
- UNKNOWN: field testing, funding program and successors.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.osti.gov/biblio/1339958, OSTI "TASQC Quantum Key Transfer Program", accessed 2026-10-24, supports the date, ORNL, USDOE and purpose
- https://github.com/ORNL/TASQC, the repo (README, LICENSE, Java and C++ sources), accessed 2026-10-28, supports the code facts
- https://api.github.com/repos/ORNL/TASQC, repo metadata, accessed 2026-10-24, supports dates, stars, forks and issues

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Confirmed by reading the public source only (nothing was run, and no host was contacted): the server's key handler only checks that an `authKey` value is present (`KeyResource.java`, the `authKey != null` branch), so any value is accepted. The client's localhost:8080 default, placeholder credentials and a TLS-verification switch are in `KeyService.cpp` and `LibcurlUtils.cpp`. The 1,024-key default queue is in `QuantumKeyContext.java`. The brief describes these as design traits of a 2015-2017 research prototype, which fits RULES 16; no wording changes needed.
- Also verified: UT-Battelle 2015 BSD-style LICENSE (GitHub shows NOASSERTION); created 2016-10-06; last push 2019-05-21; not archived; OSTI 1339958 title, date 2016-11-04 and software type.
- Map links 68 and 88 are INFERRED domain links and still accurate.

### Second pass (2026-10-29)
- Re-verified on the fresh clone: commit history (1 commit in 2016, 11 in 2017, 2 in 2019, the same by author and committer date, all branches); corrected which commit is the import. The authKey wording stays a neutral design observation; the student path keeps testing on your own machine only. The README's clone link to an ORNL-hosted GitLab is mentioned but not followed (RULES 16).
