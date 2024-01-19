This folder contains query examples illustrating SILKNOW data available on the [SILKNOW SPARQL Endpoint](http://data.silknow.org/sparql).

Some queries have only a _partial_ answer or no answer at all since the modeling and the publication of data is a work in progress.

## Table of Contents
* [A. Location](#location)
* [B. Time](#time)
* [C. Time and location](#timeandlocation)
* [D. Materials](#materials)
* [E. Artists](#artists)
* [F. Artists and time](#artistsandtime)
* [G. Artists and location](#artistsandlocation)
* [H. Style](#style)
* [I. Type of items](#typeofitems)
* [J. Type of items and materials](#typeofitemsandmaterials)
* [K. Type of items, materials and style](#typeofitemsmaterialsandstyle)
* [L. Type of items and location](#typeofitemsandlocation)
* [M. Type of items and time](#typeofitemsandtime)
* [N. Type of items, time and location](#typeofitemstimeandlocation)
* [O. Type of items, time, location and material](#typeofitemstimelocationandmaterial)
* [P. Questions in Spanish](#questionsinspanish)






<a name="location"/>

## A. Location

1. **[en]** Which items were produced in Spain? [query](./A1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct++%3Ftitle+%3Fcollection+%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A++++++%3Fs+a+ecrm%3AE12_Production+.%0D%0A++++++%3Fs+ecrm%3AP108_has_produced+%3Fobject.%0D%0A++++%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%0D%0A+%7B+%3Fs+ecrm%3AP8_took_place_on_or_within+%3Flocation+FILTER%28isIRI%28%3Flocation%29%29%0D%0A%0D%0A++++%3Flocation+geonames%3AcountryCode+%22ES%22++%7D%0D%0A++++%0D%0A%0D%0A%0D%0A%0D%0A%7D%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** Where were Mudejar-style fabrics produced?

1. **[en]** Where was the production center called Tiraz?

1. **[en]** What was la Fabrique Lyonnaise ?

1. **[en]** Which items have been produced in Italy and are now preserved in France? 

1. **[en]** Give me all the items that are preserved in the Musée des Tissus de Lyon  
[query](./A6.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Fobject+%3Ftitle%0D%0AWHERE+%7B%0D%0AGRAPH+%3Chttp%3A%2F%2Fdata.silknow.org%2Fgraph%2Fmtmad%3E%7B%0D%0A+%0D%0A+++++++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%7D%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** What Valencian fabrics are located in the Spanish royal collections?

1. **[en]** In which museums and collections around the world are Spanish textiles?
[query](./A8.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Fobj+%3Fcollection%0D%0AWHERE+%7B+GRAPH+%3Fcollection+%7B%0D%0A+++values+%3Fassignment+%7B+%3Chttp%3A%2F%2Fdata.silknow.org%2Fcategory%2F1%3E+%7D%0D%0A%0D%0A++++++%3Fs+a+ecrm%3AE12_Production+.%0D%0A++++++%3Fs+ecrm%3AP108_has_produced+%3Fobj+.%0D%0A%0D%0A+++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobj+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.+%7D%0D%0A%0D%0A+%7B+%3Fs+ecrm%3AP8_took_place_on_or_within+%3Fl%0D%0A+++++%7B+SELECT+%3Fl+SAMPLE%28%3Floc%29+as+%3Fplace%0D%0A++++++++++WHERE+%7B+%3Fl+geonames%3AcountryCode+%3Floc%7D%0D%0A+++++++%7D+.+FILTER%28isIRI%28%3Fl%29%29%0D%0A+++++++++++%3Fl+geonames%3AcountryCode+%22ES%22+%7D%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

1. **[en]** Give me a list of textile factories in a Florence 


<!-- END Location -->

<a name="time"/>

## B. Time

1. **[en]** Which items were produced during the 16th century?
[query](./B1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Ftitle++%3Fcollection+%3Fobject+%0D%0AWHERE+%7B+graph+%3Fcollection%7B%0D%0A%0D%0A+++++%3Fprod+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%3Fprod+ecrm%3AP4_has_time-span+%3Ft+.%0D%0A%3Ft+ecrm%3AP86_falls_within+%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F300404510%3E+.%0D%0A%0D%0A+++%0D%0A%0D%0A+++++%0D%0A+++++%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** What are the common decorative elements in 16th century fabrics? (0 results)
[query](./B2.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Ftitle++%3Fcollection+%3Fobject+%3Fvisual_item%0D%0AWHERE+%7B+graph+%3Fcollection%7B%0D%0A%0D%0A+++++%3Fprod+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%3Fprod+ecrm%3AP4_has_time-span+%3Ft+.%0D%0A%3Ft+ecrm%3AP86_falls_within+%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F300404510%3E+.%0D%0A%0D%0A+++%0D%0A+++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.%0D%0A+++++++++%3Ftype_group+skos%3Amember+%3Fassignment+.+FILTER+contains%28str%28%3Ftype_group%29%2C+%22fabric%22%29%7D%0D%0A%0D%0A%7B%3Fobject+ecrm%3AP65_shows_visual_item+%3Fvitem+.%0D%0A%3Fvitem++skos%3AprefLabel+%3Fvisual_item+FILTER%28lang%28str%28%3Fvisual_item%29%29+%3D+%22en%22%29%7D%0D%0Aunion%0D%0A%7B%3Fobject+ecrm%3AP65_shows_visual_item+%3Fvitem+.%0D%0A%3Fvitem++ecrm%3AP3_has_note+%3Fvisual_item%7D+%0D%0A+++++%0D%0A+++++%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

1. **[en]** Which fabric became popular in Italy in the fifteenth century?

1. **[en]** What kinds of fabrics / weaving techniques / designs were most frequent in 18th-century France? Please give me a list of the top 5 (or 10, 15…) occurrences in a particular field.

1. **[en]** Which items have been produced in 1815?
[query](./B5.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct++%3Fcollection+%3Fobject+%0D%0AWHERE+%7B+graph+%3Fcollection%7B%0D%0A+++++%3Fprod+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A+++++%3Fprod+ecrm%3AP4_has_time-span+%3Chttp%3A%2F%2Fdata.silknow.org%2Ftimespan%2F1815%3E+.%0D%0A%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** What are the most common decorative motifs in the Hispanic Middle Ages?


<!-- END Time -->


<a name="timeandlocation"/>

## C. Time and location

1. **[en]** Which items were produced in France during the 18th century?
[query](./C1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Ftitle++%3Fcollection+%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection%7B%0D%0A%0D%0A+++++%3Fprod+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%3Fprod+ecrm%3AP4_has_time-span+%3Ft+.%0D%0A%3Ft+ecrm%3AP86_falls_within+%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F300404512%3E+.%0D%0A%0D%0A+%7B+%3Fprod+ecrm%3AP8_took_place_on_or_within+%3Flocation+FILTER%28isIRI%28%3Flocation%29%29%0D%0A%0D%0A++++%3Flocation+geonames%3AcountryCode+%22FR%22++%7D+%0D%0A+++++%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** Give me all the items that have been produced after 1750 in France.

1. **[en]** Give me all the items that are preserved in the Musée des Tissus de Lyon, and that have been produced between 1650 and 1750.


1. **[en]** Who (person, institution ...) was the main textile French producer during the XVII?


<!-- END Timeandlocation -->


<a name="materials"/>

## D. Materials

1. **[en]** Which items were produced with silk and silver?  
[query](./D1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct++%3Ftitle+%3Fcollection++%3Fobject+%3Fmaterial%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+++++%3Fprd+ecrm%3AP126_employed+%3Fmaterial+.%0D%0A+++++%0D%0A++++++%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F628%3E+.+%7D%0D%0A++++++++UNION%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F368%3E+.%7D%0D%0A+%0D%0A+++++++%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** When does the "a pizzo" design become popular?

1. **[en]** When does the "bizarre" design become popular?

1. **[en]** What is the Blonda?

1. **[en]** What is the Buratto?

1. **[en]** Where does the name of the Batista fabric come from?


1. **[en]** Give me the objects that involve at most silk, silver and wool 
[query](./D7.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Fobject+%3Ftitle%0D%0AWHERE+%7B%0D%0A%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F628%3E%2C+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F368%3E%2C+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F644%3E++.%7D++++++%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** Give me the objects that involve silk, silver and wool, except those that involve gold. (Same results as the question above.)
[query](./D8.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=SELECT+distinct+%3Fobject+%3Ftitle%0D%0AWHERE+%7B%0D%0A%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+%0D%0A+optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A%0D%0A%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F628%3E%2C+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F368%3E%2C+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F644%3E++.%7D%0D%0A+%3Fprd+ecrm%3AP126_employed+%3Fmore+.%0D%0A%0D%0AFILTER+%28contains%28str%28%3Fmore%29%2C+str%28%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F627%3E%29%29+%21%3D+true%29+++++%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)


<!-- END Material -->

<a name="artists"/>

## E. Artists

1. **[en]** Which items have been created by Philippe de la Salle ?
[query](./E1.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A%0D%0A++++++values+%3Flabel+%7B+%22Philippe+de+la+Salle%22+%7D%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor.%0D%0A++++%3Factor+a+ecrm%3AE39_Actor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A++++%0D%0A%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)    

1. **[en]** Give me all the information you have on Philippe de la Salle!  

1. **[en]** Give me all the items inspired by a work of Giambologna

1. **[en]** Give me all the items designed by François Boucher
[query](./E4.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A+++++values+%3Factor+%7B+%3Chttp%3A%2F%2Fdata.silknow.org%2Factor%2Ffc74669f-81ea-35a6-8f26-839923f857ff%3E+%7D%0D%0A%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A%0D%0A++++%0D%0A++++%0D%0A%0D%0A++++%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A%7D+%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)    

1. **[en]** Give me all the items designed by Italian artists  

1. **[en]** Are there items designed by French artists in the 17th century?  

1. **[en]** Give all the items for which the designer has been influenced by Philippe de la Salle  

1. **[en]** Who were the printers or engravers that produced graph paper for making mise-en-cartes?
[query](./E8.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A%0D%0A%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor.%0D%0A++++%3Factor+a+ecrm%3AE39_Actor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A++++%0D%0A++++%7B%3Fproduction+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F856%3E+.+%7D%0D%0A++++%7B%3Fproduction+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F441%3E+.+%7D%0D%0A%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+) (0 Results)  


<!-- END Artists -->


<a name="artistsandtime"/>

## F. Artists and time

1. **[en]** Give me all the items designed by François Boucher in the 18th century
[query](./F1.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A++++++values+%3Factor+%7B+%3Chttp%3A%2F%2Fdata.silknow.org%2Factor%2Ffc74669f-81ea-35a6-8f26-839923f857ff%3E+%7D%0D%0A%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A++++%0D%0A++++%3Fprododuction+ecrm%3AP4_has_time-span+%3Ft+.%0D%0A++++%3Ft+ecrm%3AP86_falls_within+%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F300404512%3E+.%0D%0A++++%0D%0A++++%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A%7D+%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

1. **[en]** Give me all the items created by Philippe de la Salle in the last 5 years of his life.
[query](./F2.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A++++++values+%3Flabel+%7B+%22Philippe+de+la+Salle%22+%7D%0D%0A%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor.%0D%0A++++%3Factor+a+ecrm%3AE39_Actor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A++++%0D%0A++++%3Fprododuction+ecrm%3AP4_has_time-span+%3Ft1+.%0D%0A++++%3Ft1+time%3AhasBeginning+%3Chttp%3A%2F%2Fdata.silknow.org%2Ftimespan%2F1799%2Fstart%3E+.%0D%0A++++%0D%0A++++%3Fprododuction+ecrm%3AP4_has_time-span+%3Ft2+.%0D%0A++++%3Ft2+time%3AhasEnd+%3Chttp%3A%2F%2Fdata.silknow.org%2Ftimespan%2F1804%2Fend%3E+.%0D%0A++++%0D%0A++++%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A%7D+%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+) (0 Results) 

1. **[en]** Give me a list of designers from Valencia during the 19th century


<!-- END Artists and time -->

<a name="artistsandlocation"/>

## G. Artists and location

1. **[en]** Give me all the designers who were born in England 

1. **[en]** Give me all the designers who were trained in Italy 

1. **[en]** Give me all the designers who were trained in Italy and in France  


<!-- END Artists and location -->

<a name="style"/>

## H. Style

1. **[en]** Who is the Revel style name after?
[query](./H1.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Factor+%3Flabel+%3Ftitle+%3Fcollection%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B%0D%0A%0D%0A++++++values+%3Flabel+%7B+%22Jean+Revel%22+%7D%0D%0A+++++++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++%3Fproduction+ecrm%3AP9_consists_of+%3Factivity+.%0D%0A++++%3Factivity+ecrm%3AP14_carried_out_by+%3Factor.%0D%0A++++%3Factor+a+ecrm%3AE39_Actor+.%0D%0A++++%3Factor+rdfs%3Alabel+%3Flabel+.%0D%0A++++%0D%0A%0D%0A%7D%7D%0D%0A%0D%0A&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+)

1. **[en]** Give me all the items that have been influenced by oriental fashion. 

1. **[en]** Give me all the items with flowers on them. 
[query](./H3.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+crmdig%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMext%2FCRMdig.rdfs%2F%3E%0D%0Aprefix+crmsci%3A+%3Chttp%3A%2F%2Fwww.ics.forth.gr%2Fisl%2FCRMsci%2F%3E%0D%0ASELECT+DISTINCT+%3Fobject+%3Ftitle+%3Fcollection+%3Fvisual_item%0D%0AWHERE+%7Bgraph+%3Fcollection+%7B+%3Fobject+ecrm%3AP65_shows_visual_item+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F743%3E++%7D%0D%0A%0D%0A%0D%0A%0D%0A++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle%7D%0D%0A++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A++++%3Fproduction+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A%0D%0A++++%0D%0A++++%0D%0A%0D%0A++++++%3Fobject+ecrm%3AP65_shows_visual_item+%3Fvitem+.%0D%0A++++++%3Fvitem++skos%3AprefLabel+%3Fvisual_item+.+%0D%0A%0D%0A++++++FILTER%28lang%28%3Fvisual_item%29+%3D+%22en%22%29%0D%0A++++++FILTER%28%3Fvitem+%3D+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F743%3E%29+%0D%0A%0D%0A++++%0D%0A++++%0D%0A%0D%0A%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+) 

1. **[en]** Give me all the items with hearts and flowers on them

1. **[en]** Give me all the items with purple 

1. **[en]** Who was the introducer of the realistic style in textiles? 

1. **[en]** Give me examples of textile designs that appear in paintings.



<!-- END style -->

<a name="typeofitems"/>

## I. Type of items

1. **[en]** Give me all the scarves
[query](./I1.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fdig+a+crmdig%3AD1_Digital_Object+.%0D%0A++++++%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22scarf%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22scarf%22%29%7D%0D%0A%0D%0A+++++%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

1. **[en]** Give me all the dresses that have been worn with a petticoat 
[query](./I2.rq) - [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2Fproperty%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fdig+a+crmdig%3AD1_Digital_Object+.%0D%0A++++++%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22dress%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22dress%22%29%7D%0D%0A%0D%0A+++++%0D%0A++++++++FILTER+contains%28str%28%3Fdescription%29%2C+%22petticoat%22%29+%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+) (0 Results)

1. **[en]** Give examples of textiles that conserve both the fabric and the mise-en-carte  
[query](./I3.rq) - [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2Fproperty%2F%3E%0D%0ASELECT+distinct+%3Fassignment+%3Ftitle++%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A%7B%0D%0A++%0D%0A++++++%3Fprod+ecrm%3AP108_has_produced+%3Fobj+.%0D%0A++++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.+%7D%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A%0D%0A%0D%0A++++++++%3Fprod+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F649%3E+.%0D%0A++++++++%3Fprod+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F441%3E+.%0D%0A%0D%0A++++++++%0D%0A%0D%0A++++++++%7B%0D%0A++++++++values+%3Fassignment+%7B+%3Chttp%3A%2F%2Fdata.silknow.org%2Fcategory%2F1%3E+%7D+%0D%0A++++++++%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment%7D%0D%0A%0D%0A%0D%0A+++++%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&should-sponge=&format=text%2Fhtml&timeout=0&debug=on&run=+Run+Query+) (0 Results)


1. **[en]** When do the first mise-en-carte appeared?


<!-- END Type of items -->

<a name="typeofitemsandmaterials"/>

## J. Type of items and materials

1. **[en]** Give me all the ribbons with cotton [query](./J1.rq)  [result](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription+group_concat%28distinct+%3Fmaterial%3Bseparator%3D%22%7C%22%29+as+%3Fmaterials+%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fdig+a+crmdig%3AD1_Digital_Object+.%0D%0A++++++%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++++++%3Fprd+ecrm%3AP126_employed+%3Fmaterial++.%0D%0A%0D%0A%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F617%3E+.%7D%0D%0A++++++++%0D%0A%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22ribbon%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22ribbon%22%29%7D%0D%0A%0D%0A+++++%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

1. **[en]** Give me all the dresses with silk, cotton and gold
[query](./J2.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fdig+a+crmdig%3AD1_Digital_Object+.%0D%0A++++++%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++++++%0D%0A++++++++%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F368%3E+.%7D%0D%0A++++++++UNION%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F617%3E+.%7D%0D%0A++++++++UNION%0D%0A++++++++%7B%3Fprd+ecrm%3AP126_employed+%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2F627%3E+.%7D%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22dress%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22dress%22%29%7D%0D%0A%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on) 

<!-- END Type of items and materials -->

<a name="typeofitemsmaterialsandstyle"/>

## K. Type of items, materials and style

1. **[en]** Give me all the scarves with cotton and with hearts on them

1. **[en]** Give me examples of imitations or revivals of textiles during the 18th century


<!-- END Type of items, materials and style -->


<a name="typeofitemsandlocation"/>

## L. Types of items and location

1. **[en]** Give me the religious clothing produced in Spain
[query](./L1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Fplace+%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B++++++++++%3Chttp%3A%2F%2Fdata.silknow.org%2Fvocabulary%2Ffacet%2Freligious_attire%3E+skos%3Amember+%3Fassignment+.+%7D%0D%0A%0D%0A%7B++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A++++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.+%7D%0D%0A%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++%7B+%3Fprd+ecrm%3AP8_took_place_on_or_within+%3Flocation+FILTER%28isIRI%28%3Flocation%29%29%0D%0A+++++%3Flocation+geonames%3Aname+%3Fplace+.%0D%0A+++++%3Flocation+geonames%3AcountryCode+%22ES%22++%7D%0D%0A++++%0D%0A%0D%0A%0D%0A++++++++%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL4+%3Fassignment+.%0D%0A%0D%0A%0D%0A++++++++%0D%0A%0D%0A%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on) 

1. **[en]** What textiles belonged to the collector Mariano Fortuny?


<!-- END Types of items and location -->

<a name="typeofitemsandtime"/>

## M. Type of items and time

1. **[en]** Give me all the dresses produced during the Victorian era
[query](./M1.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=prefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A%7B%0D%0A%0D%0A+++++%3Fobject+a+ecrm%3AE22_Man-Made_Object+.%0D%0A+++++%3Fprod+ecrm%3AP108_has_produced+%3Fobject+.+%7D%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A%0D%0A+++++%3Fprod+ecrm%3AP4_has_time-span+%3Ft+.%0D%0A+++++%3Ft+ecrm%3AP86_falls_within+%3Chttp%3A%2F%2Fvocab.getty.edu%2Faat%2F300404513%3E+.%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22dress%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22dress%22%29%7D%0D%0A%0D%0A++++++++%0D%0A%0D%0A%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

<!-- END Type of items and time -->

<a name="typeofitemstimeandlocation"/>

## N. Type of items, time and location

1. **[en]** Give me all the clothes produced in Spain during the Renaissance. 

1. **[en]** Give me all the scarves that have been produced in England between 1800 and 1850.
[query](./N2.rq) - [results](https://data.silknow.org/sparql?default-graph-uri=&query=%0D%0Aprefix+silk%3A+++%3Chttp%3A%2F%2Fdata.silknow.org%2Fontology%2F%3E%0D%0ASELECT+distinct++%3Ftitle+%3Fassignment+%3Fdescription++%3Fcollection++%3Fobject+%3Ftime%0D%0AWHERE+%7B+graph+%3Fcollection+%7B%0D%0A%0D%0A+++++%3Fdig+a+crmdig%3AD1_Digital_Object+.%0D%0A++++++%0D%0A+++++%3Fdig++ecrm%3AP129_is_about+%3Fprd+.%0D%0A+++++%3Fprd+ecrm%3AP108_has_produced+%3Fobject+.%0D%0A+%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+%7D%0D%0A+++++optional+%7B%3Fobject+ecrm%3AP3_has_note+%3Fdescription+%7D%0D%0A%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%0D%0A%0D%0A++++++++%7B%3Fobject+ecrm%3AP102_has_title+%3Ftitle+.FILTER+contains%28str%28%3Ftitle%29%2C+%22scarf%22%29%7D%0D%0A+++++++++UNION%0D%0A++++++++%7B%3Ftype+ecrm%3AP41_classified+%3Fobject+.%0D%0A+++++++++%3Ftype+silk%3AL1+%3Fassignment+.FILTER+contains%28str%28%3Fassignment%29%2C+%22scarf%22%29%7D%0D%0A%0D%0A++++++++%3Fprd+ecrm%3AP4_has_time-span+%3Fts+.%0D%0A+++++++++%3Fts+skos%3AprefLabel+%3Ftime+%3B%0D%0A++++++++++++++++time%3AhasEnd+%2F+time%3AinXSDDate+%3Fend+%3B%0D%0A++++++++++++++++time%3AhasBeginning+%2F+time%3AinXSDDate+%3Fstart+.%0D%0A%0D%0A%0D%0A++FILTER+%28+%3Fstart+%3E%3D+%221800%22%5E%5Exsd%3AgYear+AND+%3Fend+%3C%3D+%221850%22%5E%5Exsd%3AgYear+%29%0D%0A++++++++%0D%0A++++++++%0D%0A%0D%0A%7D%7D&format=text%2Fhtml&should-sponge=&timeout=0&signal_void=on)

<!-- END Type of items, time and location -->

<a name="typeofitemstimelocationandmaterial"/>

## O. Type of items, time, location and material

1. **[en]** Give me all the ribbon involving silver and produced in Italy during the Renaissance . 

1. **[en]** Give me those ornamental motifs from classical antiquity that appear in fabrics, mises-en-carte and designs ... Organized by chronology, location, place of origin ... 

<!-- END Type of items, time, location and material -->

<a name="questionsinspanish"/>

## P. Questions in Spanish

1. **[es]** ¿Cuáles son los motivos decorativos más habituales en la Edad Media hispánica?

1. **[es]** ¿Qué tejidos valencianos hay en las colecciones reales españolas?

1. **[es]** ¿Qué tejidos españoles hay en diferentes museos y colecciones?

1. **[es]** Dame ejemplos de piezas en los que se conserva tejido y puesta en carta.

1. **[es]** Dime todos los tejidos que pertenecieron al coleccionista Mariano Fortuny (provenance)

1. **[es]** Dime motivos ornamentales de la antigüedad clásica que aparecen en tejidos, puestas en carta, diseños… Organizados por cronología, ubicación, lugar de origen...

1. **[es]** ¿Quién fue el introductor del estilo realista en tejidos?

1. **[es]** ¿Quién (persona, institución…) es el principal productor francés de tejidos en el XVII?

1. **[es]** ¿Cuándo aparecen los espolinados?

1. **[es]** ¿Cuándo aparecieron las primeras puestas en carta sobre papel milimetrado impreso?

1. **[es]** ¿Qué impresores o grabadores produjeron papel milimetrado para puestas en carta?

1. **[es]** Dame una lista de talleres o fábricas textiles de una ciudad.

1. **[es]** Dime una lista de diseñadores de una ciudad o región durante un periodo.

1. **[es]** Dame ejemplos de diseños textiles que aparecen en pinturas.

1. **[es]** Dame ejemplos de imitaciones, revivals, copias, falsificaciones, … (copias de modelos antiguos hechas mucho tiempo después)

<!-- END questions in Spanish -->
