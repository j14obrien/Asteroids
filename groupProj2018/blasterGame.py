
__author__ = 'Adam Skiffington & Jon Obrien'

import graphics
import time
import random

class rect:
    def __init__ (self, pict):
        self.pict = pict
        pass

    def right(self):
        return self.pict.getAnchor().getX() + self.pict.getWidth()/2
    def left(self):
        return self.pict.getAnchor().getX() - self.pict.getWidth()/2
    def top(self):
        return self.pict.getAnchor().getY() - self.pict.getHeight()/2
    def bottom(self):
        return self.pict.getAnchor().getY() + self.pict.getHeight()/2

def overlap(r1,r2):
    hoverlaps = True
    voverlaps = True
    if (r1.left() > r2.right()) or (r1.right() < r2.left()):
        hoverlaps = False
    if (r1.top() > r2.bottom()) or (r1.bottom() < r2.top()):
        voverlaps = False
    return hoverlaps and voverlaps

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

def test_image1():
    testImage1 = graphics.Image(graphics.Point(100,100),'goodGuy.gif')
    return testImage1

def test_image2():
    testImage2 = graphics.Image(graphics.Point(100,100),'bullet.gif')
    return testImage2

def testing_overlap():
    testImage1 = test_image1()
    testImage2 = test_image2()
    # overlap(testImage1,testImage2)

def main():
    win = graphics.GraphWin("BlasterGame",500,500)
    goodGuy = create_good_guy(win)
    asteroids = create_bad_guys(win)

    event_loop(win, asteroids, goodGuy)


def create_good_guy(win):
    goodGuy = graphics.Image(graphics.Point(250,400),"goodGuy.gif")
    goodGuy.draw(win)
    return goodGuy

def create_bad_guys(win):

    roidList = []
    x = 0
    face = graphics.Image(graphics.Point(0,75),"asteroid.gif")

    for index in range(5):
        faceCopy = face.clone()
        faceCopy.move(x,0)
        x = x + 100
        roidList.append(faceCopy)
    for index in roidList:
        index.draw(win)

    return roidList

def scoring(whatTodraw,win):
    whatTodraw.draw(win)

def event_loop(win, asteroids, goodGuy):
    var1 = True
    var2 = True
    var3 = True
    var4 = True
    var5 = True
    scoreList = [1,1,1,1,1]
    score = 0
    scoreText = graphics.Text(graphics.Point(50,25),('Score:',score))
    scoreText.draw(win)
    winText = graphics.Text(graphics.Point(250,250),'Congrats, you won! \n Press "Q" to quit')
    movement = 1
    x=0
    currentTime = 0
    adder = 1
    counter = 0

    projectileGoodguyList = []
    hitboxAsteroidList = []

    while True:

        currentTime = currentTime + adder
        time.sleep(0.0005)
        if currentTime == 150:
            counter = counter + 1
            currentTime = 0
        if counter > 3:
            counter = 0
            asteroidsXCoordsList = []
            for a in asteroids:
                asteroidsXCoordsList.append(a.getAnchor().x)

            #randomEnemyX = random.choice(asteroidsXCoordsList)
            #projectileEnemy = graphics.Image(graphics.Point(randomEnemyX,),'bomb.gif')
            #projectileEnemy.draw(win)
            #projectileEnemyList.append(projectileEnemy)

        #print(counter)



        for index in asteroids:
            index.move(movement,0.2)
            time.sleep(0.001)
        if asteroids[0].getAnchor().x < 0:
            movement = +1
        if asteroids[4].getAnchor().x > 500:
            movement = -1

        keyPressed = win.checkKey()
        goodGuy.move(x,0)

        if goodGuy.getAnchor().x < 15:
            x=1
        if goodGuy.getAnchor().x > 485:
            x=-1

        if keyPressed == 'a':
            x=-1
        if keyPressed == 'd':
            x=1
        if keyPressed == 'q':
            win.close()
            return False
        if keyPressed == 'space':
            projectile = graphics.Image(graphics.Point(goodGuy.getAnchor().x,400),"bullet.gif")
            projectileGoodguyList.append(projectile)
            projectile.draw(win)

        #if keyPressed == 'Shift_L':
            #asteroidsXCoordsList = []
            #for a in asteroids:
            #    asteroidsXCoordsList.append(a.getAnchor().x)

            #randomEnemyX = random.choice(asteroidsXCoordsList)
            #projectileEnemy = graphics.Image(graphics.Point(randomEnemyX,50),'bomb.gif')
            #projectileEnemy.draw(win)
            #projectileEnemyList.append(projectileEnemy)


        # HITBOX RELATED CODE BELOW:

        hitboxGoodguy = rect(goodGuy)

        for value in asteroids:
            hitboxAsteroid = rect(value)
            hitboxAsteroidList.append(hitboxAsteroid)

            if overlap(hitboxGoodguy,hitboxAsteroid):
                for index in range(5):
                    asteroids[index].undraw()
                    goodGuy.undraw()
                losingText = graphics.Text(graphics.Point(250,100),'You lost! Press "Q" to quit.')
                losingText.draw(win)

                adder = 0
                score = 1


        for value in projectileGoodguyList:
            hitboxProjectileGoodguy = rect(value)
            for index in range(5):
                if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[index]):
                    scoreList[index] = 0
                    asteroids[index].undraw()
                    value.undraw()

                    # scoring(scoreText,win)

            value.move(0,-0.9)

        # SCORE CODE BELOW:

        if var1 == True:
            if scoreList[0] == 0:
                score = score + 5
                var1 = False
        if var2 == True:
            if scoreList[1] == 0:
                score = score + 5
                var2 = False
        if var3 == True:
            if scoreList[2] == 0:
                score = score + 5
                var3 = False
        if var4 == True:
            if scoreList[3] == 0:
                score = score + 5
                var4 = False
        if var5 == True:
            if scoreList[4] == 0:
                score = score + 5
                var5 = False

        scoreText.undraw()
        scoreText = graphics.Text(graphics.Point(50,25),('Score:',score))
        if score != (1 or 25):
            scoreText.draw(win)


        if score == 25:
            for index in asteroids:
                index.undraw()
            goodGuy.undraw()
            for index in projectileGoodguyList:
                index.undraw()
            winText.draw(win)
            adder = 0
            score = 1

        # scoreText.undraw()
        # scoreText.draw(win)
        # print(score)

        # if counter > number:
        #     score = score + 5

            # if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[1]):
            #     asteroids[1].undraw()
            #     # counter = counter + 1
            # if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[2]):
            #     asteroids[2].undraw()
            #     # counter = counter + 1
            # if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[3]):
            #     asteroids[3].undraw()
            #     # counter = counter + 1
            # if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[4]):
            #     asteroids[4].undraw()
            #     counter = counter + 1

            # print('end')
        # if counter > 0:
        #
        #     counter = counter + 5
        #     print(counter)
        #     counter = 0
            # score = True



        # for index in range(5):
        #     if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[index]):
        #         counter = counter + 1
        #         print(counter)

        # if keyPressed == 'space':
        #     print('pressed space')
        #     for index in range(5):
        #         if overlap(hitboxProjectileGoodguy,hitboxAsteroidList[index]):
        #             print('overlapping')

        # print(counter)
        # if countedKilled == 5:
        #     for index in range(5):
        #         goodGuy.undraw()
        #         asteroids[index].undraw()






        # if score == 25:
        #     for index in asteroids:
        #         index.undraw()
        #     goodGuy.undraw()
        #     for index in projectileEnemyList:
        #         index.undraw()
        #     for index in projectileGoodguyList:
        #         index.undraw()



        # if score == 25:
        #     print('dun')
        # print(asteroids)




main()