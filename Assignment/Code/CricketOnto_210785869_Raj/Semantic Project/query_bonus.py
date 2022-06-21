import rdflib
# This simple query grabs all movies with a title and a figure for how much the
# movie grossed at the box office.
query = """
PREFIX cr: <http://www.semanticweb.org/uttkarshraj/ontologies/2022/4/proj_cricketer#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT DISTINCT ?cricketplayers ?dateofbirth 
WHERE {         
        ?cricketer rdf:type cr:Cricketer .
        OPTIONAL {?cricketer cr:name ?cricketplayers} .
        OPTIONAL {?cricketer cr:dateofbirth ?dateofbirth} .
      }GROUP BY ?dateofbirth"""
# Create an empty RDF graph and then parse our generated ontology into it.
g = rdflib.Graph()
g.parse("cricketer_bonus.owl", "xml")
print("graph has %s statements.\n" % len(g))
# Don't bbe put off by the weird strings, they're formatting strings that we can
# use in Python to nicely format a table, for example. You can print things 
# however you want.
print ('{0:50s} {1:50s} '.format("cricketplayers","dateofbirth"))
for x,y in g.query(query):
    print ('{0:50s} {1:50s} '.format(str(x),str(y)))
print("")
# print("")
# print("  Try editing the code to run this query against 'movie.owl' instead.")
# print("  Notice how the query runs and a few results are returned. When")
# print("  your ontology it can be handy to define a few individuals so you can")
# print("  test your queries and perform some sanity checks. That way you can focus")
# print("  your attention on writing the proper queries to populate the rest of")
# print("  your ontology now you know what your individuals should look like.")
# print("")