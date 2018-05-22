
import wx
import WorkFrame
import Solve

class FrameLogin(wx.Frame):
    loginType = -1  # 0 is student 1 is administer 2 is teacher
    UserID = "administrator"
    Password = "123456"

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"SWS Student Management System", pos=(200, 80),
                          size=wx.Size(800, 640), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHints(wx.Size(800, 640), wx.Size(800, 640))
        self.icon = wx.Icon('icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon)

        panel = wx.Panel(self, id=wx.ID_ANY)



        self.textTitle = TransparentText(panel, id=wx.ID_ANY, label=u"SWS Student Management System", pos=(220, 120),
                                         size=(100, 50))
        font = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.textTitle.SetFont(font)



        font = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        # self.textUserID = wx.StaticText(panel, id=wx.ID_ANY, label=u"UserID:", pos=(230,250), size=(100,50), style=wx.ALIGN_RIGHT)
        self.textUserID = TransparentText(panel, id=wx.ID_ANY, label=u"UserID:", pos=(230+40, 250-40), size=(100, 50),
                                          style=wx.ALIGN_RIGHT)
        # self.textUserID.SetWindowStyle()
        self.textUserID.SetFont(font)

        # self.textPassword = wx.StaticText(panel, id=wx.ID_ANY, label=u"Password:",pos=(230,280), size = (100,50), style=wx.ALIGN_RIGHT)
        self.textPassword = TransparentText(panel, id=wx.ID_ANY, label=u"Password:",pos=(230+40,280-20), size = (100,50), style=wx.ALIGN_RIGHT)
        self.textPassword.SetFont(font)

        self.textctrlUserID = wx.TextCtrl(panel,id=wx.ID_ANY, value=u"",pos=(350+40,250-40),size=wx.DefaultSize)

        self.textctrlPassword = wx.TextCtrl(panel, id=wx.ID_ANY, value=u"", pos=(350+40, 280-20), size=wx.DefaultSize, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

        choices = [ 'Student', 'Teacher', 'Administrator' ]
        self.radiobox = wx.RadioBox(panel, id=wx.ID_ANY, label=u"", pos=(210, 340-15), size=wx.DefaultSize, choices=choices, style=wx.NO_BORDER)
        self.radiobox.SetBackgroundColour((189 ,172 ,156))
        # 211 215 216
        # 189 172 156

        self.buttonLogin = wx.Button(panel, id = wx.ID_ANY, label =u"Login", pos = (300,420), size=(200, 45), style =0)
        #self.listctrl = wx.ListCtrl(panel, -1)
        self.buttonLogin.SetForegroundColour((255, 255, 255))
        self.buttonLogin.SetBackgroundColour((17, 150, 219))


        self.buttonLogin.Bind(wx.EVT_BUTTON, self.Login)
        self.Bind(wx.EVT_TEXT_ENTER, self.Login, self.textctrlPassword)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
        panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("background0.jpg")
        # bmp.SetSize((800, 640))
        dc.DrawBitmap(bmp, 0, 0)

    def Login(self, event):
        state = False
        name = ""
        if self.textctrlPassword.GetValue() == self.Password:
            if self.radiobox.GetSelection() == 0:
                studentID = self.textctrlUserID.GetValue()
                result = Solve.IsStudentExist(studentID)
                state = result[0]
                if result[1] != ():
                    name = result[1][0]
            if self.radiobox.GetSelection() == 1:
                teacherID = self.textctrlUserID.GetValue()
                result = Solve.IsTeacherExist(teacherID)
                state = result[0]
                if result[1] != ():
                    name = result[1][0]
            if self.radiobox.GetSelection() == 2:
                if self.textctrlUserID.GetValue() == self.UserID:
                    state = True
                    name = "administrator"

        authority = self.radiobox.GetSelection()

        if state == True:
            dialogsuccess = wx.MessageDialog(self, "Login successfully", "Message", wx.OK)
            dialogsuccess.ShowModal()
            WorkFrame.secondFrame(name[0], authority, self)
            self.Close()
        else:
            dialogfail = wx.MessageDialog(self, "Invalid UserID or password","Message", wx.OK)
            dialogfail.ShowModal()


class TransparentText(wx.StaticText):
    def __init__(self, parent, id=wx.ID_ANY, label="", pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0, name='transparenttext'):
        style |= wx.CLIP_CHILDREN | wx.TRANSPARENT_WINDOW
        wx.StaticText.__init__(self, parent, id, label, pos, size, style, name)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, lambda event: None)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        font_face = self.GetFont()
        font_color = self.GetForegroundColour()
        dc.SetFont(font_face)
        dc.SetTextBackground(font_color)
        dc.SetTextForeground((0, 0, 0))
        dc.DrawText(self.GetLabel(), 0, 0)

    def OnSize(self, event):
        self.Refresh()
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    frame = FrameLogin(None)
    frame.Show(True)
    if Solve.CheckConnection() == False:
        messgae = wx.MessageDialog(None, "Connection to Database failed.", "Message", wx.OK)
        messgae.ShowModal()
        wx.Exit()
    app.MainLoop()
