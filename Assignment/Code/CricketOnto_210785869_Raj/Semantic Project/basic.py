import rdflib
from rdflib.graph import Graph, URIRef
from SPARQLWrapper import SPARQLWrapper, XML
from rdflib.plugins.stores.memory import Memory
# Configuring the end-point and constructing query.
# Notice the various SPARQL constructs we are making use of:
#
#   * PREFIX to bind prefixes in our query
#   * CONSTRUCT to build new individuals from our query
#   * OPTIONAL to indicate that some fields may not exist and that's OK
#   * FILTER to constrain our query in some way
#
# You should try and make use of as many of these constructs as possible in your
# own coursework, either in the basic or bonus task (or both!) if you want to 
# get the best mark.
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
construct_query="""
    PREFIX cr: <http://www.semanticweb.org/uttkarshraj/ontologies/2022/4/proj_cricketer#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>        
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
    PREFIX dbpprop: <http://dbpedia.org/property/> 
      
CONSTRUCT {
          ?cricketer rdf:type cr:Cricketer .
          ?cricketer cr:name ?name .
          ?cricketer cr:isCaptain ?captain .
          ?captain rdf:type cr:Captain .  
          ?cricketer cr:hasBirth ?birth .
          ?birth rdf:type cr:Birthplace .
          ?cricketer cr:mostOdiRuns ?odiruns .
          ?odiruns rdf:type cr:Odiruns .
          ?cricketer cr:hasMostRuns ?mostruns .
          ?mostruns rdf:type cr:Mostruns .
          ?cricketer cr:hasMoreTestRuns ?testRuns .
          ?testRuns rdf:type cr:MostTestRuns . 
          ?cricketer cr:height ?height . 
          ?cricketer cr:lastodiyear ?lastodiyear .
          ?cricketer cr:lastodiagainst ?lastodiagainst .
          ?cricketer cr:batting ?batting .
          ?cricketer cr:bowling ?bowling .
          ?cricketer cr:clubnumber ?clubnumber .
          ?cricketer cr:deliveries ?deliveries .
                          
    }
    WHERE{
        ?cricketer rdf:type dbpedia-owl:Cricketer .
        ?cricketer foaf:name ?name .
        
        OPTIONAL {?cricketer ^dbp:team2Captain ?captain} .
        OPTIONAL {?cricketer dbpedia-owl:birthPlace ?birth} .
        OPTIONAL {?cricketer ^dbp:team1OdisMostRuns ?odiruns} .
        OPTIONAL {?cricketer ^dbp:mostRuns ?mostruns} .
        OPTIONAL {?cricketer ^dbp:team1TestsMostRuns ?testRuns} .
        OPTIONAL {?cricketer dbpedia-owl:height ?height} .
        OPTIONAL {?cricketer dbpedia-owl:lastodiyear ?lastodiyear} .
        OPTIONAL {?cricketer dbpedia-owl:lastodiagainst ?lastodiagainst} .
        OPTIONAL {?cricketer dbpedia-owl:batting ?batting} .
        OPTIONAL {?cricketer dbpedia-owl:bowling ?bowling} .
        OPTIONAL {?cricketer dbpedia-owl:clubnumber ?clubnumber} .
        OPTIONAL {?cricketer dbpedia-owl:deliveries ?deliveries} .
      
    } LIMIT 4000
    """
    
sparql.setQuery(construct_query)
sparql.setReturnFormat(XML)
# Creating the RDF store and graph
# We've seen something similar in the lab sheets before, Week 3. We're telling
# the rdflib library to create a new graph and store it in memory (so, temporarily).
memory_store = Memory()
graph_id = URIRef("http://www.semanticweb.org/store/movie")
g = Graph(store = memory_store, identifier = graph_id)
# SPARQL queries can take some time to run, especially if the query is particularly
# large and you're grabbing very many items. 
#
# While experimenting you may want to use the LIMIT construct in SPARQL to take
# only a couple of items, this way you can experiment with things without waiting
# ages for a query to complete.
print("  I might take some time, bear with  me...")
# merging results and saving the store
# The Week 4 lab showed us this, so we know that running the query will return a
# valid RDFlib graph.
g = sparql.query().convert()
# We also saw in Week 3 that we can parse files as valid RDFlib graphs too. When
# we do both of these things, they will be merged together.
g.parse("proj_cricketer.owl")
# You can open this file in protege and compare it to the existing `movie.owl`
# ontology to see what we did. You could also open this in a text editor and have
# a poke around that way.
g.serialize("cricketer_basic_new.owl", "xml")
print("  ...All done!")
print("")
