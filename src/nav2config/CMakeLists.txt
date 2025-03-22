cmake_minimum_required(VERSION 3.5)
project(nav2config)


find_package(ament_cmake REQUIRED)


install(DIRECTORY launch/
    DESTINATION share/${PROJECT_NAME}/launch)

install(DIRECTORY maps/
    DESTINATION share/${PROJECT_NAME}/maps)

install(DIRECTORY config/
    DESTINATION share/${PROJECT_NAME}/config)

install(
  PROGRAMS
    scripts/serial_node.py
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
