import turtle

num_pts = 40 #number sides to your drawing!
for i in range(num_pts):
   turtle.left(360/num_pts)
   turtle.forward(100)
   
turtle.mainloop()
