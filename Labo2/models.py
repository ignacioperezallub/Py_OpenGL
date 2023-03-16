from math import pi,sin,cos

try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from primitives import *

class Model :
  def __init__(self,size=1.0) :
    self.size=size
    self.angle=0.0
    self.position=[0.0,0.0,0.0]
  # getter/setter

  def set_size(self,size) :
    self.size=size

  def get_size(self) :
    return self.size
  
  def set_orientation(self,angle) :
    #print(angle)
    self.angle=angle

  def get_orientation(self) :
    return self.angle
  
  def set_position(self,position) :
    self.position=position

  def get_position(self) :
    return self.position
  
  def create(self) :
    raise NotImplementedError

class Car(Model) :
  def __init__(self,size=1.0) :
    Model.__init__(self,size)
    self.wheel_rot = 0
    self.wheel_turn = 0

    glPushMatrix()
    glRotate(90, 0, 1, 0)
    glTranslatef(2, 2, 0)
    self.create()
    glPopMatrix()

  def set_wheel_rot(self,wheel_rot) :
    self.wheel_rot = wheel_rot

  def get_wheel_rot(self) :
    return self.wheel_rot
  
  def set_wheel_turn(self,wheel_turn) :
    self.wheel_turn = wheel_turn

  def get_wheel_turn(self) :
    return self.wheel_turn
  
  def reset_car(self):
    self.position=[0.0,0.0,0.0]
    self.angle=0.0


  def create(self) :
    glPushMatrix()
    #glScalef(1,1,2)
    x,y,z=self.position[0],self.position[1],self.position[2]
    glTranslatef(x,y,z)
    glRotatef(self.angle,0,1,0)

    # car body
    centralTurn = -self.size/4
    axe(0.2*self.size,0.7*self.size,centralTurn=centralTurn )

    # roue av droite
    glPushMatrix()
    glTranslatef(-0.2*self.size*0.8,0,0.2*self.size*1.5+centralTurn)
    glRotatef(90, 0, 1, 0)
    glRotatef(self.wheel_turn, 0, 1, 0)
    glRotatef(self.wheel_rot, 0, 0, 1)
    self.wheel()
    glPopMatrix()
    
    # roue av gauche
    glPushMatrix()
    glTranslatef(0.2*self.size*0.8,0,0.2*self.size*1.5+centralTurn)
    glRotatef(-90, 0, 1, 0)
    glRotatef(self.wheel_turn, 0, 1, 0)
    glRotatef(self.wheel_rot, 0, 0, 1)
    self.wheel()
    glPopMatrix()

    # roue ar droite
    glPushMatrix()
    glTranslatef(-0.2*self.size*0.8,0,0.2*self.size*0.4+centralTurn)
    glRotatef(90, 0, 1, 0)
    glRotatef(self.wheel_rot, 0, 0, 1)
    self.wheel()
    glPopMatrix()

    # roue ar gauche
    glPushMatrix()
    glTranslatef(0.2*self.size*0.8,0,0.2*self.size*0.4+centralTurn)
    glRotatef(-90, 0, 1, 0)
    glRotatef(self.wheel_rot, 0, 0, 1)
    self.wheel()
    glPopMatrix()

    glPopMatrix()

  def wheel(self,boulons=5) :
    #glutWireCube(0.2*self.size)
    angle=360.0/boulons
    glPushMatrix()
    glColor3f(0,0,0)
    torus(0.07*self.size*0.5, 0.07*self.size, 10, 10)
    glTranslatef(0,0,0.07*self.size*0.1)
    glColor3f(1,1,1)
    disk(0, 0.07*self.size*0.7)
    glPopMatrix()

    glPushMatrix()
    glRotatef(180,0,1,0)
    glTranslatef(0,0,0.07*self.size*0.1)
    disk(0, 0.07*self.size*0.7)
    glPopMatrix()
    for i in range(boulons) :
      glPushMatrix()
      glRotatef(angle*i,0.0,0.0,1.0)
      glTranslatef(0.70*(0.07*self.size/2.0),0.0,-0.5*0.5*0.07*self.size)
      stick(0.05*0.07*self.size, 0.05*0.07*self.size, 0.07*self.size*0.5)
      #glutWireCube(0.20*self.size)
      glPopMatrix()


class Crane(Model) :
  def __init__(self,size=1.0) :
    Model.__init__(self,size)
    self.arm_angle=30.0           # arm angle rotation
    self.forarm_angle=30.0        # forarm angle rotation

  def set_arm_angle(self,angle) :
    self.arm_angle=angle

  def get_arm_angle_arm(self) :
    return self.arm_angle
  
  def set_forarm_angle(self,angle) :
    self.forarm_angle=angle

  def get_forarm_angle(self) :
    return self.forarm_angle
  
  def reset_crane(self):
    self.position=[0.0,0.0,0.0]
    self.angle=0.0
    self.arm_angle=30.0          
    self.forarm_angle=30.0

  def create(self) :
    # TO DO : crane (une grue) creation
    # Cockpit : a red cube
    # forarm : a green cylinder
    # joint : a red sphere
    # arm :  a green cylinder

    glPushMatrix()
    glTranslatef(self.position[0],self.position[1],self.position[2])
    glRotatef(self.angle,0,1,0)

    # forearm : a blue cylinder
    glPushMatrix()
    glTranslatef(0.0,self.size*4.5,self.size*0.5)
    glRotatef(self.arm_angle, 0, 0, 1)  # rotate the forearm around the joint

    # first cylinder matrix
    glPushMatrix()
    # second sphere matrix                         
    glPushMatrix()                         
    glTranslatef(0.0,self.size*5,0.0)
    glRotatef(self.forarm_angle, 0, 0, 1)  # rotate the forearm around the joint
    
    # tool :  a black cone
    glPushMatrix()
    glColor3f(0.0,0.0,0.0)
    glTranslatef(0.0,self.size*5.5,0.0)
    glRotatef(-90, 1, 0, 0)
    cone(self.size,self.size*2)
    glPopMatrix()                          #######################
    # second cylinder matrix
    glPushMatrix()                         
    glTranslatef(0.0,self.size*0.5,0.0)
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.0,0.0,1.0)
    cylinder(self.size/2,self.size/2,self.size*5)
    glPopMatrix()                          #######################

    glColor3f(1.0,0.0,0.0)
    sphere(self.size)
    glPopMatrix()                          #######################

    glRotatef(-90, 1, 0, 0)
    glColor3f(0.0,0.0,1.0)
    cylinder(self.size/2,self.size/2,self.size*5)
    glPopMatrix()                          #######################

    glPopMatrix()

    # joint : a red sphere
    glPushMatrix()
    glColor3f(1.0,0.0,0.0)
    glTranslatef(0.0,self.size*4.5,self.size*0.5)
    sphere(self.size)
    glRotatef(self.arm_angle, 0, 0, 1)  # rotate the joint itself
    glPopMatrix()

    # Cockpit : a red cube
    glPushMatrix()
    glTranslatef(0.0,self.size*3,self.size*0.5)
    glRotatef(-90, 1, 0, 0)
    cube(self.size)
    glPopMatrix()

    glPopMatrix()
    

def display() :
  size=2.0
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  posx,posy,posz=2,5,10
  dirx,diry,dirz=0,0,0
  vupx,vupy,vupz=0,1,0
  gluLookAt(posx,posy,posz,dirx,diry,dirz,vupx,vupy,vupz)
  # scene creation  : begin
  floor(10*size) 
  glPushMatrix()
  glColor3f(1.0,0.0,1.0)
  # glutSolidTeapot(self.size/5.0)
  Car(size) 
  glPopMatrix()
  # scene creation  : end
  glutSwapBuffers()

def reshape(width,height) :
  glViewport(0,0, width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  fovy,ratio,near,far=60.0,width*1.0/height,0.1,50.0
  gluPerspective(fovy,ratio,near,far)

if __name__ == "__main__" :
  glutInit(sys.argv)
  glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowSize (500, 500)
  glutInitWindowPosition (100, 100)
  glutCreateWindow ("REV OpenGL modeles")
  glClearColor(1.0,1.0,1.0,1.0)
  dimension=2.0 
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)

  glutMainLoop()
