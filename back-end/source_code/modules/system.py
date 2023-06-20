class SystemChecker:
    def __init__(self):
        import platform
        self.system = platform.system()
    def returnMagickCommand(self):
        if self.system == 'Linux':
            magick_command = "./magick.appimage"
        elif self.system == 'Windows':
            magick_command = "magick"
        return magick_command
''' 
class FileDirectory:
    def __init__(self, file_path):
'''     
