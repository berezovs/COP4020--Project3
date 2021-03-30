import tkinter as tk


class Window:
    def __init__(self, fsa):
        self.fsa = fsa
        self.numStates = fsa.getNumStates()
        self.acceptStates = fsa.getAcceptStates()
        self.width = 300
        self.height = int(fsa.getNumStates())*120
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, borderwidth=0, highlightthickness=0, bg="white")
    
    def drawCircle(self, x0, y0, x1, y1):
        self.canvas.create_oval(x0, y0, x1, y1, fill="white")

    def drawCircles(self):
        for circle in range(0, self.numStates):
            self.drawCircle(120, 20+(circle*120), 180, 20+(circle*120)+60)
            if(circle in self.acceptStates):
                self.drawCircle(125, 25+(circle*120), 175, 25+(circle*120)+50)
            self.canvas.create_text(150, 20+(circle*120)+30, text=str(circle))


    def drawTransitions(self):

        transitions = self.fsa.getTransitions()
        longTransitionsCount = 0
        for which in range(0, len(transitions)):
            cir_diameter = 60
            transition = transitions[which].split(':')
             #handles transitions between two neighboring states; from the state above to state below (e.g. from state 1 to 2)
            if(int(transition[1])==(int(transition[0])+1)):
                self.canvas.create_line(150, 20+cir_diameter+int(transition[0])*(cir_diameter)*2, 150, 20+cir_diameter+int(transition[0])*(cir_diameter)*2+cir_diameter, arrow = tk.LAST)
                self.canvas.create_text(160, 50+cir_diameter+int(transition[0])*(cir_diameter)*2, text = transition[2])
            #handles transitions between two neighboring states; from the state below to state above (e.g. from state 2 to 1)
            elif(int(transition[1])==(int(transition[0])-1)):
                self.canvas.create_line(150, 20+cir_diameter+int(transition[1])*(cir_diameter)*2, 150, 20+cir_diameter+int(transition[1])(cir_diameter)*2+cir_diameter, arrow = tk.FIRST)
                self.canvas.create_text(160, 50+cir_diameter+int(transition[1])*(cir_diameter)*2, text = transition[2])
            #handles transitions from one state to the same state(e.g. from state 1 to state 1)
            elif(int(transition[1])==int(transition[0])):
                #draw a circle partially underneath the circle representing a state
                self.drawCircle(160, (cir_diameter/2)+int(transition[1])*(cir_diameter)*2, 200, (cir_diameter/2)+int(transition[1])*120+40)
                #the following two lines draw a short line(1px) with an arrow and position it on the canvas such that the circle
                # drawn by the line above looks like a circular arrow 
                self.canvas.create_line(170, (cir_diameter/2)+int(transition[1])*(cir_diameter)*2, 171, (cir_diameter/2)+int(transition[1])*120, arrow = tk.FIRST)
                self.canvas.create_text(210, 20+(cir_diameter/2)+int(transition[0])*(cir_diameter)*2, text = transition[2])
           
            else:
                #the following four lines of code handle transitions which connect two states with other states in between(e.g. state 2 and 4, or 0 and 3)
                #therefore more than one line is needed to construct such an arrow
                
                self.canvas.create_line(100-longTransitionsCount, 20+(cir_diameter/2)+int(transition[1])*(cir_diameter)*2, 100-longTransitionsCount, 20+(cir_diameter/2)+int(transition[0])*120)
                self.canvas.create_line(100-longTransitionsCount, 20+(cir_diameter/2)+int(transition[1])*(cir_diameter)*2, (cir_diameter)*2, 20+(cir_diameter/2)+int(transition[1])*(cir_diameter)*2, arrow=tk.LAST)
                self.canvas.create_line(100-longTransitionsCount, 20+(cir_diameter/2)+int(transition[0])*(cir_diameter)*2, (cir_diameter)*2, 20+(cir_diameter/2)+int(transition[0])*(cir_diameter)*2)
                self.canvas.create_text(90-longTransitionsCount, ((20+cir_diameter+int(transition[1])*(cir_diameter)*2)+(20+cir_diameter+int(transition[0])*(cir_diameter)*2))/2, text = transition[2])
                #this variable is incremented every time a long transition is drawn to ensure that multiple transitions are not drawn over each other 
                longTransitionsCount+=15

    def showFSA(self):
        self.root.wm_title("FSA")
        self.canvas.create_line(115, 15, 130, 30, arrow = tk.LAST)
        self.drawTransitions()
        self.drawCircles()
       
        self.canvas.pack()
        self.root.mainloop()
