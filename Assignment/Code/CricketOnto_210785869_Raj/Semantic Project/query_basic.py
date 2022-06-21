import rdflib

# This simple query grabs all movies with a title and a figure for how much the
# movie grossed at the box office.
query = """
PREFIX cr: <http://www.semanticweb.org/uttkarshraj/ontologies/2022/4/proj_cricketer#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX dbpprop: <http://dbpedia.org/property/> 

SELECT DISTINCT ?name ?birth ?testRuns 
WHERE { ?cricketer rdf:type cr:Cricketer .
        ?cricketer cr:name ?name .
        ?cricketer cr:hasBirth ?birth .
        ?birth rdf:type cr:Birthplace .
        ?cricketer cr:hasMoreTestRuns ?testRuns .
        ?testRuns rdf:type cr:MostTestRuns . 
      }"""
      
# Create an empty RDF graph and then parse our generated ontology into it.
g = rdflib.Graph()
g.parse("cricketer_basic_new.owl", "xml")
print("graph has %s statements.\n" % len(g))

# Don't bbe put off by the weird strings, they're formatting strings that we can
# use in Python to nicely format a table, for example. You can print things 
# however you want.

print ("Name","\t","\t","\t","\t","BirthPlace","\t","\t","\t","\t","\t","\t","\t","TestRuns")
for x,y,z in g.query(query):
    print (x,"\t","\t",y,"\t","\t","\t","\t","\t",z)

