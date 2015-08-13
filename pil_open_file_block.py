from os.path import join, dirname, realpath, isfile
from PIL import Image
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty
from nio.metadata.properties import VersionProperty
from nio.util.environment import NIOEnvironment


@Discoverable(DiscoverableType.block)
class PILOpenFile(Block):

    """ Use PIL to open a file and store the Image in a signal """

    version = VersionProperty('0.1.0')
    file = ExpressionProperty(title='Image File', default='niologo.png')

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            image = self._load_image_file(signal)
            if True:
                # TODO: resize image if configured to do so
                image = image.resize(
                        (64, 48),
                        Image.ANTIALIAS)
            signal.image = image
        self.notify_signals(signals, output_id='default')

    def _load_image_file(self, signal):
        """ Loads an image file from disk """

        # Let's figure out where the file is
        try:
            fileprop = self.file(signal)
        except:
            self._logger.exception('Failed to get file name info from signal')
            return None
        filename = self._get_valid_file(
            # First, just see if it's maybe already a file?
            fileprop,
            # Next, try in the NIO environment
            NIOEnvironment.get_path(fileprop),
            # Finally, try relative to the current file
            join(dirname(realpath(__file__)), fileprop),
        )
        if filename is None:
            self._logger.error(
                'Could not find image file {0}. Should be an absolute path or'
                ' relative to the current environment.'.format(
                    fileprop))
            return None
        image = Image.open(filename).convert('1')
        return image

    def _get_valid_file(self, *args):
        """ Go through args and return the first valid file, None if none are.
        """
        for arg in args:
            if isfile(arg):
                return arg
        return None
