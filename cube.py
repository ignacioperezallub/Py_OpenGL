# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from square import wcs,square

size,theta_y=0.5,0.0

def cube(size) :
  glBegin(GL_QUADS)
  glColor3ub(255,0,0)            # face rouge
  glVertex3d(size,size,size)
  glVertex3d(size,size,-size)
  glVertex3d(-size,size,-size)
  glVertex3d(-size,size,size)
  glColor3ub(0,255,0)            # face verte
  glVertex3d(size,-size,size)
  glVertex3d(size,-size,-size)
  glVertex3d(size,size,-size)
  glVertex3d(size,size,size) 
  glColor3ub(0,0,255)            # face bleue
  glVertex3d(-size,-size,size)
  glVertex3d(-size,-size,-size)
  glVertex3d(size,-size,-size)
  glVertex3d(size,-size,size) 
  glColor3ub(255,255,0)          #  face jaune
  glVertex3d(-size,size,size)
  glVertex3d(-size,size,-size)
  glVertex3d(-size,-size,-size)
  glVertex3d(-size,-size,size)
  glColor3ub(0,255,255)          # face cyan
  glVertex3d(size,size,-size)
  glVertex3d(size,-size,-size)
  glVertex3d(-size,-size,-size)
  glVertex3d(-size,size,-size)
  glColor3ub(255,0,255)        # face magenta
  glVertex3d(size,-size,size)
  glVertex3d(size,size,size)
  glVertex3d(-size,size,size)
  glVertex3d(-size,-size,size)
  glEnd()

def gl_init() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

def glut_init() :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(1200,1000)
  glutInitWindowPosition(100,100)
  glutCreateWindow(sys.argv[0])

def glut_event():
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(on_keyboard_action)
##  glutSpecialFunc(on_special_key_action);
##  glutIdleFunc(animate)

def display() :
  global size,theta_y
  gl_init()
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  camera=[4,3,2,0,0,0,0,1,0]
  # camera=[0,0,2,0,0,0,0,1,0]
  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
  glRotatef(theta_y,0,1,0)
#  glutWireCube(1)
  wcs(size+1)
  square(size)
  cube(size)
  glutSwapBuffers()

def reshape(width,height) :
  glViewport(0,0, width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0,width*1.0/height, 1.0, 10.0);

def on_keyboard_action(key, x, y) :
  global size,theta_y
  if key==b'h':
    print("----------------------------------------\n")
    print("Documentation interaction  : Nom-Prenom \n") 
    print("----------------------------------------\n") 
    print("h : afficher cette aide \n");
    print("f : afficher les facettes \n")
    print("a : afficher les aretes \n")
    print("s : afficher les sommets \n")
    print("c/C : afficher les faces CW/CCW \n")
    print("r/R : redimensionner l'objet \n")
    print("y/Y : tourner l'objet autour de l'axe Oy\n")
    print("e : sortie (exit) \n")
  elif key==b'f':
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
  elif key==b'a':
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
  elif key==b's' :
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
  elif key==b'e' :
    exit(0)
  else :
    pass
  glutPostRedisplay()

def on_special_key_action(key, x, y) :
  pass

def animate(key, x, y) :
  pass

if __name__ == "__main__" :
    glut_init()
    glut_event() 
    glutMainLoop()
