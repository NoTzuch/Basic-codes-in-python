-------outro codigo------------
# pag -> Number of pages
# stotal -> total time

pag=int(input("How much pages you wanna print?:"))
stotal=(pag//5)*60
hours=stotal//3600
rest=stotal%3600
minutes=rest//60
seconds=rest%60
print("It's going to take",hours,"hours, ",minutes,"minutes and ",seconds,"seconds of your precious time")



