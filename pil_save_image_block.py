from PIL import ImageFile

from nio.block.base import Block
from nio.properties import FileProperty, VersionProperty


# ignore padding and EOF errors from certain formats
ImageFile.LOAD_TRUNCATED_IMAGES = True

class PILSaveImage(Block):

    """ Save a PIL image object to disk in the specified format """

    version = VersionProperty("0.1.0")
    file = FileProperty(title='Image File', default='my_image.jpg')

    def process_signals(self, signals):
        for signal in signals:
            signal.image.save(self.file(signal).value)
        self.notify_signals(signals)
