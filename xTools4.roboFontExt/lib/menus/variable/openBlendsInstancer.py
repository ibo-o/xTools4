# menuTitle: BlendsInstancer

from importlib import reload
import xTools4.dialogs.variable.BlendsInstancer
reload(xTools4.dialogs.variable.BlendsInstancer)

from mojo.roboFont import OpenWindow
from xTools4.dialogs.variable.BlendsInstancer import BlendsInstancerController

OpenWindow(BlendsInstancerController)
