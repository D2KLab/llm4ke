# llm4ke

Repository for Large Language Models for Knowledge Engineering

## Objectives

Original idea:

> How much LLM could co-contribute in the knowledge engineering process together with our usual methodology (competency questions, ontology re-use, authoring tests, etc.).

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
├───dm-rdf <Reference data models & ...>
└───...
```

The pipeline uses [LangChain](https://www.langchain.com/), and in particular [Ollama](https://ollama.ai/).

* Install Ollama from its [website](https://ollama.ai/download).
* Install requirements `pip install -r requirements.txt`
* Download the desidered LLM `ollama pull llama2` ([full list of available LLMs](https://ollama.ai/library))
* Run it with ` python src/main.py generate_cqs -i ./dm-rdf/Odeuropa/odeuropa-ontology.owl`

## Copyright

Copyright (c) 2023, EURECOM. All rights reserved.

## License

[Apache](LICENSE).

## Maintainer

* [Raphaël TRONCY](mailto:raphael.troncy@eurecom.fr)
* [Pasquale LISENA](mailto:pasquale.lisena@eurecom.fr)
* [Lionel TAILHARDAT](mailto:lionel.tailhardat@orange.com)
