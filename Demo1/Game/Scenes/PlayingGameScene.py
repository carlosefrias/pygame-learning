from Scenes.Scene import Scene
import pygame

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
    
    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()
        pad = game.getPad()
        
        balls = game.getBalls()
        for ball in balls:
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                ball.changeDirection(pad)

            ball.updatePosition()
        
            game.screen.blit(ball.getSprite(), ball.getPosition())
        
        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())
                    
        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(True)