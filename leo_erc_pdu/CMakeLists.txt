cmake_minimum_required(VERSION 3.0.2)
project(leo_erc_pdu)

find_package(catkin REQUIRED)

catkin_package()

install(
  DIRECTORY
    config
    launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS
  scripts/pdu_driver
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
