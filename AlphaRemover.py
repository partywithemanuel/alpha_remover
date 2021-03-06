import wx
import matplotlib.pyplot as plt
import os
import sys
import subprocess
from PIL import Image

class App(wx.Frame): 
    def __init__(self, parent, title): 
      super(App, self).__init__(parent, title = title,size = (640,300))  
      panel = wx.Panel(self)
      sizer = wx.GridBagSizer(5, 4)
      
      #description
      text = wx.StaticText(panel, label="Folder path")
      sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT, border=10)
      
      #input field
      self.path = wx.TextCtrl(panel)
      sizer.Add(self.path, pos=(1, 0), span=(1, 4), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
      self.path.Bind(wx.EVT_TEXT,self.OnKeyTyped)

      #hint
      text2 = wx.StaticText(panel, style = wx.TE_MULTILINE, label="  Hint: hold Option after right-click on folder to show option to copy its path.")
      sizer.Add(text2, pos=(2, 0), span=(1, 3), flag=wx.BOTTOM|wx.TOP|wx.LEFT, border=5)

      #button open folder
      button_open = wx.Button(panel, label="Choose folder", size=(140, 24))
      button_open.Bind(wx.EVT_BUTTON, self.onDir)
      sizer.Add(button_open, pos=(1, 4), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

      

      #button execute
      button_execute = wx.Button(panel, label="Remove Alpha", size=(140, 24))
      self.Bind(wx.EVT_BUTTON, self.OnClickedExecute, button_execute)
      sizer.Add(button_execute, pos=(2, 4), flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=10)

      #output
      line = wx.TextCtrl(panel, wx.ID_ANY,style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_RICH2)
      sizer.Add(line, pos=(3, 0), span=(1, 5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
      sys.stdout = line
      sizer.AddGrowableCol(1)
      sizer.AddGrowableCol(3)
      sizer.AddGrowableRow(3) 
      panel.SetSizer(sizer)

    def OnKeyTyped(self, event):
        self.path = event.GetString()

    def OnClickedExecute(self, event):
        button_execute = event.GetEventObject().GetLabel()
        program(self.path)

    def OnClickedOpen(self, event):
        button_open = event.GetEventObject().GetLabel()
        onDir(self.path)
    
    #open folder modal
    def onDir(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            print ("Selected folder is %s" % dlg.GetPath())
            self.path = dlg.GetPath()



def remove_alpha(image):
    color=(255, 255, 255)
    image.load()  # treba za split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 je alpha channel
    return background

def program(path):
    for subdir, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".png"):
                pic_path = path+filename
                pic = Image.open(os.path.join(subdir, filename))
                if pic.mode in ('RGBA', 'LA') or (pic.mode == 'P' and 'transparency' in pic.info):
                    pic=remove_alpha(pic)
                    pic.save(os.path.join(subdir, filename))
                    print(os.path.join(subdir, filename))
                    proc = subprocess.Popen("ping %s", shell=True, stdout=subprocess.PIPE) 
                    line = proc.stdout.readline()
                      
app = wx.App(redirect=True) 
ex = App(None,  'PNG Alpha remover')
ex.Show()
app.MainLoop()
