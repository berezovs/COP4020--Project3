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
            self.drawCircle(120, 50+(circle*120), 180, 50+(circle*120)+60)
            if(circle in self.acceptStates):
                self.drawCircle(125, 55+(circle*120), 175, 55+(circle*120)+50)
            self.canvas.create_text(150, 50+(circle*120)+30, text=str(circle))


    def showFSA(self):
        self.root.wm_title("FSA")
        self.drawCircles()
        self.canvas.pack()
        self.root.mainloop()
