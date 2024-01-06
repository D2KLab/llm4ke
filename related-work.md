# llm4ke / references & related work

We have an excellent legacy to start from:

* DOREMUS: https://github.com/DOREMUS-ANR/knowledge-base/tree/master/query-examples
* SILKNOW: https://github.com/silknow/converter/tree/master/competency_questions
* Odeuropa: https://github.com/Odeuropa/ontology/tree/master/competency_questions
* NORIA: https://github.com/Orange-OpenSource/noria-ontology/tree/master/cqs

... each of these projects have competency questions nicely phrased with associated SPARQL queries!

## Related work (20234-01-05)

Method to find the below related work:

> search for "competency question" on Github, https://github.com/search?q=competency+question&type=repositories and manually inspect the 51 results.

### Ref

* "Insights from the KCL LLM Knowledge Prompting Hack Event 2023": https://datalanguage.com/blog/insights-from-kcl-llm-knowledge-graph-prompting-hack-event-2023 that @Youssra REBBOUD and @Youri Peskine attended
* "Knowledge Engineering Using Large Language Models" by Bradley P. Allen , Lise Stork , Paul Groth. https://drops.dagstuhl.de/entities/document/10.4230/TGDK.1.1.3 (with 120 relevant references!)

### Ref

* CLaRO: https://github.com/mkeet/CLaRO (Competency question Language for specifying Requirements for an Ontology) ... arxiv from 2018 and 2 papers published in 2019 and 2021
* Dataset: https://github.com/CQ2SPARQLOWL/Dataset ... interesting as they collected 234 CQ from 5 ontologies and abstracted them into 106 patterns
    - Software Ontology (SWO)
    - Stuff Ontology (Stuff)
    - African Wildlife Ontology (AWO)
    - Dementia Ambient Care Ontology (Dem@Care)
    - Ontology of Datatypes (OntoDT)
* Paper: https://arxiv.org/abs/1811.09529
* Paper: https://link.springer.com/chapter/10.1007/978-3-031-47745-4_16

### Ref

* "A framework for LM-assisted ontology engineering based on competency questions", from our Polifonia friends, https://polifonia-project.github.io/idea/
* The CQ dataset from Polifonia is at https://polifonia-project.github.io/idea/competency-questions/polifoniacq-dataset ... it could be compared with the one from DOREMUS

### Ref

* SeeQuery: An Automatic Method for Recommending Translations of Ontology Competency Questions into SPARQL-OWL, https://dl.acm.org/doi/10.1145/3459637.3482387 (CIKM 2021)
* Github: https://github.com/dwisniewski/SeeQuery
  - It makes use of https://github.com/CQ2SPARQLOWL/Dataset (see CLaRO above)
  - It makes use of https://github.com/dwisniewski/BigCQ (a big synthetic dataset of CQ templates to SPARQL-OWL templates mappings)

### Ref

* "A Tagger for Glossary of Terms Extraction from Ontology Competency Questions", https://link.springer.com/chapter/10.1007/978-3-030-32327-1_36 (ESWC 2019 Poster paper)
* Gitub: https://github.com/dwisniewski/CRFBasedGlossaryOfTermsExtraction

### Ref

* Tiny dataset: https://github.com/nikhilgowda123/SpotifyKG ... 10 CQ about Music (Spotify KG) ... can also be merged with DOREMUS and Polifonia
