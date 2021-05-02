import yaml
import sys


# Get ref with reading all lines
def getRefsFromDict(dic):
    yaml_string = yaml.dump(dic, default_flow_style=False)
    refs = [line for line in yaml_string.split("\n") if "$ref" in line]
    refs = list(set(refs))
    refs = [ref.split("schemas/")[-1][:-1] for ref in refs if "schemas" in ref]
    return refs


# Extract specified path to another file
def extractPath(
    key="/arts",
    input_file="main.v1.yaml",
    out_file="arts.v1.yaml",
    template_file="template.yaml",
    api_name="UsagiBooru Arts API",
    api_desc="Arts related api (required)"
):
    # Load template file
    with open(template_file, "r", encoding="utf8") as f:
        out = yaml.safe_load(f)
    # Load monolith document file
    with open(input_file, "r", encoding="utf8") as f:
        main = yaml.safe_load(f)

    # Set name and description of the document
    out["info"]["title"] = api_name
    out["info"]["description"] = api_desc

    # Parameters are shared
    out["components"]["parameters"] = main["components"]["parameters"]

    # Create short-hands
    out_schemas = out["components"]["schemas"]
    main_schemas = main["components"]["schemas"]
    global_tags = []

    # Input separate key
    # Loop in all paths
    for path_key in main["paths"]:
        if key in path_key:
            # Copy path
            out["paths"][path_key] = main["paths"][path_key]
            # Loop in all methods
            methods = out["paths"][path_key].keys()
            for method_key in methods:
                # Collect global tag
                if method_key != "parameters":
                    ref_method = main["paths"][path_key][method_key]
                    global_tags.append(ref_method["tags"][0])
    # Exit if couldn't find any path
    if len(out["paths"].keys()) < 1:
        print("The path didn't exist!")
        sys.exit()

    # Add global tags
    out["tags"] = [{"name": t} for t in list(set(global_tags))]

    # Get and copy schemas
    refs = getRefsFromDict(out)
    for ref in refs:
        out_schemas[ref] = main_schemas[ref]
    while len(refs) > 0:
        # Copy extra schemas
        refs = list(set(getRefsFromDict(out_schemas)) - set(refs))
        refs = list(set(refs)-set(list(out_schemas.keys())))
        # Add schemas
        for ref in refs:
            out_schemas[ref] = main_schemas[ref]

    # Export to document
    with open(out_file, "w", encoding="utf8") as f:
        yaml.dump(out, f, encoding='utf-8', allow_unicode=True)
    print(f"Saved to {out_file}!")


if __name__ == '__main__':
    key = input("Input path key: (Ex./arts/) >>")
    extractPath(key)
