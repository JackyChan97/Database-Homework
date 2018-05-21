import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(300, 200))
        self.BackgroundColour = "blue"
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        self.rb1 = wx.RadioButton(pnl, 11, label='Value A',
                                  pos=(10, 10), style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl, 22, label='Value B', pos=(10, 40))
        self.rb3 = wx.RadioButton(pnl, 33, label='Value C', pos=(10, 70))
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        lblList = ['Value X', 'Value Y', 'Value Z']

        self.rbox = wx.RadioBox(pnl, label='', pos=(80, 10), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rbox.ClearBackground()
        self.rbox.Bind(wx.EVT_RADIOBOX, self.onRadioBox)

        self.Centre()
        self.Show(True)

    def OnRadiogroup(self, e):
        rb = e.GetEventObject()

        rb.GetLabel(), ' is clicked from Radio Group'

    def onRadioBox(self, e):

        self.rbox.GetStringSelection(), ' is clicked from Radio Box'


if __name__ == '__main__':
    app = wx.App(False)
    frame = Example(None, 'RadioButton & RadioBox - www.yiibai.com')
    frame.Show(True)
    app.MainLoop()

