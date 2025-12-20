# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.10.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xc6\
Q\
PushButton {\x0d\x0a  \
  font-size: 14p\
x;\x0d\x0a    padding:\
 10px;\x0d\x0a    text\
-transform: uppe\
rcase;\x0d\x0a    bord\
er-radius: 10px;\
\x0d\x0a    background\
-color: #f0f0f0;\
\x0d\x0a}\x0d\x0a\x0d\x0aQPushButt\
on:hover {\x0d\x0a    \
background-color\
: steelblue;\x0d\x0a  \
  border-color: \
darkblue;\x0d\x0a    c\
olor: white;\x0d\x0a}\x0d\
\x0a\x0d\x0aQPushButton#p\
sb_exit {\x0d\x0a    p\
adding: 5px;\x0d\x0a}\x0d\
\x0a\x0d\x0aQLabel#lbl_ap\
p_title {\x0d\x0a    f\
ont-size: 22px;\x0d\
\x0a    font-weight\
: bold;\x0d\x0a    col\
or: blue;\x0d\x0a    t\
ext-transform: u\
ppercase;\x0d\x0a    t\
ext-align: cente\
r;\x0d\x0a}\
\x00\x00\x00\xa6\
Q\
MainWindow {\x0d\x0a  \
  background-col\
or: qlineargradi\
ent(spread:pad, \
x1:0, y1:0, x2:1\
, y2:1, stop:0 r\
gba(188, 81, 255\
, 247), stop:0.9\
59596 rgba(140, \
255, 255, 255));\
\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x06\
\x07\xac\x02\xc3\
\x00s\
\x00t\x00y\x00l\x00e\x00s\
\x00\x13\
\x02\x93\x96\xa3\
\x00m\
\x00a\x00i\x00n\x00_\x00m\x00e\x00n\x00u\x00_\x00s\x00t\x00y\x00l\x00e\x00.\x00q\
\x00s\x00s\
\x00\x15\
\x0b\xe6`\xe3\
\x00m\
\x00a\x00i\x00n\x00_\x00w\x00i\x00n\x00d\x00o\x00w\x00_\x00s\x00t\x00y\x00l\x00e\
\x00.\x00q\x00s\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x9b9\xe8\xf0\xf0\
\x00\x00\x00>\x00\x00\x00\x00\x00\x01\x00\x00\x01\xca\
\x00\x00\x01\x9b9\xe8\xf0\xf0\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
