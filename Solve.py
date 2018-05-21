import pymysql
import wx
# import WorkFrame

hoster = '127.0.0.1'
porter = 3306
username = 'root'
pwd = 'yangly2008'
database = 'test'

def CreateStudentTable():
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
            create table student
            ( studentID char(10) not null,
              studentName varchar(20) not null,
              sex varchar(6) not null check(sex in (\"male\", \"female\")),
              entranceAge integer not null check(entranceAge >= 10 and entranceAge <= 50),
              entranceYear year not null,
              class varchar(20) not null,
              primary key(studentID) )
            """
            # sql = """
            # create table student
            # ( studentID char(10),
            #   primary key(studentID) )
            # """
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        conn.commit()
    finally:
        conn.close()

def CreateTeacherTable():
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
            create table teacher
            ( teacherID char(5) not null,
              teacherName varchar(20) not null,
              primary key(teacherID) )
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        conn.commit()
    finally:
        conn.close()

def CreateCourseTable():
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
            create table course
            ( courseID char(7) not null,
              courseName varchar(20) not null,
              teacherID char(5) not null,
              credit float(3,1) not null,
              grade integer not null check(grade >= 1 and grade <= 4),
              canceledYear year,
              primary key(courseID),
              foreign key(teacherID) references teacher(teacherID) on delete cascade on update cascade)
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        conn.commit()
    finally:
        conn.close()

def CreateCourseChooseTable():
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
               create table courseChoose
               ( studentID char(10) not null,
                 courseID char(7) not null,
                 chosenYear year not null,
                 score float(4,1) not null check(score >= 0 and score <= 100),
                 primary key(courseID, studentID),
                 foreign key(studentID) references student(studentID) on delete cascade on update cascade,
                 foreign key(courseID) references course(courseID) on delete cascade on update cascade
                 )
               """

            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        conn.commit()
    finally:
        conn.close()

def AddStudent(studentID, studentName, sex, entranceAge, entranceYear, studentClass):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
              insert into student values(%s, %s, %s, %s, %s, %s)
               """
            try:
                cursor.execute(sql, (studentID, studentName, sex, entranceAge, entranceYear, studentClass))
                result = cursor.fetchall()
                print(result)
            except:
                print('Insertion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def AddTeacher(teacherID, teacherName):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                 insert into teacher values(%s, %s)
                  """
            try:
                cursor.execute(sql, (teacherID, teacherName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Insertion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def AddCourse(courseID, courseName, teacherID, credit, grade, canceledYear=None):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            if(canceledYear == ""):
                canceledYear = None
            sql = """
                insert into course values(%s, %s, %s, %s, %s, %s)
                """

            try:
                cursor.execute(sql, (courseID, courseName, teacherID, credit, grade, canceledYear))
                result = cursor.fetchall()
                print(result)
            except:
                print('Insertion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def AddCourseChoose(studentID, courseID, teacherID, chosenYear, score):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sqlCurrentYear = """select  date_format(now(),'%Y')
                        """
            sqlEntranceYear = """
                                select entranceYear
                                from student
                                where studentID = %s
                                """
            sqlGrade = """
                        select grade
                        from course
                        where courseID = %s
                        """

            sqlCanceledYear = """
                               select canceledYear
                               from course
                               where courseID = %s
                                """
            sql = """
                    insert into courseChoose values(%s, %s, %s, %s, %s)
                     """
            sqlcheck = """
                        select *
                        from course as c
                        where c.teacherID = %s
                        and c.courseID = %s
                        
                        """
            try:

                cursor.execute(sqlCurrentYear)
                currentYear = cursor.fetchall()[0][0]
                # print(currentYear)
                cursor.execute(sqlEntranceYear,(studentID))
                entranceYear = cursor.fetchall()[0][0]
                # print(entranceYear)
                cursor.execute(sqlGrade,(courseID))
                grade = cursor.fetchall()[0][0]
                # print(grade)
                cursor.execute(sqlCanceledYear,(courseID))
                canceledYear = cursor.fetchall()[0][0]
                # print(canceledYear)

                if((int(currentYear)-int(entranceYear)>=int(grade)-1) and
                        ((canceledYear ==None) or (int(chosenYear)<int(canceledYear)))):
                    InputCheck = True
                else:
                    InputCheck = False
                    state = False
                    print('Insertion invaild')
                cursor.execute(sqlcheck, (teacherID, courseID))
                checkResult = cursor.fetchall()[0][0]
                if (checkResult == None):
                    InputCheck = False
                    state = False
                print(InputCheck)
                if(InputCheck):
                    cursor.execute(sql, (studentID, courseID, chosenYear, score))
                    result = cursor.fetchall()
                    print(result)
            except:
                print('Insertion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state



def DeleteStudent(studentID):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                    delete from student
                    where studentID = %s
                    """
            try:
                cursor.execute(sql, (studentID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Deletion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state

def DeleteTeacher(teacherID):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                    delete from teacher
                    where teacherID = %s
                    """
            try:
                cursor.execute(sql, (teacherID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Deletion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def DeleteCourse(courseID):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                    delete from course
                    where courseID = %s
                    """
            try:
                cursor.execute(sql, (courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Deletion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def DeleteCourseChoose(studentID, courseID):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                       delete from courseChoose
                       where studentID = %s and courseID = %s
                       """
            try:
                cursor.execute(sql, (studentID, courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Deletion failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def UpdateStudent(studentID, studentName, sex, entranceAge, entranceYear, studentClass):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sqlCurrentYear = """select  date_format(now(),'%Y')
                                   """
            sqlMinGrade = """
                            select min(c.grade)
                            from course as c, courseChoose as cc
                            where cc.courseID = c.courseID
                            and cc.studentID = %s
                        """

            sql = """
                          update student 
                          set studentName = %s, sex = %s, entranceAge = %s, entranceYear = %s, class = %s 
                          where studentID = %s
                          """
            try:

                cursor.execute(sqlCurrentYear)
                currentYear = cursor.fetchall()[0][0]
                print(currentYear)
                cursor.execute(sqlMinGrade,(studentID))
                minGrade = cursor.fetchall()[0][0]
                print(minGrade)
                if(minGrade == None or (int(currentYear) - int(entranceYear) >= int(minGrade) - 1) ):
                    InputCheck = True
                else:
                    InputCheck = False
                    state = False
                    print('Update invalid')
                print(InputCheck)
                if(InputCheck):
                    cursor.execute(sql, (studentName, sex, entranceAge, entranceYear, studentClass, studentID))
                    result = cursor.fetchall()
                    print(result)

            except:
                print('Update failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def UpdateTeacher(teacherID, teacherName):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          update teacher
                          set teacherName = %s 
                          where teacherID = %s
                          """
            try:
                cursor.execute(sql, (teacherName, teacherID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Update failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state


def UpdateCourse(courseID, courseName, teacherID, credit, grade, canceledYear=None):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        if( canceledYear == "" ):
            canceledYear = None
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'

            sqlCurrentYear = """select  date_format(now(),'%Y')
                                   """
            sqlMaxEntranceYear = """
                                select max(s.entranceYear)
                                from student as s, courseChoose as cc
                                where s.studentID = cc.studentID
                                and cc.courseID = %s
                                """
            sqlMaxChosenYear = """
                                select max(cc.chosenYear)
                                from courseChoose as cc
                                where cc.courseID = %s
                                """
            sql = """
                          update course
                          set courseName = %s, teacherID = %s, credit = %s, grade = %s, canceledYear = %s
                          where courseID = %s
                          """
            try:
                cursor.execute(sqlCurrentYear)
                currentYear = cursor.fetchall()[0][0]
                print(currentYear)
                cursor.execute(sqlMaxEntranceYear,(courseID))
                maxEntranceYear = cursor.fetchall()[0][0]
                print(maxEntranceYear)
                cursor.execute(sqlMaxChosenYear,(courseID))
                maxChosenYear = cursor.fetchall()[0][0]
                print(maxChosenYear)

                if((maxEntranceYear == None or int(currentYear)-int(maxEntranceYear)>= int(grade)-1 )
                        and (canceledYear == None or int(maxChosenYear)<int(canceledYear) )):
                    InputCheck = True
                    # print("Im In")
                else:
                    InputCheck = False
                    print("Update invalid")
                    state = False
                if(InputCheck):
                    cursor.execute(sql, (courseName, teacherID, credit, grade, canceledYear, courseID))
                    result = cursor.fetchall()
                    print(result)
            except:
                print('Update failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state

def UpdateCourseChoose(studentID, courseID, teacherID, chosenYear, score):
    state = True
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'

            sqlCurrentYear = """select  date_format(now(),'%Y')
                                   """
            sqlEntranceYear = """
                                           select entranceYear
                                           from student
                                           where studentID = %s
                                           """
            sqlGrade = """
                                   select grade
                                   from course
                                   where courseID = %s
                                   """

            sqlCanceledYear = """
                                          select canceledYear
                                          from course
                                          where courseID = %s
                                           """
            sql = """
                          update courseChoose
                          set  chosenYear = %s, score = %s
                          where studentID = %s and courseID = %s 
                          """
            sqlcheck = """
                                    select *
                                    from course as c
                                    where c.teacherID = %s
                                    and c.courseID = %s

                                    """
            try:


                cursor.execute(sqlCurrentYear)
                currentYear = cursor.fetchall()[0][0]
                # print(currentYear)
                cursor.execute(sqlEntranceYear, (studentID))
                entranceYear = cursor.fetchall()[0][0]
                # print(entranceYear)
                cursor.execute(sqlGrade, (courseID))
                grade = cursor.fetchall()[0][0]
                # print(grade)
                cursor.execute(sqlCanceledYear, (courseID))
                canceledYear = cursor.fetchall()[0][0]
                # print(canceledYear)

                if ((int(currentYear) - int(entranceYear) >= int(grade) - 1) and
                        ((canceledYear == None) or (int(chosenYear) < int(canceledYear)))):
                    InputCheck = True
                else:
                    InputCheck = False
                    state = False
                    print('Update invaild')
                cursor.execute(sqlcheck, (teacherID, courseID))
                checkResult = cursor.fetchall()[0][0]
                if (checkResult == None):
                    InputCheck = False
                    state = False
                print(InputCheck)
                if(InputCheck):
                    cursor.execute(sql, (chosenYear, score, studentID, courseID))
                    result = cursor.fetchall()
                    print(result)
            except:
                print('Update failed.')
                state = False
        conn.commit()
    finally:
        conn.close()
        return state

def StudentNameToStudent(studentName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from student
                          where studentName = %s
                          """
            try:
                cursor.execute(sql, (studentName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result

def StudentIDToStudent(studentID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from student
                          where studentID = %s
                          """
            try:
                cursor.execute(sql, (studentID))
                result = cursor.fetchall()
                print(result)

            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result

def StudentNameToCourseChoose(studentName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.studentID in
                            ( select s.studentID
                              from student as s
                              where s.studentName = %s )
                              and
                              c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (studentName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return(result)


def StudentIDToCourseChoose(studentID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
<<<<<<< HEAD
                          select cc.studentID, cc.courseID, c.teacherID, cc.chosenYear, cc.score
=======
                          select cc.studentID, cc.courseID, c.teacherID, cc.chosenYeaer, cc.score
>>>>>>> 2336b03c18fd912865bcb0f5af294cc536bfc9a9
                          from courseChoose as cc, course as c
                          where cc.studentID = %s
                          and c.courseID = cc.courseID
                          """
            try:
                cursor.execute(sql, (studentID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result



def StudentNameAndCourseNameToGrade(studentName, courseName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.studentID in
                            ( select studentID
                              from student
                              where studentName = %s )
                              and c.courseID in
                            ( select courseID
                              from course
                              where courseName = %s )
                              and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (studentName, courseName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def StudentNameAndCourseIDToGrade(studentName, courseID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.studentID in
                            ( select studentID
                              from student
                              where studentName = %s )
                              and c.courseID = %s
                              and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (studentName, courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def StudentIDAndCourseNameToGrade(studentID, courseName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.studentID = %s
                              and c.courseID in
                            ( select courseID
                              from course
                              where courseName = %s )
                              and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (studentID, courseName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def StudentIDAndCourseIDToGrade(studentID, courseID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.studentID = %s
                              and c.courseID = %s
                              and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (studentID, courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def CourseNameToCourse(courseName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from course
                          where courseName = %s
                          """
            try:
                cursor.execute(sql, (courseName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def CourseNameToCourseChoose(courseName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.courseID in
                            ( select courseID
                              from course
                              where courseName = %s)
                              and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (courseName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def CourseIDToCourse(courseID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from course
                          where courseID = %s
                          """
            try:
                cursor.execute(sql, (courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def CourseIDToCourseChoose(courseID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, c.courseID, co.teacherID, c.chosenYear, c.score
                          from courseChoose as c, course as co
                          where c.courseID = %s
                          and c.courseID = co.courseID
                          """
            try:
                cursor.execute(sql, (courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def TeacherNameToTeacher(teacherName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from teacher
                          where teacherName = %s
                          """
            try:
                cursor.execute(sql, (teacherName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def TeacherNameToCourseChoose(teacherName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select cc.studentID, cc.courseID, t.teacherID, cc.chosenYear, cc.score
                          from courseChoose as cc, course as c, teacher as t
                          where t.teacherID in
                            ( select teacherID
                              from teacher
                              where teacherName = %s )
                              and
                              t.teacherID = c.teacherID
                              and
                              c.courseID = cc.courseID
                          """
            try:
                cursor.execute(sql, (teacherName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def TeacherIDToTeacher(teacherID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from teacher
                          where teacherID = %s
                          """
            try:
                cursor.execute(sql, (teacherID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def TeacherIDToCourseChoose(teacherID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select cc.studentID, cc.courseID, c.teacherID, cc.chosenYear, cc.score
                          from courseChoose as cc, course as c
                          where c.teacherID = %s
                            and
                            c.courseID = cc.courseID
                          """
            try:
                cursor.execute(sql, (teacherID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def AnyStudentNameToScore(studentName):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select c.studentID, avg(c.score)
                          from courseChoose as c
                          where c.studentID in
                            ( select studentID
                              from student
                              where studentName = %s )
                          group by c.studentID
                          """
            try:
                cursor.execute(sql, (studentName))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def AnyStudentIDToScore(studentID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select avg(c.score)
                          from courseChoose as c
                          where c.studentID = %s
                          group by c.studentID
                          """
            try:
                cursor.execute(sql, (studentID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result

def ClassToScore(studentClass):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select avg(c.score)
                          from courseChoose as c
                          where c.studentID in
                            ( select studentID
                              from student
                              where class = %s )
                          """
            try:
                cursor.execute(sql, (studentClass))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def CourseToScore(courseID):
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select avg(c.score)
                          from courseChoose as c
                          where c.courseID = %s
                          """
            try:
                cursor.execute(sql, (courseID))
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def ShowAllStudents():
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select *
                          from student
                          """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def ShowAllStudentAvgScore():
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select avg(c.score)
                          from courseChoose as c
                          group by c.studentID
                          """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result

def ShowAllTeacher():
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                              select *
                              from teacher
                              """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result

def ShowAllCourse():
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                              select *
                              from course
                              """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def ShowAllCourseChoose():
    result = ()
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                              select cc.studentID, cc.courseID, c.teacherID, cc.chosenYear, cc.score
                              from courseChoose as cc, course as c
                              where cc.courseID = c.courseID
                              """
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
            except:
                print('Query failed.')
        conn.commit()
    finally:
        conn.close()
        return result


def IsStudentExist(studentID):
    result = []
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                          select studentName
                          from student
                          where studentID = %s
                          """
            try:
                cursor.execute(sql, (studentID))
                studentName = cursor.fetchall()
                if studentName == ():
                    result = (False, ())
                else:
                    result = (True, studentName)
                # print(result)
                # return result
            except:
                print('Query failed.')
                result = (False, None)
        conn.commit()
    finally:
        conn.close()
        return result

def IsTeacherExist(teacherID):
    result = []
    try:
        conn = pymysql.connect(host=hoster, port=porter, user=username, passwd=pwd, db=database)
        print('Connected successfully.')
        with conn.cursor() as cursor:
            # sql = 'INSERT INTO ZHUA VALUES (13, "BUGUAIZHUA", false);'
            sql = """
                              select teacherName
                              from teacher
                              where teacherID = %s
                              """
            try:
                cursor.execute(sql, (teacherID))
                teacherName = cursor.fetchall()
                if teacherName == ():
                    result = (False, ())
                else:
                    result = (True, teacherName)
                # print(result)
                # return result
            except:
                print('Query failed.')
                result = (False, None)
        conn.commit()
    finally:
        conn.close()
        return result

if __name__ == '__main__':
    pass
    # CreateStudentTable()
    # CreateTeacherTable()
    # CreateCourseTable()
    # CreateCourseChooseTable()
    # print(AddStudent("1234567399", "zzzzzzzzy", "female", "18", "2018", "16jichuang" ))
    # print(AddTeacher("12364", "zyy"))
    # AddCourse("1234567", "zzzzzzzy'c", "12364", "10.0", "2","2017")
    # AddCourseChoose("1234567394","1234567","12364", "2015", "10")
    # DeleteStudent("1234567890")
    # DeleteCourse("1224321")
    # DeleteTeacher("12345")
    # DeleteCourseChoose("1234567890", "1234567")
    # UpdateStudent("1234567394", "zzy", "male", "18", "2017", "16jichuang")
    # UpdateTeacher("12345","zzzy")
    # UpdateCourse("1234567", "zzy'c", "12364", "10.0", "4","2018")
    # UpdateCourseChoose("1234567394","1234567","12364", "2019", "20")
    # print(StudentNameToStudent("zzzzzzzy"))
    # StudentIDToStudent("1234567890")
    # StudentNameToCourseChoose("zzy")
    # StudentIDToCourseChoose("1234567890")
    # ShowAllStudents()
    # StudentNameAndCourseNameToGrade("zzy", "zzy'c")
    # StudentNameAndCourseIDToGrade("zzy", "1234567")
    # StudentIDAndCourseNameToGrade("1234567890", "zzy'c")
    # StudentIDAndCourseIDToGrade("1234567890", "1234567")
    # CourseNameToCourse("zzy'c")
    # CourseNameToCourseChoose("zzy'c")
    # CourseIDToCourse("1234567")
    # CourseIDToCourseChoose("1234567")
    # TeacherNameToTeacher("zyy")
    # TeacherNameToCourseChoose("zyy")
    # TeacherIDToTeacher("12344")
    # TeacherIDToCourseChoose("12344")
    # AnyStudentNameToScore("zzy")
    # AnyStudentIDToScore("1234567890")
    # ShowAllStudentAvgScore()
    # ClassToScore("16jichuang")
    # CourseToScore("1234567")
    # print(IsStudentExist("1234567395"))
    # print(IsTeacherExist("12345"))