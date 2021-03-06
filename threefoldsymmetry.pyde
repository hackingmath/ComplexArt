from __future__ import division

'''Exploring how to transform the coordinates
in a grid and color them according to 
the pixels in an image
August 23, 2016
Python version June 4, 2017
June 9, 2017 added frieze'''

def setup():
    size(400,400);
    background(0)
    myphoto = loadImage("dahlia.jpg")
    img = createImage(400,400,RGB);
  
    #Create counter for img.pixels array
    counter = 0;
    #Create coefficients of complex number a + bi
    b =-2.0;
    a = -2.0;
    #when this line was "b < 1.99" it was screwing up!
    while b < 2.00:
        a = -2.0; #reset after every loop!
        while a < 2.00:
            #Create complex number as vector
            p = PVector(a,b);
            #executes the important function
            q = frieze(p)
        
            #convert range of values from -2 to 2 to 0 to 400
            x = int(map(q.x,-2,2,0,myphoto.width));
            iy = int(map(q.y,-2,2,0,myphoto.height));
        
            #get that color in "myphoto"
            c = myphoto.get(iy,x);
        
            #put that color in the new image
            img.pixels[counter] = c;
        
            #increment a and counter
            a += 4.0/img.width;
            counter += 1;

        #increment b
        b += 4.0/img.height;
    
    #draw image on screen
    image(img,0,0);

#June 9, 2017
def e(angle):
    '''defining the exponential notation'''
    return PVector(cos(angle),sin(angle))

def frieze(z):
    '''from Farris, p. 67'''
    #2pi*i*y
    term1 = TWO_PI*z.y
    #2pi*i(sqrt(3)*x-y)/2
    term2 = TWO_PI*(sqrt(3)*z.x - z.y)/2.0
    #2pi*i(-sqrt(3)*x-y)/2
    term3 = TWO_PI*(sqrt(3)*(-z.x) - z.y)/2.0
    #add together
    sum1 = e(term1)+ e(term2) + e(term3)
    #multiply by 1/3
    sum1.div(3.0)
    return sum1