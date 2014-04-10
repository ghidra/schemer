import subprocess
class output:

  terminals = ['gnome']
  use = ""
  valid = False
  
  def __init__(self,terminal):
    self.use = terminal
    self.valid = terminal in self.terminals

  def output(self,colors):
    method = getattr(self,'print'+self.use)
    s = method(colors)
    return s

  #----------
  def rgb8_to_rgb16(self,value): 
    """https://github.com/jmcantrell/python-imageutils/blob/master/imageutils/color.py
    Scales an 8-bit RGB tuple up to a 16-bit value.
    >>> rgb8_to_rgb16((255, 255, 255))
    (65535, 65535, 65535)"""
    return tuple(v*257 for v in value)

  def rgb_to_hex(self,c):
    #http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
    t = (c[0],c[1],c[2])
    return '#%02x%02x%02x' % t

  #---------

  def printgnome(self,colors):
    # ~/.gconf/apps/gnome-terminal/profiles/Default/%gconf.xml
    '''#default pallette : 
      #2E2E34343636:#CCCC00000000:#4E4E9A9A0606:#C4C4A0A00000:#34346565A4A4:#757550507B7B:#060698209A9A:#D3D3D7D7CFCF:
      #555557575353:#EFEF29292929:#8A8AE2E23434:#FCFCE9E94F4F:#72729F9FCFCF:#ADAD7F7FA8A8:#3434E2E2E2E2:#EEEEEEEEECEC

    s=""
    for c in colors:
      cc = self.rgb_to_hex(self.rgb8_to_rgb16(c))
      s+=cc+":"
    return "\n<stringvalue>"+s[:-1].upper()+"</stringvalue>\n"

    '''
    # compile the colors
    s=""
    for c in colors:
      cc = self.rgb_to_hex(self.rgb8_to_rgb16(c))
      s+=cc+":"

    cm = "gconftool-2 -s -t string /apps/gnome-terminal/profiles/Default/"
    fcm = cm+"palette /"+s[:-1].upper()

    '''fcm+=cm+"background_color " + bgcolor
    fcm+=cm+"foreground_color_color " + fgcolor
    fcm+=cm+"bold_color " + bdcolor'''
    
    #subprocess.call([fcm])
    return '\n'+fcm+'\n'