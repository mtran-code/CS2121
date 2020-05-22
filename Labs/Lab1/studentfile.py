# Implementation of the StudentFileReader ADT using a text file as the 
# input source in which each field is stored on a separate line.


class StudentRecord:
    def __init__(self, id_no=0, first_name=None, last_name=None, class_code=0, gpa=0.0):
        self.id_no = id_no
        self.first_name = first_name
        self.last_name = last_name
        self.class_code = class_code
        self.gpa = gpa

    # Establishing a string format (Used for debugging and showing student records).
    def __str__(self):
        return "ID Number: {0}\n" \
               "Name: {1} {2}\n" \
               "Class Code: {3}\n" \
               "GPA: {4}".format(self.id_no, self.first_name, self.last_name, self.class_code, self.gpa)


class StudentFileReader:
    # Create a new student reader instance.
    def __init__(self, inputFile):
        self.filename = inputFile
        self.file = None

    # Open a connection to the input file.
    def open(self):
        self.file = open(self.filename, "r")

    # Close the connection to the input file.
    def close(self):
        self.file.close()
        self.file = None

    # Extract all student records and store them in a list.
    def fetchAll(self):
        records = []
        student = self.fetchRecord()
        while student != None:
            records.append(student)
            student = self.fetchRecord()
        return records

        # Extract the next student record from the file.

    def fetchRecord(self):
        # Read the first line of the record.
        line = self.file.readline()
        if line == "":
            return None
        else:
            id_no, first_name, last_name, class_code, gpa = line.split(', ')

        # If there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.id_no = int(id_no)
        student.first_name = first_name
        student.last_name = last_name
        student.class_code = int(class_code)
        student.gpa = float(gpa)
        return student

    # Storage class used for an individual student record.


# TESTING THE CODE

personal_test_record = StudentRecord(12345, 'Michael', 'Tran', 2, 3.5)
# print(personal_test_record)

reader_test = StudentFileReader('students_lab1.txt')
reader_test.open()
record1 = reader_test.fetchRecord()
reader_test.close()
# print(record1)

reader_test = StudentFileReader('students_lab1.txt')
reader_test.open()
records = reader_test.fetchAll()
reader_test.close()
# print(records)
# print(str(records[0]) + "\n\n" + str(records[1]) + "\n\n" + str(records[2]))