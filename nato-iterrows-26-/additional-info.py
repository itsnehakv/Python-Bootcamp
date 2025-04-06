student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.score)
    if row.student=="Angela":
        print(row.score)

# Keyword Method with iterrows(). Creating dictionary by iterating through dataframe (df).
{new_key:new_value for (index, row) in df.iterrows()}

