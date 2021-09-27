from pathlib import Path

import graphql
import requests
from graphql import parse
from hypothesis import settings, given
from hypothesis_graphql._strategies import queries
from hypothesis_graphql._strategies.queries import make_selection_set_node
from hypothesis_graphql.types import SelectionNodes


def make_query_document(selections: SelectionNodes) -> graphql.DocumentNode:
    """Create top-level node for a query AST."""
    return graphql.DocumentNode(
        kind="document",
        definitions=[
            graphql.OperationDefinitionNode(
                kind="operation_definition",
                operation=graphql.OperationType.MUTATION,
                selection_set=make_selection_set_node(selections=selections),
            )
        ],
    )


schema = Path('web/products.graphql').read_text()
parsed_schema = graphql.build_schema(schema)
add_ingredient_mutation = parsed_schema.mutation_type.fields['addIngredient']
context = queries.Context(parsed_schema)
strategy = (
    queries.subset_of_fields({'addIngredient': add_ingredient_mutation})
    .flatmap(lambda field: queries.lists_of_field_nodes(context, field))
    .map(make_query_document).map(graphql.print_ast)
)


@settings(deadline=None, max_examples=500)
@given(strategy)
def test(case):
    response = requests.post('http://127.0.0.1:8000/graphql', json={'query': case})
    if graphql.validate(parsed_schema, parse(case)):
        assert response.status_code == 400
    else:
        assert response.status_code == 200
