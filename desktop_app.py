import wx
import operator

# We make a class for frame, so that each time we create a new frame,
# we can simply create a new object for it

class WordPlay(wx.Frame):
    def __init__(self, parent, title):
        super(WordPlay, self).__init__(parent, title=title)
        self.widgets()
        self.Show()

    # Declare a function to add new buttons, icons, etc. to our app
    def widgets(self):
        text_box = wx.BoxSizer(wx.VERTICAL)

        self.textbox = wx.TextCtrl(self, style=wx.TE_LEFT)
        text_box.Add(self.textbox, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)

        grid = wx.GridSizer(0, 0, 0) # Values have changed to make adjustments to button positions
        button_list = ['Run'] # List of button labels

        for lab in button_list:
            button = wx.Button(self, -1, lab) # Initialise a button object
            grid.Add(button, 0, wx.EXPAND) # Add a new button to the grid with the label from button_list

        text_box.Add(grid, proportion=2, flag=wx.EXPAND)

        self.SetSizer(text_box)

def event_handler(self, event):
    # Get label of the button clicked
    btn_label = event.GetEventObject().GetLabel()

    # Get the text entered by user
    path = self.textbox.GetValue()


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

def remove_alpha(image,):
    color=(255, 255, 255)
    image.load()  # treba za split()
    background = Image.new('RGB', image.size, color)
    background.paste(image, mask=image.split()[3])  # 3 je alpha channel
    return background

def main():
    myapp = wx.App()
    WordPlay(None, title='Word Play')
    myapp.MainLoop()

main()