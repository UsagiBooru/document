import yaml

with open("main.v1.yaml", "r", encoding="utf8") as f:
    oa = yaml.load(f)

ref = input("Input struct key: (Ex. ArtistStruct) >>")

data = str(
    oa["components"]["schemas"][ref]
).replace(
    "'", '"'
).replace(
    "False", 'false'
).replace(
    'True', 'true'
)
print(f'"{ref}": {data}')
