Competency Questions
=====================

This folder contains the competency questions (CQ) collected in the context of [the Odeuropa project](https://odeuropa.eu/) for realising and validating the Odeuropa Data Model. Those questions have been defined by domain expert at the beginning of the project.

Each CQ has been translated in SPARQL, following the Odeuropa model. Some questions can need some external knowledge (e.g. connection with other KG, such as Wikidata) or some more complex AI technique (which has been made explicit for each question).

|                                                         | n. |
|---------------------------------------------------------|----|
| :white_check_mark: Answerable by the model                                 | 62 |
| :robot: More AI needed (e.g. embeddings)                        | 7  |
| :globe_with_meridians: Answerable including external knowledge (e.g. Wikidata) | 4  |
| :pencil: Require model extension | 1 |
| TOTAL                                                   | 74 |

Detail

| Category                                         | :white_check_mark: | :robot: |  :globe_with_meridians: | :pencil: |TOT|
|--------------------------------------------------|----|----|----|----|----|
| [A. Smells](#a-smells)                           | 10 | 0 | 0 | 1|  11 |
| [B. Noses and Gestures](#b-noses-and-gestures)   | 6| 0|0|0|6  |
| [C. Identities](#c-identities) | 6| 0|0|0|6  |
| [D. Emotions](#d-emotions) | 6| 0|0|0|6  |
| [E. Practices](#e-practices) | 8| 5|0|0|13  |
| [F. Sites and contexts](#f-sites-and-contexts)  | 9| 0|2|0|11  |
| [G. Texts and images](#g-texts-and-images)  | 19| 0|2|0|21  |

Recap:


## Table of Contents
* [A. Smells](#a-smells)
* [B. Noses and Gestures](#b-noses-and-gestures)
* [C. Identities](#c-identities)
* [D. Emotions](#d-emotions)
* [E. Practices](#e-practices)
* [F. Sites and contexts](#f-sites-and-contexts)
* [G. Texts and images](#g-texts-and-images)


## A. Smells
_What smells were significant in the past?_

1. What smell sources have the highest number of documentation in the past?  
[query](./a1.rq)

1. What smell source have the highest number of documentation in [time, e.g. 18th centuries]?  
[query](./a2.rq)

1. What are the most frequent smell sources in London in the 18th century?  
[query](./a3.rq)

1. When a [specific odour] started to be mentioned in text?  
[query](./a4.rq)

1. What are the new odours that appeared during [specific period e.g 1800-1850]?  
[query](./a5.rq)

1. What are the new odours that appeared during [historical process e.g industrial revolution]?  
[query](./a6.rq)

1. Which smells were perceived during [recurrent part of year, e.g. spring]?  
[query](./a7.rq)

1. Which smells were perceived during [recurrent part of day, e.g.  morning]?  
[query](./a8.rq) :pencil:

1. Was [smell 1, e.g. muck] perceived as more [adjective, e.g. disgusting] than [smell 2, e.g. smog]?  
[query](./a9.rq) :robot: (similarity over word embeddings)

1. Which kind of smell is more likely to trigger [childhood] memories?  
[query](./a10.rq)

1. Which smells with more than [threshold, e.g 100] occurrences in [time, 18th century] did disappear afterwards?  
[query](./a11.rq)

## B. Noses and Gestures

_How did people use their noses in the past and what types of smell expertise or experience can we find?_

1. Which professions are more present in smelling experience descriptions?  
[query](./b1.rq)

1. Which adjectives were used by [profession, e.g. medical practitioners] in describing smells?  
[query](./b2.rq)

1. Which smells did people from [urban areas; rural areas; countries] describe most often?  
[query](./b3.rq)

1. Which smells are normally accompanied with [other senses perceptions, e.g. taste]?  
[query](./b4.rq)

1. What are the smelling gestures that are more connected with [smell type, e.g. putrid]?  
[query](./b6.rq)

1. Which smelling gestures have been more described in [profession, e.g. tea-merchants]' experiences?  
[query](./b7.rq)


## C. Identities

_What meaning did smells have and how did they communicate identities or stereotypes? (e.g the use of garlic to stereotype groups such Ashkenazi Jews; floral scents and femininity)_

1. What are the odours most associated with [an ethnic group such Ashkenazi Jews]?  
[query](./c1.rq)

1. Which flavours are associated with [topic, e.g. femininity] in [Asia]?  
[query](./c2.rq)

1. What are [smells, e.g. floral scents] mostly associated with?  
[query](./c3.rq)

1. Which scents were linked to the idea of heaven in X period?  
[query](./c4.rq)

1. What was an erotic scent in X period?  
[query](./c5.rq)

1. What was the scent of cleanliness in X period?  
[query](./c7.rq)


## D. Emotions

_What feelings were associated with smells in parts of Europe at different times?_

1. What feelings were associated with [a particular smell] in [parts of Europe] at [a given time]?    
[query](./d1.rq)

1. What was the dominant/average hedonic tone of smell descriptions in [period] and/or [place]?  
[query](./d2.rq)

1. What odours [disgusted OR pleased] [social marker e.g gender, race, nationality, age] Europeans?  
[query](./d3.rq)

1. What sorts of scents were produced to create a certain emotion [pleasure]?  
[query](./d4.rq)

1. Which smell triggers memories of [childhood]?  
[query](./d5.rq)

1. Which smells remember of past people or past places (commemoration)?  
[query](./d6.rq)

## E. Practices

_What kinds of practices produced smells?_

1. Which types of practices produce a bad smell?  
[query](./e11.rq) :robot: (sentiment detection)

1. Which types of practices produce [smell, e.g. sweet]?  
[query](./e12.rq)

1. What types of cooking produce a bad smell?  
[query](./e1.rq) :robot: (sentiment detection)

1. What types of cooking are producing [smell, e.g. sweet]?  
[query](./e2.rq)

1. Which practice can increment a smell intensity?  
[query](./e3.rq)

1. Which practice can reduce a smell intensity?  
[query](./e4.rq)

1. Which practice can modify an existing smell?  
[query](./e5.rq)

1. What smells produced what kinds of practices?  
[query](./e6.rq)

1. Which practice changed the smells it produced over time?  
[query](./e7.rq) :robot: (similarity over word embeddings)

1. Who were the people associated with the practices that produced/reduced smell?  
[query](./e8.rq)

1. Where were the practices that produced/reduced smell located [city/countryside/underground]?  
[query](./e9.rq)

1. What was a protective [health] scent in X period?  
[query](./e10.rq) :robot: (similarity over word embeddings)

1. Which smells are associated with hygiene? [perfume, filth]  
[query](./e13.rq) :robot: (similarity over word embeddings)

## F. Sites and contexts

_Which communities, institutions, or spaces were associated with particular smells?_

1. Which smells are associated with [general place e.g. schools, churches, docks, ships]?  
[query](./f1.rq)

1. Which smells are associated with [specific place e.g. the Amsterdam stock exchange]?  
[query](./f2.rq)

1. Which smells are associated with [a city e.g. London]?  
[query](./f3.rq)

1. Which smells are associated with [a region OR country e.g Sussex OR France]?  
[query](./f4.rq)

1. In which kind of places was possible to perceive [smell source, e.g. incense]?  
[query](./f5.rq)

1. In which kind of places was possible to perceive [smell, e.g. floreal]?  
[query](./f6.rq)

1. In which kind of places was possible to perceive both [floreal smells] a [woody smell]?  
[query](./f7.rq)

1. Which smell was possible to perceive during a [general event, e.g. a war]?  
[query](./f8.rq) :globe_with_meridians:

1. Which smell was possible to perceive during the [specific event, e.g. Crimean War]?  
[query](./f9.rq) :globe_with_meridians:

1. Which kind of event produced an increment of smell experiences?  
[query](./f10.rq)

1. Which kind of event produced a reduction of smell experiences?  
[query](./f11.rq)


## G. Texts and images
_How smells are represented in texts and images?_

1. What are the adjectives used for [smell, e.g. orange aroma] in the 15th century?  
[query](./g1.rq)

1. Which painter was portraying more [smell, e.g. smoky]?  
[query](./g2.rq)

1. Which country was portraying more [smell, e.g. smoky]?  
[query](./g3.rq)

1. Which part of the place [town, countryside, maket] is portrayed with the most smell?  
[query](./g4.rq)

1. In which part of an image [foreground, middleground, background] are smells portrayed?  
[query](./g5.rq)

1. Which time [century, decade] was portraying more smell?  
[query](./g6.rq)

1. Which portrayal of a smell [pomander, tobacco] changed [disappeared/faded/developed] over time?  
[query](./g7.rq)

1. In which text we can find [smell, e.g. citrus]?  
[query](./g8.rq)

1. What scents are associated with [genre of text]?  
[query](./g9.rq)

1. What scents are associated with [period of text]?  
[query](./g10.rq)

1. What scents do [named, country of origin, male/female] authors describe most?  
[query](./g11.rq)

1. In which paintings is [smell, e.g. citrus] present?  
[query](./g12.rq)

1. Which paintings show [pleasant, unpleasant] smells?  
[query](./g13.rq) :robot: (sentiment detection)

1. Which kind of reactions to smells are possible to find in [Dutch] paintings of [18th century]?  
[query](./g14.rq)

1. What sort of people react to smells in paintings?  
[query](./g15.rq)

1. Which smells are possible to find in paintings of the [Rijksmuseum]?  
[query](./g16.rq)

1. Which smells are possible to find in paintings whose subject is [field work]?  
[query](./g17.rq)

1. Which smells are frequently present in paintings but not in texts?  
[query](./g18.rq)

1. Which smells are frequently present in texts but not in paintings?  
[query](./g19.rq)

1. Which sources that are not objects (e.g. emotions, virtues) are described in text as emitting odours (figurative smells)?  
[query](./g20.rq) :globe_with_meridians:

1. Which adjectives are used to describe figurative smells?  
[query](./g21.rq) :globe_with_meridians:
