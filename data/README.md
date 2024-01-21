# llm4ke / data

This folder contains an implementation of the ontologies that are the focus of the research project.
It is intended to be used as a reference for experimentation.
Additionally, it includes a set of competency questions (CQs) and evaluation queries (SPARQL queries) that are related to these ontologies.

The file [dm-rdf.yml](dm-rdf.yml) lists the ontologies and their respective origins.
The canonical structure of this file is as follows:

```yaml
---
ontologies:
    - name: <ProjectName>
      group: <ProjectGroupName>
      dm:
        source: <DataModelDownloadURL|DataModelCommitURL>
      rq:
        source: <QueriesDownloadURL|QueriesCommitURL>
```

## Remarks

- The [CLaRO](https://github.com/mkeet/CLaRO) ontology set required adding [shared/time.owl](shared%2Ftime.owl) as several CLaRO ontologies are referencing it. Download from commit [57a5bd2](https://github.com/CQ2SPARQLOWL/Dataset/commit/57a5bd2ab66c8a40041af6e20cb965bd69766496).
- Polifonia
  - is a network of ontologies => potential need to merge them into a single file.
  - Where are the queries shared?
- SILKNOW looks more like KG rather than an ontology => what should we download?

## Competency questions (CQs)

For each ontology, we provide a `./<ProjectName>/cqs/cqs.yml` file for standard representation of the CQs based on the original set of competency questions brought with the ontology implementation.

The canonical structure of this file is as follows:

```yaml
---
ontology:
  name: <ProjectName>
  cqs:
    - ID: <CQId>
      question: <CQ>
      [group: <CQGroup>]
      [rq:
        - <QueryFileName>.rq]
    
```
