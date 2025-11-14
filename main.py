from kivy.app import App
import webbrowser


from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.pagelayout import PageLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.accordion import Accordion
from kivy.uix.image import Image,AsyncImage
from kivy.core.audio import SoundLoader
from kivy.uix.video import Video
from kivy.storage.jsonstore import JsonStore
from kivy.properties import ObjectProperty
from kivy.uix.carousel import Carousel
from kivy.uix.popup import Popup

from kivy.uix.spinner import Spinner
from kivy.uix.modalview import ModalView
from kivy.uix.togglebutton import ToggleButton
import random
import string
import os
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.graphics import *
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.clock import Clock
Window.clearcolor=(1,1,1,1)
class Myar(App):

    
    
      
        
        
    def stopp(self,instance):
       
       
       self.popup.dismiss()
       
       
    
    def next(self,instance):
        
        if self.n != 0 :
            self.mysound.stop()
            
          
        self.n+=1
        self.u+=1
        
        
             
             
        if self.n <=27:
            self.lab.text=self.Letter_list[self.n]
        elif self.n>27:
            self.n=0
            self.u=0
            self.lab.text=self.Letter_list[self.n]
            
        if self.n==self.u and self.r !=3:
            self.mysound=SoundLoader.load(f"{self.sound_list[self.u]}.mp3")
            self.mysound.play()
           
        
    def build(self):
        self.Letter_list=["أ","ب","ت","ث","ج","ح","خ","د","ذ","ر","ز","س","ش","ص","ض","ط","ظ","ع","غ","ف","ق","ك","ل","م","ن","ه","و","ى"]
        
        self.sound_list=["Alef","Beh","Teh","Theh","Geem","hah","Qh","Dal","Zal","Reh","Zen","Seen","Sheen","Sad","Dad","Tah","Zaah","3en","Gen","Feah","Gaf","Kaf","Lam","Mem","Non","Heah","Waw","Yeh"]
        self.lay=Widget()
        self.n=0
        self.sx=0
        self.u=0
        self.r=0
        self.st=0
       
        
        
        
        self.lab=Label(text=self.Letter_list[self.n],font_name="arial-1.ttf",font_size=150,pos=(300,750),color=(0,0,0,1))
        
        self.but=Button(text="go",size_hint=(None,None),size=(150,70),pos=(300,200),on_press=self.next)
        
        
        
        
        self.mysoundc=SoundLoader.load(f"Question about the letter Alif.mp3")
        
        
        
      
        
        
        self.mysound1=SoundLoader.load("Alef.mp3")
        self.mysound1.play()
        
        self.mysound2=SoundLoader.load("Beh.mp3")
        
        self.mysound3=SoundLoader.load("Teh.mp3")
        
        self.mysound4=SoundLoader.load("Theh.mp3")
        
        self.mysound5=SoundLoader.load("Geem.mp3")
        
        self.mysound6=SoundLoader.load("hah.mp3")
        
        self.mysound7=SoundLoader.load("Qh.mp3")
        
        self.mysound8=SoundLoader.load("Dal.mp3")
        
        self.mysound9=SoundLoader.load("Zal.mp3")
        
        self.mysound10=SoundLoader.load("Reh.mp3")
        
        self.mysound11=SoundLoader.load("Zen.mp3")
        
        self.mysound12=SoundLoader.load("Seen.mp3")
        
        self.mysound13=SoundLoader.load("Sheen.mp3")
        
        self.mysound13=SoundLoader.load("Sad.mp3")
        
        self.mysound14=SoundLoader.load("Dad.mp3")
        
        self.mysound15=SoundLoader.load("Tah.mp3")
        
        self.mysound16=SoundLoader.load("Zaah.mp3")
        
        self.mysound18=SoundLoader.load("3en.mp3")
        
        self.mysound19=SoundLoader.load("Gen.mp3")
        
        self.mysound20=SoundLoader.load("Feah.mp3")
        
        self.mysound21=SoundLoader.load("Gaf.mp3")
        
        self.mysound22=SoundLoader.load("Kaf.mp3")
        
        self.mysound23=SoundLoader.load("Lam.mp3")
        
        self.mysound24=SoundLoader.load("Mem.mp3")
        
        self.mysound25=SoundLoader.load("Non.mp3")
        
        self.mysound26=SoundLoader.load("Heah.mp3")
        
        self.mysound27=SoundLoader.load("Waw.mp3")
        
        self.mysound28=SoundLoader.load("Yeh.mp3")
        
        
        self.lay.add_widget(self.lab)
        self.lay.add_widget(self.but)
        return self.lay
        
        
        
if __name__=="__main__":
    Myar().run()
