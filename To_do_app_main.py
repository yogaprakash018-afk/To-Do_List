from turtle import Turtle as T, Screen as S
from datetime import datetime # This will give string output as date and time

t = T()
s = S()

s.setup(500, 500)
s.title("To Do List App!")
no_of_inputs = s.numinput(title = "Type the number of Todos for today!", prompt="") # This will give float, so we are converting it to int in for loops.    

def remainder(todotime, todo):
    now = datetime.now()
    time = now.strftime("%H:%M")
    for k in range(len(todo)):
        if time == todotime[k]:
            t.teleport(x = 0, y = y[k])
            t.color("red")       # highlight reminder
            t.write(f"⏰ REMINDER: {todo[k]}", font=("Times New Roman", 12, "bold"))
    s.ontimer(lambda:remainder(todos_time, todos), 1000)

todos_time = [s.textinput(title = "Type your time to remind you of the TODOS in 24H format ex: 14:15", prompt = "") for _ in range(int(no_of_inputs))]
todos = [s.textinput(title = "Type your TODOS here", prompt = "") for _ in range(int(no_of_inputs))]

y = []

for pos in range(220, 220 - int((no_of_inputs * 30)), -30):  # ✅ correct!
    y.append(pos)
    if t.xcor() == -230:
        print("Enough space has consumed!, Please delete any TODOS.")

for i in range(len(todos)):
    t.teleport(x = -220, y = y[i])
    t.write(todos[i], font= ("Times New Roman", 12, "normal"))

remainder(todos_time, todos)
s.mainloop()