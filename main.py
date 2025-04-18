from HW2_8 import DatabaseModel, Person, Student, Course, Enrollments
def main():
    while True:
        print("\n1. Добавить студента")
        print("2. Добавить курс")
        print("3. Записать студента на курс")
        print("4. Поставить оценку")
        print("5. Показать студентов с курсами и оценками")
        print("6. Показать курсы с записанными студентами")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Имя студента: ")
            age = int(input("Возраст: "))
            student = Student(name, age)
            student.save_to_db()
            print("Студент добавлен")

        elif choice == '2':
            title = input("Название курса: ")
            teacher = input("Имя преподавателя: ")
            course = Course(title, teacher)
            course.save_to_db()
            print("Курс добавлен")

        elif choice == '3':
            student_id = int(input("ID студента: "))
            course_id = int(input("ID курса: "))
            grades = None
            enrollment = Enrollments()
            enrollment.save_to_db(student_id, course_id, grades)
            print("Студент записан на курс")

        elif choice == "4":
                student_id = int(input("Введите ID студента: "))
                course_id = int(input("Введите ID курса: "))
                new_grade = input("Введите новую оценку: ")
                enrollment = Enrollments()
                enrollment.update_grade(student_id, course_id, new_grade)

                print("Оценка успешно обновлена.")
        

        elif choice == '5':
                enrollment = Enrollments()
                enrollment._cursor.execute("SELECT * FROM enrollments")
                print(enrollment._cursor.fetchall())
                data = enrollment.get_students_with_courses()
                if data:
                 print("\nСтуденты с их курсами и оценками:")
                 for full_name, course_title, grades in data:
                  print(f"{full_name} - {course_title} - Оценка- {grades}")

        
        
        elif choice == '6':
            enrollment = Enrollments()
            data = enrollment.get_courses_with_students()
            print("\nКурсы с записанными и оценками:")
            if data:
                for course_title, full_name, grades in data:
                 print(f"Курс: {course_title}, Студент: {full_name}, Оценка: {grades}")

        elif choice == '0':
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Повторите.")

       

if __name__ == '__main__':
    main()


if __name__ == "__main__":
   DatabaseModel.create_table()
