key_dict = {
    "MALE": "Male",
    "FEMALE": "Female",
    "BLACK OR AFRICAN AMERICAN": "Black",
    "HISPANIC OR LATINO": "Hispanic/Latino",
    "AMERICAN INDIAN OR ALASKA NATIVE": "American Indian/Alaska Native",
    "ASIAN OR NATIVE HAWAIIAN/OTHER PACIFIC ISLANDER": "Asian/Hawaiian/Pacific Islander",
    "WHITE": "White",
    "MULTIRACIAL": "Multiracial",
    "ENGLISH LANGUAGE LEARNERS": "Learning English",
    "STUDENTS WITH DISABILITIES": "Disabilities",
    "ECONOMICALLY DISADVANTAGED": "Economically Disadvantaged",
    "MIGRANT": "Migrant",
    "HOMELESS": "Homeless",
    "FOSTER CARE": "Foster Care",
    "PARENT IN ARMED FORCES": "Parents In Armed Forces"
}

def switch_key(key):
    if key not in key_dict:
        return key
    return key_dict[key]

def int_or_null(i):
    if i == "—":
        return -1
    return int(i)