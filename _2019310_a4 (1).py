#NAME=ISHIKA JOSHI ROLL NO.=2019310




import os
import time
import random
#CLASS GRID IS PARENT CLASS IN THE CODE
class Grid:
	N=eval(input())
	
	start = [0,0]
	goal = [N-1,N-1]
	
    
	#THE FOLLOWING IS THE NESTED LIST USED FOR MAKING THE GRID
	myReward=[]
	myObstacle=[]
	o4=[]
	r4=[]
	for e in range(0,N):

		o2=random.sample(range(0,N),2)
		o4.append(o2)

	o1=random.randint(0,int(0.50*N))
	o3=(random.sample(o4,o1))
	myObstacle.append(o3)
	
	for e in range(0,N):

		r2=random.sample(range(0,N),2)
		r4.append(o2)
	r1=random.randint(0,int(0.50*N))
	r3=(random.sample(r4,r1))
	myReward.append(r3)
	x=[['.']]
	for y in range(0,N):
		for z in range(0,N):
			x[y].append('.')
		if len(x)<=N:
			x.append(['.'])
	
	for y in range(0,len(myObstacle[0])):
		if type((myObstacle)[0][y])==list and len((myObstacle)[0][y])==2 :
			x[(myObstacle)[0][y][0]][(myObstacle)[0][y][1]]='#'
		else:
			pass
	for y in range(0,len(myReward[0])):
		if type((myReward)[0][y])==list and len((myReward)[0][y])==2:
			x[(myReward)[0][y][0]][(myReward)[0][y][1]]=random.randint(0,9)
		else:
			pass
	
#x IS THE DESIRED NESTED LIST
		
		
	def showGrid(self):
		

		#WE OBTAIN THE GRID USING THE GIVEN FUNCTION 
		self.x[self.start[1]][self.start[0]]='O'
		self.x[self.goal[1]][self.goal[0]]='W'
		for i in range(0,self.N):
			for j in range(0,self.N):
				print ((self.x)[i][j],end=' ')
			print ('')

	def rotateAnticlockwise(self,n):
		self.n=n
		#THE GRID WILL ROTATE AS ASKED
		
		for y in range(0,self.n):
			self.x[self.start[0]][self.start[1]]='.'
			self.x[self.N-self.start[1]-1][self.start[0]]='O'
			self.start=[self.N-self.start[1]-1,self.start[0]]
			print (self.start)
			self.showGrid()

		

	def rotateClockwise(self,n):
		self.n=n
		#THE GRID WILL ROTATE AS ASKED
		for y in range(0,self.n):
			print (y)
			self.x[self.start[0]][self.start[1]]='.'
			self.x[self.start[1]][self.N-self.start[0]-1]='O'
			self.start=[self.start[1],self.N-self.start[0]-1]
			
			print (self.start)
			self.showGrid()

		


class Obstacle(Grid):
    
    def __init__(self):
        

        print (Grid.myObstacle)


class Reward(Grid):
    
    def __init__(self):
        

        print (Grid.myReward)
#the following class will be called to play the game
class Player(Grid):
	s=input('INPUT=')
	splC=int(input('splC='))
	splA=int(input('splA='))
	
	#s is the input str given by the player
	#splA and splC is the special fubction of clockwise rotation in which player will 
	#give the input as the number of desired rotations in anti clock(splA) and clock directions(splC)
	x1=(Grid.start)[0]
	y1=(Grid.start)[1]
	energy=2*(Grid.N)

	def makeMove(self):
		super().showGrid()
		print(self.energy)
		
		
#FIRST INPUT WILL THE ORIGINAL GRID
		
		while Grid.start!=Grid.goal and int(self.energy)>0:
			self.s=input('INPUT=')
			self.splC=int(input('splC='))
			self.splA=int(input('splA='))
			
			
			q=0
			p=0
			super().rotateAnticlockwise(self.splA)
			for i in range(self.splA):
				q=q+1

			self.energy=self.energy-(Grid.N//3)*(self.splA)
			

			super().rotateClockwise(self.splC)
			for i in range(self.splA):
				p=p+1
			self.energy=self.energy-(Grid.N//3)*(self.splC)
			super().showGrid
			print (self.energy)
			

			for inp in self.s:
				
				if inp=='D':
					next=int(self.s[(self.s).index(inp)+1])
					print (next)

					for z in range(0,next):

						if Grid.start[1]!=Grid.N -1:
							if Grid.x[(Grid.start)[1]+1][(Grid.start)[0]]=='#':
								#IF THE PLAYER MOVES INTO THE OBSTACLE ITS FORMER POSITION WILL NOT CHANGE

								Grid.start[1]==Grid.start[1]
								self.energy-=4*Grid.N
								Grid.x


								print (self.energy)
								super().showGrid()
							elif type(Grid.x[Grid.start[1]+1][Grid.start[0]])==int:

								Grid.start[1]+=1
								self.energy+=Grid.N
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								print (Grid.myReward[0])
								
								Grid.x

								print (self.energy)
								super().showGrid()

							else:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								Grid.start[1]+=1
								self.energy-=1
								print (Grid.start)

								Grid.x
								print (self.energy)
								super().showGrid()


						else:
							Grid.x[Grid.start[1]][Grid.start[0]]='.'
							Grid.start[1]=0

							self.energy-=1
							Grid.x
							print (self.energy)
							super().showGrid() 


				if inp=='U':
					next=int(self.s[(self.s).index(inp)+1])
					for x in range(0,next):

						if Grid.start[1]!=0:
							if Grid.x[Grid.start[1]-1][Grid.start[0]]=='#':
								#IF THE PLAYER MOVES INTO THE OBSTACLE ITS FORMER POSITION WILL NOT CHANGE

								Grid.start[1]=Grid.start[1]
								self.energy-=4*Grid.N
								Grid.x

								print (self.energy)
								super().showGrid()
							elif type(Grid.x[Grid.start[1]-1][Grid.start[0]])==int:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'

								Grid.start[1]-=1
								self.energy+=Grid.N
								
								
								Grid.x

								print (self.energy)
								super().showGrid()

							else:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								Grid.start[1]-=1
								self.energy-=1
								print (Grid.start)

								Grid.x
								print (self.energy)
								super().showGrid()


						else:
							Grid.x[Grid.start[1]][Grid.start[0]]='.'
							Grid.start[1]=Grid.N-1
							self.energy-=1
							Grid.x
							print (self.energy)
							super().showGrid()


				if inp=='L':
					next=int(self.s[(self.s).index(inp)+1])
					for x in range(0,next):

						if Grid.start[0]!=0:
							if Grid.x[Grid.start[1]][Grid.start[0]-1]=='#':
								#IF THE PLAYER MOVES INTO THE OBSTACLE ITS FORMER POSITION WILL NOT CHANGE


								Grid.start[0]=Grid.start[0]
								self.energy-=4*Grid.N
								Grid.x

								print (self.energy)
								super().showGrid()
							elif type(Grid.x[Grid.start[1]][Grid.start[0]-1])==int:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'

								Grid.start[0]-=1
								self.energy+=Grid.N
								
								
								Grid.x

								print (self.energy)
								super().showGrid()

							else:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								Grid.start[0]-=1
								self.energy-=1
								Grid.x
								print (self.energy)
								super().showGrid()


						else:
							Grid.x[Grid.start[1]][Grid.start[0]]='.'
							Grid.start[0]=Grid.N-1
							self.energy-=1
							Grid.x
							print (self.energy)
							super().showGrid() 


				if inp=='R':
					next=int(self.s[(self.s).index(inp)+1])
					for x in range(0,next):

						if Grid.start[0]!=Grid.N-1:
							if Grid.x[Grid.start[1]][Grid.start[0]+1]=='#':
								#IF THE PLAYER MOVES INTO THE OBSTACLE ITS FORMER POSITION WILL NOT CHANGE

								Grid.start[0]=Grid.start[0]
								self.energy-=4*Grid.N
								Grid.x

								print (self.energy)
								super().showGrid()
							elif type(Grid.x[Grid.start[1]][Grid.start[0]+1])==int:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								Grid.start[0]+=1
								self.energy+=Grid.N
								
								
								Grid.x

								print (self.energy)
								super().showGrid()

							else:
								Grid.x[Grid.start[1]][Grid.start[0]]='.'
								Grid.start[0]+=1
								self.energy-=1
								Grid.x
								print (self.energy)
								super().showGrid()


						else:
							Grid.x[Grid.start[1]][Grid.start[0]]='.'
							Grid.start[0]=0
							self.energy-=1
							Grid.x
							print (self.energy)
							super().showGrid()



			print (Grid.start)
			
		if Grid.start==Grid.goal:
			print('YOU WIN')

		else:
			print('YOU LOSE')

			



game1=Grid()
ya=Player()
ya.makeMove()
 


					




			