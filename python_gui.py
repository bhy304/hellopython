# wxPython으로 윈도우프로그램(GUI) 만들기
# https://wxpython.org/pages/overview/

# pip install wxPython
# import wx
# wx.version()


import wx

class HelloFrame(wx.Frame):
    def __init__(self, *argv, **kw):
        super(HelloFrame, self).__init__(*argv, **kw)

        self.pnl = wx.Panel(self)
        
        self.makeControl()
        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!!")

    def makeControl(self):
        self.txt = wx.TextCtrl(self.pnl, -1, size=(140, -1))
        self.txt.SetValue("This is placeholder..")

        self.btn = wx.Button(self.pnl, wx.ID_ANY, '실행')
        self.Bind(wx.EVT_BUTTON, self.actButton, self.btn)

        self.btnFile = wx.Button(self.pnl, wx.ID_ANY, 'Open File')
        self.Bind(wx.EVT_BUTTON, self.openFile, self.btnFile)

        self.st = wx.StaticText(self.pnl, label="Hello World!")
        font = self.st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        self.st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.st)
        sizer.Add(self.txt)

        sizerButtons = wx.WrapSizer(wx.HORIZONTAL)
        sizerButtons.Add(self.btn)
        sizerButtons.Add(self.btnFile)
        sizer.Add(sizerButtons)
        self.pnl.SetSizer(sizer)

    def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H", "Help string shown in status bar")
        
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def actButton(self, evt):
        msg = "Button Clicked"
        msg = self.txt.GetLineText(0)
        wx.MessageBox(msg, "Button Alert")

    def openFile(self, evt):
            self.txt.LoadFile("games.csv")

    def OnExit(self, event):
        self.Destroy()

    def OnHello(self, event):
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK | wx.ICON_INFORMATION)

app = wx.App()
# frm = wx.Frame(None, wx.ID_ANY, title="Hello Python")
frm = HelloFrame(None, title="Hello Frame", size=(500,200))
frm.Show()
app.MainLoop()