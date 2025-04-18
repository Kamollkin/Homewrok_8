import sqlite3
class DatabaseModel:
   _conn = sqlite3.connect("college.db")
   _cursor = _conn.cursor()

   @classmethod
   def save(cls):
      cls._conn.commit()
   


class Person:
   def __init__(self, full_name,age):
      self._full_name = full_name
      self._age = age

   def get_full_name(self):
      return self._full_name
   
   def get_age(self):
      return self._age
   
   def set_full_name(self,name):
      self._full_name = name
   
   def set_age(self,age):
      self._age = age


   
class Student(Person, DatabaseModel):
   def __init__(self, full_name, age):
      super().__init__(full_name, age)

   def _create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        self.save()

   def save_to_db(self):
        self._cursor.execute("INSERT INTO students( full_name, age)VALUES (?, ?)", (self.get_full_name(), self.get_age()))
        self.save()

   def info(self):
      return f"Студент {self.__id}: {self.get_full_name()},Возраст : {self.get_age()}"

   
   
class Course(DatabaseModel):
   def __init__(self,title, teacher):
      self.__title = title
      self._teacher = teacher
      super().__init__()
   
   
   def get_course_title(self):
      return self.__title
   
   def set_course_title(self, title):
        self.__title = title

   def get_course_teacher(self):
      return self._teacher
   
   def set_course_teacher(self, teacher):
        self._teacher = teacher
      
   def _create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                teacher TEXT
            )
        ''')
        self.save()
   
   def save_to_db(self):
        self._cursor.execute('INSERT INTO courses (title, teacher) VALUES (?, ?)',
                             (self.get_course_title(), self.get_course_teacher()))
        self.save()

   def info(self):
        return f"Курс: {self.get_title()}, Преподаватель: {self.get_teacher()}"

   
class Enrollments(DatabaseModel):
    def __init__(self, grades=None):
        self.__grades = grades

    def _create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                grades TEXT,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id)
            )
        ''')
        self.save()

    def save_to_db(self, student_id, course_id, grades=None):
        self._cursor.execute(
            'INSERT INTO enrollments (student_id, course_id, grades) VALUES (?, ?, ?)',
            (student_id, course_id, grades)
        )
        self.save()

    def update_grade(self, student_id, course_id, new_grade):
        self._cursor.execute('''
            UPDATE enrollments
            SET grades = ?
            WHERE student_id = ? AND course_id = ?
        ''', (new_grade, student_id, course_id))
        self.save()

    def get_students_with_courses(self):
        self._cursor.execute('''
            SELECT students.full_name, courses.title, enrollments.grades
            FROM enrollments
            JOIN students ON enrollments.student_id = students.id
            JOIN courses ON enrollments.course_id = courses.id
        ''')
        return self._cursor.fetchall()
      
    def get_courses_with_students(self):
       self._cursor.execute(''' 
            SELECT courses.title, students.full_name, enrollments.grades
            FROM enrollments
            JOIN courses ON enrollments.course_id = courses.id
            JOIN students ON enrollments.student_id = students.id
            ORDER BY courses.title
                            
                            ''')
       return self._cursor.fetchall()

    def get_grades(self):
        return self.__grades
   
    def set_grades(self, grades):
       self.__grades = grades
       

   
   


   


   

    




    