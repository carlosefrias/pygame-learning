from Scenes.Scene import Scene

class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)
    
    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)