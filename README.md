PILDrawText
===========
Draw text to an existing PIL Image

Properties
----------
- **coordinate**: x, y cooridinate to start text
- **text**: text to draw to image

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input.

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)


PILNewImage
===========
Create a new PIL Image and store it in the *image* attribute of the input signal.

Properties
----------
- **size**: x,y size of new image

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input, with the added *image* attribute.

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)

Input
-----
Any list of signals.

Output
------
Same list of signals as input, with the added *image* attribute.

PILOpenFile
===========
Load and image file from disk and create a new PIL Image and store it in the *image* attribute of the input signal.

Properties
----------
- **file**: Location of image file to open

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input, with the added *image* attribute.

Commands
--------
None

Dependencies
------------
-   [**Pillow**](https://pypi.python.org/pypi/Pillow)
