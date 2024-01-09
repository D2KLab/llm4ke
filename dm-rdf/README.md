# llm4ke / dm-rdf

This folder contains a copy of the implementation of the ontologies targeted by the research project to serve as a reference for experimentation.
The file [dm-rdf.yml](dm-rdf.yml) lists the ontologies and their origin.

## Remarks

- The [CLaRO](https://github.com/mkeet/CLaRO) ontology set required adding [shared/time.owl](shared%2Ftime.owl) as several CLaRO ontologies are referencing it. Download from commit [57a5bd2](https://github.com/CQ2SPARQLOWL/Dataset/commit/57a5bd2ab66c8a40041af6e20cb965bd69766496).
- Polifonia is a network of ontologies => potential need to merge them into a single file.
- SILKNOW looks more like KG rather than an ontology => what should we download? 