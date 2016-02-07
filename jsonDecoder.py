import json
obj = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(obj)

print(
    obj[1]['bar'][0]
)
