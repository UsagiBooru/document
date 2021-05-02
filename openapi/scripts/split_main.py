from extract_path import extractPath
import os

optional_keys = [
    "/activitypub",
    "/garbage_collect",
    "/ml",
    "/navigations",
    "/news",
    "/ranking",
    "/report",
    "/scrape",
    "/token",
    "/wiki",
]
required_keys = [
    "/accounts",
    "/arts",
    "/catalog",
    "/invites",
    "/mylists",
    "/search",
    "/tags",
    "/upload",
]

keys = optional_keys + required_keys


if __name__ == "__main__":
    for i, keys in enumerate([required_keys, optional_keys]):
        for k in keys:
            name = k.replace("/", "")
            api_name = f"UsagiBooru {name.capitalize()} API"
            if i == 0:
                api_desc = f"{name.capitalize()} related api (required)"
                out_file = f"../separated/required-api/{name}.v1.yaml"
            else:
                api_desc = f"{name.capitalize()} related api (optional)"
                out_file = f"../separated/optional-api/{name}.v1.yaml"
            extractPath(
                k,
                input_file="../main.v1.yaml",
                out_file=out_file,
                api_name=api_name,
                api_desc=api_desc
            )
