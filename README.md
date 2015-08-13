PILNewImage
===========

Create a new PIL Image and store it in the *image* attribute of the input signal.

Properties
----------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

Commands
--------
None

Input
-----
Any list of signals.

Output
------
Same list of signals as input, with the added *image* attribute.

------------------------------------------------------------------------------

PILDrawText
===========

Draw text to an existing PIL Image

Properties
----------
-   cooridinate (x, y) (exp): x, y cooridinate to start text
-   text (exp): text to draw to image

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

Commands
--------
None

Input
-----
Any list of signals.

Output
------
Same list of signals as input.

------------------------------------------------------------------------------

PILOpenFile
===========

Load and image file from disk and create a new PIL Image and store it in the *image* attribute of the input signal.

Properties
----------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

Commands
--------
None

Input
-----
Any list of signals.

Output
------
Same list of signals as input, with the added *image* attribute.
