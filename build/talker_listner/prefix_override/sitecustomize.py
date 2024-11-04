import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nchougul/ros2_ws/src/talker_listner/install/talker_listner'
