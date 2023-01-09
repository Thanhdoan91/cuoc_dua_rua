import turtle 
import random


screen = turtle.Screen()
screen.setup(height=500, width = 600)
#form cho người dùng nhập vào dự đoán
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng", title ="Nhập vào màu con rùa(đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")

#list colors chứa màu của từng con rùa
colors = ["red", "brown", "blue", "green", "orange", "pink"]
turtle_speeds=[19,15,20,25,30,5] 

#Tọa độ x của các con rùa

x= -250

#tọa độ y của các con rùa
ys =[-60, -30, 0, 30, 60, 90]

#Biến lưu trữ bút vẽ cho từng con rùa
all_turtles= []
run = True

#vẽ vạch đích
but_ve_dich = turtle.Turtle()
but_ve_dich.penup()
but_ve_dich.goto(250,-150)
but_ve_dich.left(90)
but_ve_dich.pendown()
but_ve_dich.forward(300)
but_ve_dich.hideturtle()

#vẽ đường đua
but_ve_duong_dua = turtle.Turtle()
but_ve_duong_dua.speed(0)
but_ve_duong_dua.penup()
but_ve_duong_dua.goto(-250,160)
but_ve_duong_dua.right( 90)
but_ve_duong_dua.hideturtle()

for i in range(-250, 250, 25):
    for j in range(-120, 200, 40):
        but_ve_duong_dua.penup()
        but_ve_duong_dua.goto(i,j)
        but_ve_duong_dua.pendown()
        but_ve_duong_dua.forward(30)
        
#Vẽ trục số
but_ve_so = turtle.Turtle()
but_ve_so.speed(0)
but_ve_so.hideturtle()
for i in range(21):
    but_ve_so.penup()
    but_ve_so.goto(-250 +i*25,165)
    but_ve_so.write(i)
    
    but_ve_so.penup()
    but_ve_so.goto(-250 +i*25,-165)
    but_ve_so.write(i)
    
#khởi tạo các bút vẽ cho từng con rùa
for i in range(6):
    but_ve= turtle.Turtle()
    but_ve.shape("turtle")
    but_ve.color(colors[i])
    but_ve.penup()
    but_ve.goto(-250, ys[i])
    all_turtles.append(but_ve)

# mỗi con rùa sẽ chọn một tốc độ ngẫu nhiên trong list speed
def random_walk(all_turtles):
    global run 
    for t in all_turtles:
        t.forward(random.choice(turtle_speeds))
        #nếu có con rùa nào có tọa độ x>250 thì run = False
        #t.xcor() trả về tọa độ x của bút vẽ tại thời điểm được gọi
        if t.xcor() >= 250:
            run = False
#lặp lại các bước chạy cho tới khi run == False           
while run==True:
    random_walk(all_turtles)
    

#chương trình kết thúc khi click vào màn hình
screen.exitonclick()


turtle.done()
           