import yaml

# Load monolith document file
with open("main.v1.yaml", "r", encoding="utf8") as f:
    main = yaml.safe_load(f)

# Load target file
target = input("Input target file: (Ex. arts.v1.yaml) >>")
with open(target, "r", encoding="utf8") as f:
    out = yaml.safe_load(f)

# Copy main schemas to target file
out_schemas = out["components"]["schemas"]
main_schemas = main["components"]["schemas"]
for out_key in out_schemas.keys():
    out_schemas[out_key] = main_schemas[out_key]

# Export to file
with open(target, "w", encoding="utf8") as f:
    yaml.dump(out, f, encoding='utf-8', allow_unicode=True)
print(f"Saved to {target}!")
