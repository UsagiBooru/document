import yaml

# Load template file
with open("template.yaml", "r", encoding="utf8") as f:
    out = yaml.safe_load(f)

# Load monolith document file
with open("main.v1.yaml", "r", encoding="utf8") as f:
    main = yaml.safe_load(f)

# Parameters are shared
out["components"]["parameters"] = main["components"]["parameters"]

# Create short-hands
out_schemas = out["components"]["schemas"]
main_schemas = main["components"]["schemas"]
global_tags = []

# Input separate key
SPLIT_KEY = input("Input path key: (Ex./arts/) >>")


# Loop in all paths
for path_key in main["paths"]:
    if SPLIT_KEY in path_key:
        print("Path: ", path_key)
        # Copy path
        out["paths"][path_key] = main["paths"][path_key]
        # Loop in all methods
        methods = out["paths"][path_key].keys()
        for method_key in methods:
            print("Method: ", method_key)
            # Copy url param tag
            ref_method = main["paths"][path_key][method_key]
            if method_key == "parameters":
                out["paths"][path_key][method_key] = ref_method
                continue
            # Copy request model
            if method_key != "get":
                if "requestBody" in ref_method.keys():
                    req_body = ref_method["requestBody"]["content"]
                    content_type = list(req_body.keys())[0]
                    ref_schema = req_body[content_type]["schema"]["$ref"]
                    ref_schema = ref_schema.split("/")[-1]
                    out_schemas[ref_schema] = main_schemas[ref_schema]
            # Copy response model
            ref_method_out = out["paths"][path_key][method_key]["responses"]
            for resp_key in ref_method_out.keys():
                req_body = ref_method_out[resp_key]["content"]
                content_type = list(req_body.keys())[0]
                ref_schema = req_body[content_type]["schema"]["$ref"]
                ref_schema = ref_schema.split("/")[-1]
                out_schemas[ref_schema] = main_schemas[ref_schema]
            # Copy global tag
            global_tags.append(ref_method["tags"][0])

# Add struct model
toadd = []
for s in out_schemas.keys():
    for p in out_schemas[s]["properties"].keys():
        if "$ref" in out_schemas[s]["properties"][p].keys():
            ref = out_schemas[s]["properties"][p]["$ref"]
            ref = ref.split("/")[-1]
            toadd.append([ref, main["components"]["schemas"][ref]])
        elif out_schemas[s]["properties"][p]["type"] == "array":
            if "$ref" in out_schemas[s]["properties"][p]["items"].keys():
                ref = out_schemas[s]["properties"][p]["items"]["$ref"]
                ref = ref.split("/")[-1]
                toadd.append([ref, main["components"]["schemas"][ref]])
for a in toadd:
    out_schemas[a[0]] = a[1]

# Add global tag
out["tags"] = [{"name": t} for t in list(set(global_tags))]

# Export to document
with open(f"{SPLIT_KEY.replace('/','')}.v1.yaml", "w", encoding="utf8") as f:
    yaml.dump(out, f, encoding='utf-8', allow_unicode=True)
