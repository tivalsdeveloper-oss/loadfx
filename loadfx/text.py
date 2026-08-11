import sys,time
from .colors import *
class TextFX:
 @staticmethod
 def color(text,code):return f"{code}{text}{RESET}"
 @staticmethod
 def red(t):return TextFX.color(t,RED)
 @staticmethod
 def green(t):return TextFX.color(t,GREEN)
 @staticmethod
 def yellow(t):return TextFX.color(t,YELLOW)
 @staticmethod
 def blue(t):return TextFX.color(t,BLUE)
 @staticmethod
 def magenta(t):return TextFX.color(t,MAGENTA)
 @staticmethod
 def cyan(t):return TextFX.color(t,CYAN)
 @staticmethod
 def white(t):return TextFX.color(t,WHITE)
 @staticmethod
 def gray(t):return TextFX.color(t,GRAY)
 @staticmethod
 def bold(t):return TextFX.color(t,BOLD)
 @staticmethod
 def dim(t):return TextFX.color(t,DIM)
 @staticmethod
 def underline(t):return TextFX.color(t,UNDERLINE)
 @staticmethod
 def blink(t):return TextFX.color(t,BLINK)
 @staticmethod
 def reverse(t):return TextFX.color(t,REVERSE)
 @staticmethod
 def rgb(text,r,g,b):return TextFX.color(text,rgb(r,g,b))
 @staticmethod
 def typewrite(text,speed=.03,end="\n",stream=None):
  stream=stream or sys.stdout
  for c in str(text):stream.write(c);stream.flush();time.sleep(speed)
  stream.write(end);stream.flush()
 @staticmethod
 def rainbow(text):
  codes=[RED,YELLOW,GREEN,CYAN,BLUE,MAGENTA];return "".join(codes[i%6]+c for i,c in enumerate(str(text)))+RESET
 @staticmethod
 def gradient(text,start=(255,80,80),end=(80,120,255)):
  s=str(text); n=max(1,len(s)-1); out=[]
  for i,c in enumerate(s):
   t=i/n; out.append(rgb(int(start[0]+(end[0]-start[0])*t),int(start[1]+(end[1]-start[1])*t),int(start[2]+(end[2]-start[2])*t))+c)
  return "".join(out)+RESET
 @staticmethod
 def box(text,padding=1,char="─"):
  lines=str(text).splitlines() or [""]; w=max(map(len,lines)); top="┌"+char*(w+padding*2)+"┐"; body=["│"+" "*padding+x.ljust(w)+" "*padding+"│" for x in lines]; return "\n".join([top,*body,"└"+char*(w+padding*2)+"┘"])
 @staticmethod
 def banner(text,width=None,char="="):
  text=str(text); width=width or max(len(text)+8,30); return f"{char*width}\n{text.center(width)}\n{char*width}"
 @staticmethod
 def center(text,width=None):return "\n".join(x.center(width or 80) for x in str(text).splitlines())
