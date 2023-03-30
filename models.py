from marshmallow import Schema, fields, validate

commands = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')


class RequestSchema(Schema):
    """ Schema for request """
    cmd = fields.Str(required=True, validate=validate.OneOf(commands))
    value = fields.Str(required=True)


class BatchRequestSchema(Schema):
    """ Schema for batch of requests """
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
