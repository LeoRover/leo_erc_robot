cmake_minimum_required(VERSION 3.0.2)
project(leo_erc_bringup)

find_package(catkin)

catkin_package()

install(
  DIRECTORY
    config
    launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS
  scripts/zed_odom
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
