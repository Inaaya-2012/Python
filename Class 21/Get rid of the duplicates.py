student = {
    "id1":{
        "name":"Sara",
        "grade":"8",
        "subject":['English','Maths','Science']
    },
    "id2":{
        "name":"Gabriella",
        "grade":"8",
        "subject":['German','Maths','Science']
    },
    "id3":{
        "name":"Sara",
        "grade":"8",
        "subject":['English','Maths','Science']
    },
    "id4":{
        "name":"Peter",
        "grade":"8",
        "subject":['German','Maths','Sanskrit']
    }
}

result = {}
for key, value in student.items():
    if value not in result.values():
        result[key] = value

print("Without duplicates")
print(result)        