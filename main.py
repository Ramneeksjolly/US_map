import turtle
import pandas
data=pandas.read_csv(r"csv projects\us_states.csv")
screen=turtle.Screen()
screen.title("states guessing game")
image="csv projects\map.gif"
turtle.addshape(image)
turtle.shape(image)

state=data["state"].to_list()


guessed=[]
score=0

while score < 50: 
    answer=turtle.textinput(title=f"{score}/50",prompt="whats the name of another state ").title()
    if (answer=="Exit"):
    #     not_guessed=[]
    #     for names in state:
    #         if names not in guessed:
    #             not_guessed.append(names)
    #   break
        not_guessed=[names for names in state if names not in guessed]
        break
    if answer in state:
        guessed.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)
        score+=1


print(not_guessed)
data_states=pandas.DataFrame(not_guessed)
data_states.to_csv("manleen.csv")

            
            


    
      
        
        
        

screen.exitonclick()