__author__ = 'chris'
#import sip  # these lines are necessary because of a Traits dependancy on use of V2 of these APIs.
#sip.setapi('QString', 2)
#sip.setapi('QVariant', 2)
from PyQt6 import QtGui, QtWidgets
from .main import *
from . import cleaning
from .utils import *
import sys


qapp = QtWidgets.QApplication.instance()
if qapp is None:
    qapp = QtWidgets.QApplication(sys.argv)