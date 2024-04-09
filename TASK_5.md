
![circuit](https://github.com/m0h1t19/Awesome_Robotics_Club_-Mohit-Choudhary-_-230658-/assets/139625998/cdf60223-c834-49b0-b993-2dd6e35e0e45)


https://www.tinkercad.com/things/dtEDHORBxqc-fantastic-inari-wluff

I first created a boolean variable over to check if the game is over or not and then used the lcd.print command to print game over if the bird hits the obstacle.
I created both the 1st row and 2nd row obstacles as arrays. After initiating them as arrays , I print them using the same command mentioned above by changing the place of the cursor as requirement.
I used the analogread function to read the value of potentiometer and if it is more than 500 i set cursor to 1st row first block and if there is an obstacle there at that time that means the bird and obstacle has collided , hence, game over.
And this loop gets repeated again and again , reprinting the things , making them look as if they are mobing.
