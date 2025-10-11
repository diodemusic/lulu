python3 pyke/_models/get_schema_json.py

datamodel-codegen \
  --input pyke/_schema/schema.json \
  --input-file-type openapi \
  --output pyke/_models/ \
  --snake-case-field

black .
