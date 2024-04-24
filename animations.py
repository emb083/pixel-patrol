class Animation:

    def __init__(self, target:"Entity", name:str, keyframes:list, framerate:int, repeat:bool=False, trigger:"function"=None, trigger_data:list=None) -> None:
        self.running = False
        self.animationFrame = 0
        self.animationDelay = 0
        self.target = target
        self.keyframes = [f"{name}-{keyframe}.png" for keyframe in keyframes]
        self.framerate = framerate
        self.repeat = repeat
        self.trigger = trigger
        self.trigger_data = trigger_data

    def updateAnimation(self) -> bool:
        if self.animationFrame >= len(self.keyframes): # if animation over,
            self.animationFrame = 0 # reset to beginning
            if self.repeat is False: # if not repeating,
                return True # signal end
        # if not over,
        self.target.updateSprite(self.keyframes[self.animationFrame]) # update sprite
        self.animationFrame += 1 # tick to next frame
        if self.animationFrame < len(self.keyframes) and "trigger" in self.keyframes[self.animationFrame]: # if upcoming step is trigger,
            self.trigger(*self.trigger_data)
            self.animationFrame += 1 # tick to next actual frame
        return False # signal animation continue