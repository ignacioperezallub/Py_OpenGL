# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,cos,sin,radians

from primitives import wcs,square,stick

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from primitives import *

size,theta_y=0.5,0.0
position=[0,0,0]
orientation=0
length = 0.5
phi = 30*pi/180
wcs_visible = True

# TODO : create bolts 
def bolt(radius, height):
   pass

def wheel(size,bolts=5) :
  glPushMatrix()
  glColor3f(0,0,0)
  torus(size*0.5, size, 10, 10)
  glTranslatef(0,0,size*0.1)
  glColor3f(1,1,1)
  disk(0, size*0.7)
  glPopMatrix()

  glPushMatrix()
  glRotatef(180,0,1,0)
  glTranslatef(0,0,size*0.1)
  disk(0, size*0.7)
  glPopMatrix()


  glPushMatrix()
  glTranslatef(0.3*size, 0 , -0.5*0.5*size)
  stick(0.05*size, 0.05*size, size*0.5)
  glPopMatrix()
  glPushMatrix()
  glTranslatef(0.3*size*cos(radians(1*360/5)),0.3*size*sin(radians(1*360/5)),-0.5*0.5*size)
  stick(0.05*size, 0.05*size, size*0.5)
  glPopMatrix()
  glPushMatrix()
  glTranslatef(0.3*size*cos(radians(2*360/5)),0.3*size*sin(radians(2*360/5)),-0.5*0.5*size)
  stick(0.05*size, 0.05*size, size*0.5)
  glPopMatrix()
  glPushMatrix()
  glTranslatef(0.3*size*cos(radians(3*360/5)),0.3*size*sin(radians(3*360/5)),-0.5*0.5*size)
  stick(0.05*size, 0.05*size, size*0.5)
  glPopMatrix()
  glPushMatrix()
  glTranslatef(0.3*size*cos(radians(4*360/5)),0.3*size*sin(radians(4*360/5)),-0.5*0.5*size)
  stick(0.05*size, 0.05*size, size*0.5)
  glPopMatrix()

def car(size) :
  base = size/5
  height = size*1.5
  cylinder_base = base * 0.6
  cylinder_height = height * 0.6
  glTranslatef(0,0.04,0)
  glPushMatrix()
  position=[0,cylinder_base/1.2,0] #size*1.5
  glTranslatef(position[0],position[1],position[2])
  #glRotatef(0, 0, 0, 1)
  glColor3f(1.0, 0.5, 0.2)  # yellow
  axe(base,height)
  glPopMatrix()
  
  #Wheel FR
  glPushMatrix()
  glTranslatef(-cylinder_base*1.3,0,cylinder_height*0.8)
  glRotatef(90, 0, 1, 0)
  wheel(size/8,5)
  glPopMatrix()

  #Wheel FL
  glPushMatrix()
  glTranslatef(cylinder_base*1.3,0,cylinder_height*0.8)
  glRotatef(90, 0, 1, 0)
  wheel(size/8,5)
  glPopMatrix()
  
  #Wheel BR
  glPushMatrix()
  glTranslatef(-cylinder_base*1.3,0,cylinder_height*0.2)
  glRotatef(90, 0, 1, 0)
  wheel(size/8,5)
  glPopMatrix()
  
  #Wheel BL
  glPushMatrix()
  glTranslatef(cylinder_base*1.3,0,cylinder_height*0.2)
  glRotatef(90, 0, 1, 0)
  wheel(size/8,5)
  glPopMatrix()
  #glPopMatrix()
  

def display() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  #camera=[0,0,2,0,0,0,0,1,0]
  
  camera=[length*sin(phi)*cos(theta_y), length*cos(phi), length*sin(phi)*sin(theta_y),
          0,0,0,
          0,1,0]

  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
  glRotatef(theta_y,0,1,0)
  floor(size*10)
  if wcs_visible: wcs(size*0.8)  
  
  glPushMatrix()
  glTranslatef(position[0],position[1],position[2])
  glRotatef(orientation,0,1,0)
  car(0.5*size)
  glPopMatrix()
  glPushMatrix()
  
  glutSwapBuffers()
  # glPushMatrix()
  # glTranslatef(position[0],position[1],position[2])
  # cube(0.3*size)
  # glRotatef(orientation,0,1,0)
  # glColor3f(1,0,0)
  # torus(0.1*size,0.5*size)
  glPopMatrix()
  

def reshape(width,height) :
  print("reshape width : {}, height : {}".format(width,height))
  glViewport(0,0,width,height)
  perspective=[60.0,width*1.0/height, 0.1,10.]
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(perspective[0],perspective[1],perspective[2],perspective[3])

def on_keyboard_action(key,x,y) :
  global size,theta_y,wcs_visible, length
  if key==b'h':
    print("Documentation Interaction  : Nom-Prenom ") 
    print("h : afficher cette aide")
    # print("s : sortie d'application")
    print("----------------------------------------") 
    print("---------") 
    print("Affichage")
    print("---------") 
    print("e : aretes \n")
    print("f : facettes \n")
    print("v : sommets \n")
    print("c/C : faces CW/CCW \n")
    print("r/R : redimensionner l'objet \n")
    print("y/Y : tourner l'objet autour de l'axe Oy\n")
    print("w : afficher/cacher le repere de scene")
  elif key==b'e':
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
  elif key==b'f':
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
  elif key==b'v' :
    glPolygonMode(GL_FRONT_AND_BACK,GL_POINT)
  elif key==b'c' :
    glFrontFace(GL_CW)
  elif key==b'C' :
    glFrontFace(GL_CCW)
  elif key==b'r' :
    length-=0.1
  elif key==b'R' :
    length+=0.1
  elif key==b'y' :
    theta_y-=1.0*pi/180
  elif key==b'Y' :
    theta_y+=1.0*pi/180
  # elif key==b's' :
  #   sys.exit()
  elif key==b'w' :
    wcs_visible = True
  elif key==b'W' :
    wcs_visible = False
  else :
    pass
  glutPostRedisplay()
  
def on_special_key_action(key,x,y) :
  global position,orientation
  if key ==  GLUT_KEY_UP :
    position[0]+=0.1*size*sin(orientation*pi/180.0)
    position[2]+=0.1*size*cos(orientation*pi/180.0)
  elif  key ==  GLUT_KEY_DOWN :
    position[0]-=0.1*size*sin(orientation*pi/180.0)
    position[2]-=0.1*size*cos(orientation*pi/180.0)
  elif key ==  GLUT_KEY_LEFT :
    orientation+=5
  elif  key ==  GLUT_KEY_RIGHT :
    orientation-=5
  else :
    pass
  glutPostRedisplay()

def animation() :
   print("animation()")

if __name__ == "__main__" :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(600,400)
  glutInitWindowPosition(600,300)
  glutCreateWindow("REV OpenGL Scene : Dupont Jean")
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(on_keyboard_action)
  glutSpecialFunc(on_special_key_action)
#   glutIdleFunc(animation)
  glutMainLoop()

