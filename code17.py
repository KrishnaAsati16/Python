student = {
    "name": "kaju",
    "subjects": {
        "phy": 97,
        "chem": 89,
        "math": 95
    }
}

#Method Dictonary

print(len(student))
print(list(student.keys())) # return all keys


print(student.values()) # return all val


print(list(student.items())) # return all(key,val) pairs of tuple
#print(pairs[0])


print(student['name'])
print(student.get('name'))  # return the keys acc to val


student.update({'city : "delhi'})
print(student)  #cinsert the specified items to the dictionary


