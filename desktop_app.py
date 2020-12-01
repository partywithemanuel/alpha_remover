import wx
import matplotlib.pyplot as plt
import os
import sys
from PIL import Image

directory = "/Users/emanuel/Downloads/Archive" # root - tu promijeni path u root folder gdje su ti slike

class Mywin(wx.Frame): 
    def __init__(self, parent, title): 
      super(Mywin, self).__init__(parent, title = title,size = (200,150))  
      panel = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      
      #textbox
      hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
      l1 = wx.StaticText(panel, -1, "Folder path") 
		
      hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      self.t1 = wx.TextCtrl(panel) 
		
      hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
      self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
      vbox.Add(hbox1) 

      #button
      self.btn = wx.Button(panel,-1,"Remove Alpha channel") 
      vbox.Add(self.btn,0,wx.ALIGN_CENTER) 
      self.btn.Bind(wx.EVT_BUTTON,self.OnClicked)


      #output
      log = wx.TextCtrl(panel, size=(300,100))
      sys.stdout=log

  
      hbox = wx.BoxSizer(wx.HORIZONTAL) 
      vbox.Add(hbox,1,wx.ALIGN_CENTER) 
      panel.SetSizer(vbox) 
        
      self.Centre() 
      self.Show() 
      self.Fit()

    def OnKeyTyped(self, event):
        directory=event.GetString()

    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel() 
        print("Label of pressed button = ",btn )
        program(directory)

def remove_alpha(image,):
    color=(255, 255, 255)
    image.load()  # treba za split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 je alpha channel
    return background

def program(path):
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".png"):
                pic_path = directory+filename
                pic = Image.open(os.path.join(subdir, filename))
                if pic.mode in ('RGBA', 'LA') or (pic.mode == 'P' and 'transparency' in pic.info):
                    pic=remove_alpha(pic)
                    pic.save(os.path.join(subdir, filename))
                    print(os.path.join(subdir, filename))  

app = wx.App(redirect=True) 
Mywin(None,  'PNG Alpha remover') 
app.MainLoop()
