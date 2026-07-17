class PreviewManager:

    def __init__(self):
        self.preview = None


    def start(self, preview):
        self.preview = preview


    def update(self, settings):

        if self.preview:
            self.preview.update_area(settings)


    def stop(self):
        self.preview = None



_preview_manager = PreviewManager()


def get_preview_manager():
    return _preview_manager