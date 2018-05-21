# -*- encoding: utf-8 -*-

import wx
import sys
import LoginFrame
import Solve

class Frame(wx.Frame):

    def __init__(self, parent,userName,userType):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"WORK", pos=(200, 80),
                          size=wx.Size(800, 640), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(800, 640), wx.Size(800, 640))

        panel = wx.Panel(self, id=wx.ID_ANY, pos=(0, 0), size=(800, 120))

        imageSchoolBadge = wx.Image("schoolBadge1.png", wx.BITMAP_TYPE_ANY)
        imageSchoolBadge = imageSchoolBadge.Scale(70, 70)
        temp = imageSchoolBadge.ConvertToBitmap()
        self.bmpSchoolBadge = wx.StaticBitmap(panel, bitmap=temp, pos=(10, 5), size=(70, 70))

        imageSmallCat = wx.Image("smallcat.png", wx.BITMAP_TYPE_PNG)
        imageSmallCat = imageSmallCat.Scale(185, 210)
        temp = imageSmallCat.ConvertToBitmap()
        self.bmpSmallCat = wx.StaticBitmap(panel, bitmap=temp, pos=(597, -80), size=(185, 210))
        self.textTitle = LoginFrame.TransparentText(panel, id=wx.ID_ANY, label=u"SWS Student Management System",
                                                    pos=(100, 25),
                                                    size=(100, 50))
        font = wx.Font(23, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.textTitle.SetFont(font)

        # self.textWelcome = wx.StaticText(panel, id=wx.ID_ANY, label=u"Welcome "+ userName + "!", pos=(300, 10), size=(470, 20), style=wx.ALIGN_RIGHT)


        self.buttonStudent = wx.Button(panel, id=wx.ID_ANY, label=u"Student", pos=(0, 80), size=wx.DefaultSize, style=0)
        self.buttonTeacher = wx.Button(panel, id=wx.ID_ANY, label=u"Teacher", pos=(112, 80), size=wx.DefaultSize, style=0)
        self.buttonCourse = wx.Button(panel, id=wx.ID_ANY, label=u"Course", pos=(224, 80), size=wx.DefaultSize, style=0)
        self.buttonSelect = wx.Button(panel, id=wx.ID_ANY, label=u"Select", pos=(336, 80), size=wx.DefaultSize, style=0)
        self.buttonStatistics = wx.Button(panel, id=wx.ID_ANY, label=u"Statistics", pos=(448, 80), size=wx.DefaultSize, style=0)

        self.panelStudent = wx.Panel(self, id=wx.ID_ANY, pos=(0, 121), size=(800, 520))
        # self.panelStudent.Hide()
        self.panelTeacher = wx.Panel(self, id=wx.ID_ANY, pos=(0, 121), size=(800, 520))
        self.panelTeacher.Hide()
        self.panelCourse = wx.Panel(self, id=wx.ID_ANY, pos=(0, 121), size=(800, 520))
        self.panelCourse.Hide()
        self.panelSelect = wx.Panel(self, id=wx.ID_ANY, pos=(0, 121), size=(800, 520))
        self.panelSelect.Hide()
        self.panelStatistics = wx.Panel(self, id=wx.ID_ANY, pos=(0, 121), size=(800, 520))
        self.panelStatistics.Hide()

# 输入设置

        self.inputTextSize = (100,23)
        self.inputInputSize = (100,23)
        self.inputA11TextPosition = (0,10)
        self.inputA11InputPosition = (110,8)
        self.inputA12TextPosition = (220, 10) # 250 10
        self.inputA12InputPosition = (330, 8) # 360 8

        self.inputA21TextPosition = (0, 40)
        self.inputA21InputPosition = (110, 38)
        self.inputA22TextPosition = (220, 40)
        self.inputA22InputPosition = (330, 38)

        self.inputA31TextPosition = (0, 70)
        self.inputA31InputPosition = (110, 68)
        self.inputA32TextPosition = (220, 70)
        self.inputA32InputPosition = (330, 68)

# p1

        self.p1StudentName = wx.StaticText(self.panelStudent, id = wx.ID_ANY, label = u"Student Name", pos = self.inputA11TextPosition, size=self.inputTextSize, style = wx.ALIGN_RIGHT)
        self.p1StudentNameInput = wx.TextCtrl( self.panelStudent, id = wx.ID_ANY, value = u"", pos = self.inputA11InputPosition,size = self.inputInputSize )
        self.p1StudentID = wx.StaticText(self.panelStudent, id=wx.ID_ANY, label=u"Student ID", pos=self.inputA12TextPosition,size=self.inputTextSize, style = wx.ALIGN_RIGHT)
        self.p1StudentIDInput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=self.inputA12InputPosition, size= self.inputInputSize)


        self.p1ButtonQuery = wx.Button(self.panelStudent, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28), style=0)
        self.p1ButtonDelete = wx.Button(self.panelStudent, id=wx.ID_ANY, label=u"Delete", pos=(620, 3), size=(80, 28), style=0)
        self.p1ButtonAdd = wx.Button(self.panelStudent, id=wx.ID_ANY, label=u"Add", pos=(460, 3), size=(80, 28), style=0)
        self.p1ButtonModify = wx.Button(self.panelStudent, id=wx.ID_ANY, label=u"Modify", pos=(540, 3), size=(80, 28), style=0)
        self.p1ButtonConfirm = wx.Button(self.panelStudent, id=wx.ID_ANY, label=u"Confirm", pos=(700, 438), size=(80, 28), style=0)


        self.p1StudentIDOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(5, 443), size=(120, 20))
        self.p1StudentNameOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(140, 443), size=(100, 20))
        self.p1EntranceAgeOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(260, 443), size=(100, 20))
        self.p1EntranceYearOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(380, 443), size=(100, 20))
        self.p1ClassOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(500, 443), size=(100, 20))
        self.p1SexOutput = wx.TextCtrl(self.panelStudent, id=wx.ID_ANY, value=u"", pos=(620, 443), size=(70, 20))

        self.p1StudentList = wx.ListCtrl(self.panelStudent, -1, pos=(0,35),size=(785,400) ,style=wx.LC_REPORT)
        self.p1StudentList.InsertColumn(0, "Student ID")
        self.p1StudentList.InsertColumn(1, "Student Name")
        self.p1StudentList.InsertColumn(2, "Entrance Age")
        self.p1StudentList.InsertColumn(3, "Entrance Year")
        self.p1StudentList.InsertColumn(4, "Class")
        self.p1StudentList.InsertColumn(5, "Sex")


        self.p1StudentList.SetColumnWidth(0, 135)  # 设置每一列的宽度
        self.p1StudentList.SetColumnWidth(1, 120)
        self.p1StudentList.SetColumnWidth(2, 120)
        self.p1StudentList.SetColumnWidth(3, 120)
        self.p1StudentList.SetColumnWidth(4, 120)
        self.p1StudentList.SetColumnWidth(5, 166)


# p2

        self.p2TeacherName = wx.StaticText(self.panelTeacher, id=wx.ID_ANY, label=u"Teacher Name",
                                           pos=self.inputA11TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p2TeacherNameInput = wx.TextCtrl(self.panelTeacher, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA11InputPosition, size=self.inputInputSize)
        self.p2TeacherID = wx.StaticText(self.panelTeacher, id=wx.ID_ANY, label=u"Teacher ID",
                                         pos=self.inputA12TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p2TeacherIDInput = wx.TextCtrl(self.panelTeacher, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA12InputPosition, size=self.inputInputSize)
        self.p2ButtonQuery = wx.Button(self.panelTeacher, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
                                        style=0)
        self.p2ButtonDelete = wx.Button(self.panelTeacher, id=wx.ID_ANY, label=u"Delete", pos=(620, 3), size=(80, 28),
                                       style=0)
        self.p2ButtonAdd = wx.Button(self.panelTeacher, id=wx.ID_ANY, label=u"Add", pos=(460, 3), size=(80, 28),
                                     style=0)
        self.p2ButtonModify = wx.Button(self.panelTeacher, id=wx.ID_ANY, label=u"Modify", pos=(540, 3), size=(80, 28),
                                        style=0)
        self.p2ButtonConfirm = wx.Button(self.panelTeacher, id=wx.ID_ANY, label=u"Confirm", pos=(700, 438),
                                         size=(80, 28), style=0)
        self.p2TeacherIDOutput = wx.TextCtrl(self.panelTeacher, id=wx.ID_ANY, value=u"", pos=(5, 443), size=(120, 20))
        self.p2TeacherNameOutput = wx.TextCtrl(self.panelTeacher, id=wx.ID_ANY, value=u"", pos=(140, 443),
                                               size=(100, 20))

        self.p2TeacherList = wx.ListCtrl(self.panelTeacher, -1, pos=(0, 35), size=(785, 400), style=wx.LC_REPORT)
        self.p2TeacherList.InsertColumn(0, "Teacher ID")
        self.p2TeacherList.InsertColumn(1, "Teacher Name")

        self.p2TeacherList.SetColumnWidth(0, 135)  # 设置每一列的宽度
        self.p2TeacherList.SetColumnWidth(1, 650)

# p3

        self.p3CourseName = wx.StaticText(self.panelCourse, id=wx.ID_ANY, label=u"Course Name",
                                           pos=self.inputA11TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p3CourseNameInput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA11InputPosition, size=self.inputInputSize)
        self.p3CourseID = wx.StaticText(self.panelCourse, id=wx.ID_ANY, label=u"Course ID",
                                         pos=self.inputA12TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p3CourseIDInput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA12InputPosition, size=self.inputInputSize)

        self.p3ButtonQuery = wx.Button(self.panelCourse, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
                                        style=0)
        self.p3ButtonDelete = wx.Button(self.panelCourse, id=wx.ID_ANY, label=u"Delete", pos=(620, 3), size=(80, 28),
                                       style=0)
        self.p3ButtonAdd = wx.Button(self.panelCourse, id=wx.ID_ANY, label=u"Add", pos=(460, 3), size=(80, 28),
                                     style=0)
        self.p3ButtonModify = wx.Button(self.panelCourse, id=wx.ID_ANY, label=u"Modify", pos=(540, 3), size=(80, 28),
                                        style=0)

        self.p3CourseIDOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(5, 443), size=(100, 20))
        self.p3CourseNameOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(125, 443),
                                               size=(100, 20))
        self.p3TeacherIDOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(245, 443),
                                               size=(100, 20))
        self.p3CreditOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(360, 443),
                                                size=(80, 20))
        self.p3GradeOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(450, 443), size=(80, 20))
        self.p3CanceledYearOutput = wx.TextCtrl(self.panelCourse, id=wx.ID_ANY, value=u"", pos=(535, 443), size=(100, 20))

        self.p3ButtonConfirm = wx.Button(self.panelCourse, id=wx.ID_ANY, label=u"Confirm", pos=(700, 438),
                                         size=(80, 28), style=0)

        self.p3CourseList = wx.ListCtrl(self.panelCourse, -1, pos=(0, 35), size=(785, 400), style=wx.LC_REPORT)
        self.p3CourseList.InsertColumn(0, "Course ID")
        self.p3CourseList.InsertColumn(1, "Course Name")
        self.p3CourseList.InsertColumn(2, "Teacher ID")
        self.p3CourseList.InsertColumn(3, "Credit")
        self.p3CourseList.InsertColumn(4, "Grade")
        self.p3CourseList.InsertColumn(5, "Canceled Year")

        self.p3CourseList.SetColumnWidth(0, 120)  # 设置每一列的宽度
        self.p3CourseList.SetColumnWidth(1, 120)
        self.p3CourseList.SetColumnWidth(2, 120)
        self.p3CourseList.SetColumnWidth(3, 90)
        self.p3CourseList.SetColumnWidth(4, 80)
        self.p3CourseList.SetColumnWidth(5, 253)

# p4

        self.p4StudentName = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Student Name",
                                           pos=self.inputA11TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4StudentNameInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA11InputPosition, size=self.inputInputSize)
        self.p4StudentID = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Student ID",
                                         pos=self.inputA12TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4StudentIDInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA12InputPosition, size=self.inputInputSize)

        self.p4TeacherName = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Teacher Name",
                                           pos=self.inputA21TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4TeacherNameInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA21InputPosition, size=self.inputInputSize)
        self.p4TeacherID = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Teacher ID",
                                         pos=self.inputA22TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4TeacherIDInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                            pos=self.inputA22InputPosition, size=self.inputInputSize)

        self.p4CourseName = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Course Name",
                                           pos=self.inputA31TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4CourseNameInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA31InputPosition, size=self.inputInputSize)
        self.p4CourseID = wx.StaticText(self.panelSelect, id=wx.ID_ANY, label=u"Course ID",
                                         pos=self.inputA32TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p4CourseIDInput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"",
                                            pos=self.inputA32InputPosition, size=self.inputInputSize)

        self.p4ButtonQuery = wx.Button(self.panelSelect, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
                                        style=0)
        self.p4ButtonDelete = wx.Button(self.panelSelect, id=wx.ID_ANY, label=u"Delete", pos=(620, 3), size=(80, 28),
                                       style=0)
        self.p4ButtonAdd = wx.Button(self.panelSelect, id=wx.ID_ANY, label=u"Add", pos=(460, 3), size=(80, 28),
                                     style=0)
        self.p4ButtonModify = wx.Button(self.panelSelect, id=wx.ID_ANY, label=u"Modify", pos=(540, 3), size=(80, 28),
                                        style=0)

        self.p4StudentIDOutput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"", pos=(5, 443), size=(100, 20))
        self.p4TeacherIDOutput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"", pos=(125, 443),
                                              size=(100, 20))
        self.p4CourseIDOutput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"", pos=(245, 443),
                                             size=(100, 20))
        self.p4SelectYearOutput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"", pos=(360, 443),
                                          size=(100, 20))
        self.p4GradeOutput = wx.TextCtrl(self.panelSelect, id=wx.ID_ANY, value=u"", pos=(480, 443), size=(80, 20))

        self.p4ButtonConfirm = wx.Button(self.panelSelect, id=wx.ID_ANY, label=u"Confirm", pos=(700, 438),
                                         size=(80, 28), style=0)


        self.p4SelectList = wx.ListCtrl(self.panelSelect, -1, pos=(0, 95), size=(785, 340), style=wx.LC_REPORT)
        self.p4SelectList.InsertColumn(0, "Student ID")
        self.p4SelectList.InsertColumn(1, "Teacher ID")
        self.p4SelectList.InsertColumn(2, "Course ID")
        self.p4SelectList.InsertColumn(3, "Select Year")
        self.p4SelectList.InsertColumn(4, "Score")

        self.p4SelectList.SetColumnWidth(0, 120)  # 设置每一列的宽度
        self.p4SelectList.SetColumnWidth(1, 120)
        self.p4SelectList.SetColumnWidth(2, 120)
        self.p4SelectList.SetColumnWidth(3, 120)
        self.p4SelectList.SetColumnWidth(4, 304)

# p5
        self.p5StudentName = wx.StaticText(self.panelStatistics, id=wx.ID_ANY, label=u"Student Name",
                                           pos=self.inputA11TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p5StudentNameInput = wx.TextCtrl(self.panelStatistics, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA11InputPosition, size=self.inputInputSize)
        self.p5StudentID = wx.StaticText(self.panelStatistics, id=wx.ID_ANY, label=u"Student ID",
                                         pos=self.inputA12TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p5StudentIDInput = wx.TextCtrl(self.panelStatistics, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA12InputPosition, size=self.inputInputSize)

        self.p5Class = wx.StaticText(self.panelStatistics, id=wx.ID_ANY, label=u"Class",
                                           pos=self.inputA21TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p5ClassInput = wx.TextCtrl(self.panelStatistics, id=wx.ID_ANY, value=u"",
                                              pos=self.inputA21InputPosition, size=self.inputInputSize)
        self.p5CourseID = wx.StaticText(self.panelStatistics, id=wx.ID_ANY, label=u"Course ID",
                                         pos=self.inputA22TextPosition, size=self.inputTextSize, style=wx.ALIGN_RIGHT)
        self.p5CourseIDInput = wx.TextCtrl(self.panelStatistics, id=wx.ID_ANY, value=u"",
                                            pos=self.inputA22InputPosition, size=self.inputInputSize)


        self.p5ButtonQuery = wx.Button(self.panelStatistics, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
                                        style=0)
        # self.p5ButtonQuery = wx.Button(self.panelStatistics, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
        #                                style=0)
        # self.p5ButtonQuery = wx.Button(self.panelStatistics, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
        #                                style=0)
        # self.p5ButtonQuery = wx.Button(self.panelStatistics, id=wx.ID_ANY, label=u"Query", pos=(700, 3), size=(80, 28),
        #                                style=0)
        # self.p5StatisticsList = wx.ListCtrl( self.panelStatistics, id=wx.ID_ANY, pos=(0, 65), size=(785, 405), style=wx.LC_REPORT)
        # self.p5StatisticsList.InsertColumn(0, "Student ID")
        # self.p5StatisticsList.InsertColumn(1, "Average score")
        # self.p5StatisticsList.SetColumnWidth(0, 160)
        # self.p5StatisticsList.SetColumnWidth(1, 170)


        # self.Show()

# Bind
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.buttonStudent.Bind(wx.EVT_BUTTON, self.PressStudent)
        self.buttonTeacher.Bind(wx.EVT_BUTTON, self.PressTeacher)
        self.buttonCourse.Bind(wx.EVT_BUTTON, self.PressCourse)
        self.buttonSelect.Bind(wx.EVT_BUTTON, self.PressSelect)
        self.buttonStatistics.Bind(wx.EVT_BUTTON, self.PressStatistics)

# initial function
        self.isAddORModify = ""
        self.userType = userType
        # self.userType = "administrator" # teacher / student
        self.userAuthority()
        self.disableAll()

#p1 Bind

        self.p1ButtonAdd.Bind(wx.EVT_BUTTON,  self.p1PressAddButton)
        self.p1ButtonModify.Bind(wx.EVT_BUTTON, self.p1PressModifyButton)
        self.p1ButtonDelete.Bind(wx.EVT_BUTTON, self.p1PressDeleteButton)
        self.p1ButtonQuery.Bind(wx.EVT_BUTTON, self.p1PressQueryButton)
        self.p1ButtonConfirm.Bind(wx.EVT_BUTTON, self.p1PressConfirmButton)

        self.p1StudentList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.p1ListFocus)
        self.p1StudentList.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.p1ListNoFocus)


# p2 Bind
        self.p2ButtonAdd.Bind(wx.EVT_BUTTON, self.p2PressAddButton)
        self.p2ButtonModify.Bind(wx.EVT_BUTTON, self.p2PressModifyButton)
        self.p2ButtonDelete.Bind(wx.EVT_BUTTON, self.p2PressDeleteButton)
        self.p2ButtonQuery.Bind(wx.EVT_BUTTON, self.p2PressQueryButton)
        self.p2ButtonConfirm.Bind(wx.EVT_BUTTON, self.p2PressConfirmButton)

        self.p2TeacherList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.p2ListFocus)
        self.p2TeacherList.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.p2ListNoFocus)

# p3 Bind
        self.p3ButtonAdd.Bind(wx.EVT_BUTTON, self.p3PressAddButton)
        self.p3ButtonModify.Bind(wx.EVT_BUTTON, self.p3PressModifyButton)
        self.p3ButtonDelete.Bind(wx.EVT_BUTTON, self.p3PressDeleteButton)
        self.p3ButtonQuery.Bind(wx.EVT_BUTTON, self.p3PressQueryButton)
        self.p3ButtonConfirm.Bind(wx.EVT_BUTTON, self.p3PressConfirmButton)

        self.p3CourseList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.p3ListFocus)
        self.p3CourseList.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.p3ListNoFocus)

# p4 Bind
        self.p4ButtonAdd.Bind(wx.EVT_BUTTON, self.p4PressAddButton)
        self.p4ButtonModify.Bind(wx.EVT_BUTTON, self.p4PressModifyButton)
        self.p4ButtonDelete.Bind(wx.EVT_BUTTON, self.p4PressDeleteButton)
        self.p4ButtonQuery.Bind(wx.EVT_BUTTON, self.p4PressQueryButton)
        self.p4ButtonConfirm.Bind(wx.EVT_BUTTON, self.p4PressConfirmButton)

        self.p4SelectList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.p4ListFocus)
        self.p4SelectList.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.p4ListNoFocus)

# p5 Bind
        self.p5ButtonQuery.Bind(wx.EVT_BUTTON, self.p5PressQueryButton)

#total def

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.BLACK_PEN)
        dc.DrawLine(0, 120, 800, 120)

    def PressStudent(self, event):
        self.buttonStudent.SetBackgroundColour(wx.WHITE)
        self.buttonTeacher.SetBackgroundColour((240, 240, 240, 255))
        self.buttonCourse.SetBackgroundColour((240, 240, 240, 255))
        self.buttonSelect.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStatistics.SetBackgroundColour((240, 240, 240, 255))
        self.panelStudent.Show()
        self.panelTeacher.Hide()
        self.panelCourse.Hide()
        self.panelSelect.Hide()
        self.panelStatistics.Hide()

        self.disableAll()

    def PressTeacher(self, event):
        self.buttonTeacher.SetBackgroundColour(wx.WHITE)
        self.buttonStudent.SetBackgroundColour((240, 240, 240, 255))
        self.buttonCourse.SetBackgroundColour((240, 240, 240, 255))
        self.buttonSelect.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStatistics.SetBackgroundColour((240, 240, 240, 255))
        self.panelStudent.Hide()
        self.panelTeacher.Show()
        self.panelCourse.Hide()
        self.panelSelect.Hide()
        self.panelStatistics.Hide()

        self.disableAll()

    def PressCourse(self, event):
        self.buttonCourse.SetBackgroundColour(wx.WHITE)
        self.buttonTeacher.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStudent.SetBackgroundColour((240, 240, 240, 255))
        self.buttonSelect.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStatistics.SetBackgroundColour((240, 240, 240, 255))
        self.panelStudent.Hide()
        self.panelTeacher.Hide()
        self.panelCourse.Show()
        self.panelSelect.Hide()
        self.panelStatistics.Hide()

        self.disableAll()

    def PressSelect(self, event):
        self.buttonSelect.SetBackgroundColour(wx.WHITE)
        self.buttonTeacher.SetBackgroundColour((240, 240, 240, 255))
        self.buttonCourse.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStudent.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStatistics.SetBackgroundColour((240, 240, 240, 255))
        self.panelStudent.Hide()
        self.panelTeacher.Hide()
        self.panelCourse.Hide()
        self.panelSelect.Show()
        self.panelStatistics.Hide()

        self.disableAll()

    def PressStatistics(self, event):
        self.buttonStatistics.SetBackgroundColour(wx.WHITE)
        self.buttonTeacher.SetBackgroundColour((240, 240, 240, 255))
        self.buttonCourse.SetBackgroundColour((240, 240, 240, 255))
        self.buttonStudent.SetBackgroundColour((240, 240, 240, 255))
        self.buttonSelect.SetBackgroundColour((240, 240, 240, 255))
        self.panelStudent.Hide()
        self.panelTeacher.Hide()
        self.panelCourse.Hide()
        self.panelSelect.Hide()
        self.panelStatistics.Show()

#p1 def

    def p1PressAddButton(self, event ):

        # print("enter p1pressAddButton()")
        self.p1ButtonConfirm.Enable()
        self.p1StudentIDOutput.Enable()
        self.p1StudentNameOutput.Enable()
        self.p1EntranceAgeOutput.Enable()
        self.p1EntranceYearOutput.Enable()
        self.p1ClassOutput.Enable()
        self.p1SexOutput.Enable()
        self.isAddORModify = "Add"
        self.clearAllOutput()
        # print("p1PressAddButton "+ self.isAddORModify)

    def p1PressModifyButton(self, event):
        self.p1ButtonConfirm.Enable()
        self.p1StudentIDOutput.Disable()
        self.p1StudentNameOutput.Enable()
        self.p1EntranceAgeOutput.Enable()
        self.p1EntranceYearOutput.Enable()
        self.p1ClassOutput.Enable()
        self.p1SexOutput.Enable()


        item = self.p1StudentList.GetFocusedItem()
        # print(self.p1StudentList.GetItemText(item, 1))
        self.p1StudentIDOutput.SetValue(self.p1StudentList.GetItemText(item, 0))
        self.p1StudentNameOutput.SetValue(self.p1StudentList.GetItemText(item, 1))
        self.p1EntranceAgeOutput.SetValue(self.p1StudentList.GetItemText(item, 2))
        self.p1EntranceYearOutput.SetValue(self.p1StudentList.GetItemText(item, 3))
        self.p1ClassOutput.SetValue(self.p1StudentList.GetItemText(item, 4))
        self.p1SexOutput.SetValue(self.p1StudentList.GetItemText(item, 5))


        self.isAddORModify = "Modify"

    def p1PressDeleteButton(self, event):
        self.p1ButtonConfirm.Disable()
        self.p1StudentIDOutput.Disable()
        self.p1StudentNameOutput.Disable()
        self.p1EntranceAgeOutput.Disable()
        self.p1EntranceYearOutput.Disable()
        self.p1ClassOutput.Disable()
        self.p1SexOutput.Disable()
        self.p1IsDelete = wx.MessageDialog(self,"Are you sure to delete it ?","Delete",wx.YES_NO )
        if self.p1IsDelete.ShowModal() == wx.ID_YES:
            print("self.p1IsDelete.ShowModal() == wx.ID_YES:")
            item = self.p1StudentList.GetFocusedItem()
            Solve.DeleteStudent(self.p1StudentList.GetItemText(item, 0))
            self.p1StudentList.DeleteAllItems()
        self.p1ButtonDelete.Disable()
        self.p1ButtonModify.Disable()

    def p1PressQueryButton(self, event):

        self.p1StudentList.DeleteAllItems()
        self.clearAllOutput()
        self.p1ButtonDelete.Disable()
        self.p1ButtonModify.Disable()
        self.p1ButtonConfirm.Disable()
        self.p1StudentIDOutput.Disable()
        self.p1StudentNameOutput.Disable()
        self.p1EntranceAgeOutput.Disable()
        self.p1EntranceYearOutput.Disable()
        self.p1ClassOutput.Disable()
        self.p1SexOutput.Disable()

        if( self.p1StudentIDInput.GetValue() == "" and
                self.p1StudentNameInput.GetValue() == "" ):
            tmp = Solve.ShowAllStudents()
            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p1StudentList.InsertItem(self.p1StudentList.GetItemCount(),str(data[0]));
                self.p1StudentList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]
                self.p1StudentList.SetItem(index, 2, str(data[3]))
                self.p1StudentList.SetItem(index, 3, str(data[4]))
                self.p1StudentList.SetItem(index, 4, str(data[5]))
                self.p1StudentList.SetItem(index, 5, str(data[2]))

        print(self.p1StudentIDInput.GetValue())

        if (self.p1StudentIDInput.GetValue() != "" and
                self.p1StudentNameInput.GetValue() == ""):
            tmp = Solve.StudentIDToStudent(self.p1StudentIDInput.GetValue())
            print(tmp)
            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p1StudentList.InsertItem(self.p1StudentList.GetItemCount(),str(data[0]));
                self.p1StudentList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]
                self.p1StudentList.SetItem(index, 2, str(data[3]))
                self.p1StudentList.SetItem(index, 3, str(data[4]))
                self.p1StudentList.SetItem(index, 4, str(data[5]))
                self.p1StudentList.SetItem(index, 5, str(data[2]))

        if (self.p1StudentIDInput.GetValue() == "" and
                self.p1StudentNameInput.GetValue() != ""):
            tmp = Solve.StudentNameToStudent(self.p1StudentNameInput.GetValue())
            print(tmp)
            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p1StudentList.InsertItem(self.p1StudentList.GetItemCount(),str(data[0]));
                self.p1StudentList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]
                self.p1StudentList.SetItem(index, 2, str(data[3]))
                self.p1StudentList.SetItem(index, 3, str(data[4]))
                self.p1StudentList.SetItem(index, 4, str(data[5]))
                self.p1StudentList.SetItem(index, 5, str(data[2]))

        if (self.p1StudentIDInput.GetValue() != "" and
                self.p1StudentNameInput.GetValue() != ""):
            tmp1 = Solve.StudentIDToStudent(self.p1StudentIDInput.GetValue())
            tmp2 = Solve.StudentNameToStudent(self.p1StudentNameInput.GetValue())
            tmp = tuple(set(tmp1) & set(tmp2))

            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p1StudentList.InsertItem(self.p1StudentList.GetItemCount(),str(data[0]));
                self.p1StudentList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]
                self.p1StudentList.SetItem(index, 2, str(data[3]))
                self.p1StudentList.SetItem(index, 3, str(data[4]))
                self.p1StudentList.SetItem(index, 4, str(data[5]))
                self.p1StudentList.SetItem(index, 5, str(data[2]))

    def p1PressConfirmButton(self, event):

        if( self.isAddORModify == "Add"):
            p1IsAdd = wx.MessageDialog(self, "Are you sure to add?", "Message", wx.YES_NO)
            if p1IsAdd.ShowModal() == wx.ID_YES:
                isOK = Solve.AddStudent(self.p1StudentIDOutput.GetValue(),self.p1StudentNameOutput.GetValue(),
                             self.p1SexOutput.GetValue(),self.p1EntranceAgeOutput.GetValue(),
                             self.p1EntranceYearOutput.GetValue(),self.p1ClassOutput.GetValue())

                if( isOK == False ):
                  wx.MessageDialog(self, "Add failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p1StudentList.DeleteAllItems()


        if self.isAddORModify == "Modify" :
            p1IsModify = wx.MessageDialog(self, "Are you sure to modify ?", "Modify", wx.YES_NO)
            if p1IsModify.ShowModal() == wx.ID_YES:
                isOK = Solve.UpdateStudent(self.p1StudentIDOutput.GetValue(),self.p1StudentNameOutput.GetValue(),
                             self.p1SexOutput.GetValue(),self.p1EntranceAgeOutput.GetValue(),
                             self.p1EntranceYearOutput.GetValue(),self.p1ClassOutput.GetValue())
                if( isOK == False ):
                    wx.MessageDialog(self, "Modify failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p1StudentList.DeleteAllItems()

    def p1ListFocus(self, event):
        self.p1ButtonDelete.Enable()
        self.p1ButtonModify.Enable()

    def p1ListNoFocus(self, event):
        self.p1ButtonDelete.Disable()
        self.p1ButtonModify.Disable()
        self.p1ButtonConfirm.Disable()
        self.p1StudentIDOutput.Disable()
        self.p1StudentNameOutput.Disable()
        self.p1EntranceAgeOutput.Disable()
        self.p1EntranceYearOutput.Disable()
        self.p1ClassOutput.Disable()
        self.p1SexOutput.Disable()
        self.clearAllOutput()

#p2 def

    def p2PressAddButton(self, event ):
        self.p2ButtonConfirm.Enable()
        self.p2TeacherIDOutput.Enable()
        self.p2TeacherNameOutput.Enable()
        self.isAddORModify = "Add"
        self.clearAllOutput()

    def p2PressModifyButton(self, event):
        self.p2ButtonConfirm.Enable()
        self.p2TeacherIDOutput.Disable()
        self.p2TeacherNameOutput.Enable()

        item = self.p2TeacherList.GetFocusedItem()
        self.p2TeacherIDOutput.SetValue(self.p2TeacherList.GetItemText(item, 0))
        self.p2TeacherNameOutput.SetValue(self.p2TeacherList.GetItemText(item, 1))

        self.isAddORModify = "Modify"

    def p2PressDeleteButton(self, event):
        self.p2ButtonConfirm.Disable()
        self.p2TeacherIDOutput.Disable()
        self.p2TeacherNameOutput.Disable()
        self.p2IsDelete = wx.MessageDialog(self,"Are you sure to delete it ?","Delete",wx.YES_NO )
        if self.p2IsDelete.ShowModal() == wx.ID_YES:
            item = self.p2TeacherList.GetFocusedItem()
            Solve.DeleteTeacher(self.p2TeacherList.GetItemText(item, 0))
            self.p2TeacherList.DeleteAllItems()
        self.p2ButtonDelete.Disable()
        self.p2ButtonModify.Disable()

    def p2PressQueryButton(self, event):

        self.p2TeacherList.DeleteAllItems()
        self.clearAllOutput()
        self.p2ButtonDelete.Disable()
        self.p2ButtonModify.Disable()
        self.p2ButtonConfirm.Disable()
        self.p2TeacherIDOutput.Disable()
        self.p2TeacherNameOutput.Disable()

        if( self.p2TeacherIDInput.GetValue() == "" and
                self.p2TeacherNameInput.GetValue() == "" ):

            tmp = Solve.ShowAllTeacher()
            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p2TeacherList.InsertItem(self.p2TeacherList.GetItemCount(),str(data[0]));
                self.p2TeacherList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]


        if (self.p2TeacherIDInput.GetValue() != "" and
                self.p2TeacherNameInput.GetValue() == ""):
            tmp = Solve.TeacherIDToTeacher(self.p2TeacherIDInput.GetValue())

            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p2TeacherList.InsertItem(self.p2TeacherList.GetItemCount(),str(data[0]));
                self.p2TeacherList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]

        if (self.p2TeacherIDInput.GetValue() == "" and
                self.p2TeacherNameInput.GetValue() != ""):
            tmp = Solve.TeacherNameToTeacher(self.p2TeacherNameInput.GetValue())

            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p2TeacherList.InsertItem(self.p2TeacherList.GetItemCount(),str(data[0]));
                self.p2TeacherList.SetItem(index, 1, str(data[1]))

        if (self.p2TeacherIDInput.GetValue() != "" and
                self.p2TeacherNameInput.GetValue() != ""):
            tmp1 = Solve.TeacherIDToTeacher(self.p2TeacherIDInput.GetValue())
            tmp2 = Solve.TeacherNameToTeacher(self.p2TeacherNameInput.GetValue())
            tmp = tuple(set(tmp1) & set(tmp2))

            for data in tmp:
                # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
                index = self.p2TeacherList.InsertItem(self.p2TeacherList.GetItemCount(),str(data[0]));
                self.p2TeacherList.SetItem(index, 1, str(data[1]))

    def p2PressConfirmButton(self, event):

        if( self.isAddORModify == "Add"):
            p2IsAdd = wx.MessageDialog(self, "Are you sure to add?", "Message", wx.YES_NO)
            if p2IsAdd.ShowModal() == wx.ID_YES:
                isOK = Solve.AddTeacher(self.p2TeacherIDOutput.GetValue(),self.p2TeacherNameOutput.GetValue())
                if( isOK == False ):
                  wx.MessageDialog(self, "Add failed!", "Message").ShowModal()
                else:
                    self.disableAll()
                    self.p2TeacherList.DeleteAllItems()

        if self.isAddORModify == "Modify" :
            p2IsModify = wx.MessageDialog(self, "Are you sure to modify ?", "Modify", wx.YES_NO)
            if p2IsModify.ShowModal() == wx.ID_YES:
                isOK = Solve.UpdateTeacher(self.p2TeacherIDOutput.GetValue(),self.p2TeacherNameOutput.GetValue())
                if( isOK == False ):
                    wx.MessageDialog(self, "Modify failed!", "Message").ShowModal()
                else:
                    self.disableAll()
                    self.p2TeacherList.DeleteAllItems()

    def p2ListFocus(self, event):
        self.p2ButtonDelete.Enable()
        self.p2ButtonModify.Enable()

    def p2ListNoFocus(self, event):
        self.p2ButtonDelete.Disable()
        self.p2ButtonModify.Disable()
        self.p2ButtonConfirm.Disable()
        self.p2TeacherIDOutput.Disable()
        self.p2TeacherNameOutput.Disable()
        self.clearAllOutput()


# p3 def
    def p3PressAddButton(self, event ):
        self.p3ButtonConfirm.Enable()
        self.p3CourseIDOutput.Enable()
        self.p3CourseNameOutput.Enable()
        self.p3TeacherIDOutput.Enable()
        self.p3CreditOutput.Enable()
        self.p3GradeOutput.Enable()
        self.p3CanceledYearOutput.Enable()
        self.isAddORModify = "Add"
        self.clearAllOutput()

    def p3PressModifyButton(self, event):
        self.p3ButtonConfirm.Enable()
        self.p3CourseIDOutput.Disable()
        self.p3CourseNameOutput.Enable()
        self.p3TeacherIDOutput.Enable()
        self.p3CreditOutput.Enable()
        self.p3GradeOutput.Enable()
        self.p3CanceledYearOutput.Enable()

        if self.userType == 1:
            pass

        tmp = self.p3CanceledYearOutput.GetValue()
        if (tmp == None):
            tmp = ""

        item = self.p3CourseList.GetFocusedItem()
        self.p3CourseIDOutput.SetValue(self.p3CourseList.GetItemText(item, 0))
        self.p3CourseNameOutput.SetValue(self.p3CourseList.GetItemText(item, 1))
        self.p3TeacherIDOutput.SetValue(self.p3CourseList.GetItemText(item, 2))
        self.p3CreditOutput.SetValue(self.p3CourseList.GetItemText(item, 3))
        self.p3GradeOutput.SetValue(self.p3CourseList.GetItemText(item,4))
        self.p3CanceledYearOutput.SetValue(tmp)

        self.isAddORModify = "Modify"

    def p3PressDeleteButton(self, event):
        self.p3ButtonConfirm.Disable()
        self.p3CourseIDOutput.Disable()
        self.p3CourseNameOutput.Disable()
        self.p3TeacherIDOutput.Disable()
        self.p3CreditOutput.Disable()
        self.p3GradeOutput.Disable()
        self.p3CanceledYearOutput.Disable()

        self.p3IsDelete = wx.MessageDialog(self,"Are you sure to delete it ?","Delete",wx.YES_NO )
        if self.p3IsDelete.ShowModal() == wx.ID_YES:
            print("self.p3IsDelete.ShowModal() == wx.ID_YES:")
            item = self.p3CourseList.GetFocusedItem()
            Solve.DeleteCourse(self.p3CourseList.GetItemText(item, 0))
            self.p3CourseList.DeleteAllItems()
        self.p3ButtonDelete.Disable()
        self.p3ButtonModify.Disable()

    def p3PressQueryButton(self, event):

        self.p3CourseList.DeleteAllItems()
        self.clearAllOutput()
        self.disableAll()

        tmp = ()
        tmp11 = self.p3CourseNameInput.GetValue()
        tmp12 = self.p3CourseIDInput.GetValue()
        if (tmp11 == "" and tmp12 == "" ):
            tmp = Solve.ShowAllCourse()
        else :
            if tmp11 != "" :
                tmp = Solve.CourseNameToCourse(tmp11)
            if tmp12 != "" :
                if tmp == () :
                    # print("tmp12 "+tmp12)
                    tmp = Solve.CourseIDToCourse(tmp12)
                else :
                    tmp = tuple( set(tmp) & set(Solve.CourseIDToCourse(tmp12)))

        for data in tmp:
            # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
            index = self.p3CourseList.InsertItem(self.p3CourseList.GetItemCount(), str(data[0]));
            self.p3CourseList.SetItem(index, 1, str(data[1]))  # 再添加一列，设置文本为data[1]
            self.p3CourseList.SetItem(index, 2, str(data[2]))
            self.p3CourseList.SetItem(index, 3, str(data[3]))
            self.p3CourseList.SetItem(index, 4, str(data[4]))
            self.p3CourseList.SetItem(index, 5, str(data[5]))

    def p3PressConfirmButton(self, event):

        if( self.isAddORModify == "Add"):
            p3IsAdd = wx.MessageDialog(self, "Are you sure to add?", "Message", wx.YES_NO)
            if p3IsAdd.ShowModal() == wx.ID_YES:
                isOK = Solve.AddCourse(self.p3CourseIDOutput.GetValue(),
                                            self.p3CourseNameOutput.GetValue(),
                                            self.p3TeacherIDOutput.GetValue(),
                                            self.p3CreditOutput.GetValue(),
                                            self.p3GradeOutput.GetValue(),
                                            self.p3CanceledYearOutput.GetValue())

                if( isOK == False ):
                  wx.MessageDialog(self, "Add failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p3CourseList.DeleteAllItems()


        if self.isAddORModify == "Modify" :
            p3IsModify = wx.MessageDialog(self, "Are you sure to modify ?", "Modify", wx.YES_NO)
            tmp = self.p3CanceledYearOutput.GetValue()
            # if( tmp == "" ):
            #     print( "tmpp == "" ")
            if p3IsModify.ShowModal() == wx.ID_YES:
                isOK = Solve.UpdateCourse(self.p3CourseIDOutput.GetValue(),
                                            self.p3CourseNameOutput.GetValue(),
                                            self.p3TeacherIDOutput.GetValue(),
                                            self.p3CreditOutput.GetValue(),
                                            self.p3GradeOutput.GetValue(),
                                            tmp)
                if( isOK == False ):
                    wx.MessageDialog(self, "Modify failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p3CourseList.DeleteAllItems()

    def p3ListFocus(self, event):
        self.p3ButtonDelete.Enable()
        self.p3ButtonModify.Enable()

    def p3ListNoFocus(self, event):
        self.disableAll()
        self.clearAllOutput()

# p4 def
    def p4PressAddButton(self, event ):
        self.p4ButtonConfirm.Enable()
        self.p4StudentIDOutput.Enable()
        self.p4TeacherIDOutput.Enable()
        self.p4CourseIDOutput.Enable()
        self.p4SelectYearOutput.Enable()
        self.p4GradeOutput.Enable()
        self.isAddORModify = "Add"
        self.clearAllOutput()

        if self.userType == 2 :
            self.p4GradeOutput.Disable()
            self.p4GradeOutput.SetValue("0")

    def p4PressModifyButton(self, event):
        self.p4ButtonConfirm.Enable()
        self.p4StudentIDOutput.Disable()
        self.p4TeacherIDOutput.Enable()
        self.p4CourseIDOutput.Enable()
        self.p4SelectYearOutput.Enable()
        self.p4GradeOutput.Enable()

        if self.userType == 2 :
            self.p4GradeOutput.Disable()

        item = self.p4SelectList.GetFocusedItem()
        self.p4StudentIDOutput.SetValue(self.p4SelectList.GetItemText(item, 0))
        self.p4TeacherIDOutput.SetValue(self.p4SelectList.GetItemText(item, 1))
        self.p4CourseIDOutput.SetValue(self.p4SelectList.GetItemText(item, 2))
        self.p4SelectYearOutput.SetValue(self.p4SelectList.GetItemText(item,3))
        self.p4GradeOutput.SetValue(self.p4SelectList.GetItemText(item,4))

        self.isAddORModify = "Modify"

    def p4PressDeleteButton(self, event):
        self.p4ButtonConfirm.Disable()
        self.p4StudentIDOutput.Disable()
        self.p4TeacherIDOutput.Disable()
        self.p4CourseIDOutput.Disable()
        self.p4SelectYearOutput.Disable()
        self.p4GradeOutput.Disable()

        self.p4IsDelete = wx.MessageDialog(self,"Are you sure to delete it ?","Delete",wx.YES_NO )
        if self.p4IsDelete.ShowModal() == wx.ID_YES:
            print("self.p4IsDelete.ShowModal() == wx.ID_YES:")
            item = self.p4SelectList.GetFocusedItem()
            Solve.DeleteCourseChoose(self.p4SelectList.GetItemText(item, 0),
                                     self.p4SelectList.GetItemText(item, 2))
            self.p4SelectList.DeleteAllItems()
        self.p4ButtonDelete.Disable()
        self.p4ButtonModify.Disable()

    def p4PressQueryButton(self, event):

        self.p4SelectList.DeleteAllItems()
        self.clearAllOutput()
        self.disableAll()

        tmp = "fuckyou"
        tmp11 = self.p4StudentNameInput.GetValue()
        tmp12 = self.p4StudentIDInput.GetValue()
        tmp21 = self.p4TeacherNameInput.GetValue()
        tmp22 = self.p4TeacherIDInput.GetValue()
        tmp31 = self.p4CourseNameInput.GetValue()
        tmp32 = self.p4CourseIDInput.GetValue()

        if (tmp11 == "" and tmp12 == "" and
            tmp21 == "" and tmp22 == "" and
            tmp31 == "" and tmp32 == ""    ):
            tmp = Solve.ShowAllCourseChoose()
        else :
            if tmp11 != "" :
                tmp = Solve.StudentNameToCourseChoose(tmp11)
            if tmp12 != "" :
                if tmp == "fuckyou" :
                    tmp = Solve.StudentIDToCourseChoose(tmp12)
                else :
                    tmp = tuple( set(tmp) & set(Solve.StudentIDToCourseChoose(tmp12)))
            if tmp21 != "" :
                if tmp == "fuckyou" :
                    tmp = Solve.TeacherNameToCourseChoose(tmp21)
                else :
                    tmp = tuple( set(tmp) & set(Solve.TeacherNameToCourseChoose(tmp21)))
            if tmp22 != "" :
                if tmp == "fuckyou" :
                    tmp = Solve.TeacherIDToCourseChoose(tmp22)
                else :
                    tmp = tuple( set(tmp) & set(Solve.TeacherIDToCourseChoose(tmp22)))
            if tmp31 != "" :
                if tmp == "fuckyou" :
                    tmp = Solve.CourseNameToCourseChoose(tmp31)
                else :
                    tmp = tuple( set(tmp) & set(Solve.CourseNameToCourseChoose(tmp31)))
            if tmp32 != "" :
                if tmp == "fuckyou" :
                    tmp = Solve.CourseIDToCourseChoose(tmp32)
                else :
                    tmp = tuple( set(tmp) & set(Solve.CourseIDToCourseChoose(tmp32)))

        for data in tmp:
            # 插入一个item，参数1为在什么地方插入，参数二为这个item的文本内容，刚开始item默认仅有一列
            index = self.p4SelectList.InsertItem(self.p4SelectList.GetItemCount(), str(data[0]));
            self.p4SelectList.SetItem(index, 1, str(data[2]))  # 再添加一列，设置文本为data[1]
            self.p4SelectList.SetItem(index, 2, str(data[1]))
            self.p4SelectList.SetItem(index, 3, str(data[3]))
            self.p4SelectList.SetItem(index, 4, str(data[4]))


    def p4PressConfirmButton(self, event):

        if( self.isAddORModify == "Add"):
            p4IsAdd = wx.MessageDialog(self, "Are you sure to add?", "Message", wx.YES_NO)

            if p4IsAdd.ShowModal() == wx.ID_YES:
                isOK = Solve.AddCourseChoose( self.p4StudentIDOutput.GetValue(),
                                        self.p4CourseIDOutput.GetValue(),
                                        self.p4TeacherIDOutput.GetValue(),
                                        self.p4SelectYearOutput.GetValue(),
                                        self.p4GradeOutput.GetValue())

                if( isOK == False ):
                  wx.MessageDialog(self, "Add failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p4SelectList.DeleteAllItems()


        if self.isAddORModify == "Modify" :
            p4IsModify = wx.MessageDialog(self, "Are you sure to modify ?", "Modify", wx.YES_NO)
            if p4IsModify.ShowModal() == wx.ID_YES:

                isOK = Solve.UpdateCourseChoose(  self.p4StudentIDOutput.GetValue(),
                                            self.p4CourseIDOutput.GetValue(),
                                            self.p4TeacherIDOutput.GetValue(),
                                            self.p4SelectYearOutput.GetValue(),
                                            self.p4GradeOutput.GetValue())
                if( isOK == False ):
                    wx.MessageDialog(self, "Modify failed!", "Message").ShowModal()
                else :
                    self.disableAll()
                    self.p4SelectList.DeleteAllItems()

    def p4ListFocus(self, event):
        self.p4ButtonDelete.Enable()
        self.p4ButtonModify.Enable()

    def p4ListNoFocus(self, event):
        self.disableAll()
        self.clearAllOutput()


# p5 def
    def p5PressQueryButton(self, event):
        if self.p5StudentIDInput.GetValue() != "":
            result = Solve.AnyStudentIDToScore(self.p5StudentIDInput.GetValue())
            if result[0][0] != None:
                self.studentScoreMessage = wx.MessageDialog(self, "The average score of student " + self.p5StudentIDInput.GetValue() + " is " + str(result[0][0]) + "!", "Message", wx.OK)
                self.studentScoreMessage.ShowModal()

        elif self.p5StudentNameInput.GetValue() != "":
            result = Solve.AnyStudentNameToScore(self.p5StudentNameInput.GetValue())
            if result[0][0] != None:
                self.studentScoreMessage = wx.MessageDialog(self, "The average score of student " + self.p5StudentNameInput.GetValue() + " is " + str(result[0][1]) + "!", "Message", wx.OK)
                self.studentScoreMessage.ShowModal()

        elif self.p5ClassInput.GetValue() != "":
            result = Solve.ClassToScore(self.p5ClassInput.GetValue())
            if result[0][0] != None:
                self.classScoreMessage = wx.MessageDialog(self, "The average score of class " + self.p5ClassInput.GetValue() + " is " + str(result[0][0]) + "!", "Message", wx.OK)
                self.classScoreMessage.ShowModal()

        elif self.p5CourseIDInput.GetValue() != "":
            result = Solve.CourseToScore(self.p5CourseIDInput.GetValue())
            if result[0][0] != None:
                self.courseScoreMessage = wx.MessageDialog(self,
                    "The average score of course " + self.p5CourseIDInput.GetValue() + " is " + str(
                            result[0][0]) + "!", "Message", wx.OK)
                self.courseScoreMessage.ShowModal()

        else:
            result = Solve.ShowAllStudentAvgScore()
            print(result)
            if result[0][0] != None:
                self.allStudentScoreMessage = wx.MessageDialog(self,
                    "The average score of all students is " + str(
                            result[0][0]) + "!", "Message", wx.OK)
                self.allStudentScoreMessage.ShowModal()



#other def

    def userAuthority(self):
        if( self.userType == 1 or self.userType == 0 ):
            self.p1ButtonAdd.Hide()
            self.p1ButtonModify.Hide()
            self.p1ButtonDelete.Hide()
            self.p1ButtonConfirm.Hide()
            self.p1StudentIDOutput.Hide()
            self.p1StudentNameOutput.Hide()
            self.p1EntranceAgeOutput.Hide()
            self.p1EntranceYearOutput.Hide()
            self.p1ClassOutput.Hide()
            self.p1SexOutput.Hide()

            self.p2ButtonAdd.Hide()
            self.p2ButtonModify.Hide()
            self.p2ButtonDelete.Hide()
            self.p2ButtonConfirm.Hide()
            self.p2TeacherIDOutput.Hide()
            self.p2TeacherNameOutput.Hide()

            self.p3ButtonAdd.Hide()
            self.p3ButtonModify.Hide()
            self.p3ButtonDelete.Hide()
            self.p3ButtonConfirm.Hide()
            self.p3CourseIDOutput.Hide()
            self.p3CourseNameOutput.Hide()
            self.p3TeacherIDOutput.Hide()
            self.p3CreditOutput.Hide()
            self.p3GradeOutput.Hide()
            self.p3CanceledYearOutput.Hide()

            self.p4ButtonAdd.Hide()
            self.p4ButtonModify.Hide()
            self.p4ButtonDelete.Hide()
            self.p4ButtonConfirm.Hide()
            self.p4StudentIDOutput.Hide()
            self.p4TeacherIDOutput.Hide()
            self.p4CourseIDOutput.Hide()
            self.p4SelectYearOutput.Hide()
            self.p4GradeOutput.Hide()

        if self.userType == 1:
            self.p4ButtonModify.Show()
            self.p4GradeOutput.Show()
            self.p4ButtonConfirm.Show()




    def clearAllInput(self):
        self.p1StudentIDInput.SetValue("")
        self.p1StudentNameInput.SetValue("")

        self.p2TeacherIDInput.SetValue("")
        self.p2TeacherNameInput.SetValue("")

        self.p3CourseIDInput.SetValue("")
        self.p3CourseNameInput.SetValue("")

        self.p4StudentIDInput.SetValue("")
        self.p4StudentNameInput.SetValue("")
        self.p4TeacherIDInput.SetValue("")
        self.p4TeacherNameInput.SetValue("")
        self.p4CourseIDInput.SetValue("")
        self.p4CourseNameInput.SetValue("")

        self.p5StudentIDInput.SetValue("")
        self.p5StudentNameInput.SetValue("")
        self.p5CourseIDInput.SetValue("")
        self.p5CourseNameInput.SetValue("")

    def clearAllOutput(self):
        self.p1StudentIDOutput.SetValue("")
        self.p1StudentNameOutput.SetValue("")
        self.p1EntranceAgeOutput.SetValue("")
        self.p1EntranceYearOutput.SetValue("")
        self.p1ClassOutput.SetValue("")
        self.p1SexOutput.SetValue("")

        self.p2TeacherIDOutput.SetValue("")
        self.p2TeacherNameOutput.SetValue("")

        self.p3CourseIDOutput.SetValue("")
        self.p3CourseNameOutput.SetValue("")
        self.p3TeacherIDOutput.SetValue("")
        self.p3CreditOutput.SetValue("")
        self.p3GradeOutput.SetValue("")
        self.p3CanceledYearOutput.SetValue("")

        self.p4StudentIDOutput.SetValue("")
        self.p4TeacherIDOutput.SetValue("")
        self.p4CourseIDOutput.SetValue("")
        self.p4SelectYearOutput.SetValue("")
        self.p4GradeOutput.SetValue("")

    def disableAll(self):
        self.p1ButtonConfirm.Disable()
        self.p1ButtonDelete.Disable()
        self.p1ButtonModify.Disable()
        self.p1StudentIDOutput.Disable()
        self.p1StudentNameOutput.Disable()
        self.p1EntranceAgeOutput.Disable()
        self.p1EntranceYearOutput.Disable()
        self.p1ClassOutput.Disable()
        self.p1SexOutput.Disable()


        self.p2ButtonConfirm.Disable()
        self.p2ButtonDelete.Disable()
        self.p2ButtonModify.Disable()
        self.p2TeacherIDOutput.Disable()
        self.p2TeacherNameOutput.Disable()

        self.p3ButtonDelete.Disable()
        self.p3ButtonModify.Disable()
        self.p3ButtonConfirm.Disable()
        self.p3CourseIDOutput.Disable()
        self.p3CourseNameOutput.Disable()
        self.p3TeacherIDOutput.Disable()
        self.p3CreditOutput.Disable()
        self.p3GradeOutput.Disable()
        self.p3CanceledYearOutput.Disable()

        self.p4ButtonDelete.Disable()
        self.p4ButtonModify.Disable()
        self.p4ButtonConfirm.Disable()
        self.p4StudentIDOutput.Disable()
        self.p4TeacherIDOutput.Disable()
        self.p4CourseIDOutput.Disable()
        self.p4SelectYearOutput.Disable()
        self.p4GradeOutput.Disable()

if __name__ == '__main__':
    app = wx.App(False)
    frame = Frame(None, "student", 0)
    # frame = Frame(None , "teacher" , 1)
    # frame = Frame(None, "Administrator", 2)
    frame.Show(True)
    app.MainLoop()


def secondFrame( userName , userType ,sframe):
    # print( "id " + userName + " type " + str(userType )
    frame = Frame(None, userName, userType)
    frame.Show(True)