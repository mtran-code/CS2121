# Produces a student report from data extracted from an external source.
from studentfile import StudentFileReader

# Name of the file to open.
FILE_NAME = "students_lab1.txt"


def main():
    # Extract the student records from the given text file.
    reader = StudentFileReader(FILE_NAME)
    reader.open()
    student_list = reader.fetchAll()
    reader.close()

    # Sort the list by id number. Each object is passed to the lambda
    # expression which returns the idNum field of the object.
    student_list.sort(key=lambda rec: rec.gpa, reverse=True)

    # Print the student report.
    printReport(student_list)


# Prints the student report.  
def printReport(theList):
    # The class names associated with the class codes.
    class_names = (None, "Freshman", "Sophomore", "Junior", "Senior")

    # Print the header.
    print("LIST OF STUDENTS".center(50))
    print("")
    print("%-5s  %-25s  %-10s  %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
    print("%5s  %25s  %10s  %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    # Print the body.
    for record in theList:
        print("%5d  %-25s  %-10s  %4.2f" %
              (record.id_no,
               record.last_name + ', ' + record.first_name,
               class_names[record.class_code], record.gpa))
    # Add a footer.
    print("-" * 50)
    print("Number of students:", len(theList))


# Executes the main routine.
main()
