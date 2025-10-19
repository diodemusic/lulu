python3 src/pyke/_schema/get_schema_json.py

datamodel-codegen \
  --input src/pyke/_schema/schema.json \
  --input-file-type openapi \
  --output src/pyke/models/ \
  --snake-case-field

black .
