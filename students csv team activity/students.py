import csv


def main():
    print(read_dict("students.csv"))

    student = input("Enter a student ID: ")

    students_dictionary = read_dict("students.csv")

    if student in students_dictionary[student]: 
    #I am not that sure about this one 
    #but everything else works just fine

        print(students_dictionary[student])

    else:
        print("Invalid I-Number")



def read_dict(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    students_dict = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            if len(row_list) != 0:

                key = row_list[0]

                students_dict[key] = row_list[1]

    return students_dict



if __name__ == "__main__":
    main()