student_results = []

def collect_student_results(student_count):
    '''This asks for student's name and results'''
    for student in student_count:
        results = dict(
                    student_name = input(f"Enter student {student + 1}'s name: "),
                    drone_type = input("Enter in your drone type: "),
                    distance = input("Enter in distance travelled: "),
                    )
        student_results.append(results)
        
def print_student_results(results):
    '''Prints out each student's result'''
    for result in results:
        print(f"""
        Today's flight saw {result["student_name"]}'s fly their {result["drone_type"]}.
        Their drone travelled {result["distance"]}. It was great!
            """)

print("Welcome to student flight log!\n")
students = int(input("How many students are you logging today? "))
students = range(students)

collect_student_results(students)
print_student_results(student_results)