import wx
import WorkFrame
import Solve

class FrameLogin(wx.Frame):
    loginType = -1  # 0 is student 1 is administer 2 is teacher
    UserName = "abc"
    Password = "123456"

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"LOGIN", pos=(200, 80),
                          size=wx.Size(800, 640), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(800, 640), wx.Size(800, 640))

        panel = wx.Panel(self, id=wx.ID_ANY)

        font = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL)

        self.textUserName = wx.StaticText(panel, id=wx.ID_ANY, label=u"UserID:", pos=(230,250), size=(100,50), style=wx.ALIGN_RIGHT)
        self.textUserName.SetFont(font)

        self.textPassword = wx.StaticText(panel, id=wx.ID_ANY, label=u"Password:",pos=(230,280), size = (100,50), style=wx.ALIGN_RIGHT)
        self.textPassword.SetFont(font)

        self.textctrlUserName = wx.TextCtrl(panel,id=wx.ID_ANY, value=u"",pos=(350,250),size=wx.DefaultSize)

        self.textctrlPassword = wx.TextCtrl(panel, id=wx.ID_ANY, value=u"", pos=(350, 280), size=wx.DefaultSize, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

        choices = [ 'Student', 'Administer','Teacher']
        self.radiobox = wx.RadioBox(panel, id=wx.ID_ANY, label=u"", pos=(240, 340), size=wx.DefaultSize, choices=choices)

        self.buttonLogin = wx.Button(panel, id = wx.ID_ANY, label =u"Login", pos = (330,420), size=wx.DefaultSize, style =0)
        #self.listctrl = wx.ListCtrl(panel, -1)
        self.buttonLogin.Bind(wx.EVT_BUTTON, self.Login)
        self.Bind(wx.EVT_TEXT_ENTER, self.Login, self.textctrlPassword)



    def Login(self, event):
        if(self.textctrlUserName.GetValue()==self.UserName and self.textctrlPassword.GetValue()==self.Password):
            if(self.radiobox.GetSelection()==0):
                loginType = 0
                print(loginType)
            if(self.radiobox.GetSelection()==1):
                loginType = 1
                print(loginType)
            if(self.radiobox.GetSelection()==2):
                loginType = 2
                print(loginType)
            dialogsuccess = wx.MessageDialog(self, "Login successfully", "Message", wx.OK)

            dialogsuccess.ShowModal()
            WorkFrame.secondFrame("zzzy", "administrator", self)
            self.Close()


        else:

            dialogfail = wx.MessageDialog(self, "Invalid username or password","Message", wx.OK)
            dialogfail.ShowModal()


if __name__ == '__main__':
    app = wx.App(False)
    frame = FrameLogin(None)
    frame.Show(True)
    app.MainLoop()
