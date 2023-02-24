# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,cos,sin, radians

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

# TODO : create bolts 
def bolt(radius, height):
  stick(radius, radius, height)

# TODO : create wheel with bolts 
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
# TODO : create car : body (axe) + 4 wheels
def car(size) :
   pass

def display() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  camera=[0,0,2,0,0,0,0,1,0]
  # camera=[1,1,1,0,0,0,0,1,0]
  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
  floor(10*size)
  wcs(2*size)
  glRotatef(theta_y,0,1,0)

  wheel(size,5)
  # glPushMatrix()
  # glTranslatef(position[0],position[1],position[2])
  # cube(0.3*size)
  # glRotatef(orientation,0,1,0)
  # glColor3f(1,0,0)
  # torus(0.1*size,0.5*size)
  # glPopMatrix()
  glutSwapBuffers()

def reshape(width,height) :
  print("reshape width : {}, height : {}".format(width,height))
  glViewport(0,0,width,height)
  perspective=[60.0,width*1.0/height, 0.1,10.]
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(perspective[0],perspective[1],perspective[2],perspective[3])

def on_keyboard_action(key,x,y) :
  global size,theta_y,wcs_visible
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
    size-=0.1
  elif key==b'R' :
    size+=0.1
  elif key==b'y' :
    theta_y-=1.0
  elif key==b'Y' :
    theta_y+=1.0
  elif key==b's' :
    sys.exit()
  elif key==b'w' :
    pass
  else :
    pass
  glutPostRedisplay()
  
def on_special_key_action(key,x,y) :
  global position,orientation
  if key ==  GLUT_KEY_UP :
    position[0]+=0.1*size*sin(orientation*pi/180.0)
    position[2]+=0.1*size*cos(orientation*pi/180.0)
  elif  key ==  GLUT_KEY_DOWN :
    pass
  elif key ==  GLUT_KEY_LEFT :
    orientation+=5
  elif  key ==  GLUT_KEY_RIGHT :
    pass
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
