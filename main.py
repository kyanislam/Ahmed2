from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget

from kivy.app import App
from kivy.uix.button import Button, Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import Image,AsyncImage
from kivy.animation import Animation



Window.clearcolor=("#ff99e5ff")


class kyan(App):
    
    
    
    
    
    
    def start(self,instance):
        if self.m==0:
            
            animation= Animation(color=(1,0,1,1),duration=1)
            animation+= Animation(pos=(50,1350),size=(280,50),duration=1,t="in_sine")
            
            animation+= Animation(pos=(1,290),size=(717,970),duration=1,t="in_sine")
            
            animation.start(instance)
            animation.repeat= True
            
            self.but3.font_size=80
            self.m+=1
        elif self.m==1:
        
            self.lay.add_widget(self.but)
            self.lay.add_widget(self.but2)
            self.lay.remove_widget(self.lab2)
            self.lay.remove_widget(self.img)
            self.lay.remove_widget(self.but3)
            if  self.n ==0:
                Window.clearcolor = (self.z[self.n])
                
                self.lab.text="Red"
                self.mysound.play()
                self.n+=1
        
        
        
        
    def back(self,instance):
        if self.n !=12:
            self.lab.color=(1,1,1,1)
        if self.n==2:
            
            Window.clearcolor = (self.z[0])
            self.lab.text="Red"
            self.mysound.play()
            self.n=1
            
            
            
        elif self.n==3:
            
            Window.clearcolor = (self.z[1])
            self.lab.text="Green"
            self.mysound2.play()
            self.n=2
            
            
            
        elif self.n==4:
            
            Window.clearcolor = (self.z[2])
            self.lab.text="Blue"
            self.mysound3.play()
            self.n=3
            
        elif self.n==5:
            
            Window.clearcolor = (self.z[3])
            self.lab.text="Yellow"
            self.mysound4.play()
            self.n=4
            
        elif self.n==6:
            
            Window.clearcolor = (self.z[4])
            self.lab.text="Gray"
            self.mysound5.play()
            self.n=5
            
        elif self.n==7:
            
            Window.clearcolor = (self.z[5])
            self.lab.text="brown"
            self.mysound6.play()
            self.n=6
            
        elif self.n==8:
            
            Window.clearcolor = (self.z[6])
            self.lab.text="Silver"
            self.mysound7.play()
            self.n=7
            
        elif self.n==9:
            
            Window.clearcolor = (self.z[7])
            self.lab.text="Purple"
            self.mysound8.play()
            self.n=8
            
        elif self.n==10:
            
            Window.clearcolor = (self.z[8])
            self.lab.text="Labani"
            self.mysound9.play()
            self.n=9
            
            
        elif self.n==11:
            
            Window.clearcolor = (self.z[9])
            self.lab.text="orange"
            self.mysound10.play()
            self.n=10
            
        elif self.n==12:
            
            Window.clearcolor = (self.z[10])
            self.lab.text="Golden"
            self.mysound11.play()
            self.n=11
            
            
        elif self.n==0:
            
            Window.clearcolor = (self.z[11])
            
            self.lab.text="black"
            self.mysound12.play()
            self.n=12
            
        elif self.n ==1:
            Window.clearcolor = (self.z[12])
            self.lab.color=(0,0,0,1)
            self.lab.text="white"
            self.mysound13.play()
            self.n=0
            
            
        
 
            
        
            
        
            
            
            
        
    
    
            
            
            
            
    
    
        
    
    def stop(self,instance):
       
        
            
        if self.n != 12:
             self.lab.color=(1,1,1,1)
            
        
        if  self.n ==0:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Red"
            self.mysound.play()
            self.n+=1
            self.m=0
            self.lay.remove_widget(self.lab2)
            self.lay.remove_widget(self.img)
            
        
            
            
        elif self.n==1:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Green"
            self.mysound2.play()
            self.n+=1
            self.m=1
            
            
        elif self.n==2:
            
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Blue"
            self.mysound3.play()
            self.n+=1
            self.m=2
           
        elif self.n==3:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Yellow"
            self.mysound4.play()
            self.n+=1
            self.m=3
            
        elif self.n==4:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Gray"
            self.mysound5.play()
            self.n+=1
            self.m=4
          
        elif self.n==5:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="brown"
            self.mysound6.play()
            self.n+=1
            self.m=5
        elif self.n==6:
            Window.clearcolor = (self.z[self.n])
            
            
            self.lab.text="Silver"
            self.mysound7.play()
            self.n+=1
            self.m=6
            
        elif self.n==7:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Purple"
            self.mysound8.play()
            self.n+=1
            self.m=7
            
            
        elif self.n==8:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Labani"
            self.mysound9.play()
            self.n+=1
            self.m=8
            
        elif self.n==9:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="orange"
            self.mysound10.play()
            self.n+=1
            self.m=9
           
        elif self.n==10:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.text="Golden"
            self.mysound11.play()
            self.n+=1
            self.m=10
           
        elif self.n==11:
            Window.clearcolor = (self.z[self.n])
            self.lab.text="black"
            self.mysound12.play()
            self.n+=1
            self.m=11
            
        elif self.n == 12:
            Window.clearcolor = (self.z[self.n])
            
            self.lab.color=(0,0,0,1)
            self.lab.text="white"
            self.mysound13.play()
            
            self.m=12
            self.n=0
            
        
            
    
            
         
            
       
            
        
          
            
            
        
            
        
        
    def build(self):
        self.z=["#FF0000","#008000","#0000FF","#FFFF00","#808080","#806545","#C0C0C0","#7F00FF",'#00CED1',"#FF7F00","#FFD700","#000000","#FFFFFF"]
        self.n=0
        self.m=0
        self.lay=Widget()
        
        self.lab=Label(size_hint=(None,None),font_size=50,pos=(300,800))
        
        
        self.mysound=SoundLoader.load("red.mp3")
        
        self.mysound2=SoundLoader.load("green.mp3")
        self.mysound3=SoundLoader.load("Blue.mp3")
        self.mysound4=SoundLoader.load("Yellow.mp3")
        self.mysound5=SoundLoader.load("Gray.mp3")
        self.mysound6=SoundLoader.load("brown.mp3")
        self.mysound7=SoundLoader.load("Silver.mp3")
        self.mysound8=SoundLoader.load("Purple.mp3")
        self.mysound9=SoundLoader.load("Labani.mp3")
        self.mysound10=SoundLoader.load("orange.mp3")
        self.mysound11=SoundLoader.load("Golden.mp3")
        self.mysound12=SoundLoader.load("black.mp3")
        
        self.mysound13=SoundLoader.load("white.mp3")
        
        
        self.but=Button(text="Next",on_press=self.stop,size_hint=(None,None),size=(150,70))
        
        self.but2=Button(text="back",size_hint=(None,None),size=(150,70),pos=(570,1),on_press=self.back)
        
        self.but3=Button(text="start",size_hint=(None,None),size=(250,80),pos=(250,200),on_press=self.start,background_color=(0,1,0,1),font_size=50)
        
        self.lab2=Label(text="Colors game",font_size=60,pos=(300,1050))
        
        self.img=Image(source="images (5).png",pos=(180,600),size=(400,400))
        
        list_widget=[self.but,self.but2,self.lab,self.lab2,self.img]
        
        
        self.lay.add_widget(self.lab)
        self.lay.add_widget(self.lab2)
        self.lay.add_widget(self.img)
        self.lay.add_widget(self.but3)
        
        return self.lay
            
            

kyan().run()

