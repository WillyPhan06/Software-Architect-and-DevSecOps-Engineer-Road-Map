import json

info_dict = {"name": "Willy", "age": "100", "languages": ["English", "Vietnamese"]}
info_json = json.dumps(info_dict, indent=2)
print(info_json)

subject_json = '{"subject": "math", "color":"blue", "score":100}'
subject_dict = json.loads(subject_json)
print(subject_dict["score"])

