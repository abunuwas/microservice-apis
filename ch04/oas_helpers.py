def make_response(schema=None, status_code='200', content_type='application/json', description=None):
    response = {
        status_code: {
            'content': {
                content_type: {
                    'schema': schema
                }
            },
        }
    }
    if description is not None:
        response[status_code]['description'] = description
    return response


def make_request_body(schema, required=True, content_type='application/json'):
    return {
        'required': required,
        'content': {
            content_type: {
                'schema': schema
            }
        }
    }


def make_parameter(in_, name, schema, required=True):
    return {
        'in': in_,
        'name': name,
        'schema': schema,
        'required': required
    }
