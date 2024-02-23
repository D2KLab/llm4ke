# llm4ke

Repository for Large Language Models for Knowledge Engineering

## Objectives

Original idea:

> How much LLM could co-contribute in the knowledge engineering process together with our usual methodology (competency
> questions, ontology re-use, authoring tests, etc.).

Set of questions we could investigate:

1. Could a LLM reverse engineer an ontology and find out what good competency questions could be derived?
2. Could a LLM take as input the CQ and generate parts of the ontology?
3. Could a LLM take as input the CQ and extend an existing ontology?
4. Could a LLM take as input the CQ and generate abstract patterns?
5. Could a LLM write an authoring test (a SPARQL query) given the ontology and the CQ?
6. Given a dataset and an ontology, is an LLM able to generate an adequate set of RML rules for data ingestion?
7. Could a LLM take as input the CQ and extend an existing ontology?

## Usage

See the *Repository Structure* for navigating into this repository:

```
llm4ke
├───data <Reference data models with their related components>
│   └─[DataModelName]
│     ├─dm <data model implementation>
│     ├─rq <set of queries>
│     └─...
├───src <Processing pipeline code>
└───...
```

### Generating Competency Questions

We will now address the research question "*1. Could a LLM reverse engineer an ontology and identify potential competency questions?*" mentioned above.

The pipeline uses [LangChain](https://www.langchain.com/), and in particular [Ollama](https://ollama.ai/).

* Install Ollama from its [website](https://ollama.ai/download).
* Install requirements
  ```shell
  pip install -r requirements.txt
  ```
* Download the desidered LLM ([full list of available LLMs](https://ollama.ai/library))
  ```shell
  ollama pull llama2
  ```
* Run the pipeline to generate Competency Questions for a given ontology
  ```shell
  # Canonical form:
  # python src/main.py <task> --name <OntologyName> --input <OntologyFolder> --llm <ModelName>
  
  # Basic example for the Odeuropa ontology:
  python src/main.py all_classes --name Odeuropa --input ./data/Odeuropa/ --llm llama2
  ```
  Then browse the results in the `out/Odeuropa/` directory.
  You can get the full list of available parameters with `python src/main.py --help`

### Evaluating the LLM's Competency Questions 

With the output data from the above *Generating Competency Questions* step,

* Run the evaluation pipeline to compute similarity scores for all ontologies or a given ontology
  ```shell
  # Canonical form:
  # python src/eval.py <all|OntologyName>
  
  # Basic example for the Odeuropa ontology with a 0.8 similarity threshold and verbose logging:
  python3 ./src/eval.py Odeuropa -t 0.8 --log 10
  ```
  Then browse the results in the `./results_<all|OntologyName>.json/` file.

## Copyright

Copyright (c) 2023, EURECOM. All rights reserved.

## License

[Apache](LICENSE).

## Maintainer

* [Raphaël TRONCY](mailto:raphael.troncy@eurecom.fr)
* [Pasquale LISENA](mailto:pasquale.lisena@eurecom.fr)
* [Youssra REBBOUD](mailto:Youssra.Rebboud@eurecom.fr)
* [Lionel TAILHARDAT](mailto:lionel.tailhardat@orange.com)
