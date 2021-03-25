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
        for which in range(0, len(transitions)):
            transition = transitions[which].split(':')

            if(int(transition[1])==(int(transition[0])+1)):
                self.canvas.create_line(150, 20+60+int(transition[0])*120, 150, 20+60+int(transition[0])*120+60, arrow = tk.LAST)
                self.canvas.create_text(160, 50+60+int(transition[0])*120, text = transition[2])

            elif(int(transition[1])==(int(transition[0])-1)):
                self.canvas.create_line(150, 20+60+int(transition[1])*120, 150, 20+60+int(transition[1])*120+60, arrow = tk.FIRST)
                self.canvas.create_text(160, 50+60+int(transition[1])*120, text = transition[2])

            elif(int(transition[1])<(int(transition[0])-1)):
                print(transition[0],":", transition[1])
                self.canvas.create_line(100, 20+30+int(transition[1])*120, 100, 20+30+int(transition[0])*120)
                self.canvas.create_line(100, 20+30+int(transition[1])*120, 120, 20+30+int(transition[1])*120, arrow=tk.LAST)
                self.canvas.create_line(100, 20+30+int(transition[0])*120, 120, 20+30+int(transition[0])*120)
                self.canvas.create_text(90, 50+60+int(transition[1])*120, text = transition[2])

            elif(int(transition[1])>(int(transition[0])+1)):
                self.canvas.create_line(100, 20+30+int(transition[1])*120, 100, 20+30+int(transition[0])*120)
                self.canvas.create_line(100, 20+30+int(transition[1])*120, 120, 20+30+int(transition[1])*120, arrow = tk.LAST)
                self.canvas.create_line(100, 20+30+int(transition[0])*120, 120, 20+30+int(transition[0])*120)
                self.canvas.create_text(90, 50+60+int(transition[0])*120, text = transition[2])

            elif(int(transition[1])==(int(transition[0]))):
                self.drawCircle(160, 30+int(transition[1])*120, 200, 30+int(transition[1])*120+40)
                self.canvas.create_line(170, 30+int(transition[1])*120, 171, 30+int(transition[1])*120, arrow = tk.FIRST)
                self.canvas.create_text(210, 20+30+int(transition[0])*120, text = transition[2])
           

       


    def showFSA(self):
        self.root.wm_title("FSA")
        self.canvas.create_line(115, 15, 130, 30, arrow = tk.LAST)
        self.drawTransitions()
        self.drawCircles()
       
        self.canvas.pack()
        self.root.mainloop()
