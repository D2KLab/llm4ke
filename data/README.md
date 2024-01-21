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
      cqs:
        source: <CQSDownloadURL|CQSCommitURL>
```

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

### Notes on transforming native CQs to YAML

#### For *[awo](./awo)*, *[DemCare](./DemCare)*, *[ontodt](./ontodt)*, *[stuff](./stuff)* and *[swo](./swo)*

* We extract parts of the original `CQs only Dataset.csv` file related to each ontology
* From the resulting parts, we map the columns to the above YAML structure as follows:
  * `ID` => `ID`
  * `CQ` => `question`

For example, for *ontodt*:

```
demcare_106,What are the possible types of fixed sensors?
demcare_107,What are the possible types processing components?
,
,
,
Ontology name:,OntoDT
URI: ,http://ontodm.com/ontodt/OntoDT.owl
Publication:,"P.Panov, L.N.Soldatova, S.Dzeroski,Generic ontology of datatypes, Inf. Sci. 329 (C) (2016) 900 920. doi:10.1016/j.ins.2015.08.006. URL https://doi.org/10.1016/j.ins.2015.08.006"
CQs URI:,http://www.ontodm.com/doku.php?id=ontodt
Comments,dematerialised components highlighted
ID,CQ
ontodt_01,What is the set of characterizing operations for [a datatype X]?
ontodt_02,What is the set of datatype qualities for [a datatype X]?
```

... we extract rows starting with `ontodt_` and mapped them to:

```yaml
---
ontology:
  name: ontodt
  cqs:
    - ID: ontodt_01
      question: What is the set of characterizing operations for [a datatype X]?
    - ID: ontodt_02
      question: What is the set of datatype qualities for [a datatype X]?
```

#### For *[DOREMUS](./DOREMUS)*, *[Odeuropa](./Odeuropa)* and *[SILKNOW](./SILKNOW)*

* We parse the content of the ontologies' companion *README.md* file where CQs are listed
* For each competency question, we map the data as follows:
  * `**[<language>]** <question>` => `question`. For questions were two or more translations are available, we select the *en* version of the competency question. 
  * `[query](./<query_file_name>.rq)` => `rq`
  * `## <question group>` => `group`

For example, for *SILKNOW*:

```
## A. Location
1. **[en]** Which items were produced in Spain? [query](./A1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct++%3Ftitle+%3Fcollection+%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A++++++%3Fs+a+ecrm%3AE12_Production+.%0D%0A++++++%3Fs+ecrm%3AP108_has_produced+%3Fobject.%0D%0A++++%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%0D%0A+%7B+%3Fs+ecrm%3AP8_took_place_on_or_within+%3Flocation+FILTER%28isIRI%28%3Flocation%29%29%0D%0A%0D%0A++++%3Flocation+geonames%3AcountryCode+%22ES%22++%7D%0D%0A++++%0D%0A%0D%0A%0D%0A%0D%0A%7D%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)
```

... we mapped rows to:

```yaml
ontology:
  name: SILKNOW
  cqs:
    - ID: <CQId>
      question: Which items were produced in Spain?
      group: A. Location
      rq:
        - A1.rq
```

#### For *[noria-o](./noria-o)*

* We filter and rename keys of the original YAML file with the competency questions:
  * `Question` => `question`
  * `Evaluation.query` => `rq`

#### For *[Polifonia](./Polifonia)*

* We process the *cq_sanity_checks.csv* file by extrzacting parts of the document conform to CSV syntax.
* For each row, we map the columns as follows:
  * `persona,story,id` => `ID`
  * `cq` => `question`. For questions with the `to-split` tag (*issues* column), we concatenate all questions in a single `question` key.
  * Inner comments => `group`

For example:

```
Ortenz,2_MusicalSocialNetwork,CQ4,"What is the provenance of the event attendees? What and how they happened to be there?

* Did they travel to reach the place?
* Where they invited? Was the meeting accidental?","['to-split', 'complex', 'hard']"
```

... is mapped to:

```yaml
---
ontology:
  name: Polifonia
  cqs:
    - ID: Ortenz,2_MusicalSocialNetwork,CQ4
      question: What is the provenance of the event attendees? What and how they happened to be there? Did they travel to reach the place? Where they invited? Was the meeting accidental?
      group: default
```

## Remarks

- The [CLaRO](https://github.com/mkeet/CLaRO) ontology set required adding [shared/time.owl](shared%2Ftime.owl) as several CLaRO ontologies are referencing it. Download from commit [57a5bd2](https://github.com/CQ2SPARQLOWL/Dataset/commit/57a5bd2ab66c8a40041af6e20cb965bd69766496).
- Polifonia
  - is a network of ontologies => potential need to merge them into a single file.
  - Where are the queries shared?
- SILKNOW looks more like KG rather than an ontology => what should we download?
