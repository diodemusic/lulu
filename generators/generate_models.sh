python3 get_schema_json.py

datamodel-codegen \
  --input src/pyke/generators/schema.json \
  --input-file-type openapi \
  --output src/pyke/models/ \
  --snake-case-field

black .
