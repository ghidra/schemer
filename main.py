import os
import sys
from PIL import Image, ImageFilter
from output import *

def load_image(im):
  try:
    my_im = Image.open(im)
    #my_im.load()
    return my_im
  except:
    return "error"

def color_difference(c1,c2,th):
  rd = abs( int(c1[0])-int(c2[0]) )
  gd = abs( int(c1[1])-int(c2[1]) )
  bd = abs( int(c1[2])-int(c2[2]) )

  t = rd+gd+bd
  return t>=th

def get_distinct_colors(co,th,mn,mx):
  colors = []
  for c in co:
    same = False
    if not color_difference(c,(0,0,0),mn):
      continue
    if not color_difference(c,(255,255,255),mx):
      continue
    for k in colors:
      if not color_difference(c,k,th):
	same = True
	break
    if not same:
      colors.append(c)
  return colors
    
def get_extremes(v,c):
  start = 255-v
  r = start
  count = 0
  i = 0
  for cs in c:
    ca = (cs[0]+cs[1]+cs[2])/3
    if start > 0:
      if ca < r:
        r = ca
        i=count
    else:
      if ca > r:
        r = ca
        i=count
    count+=1
  return i

def main(kwargs):
  #terminal output init
  out = output(kwargs[1])
  if not out.valid:
    print "Did not recognize format \""+ kwargs[1]+"\""
    return
  #parameters
  threshold = len(kwargs)>3 and kwargs[3] or 50
  min_brightness = len(kwargs)>4 and kwargs[4] or 50
  max_brightness = len(kwargs)>5 and kwargs[5] or 200
  display = len(kwargs)>6 and kwargs[6] or True
  debug = len(kwargs)>7 and kwargs[7] or False

  if min_brightness > 255 or max_brightness > 255:
    print "minimum and maximum brightness must be between 0 and 255"
    return
  if threshold > 255:
    print "threshold should be an integer between 0 and 255"
    return

  #Load the image and create an array of colors 
  fuzziness = 5
  my_im = load_image(kwargs[2])
  if my_im != "error":
    w,h = my_im.size
    if debug:
      print "image width:"+w
      print "image height:"+h
  else:
    print "image not recognized"
    return
  colors = []
  l = my_im.load()
  for x in range(0,w-1,fuzziness):
    for y in range(0,h-1,fuzziness):
      c = l[x,y]
      colors.append(c)

  #get distinct colors
  distinct_colors = get_distinct_colors(colors,threshold,min_brightness,max_brightness)
  #ensure there are 16
  count = 0
  nc = 18 #number of colors
  while len(distinct_colors)<nc:
    count+=1
    distinct_colors.extend(get_distinct_colors(colors,threshold-count,min_brightness,max_brightness))
    if count == threshold:
      print "could not get colors from image with settings specified, Aborting.\n"
      return
  if len(distinct_colors)>nc:
    del distinct_colors[nc:]

  #get the darkest and lightest color
  darkest_i = get_extremes(0,distinct_colors)
  darkest = distinct_colors[darkest_i]
  del distinct_colors[darkest_i]
  lightest_i = get_extremes(255,distinct_colors)
  lightest = distinct_colors[lightest_i]
  del distinct_colors[lightest_i]

  #display
  if display:
    margin = 16
    im = Image.new("RGB", (512+(margin*2), 512+(margin*2)), darkest)
    sq = 128
    count = 0
    for c in distinct_colors:
      x = ((count%4)*sq)+margin
      y = ((count/4)*sq)+margin
      im.paste(c,(x,y,x+sq,y+sq))
      count+=1
    im.paste(lightest,(margin*2,margin*2,margin*4,margin*4))
    im.show()
      
  #output
  print out.output(distinct_colors,lightest,darkest)


if __name__ == "__main__":
  main(sys.argv)
