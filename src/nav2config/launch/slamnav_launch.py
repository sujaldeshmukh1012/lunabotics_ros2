from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

	IncludeLaunchDescription(
	    PythonLaunchDescriptionSource(
	       PathJoinSubstitution([
	           FindPackageShare("sllidar_ros2"),
		   "launch",
		   "view_sllidar_a1_launch.py"
	       ])
	    )
	),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser']
	),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom']
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link']
        ),

        Node(
            package='ros2_laser_scan_matcher',
            executable='laser_scan_matcher',
            output='screen'
        ),
    ])
