# Querying a WPG

## Basic Setup
To query the WPGs, you can use the `wpg_neo4j.db_utility` module.
```python
# import the querying module
import wpg_neo4j.db_utility as neo4jDatabaseUtilityModule

# define a query
def get_query():
   query="""
   YOUR CYPHER QUERY GOES HERE
   """
   return query

# run the query 
def run_query(tx):
   query = get_query()
   return tx.run(query)

# execute the run_query() function within a neo4j transaction context
results = neo4jDatabaseUtilityModule.exec_fn_within_transaction(run_query)

```

## Example Queries

**Example 1.** Finding identifiers that contain the keyword `example` in their name
```python
query = """
	MATCH (n {Type: 'Identifier'})
	WHERE (n.Code =~ 'example')
	RETURN n
"""
``` 



**Example 2.** Finding all AST children of a node with a given id, say `2`.
```python
query = """
        MATCH (root { Id: '2' })-[:AST_parentOf]->(child)
        RETURN collect(distinct child)
        AS children
"""
``` 


**Example 3.** Finding all `print()`statements
```python
query = """
	MATCH (t {Type: 'ExpressionStatement'})-[:AST_parentOf {RelationType: 'expression'}]->(n {Type: 'CallExpression'})-[:AST_parentOf {RelationType: 'callee'}]-> (pr {Type: 'Identifier', Code: 'print'}), 
	RETURN t, pr
"""
``` 



**Example 4.** Finding all HTTP requests with the `Fetch` API.
```python
query = """
	MATCH (t {Type: 'ExpressionStatement'})-[:AST_parentOf {RelationType: 'expression'}]->(n {Type: 'CallExpression'})-[:AST_parentOf {RelationType: 'callee'}]-> (req {Type: 'Identifier', Code: 'fetch'}), 
	(n)-[:AST_parentOf {RelationType: 'arguments', Arguments: '{\"arg\":0}'}]->(a)
	RETURN t, n, a
"""
```


**Example 5.** Finding the PDG relations of a given node id, say `2`, for a given a variable name, say `XYZ`
```python
query = """
        MATCH (n_s { Id: '2' })<-[:PDG_parentOf { Arguments: 'XYZ' }]-(n_t)
        RETURN collect(distinct n_t) 
        AS resultset
"""
```



 

