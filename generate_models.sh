python3 pyke/models/get_schema_json.py

datamodel-codegen \
  --input pyke/schema/schema.json \
  --input-file-type openapi \
  --output pyke/models/ \
  --snake-case-field

black .
