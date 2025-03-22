from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    nav2config_dir = FindPackageShare('nav2config')
    nav2_bringup_launch_file = PathJoinSubstitution(
	[FindPackageShare('nav2_bringup'), 'launch', 'bringup_launch.py']
    )

    map_yaml_file = LaunchConfiguration('map')
    params_file = LaunchConfiguration('params_file')
    use_sim_time = LaunchConfiguration('use_sim_time')


    declare_map_yaml_cmd = DeclareLaunchArgument(
	'map',
	default_value=PathJoinSubstitution([nav2config_dir, 'maps', 'my_map1.yaml']),
	description='Full path to the map yaml file',
    )

    declare_params_file_cmd = DeclareLaunchArgument(
	'params_file',
	default_value=PathJoinSubstitution([nav2config_dir, 'config', 'navigation.yaml']),
	description='Full path to the ROS2 parameters file for all nodes',
    )

    declare_use_sim_time_cmd = DeclareLaunchArgument(
	'use_sim_time', default_value='false', description='Use simulation clock'
    )

    
    nav2_bringup_launch = IncludeLaunchDescription(
	PythonLaunchDescriptionSource(nav2_bringup_launch_file),
	launch_arguments={
	    'map': map_yaml_file,
	    'params_file': params_file,
	    'use_sim_time': use_sim_time,
	}.items(),
    )


    return LaunchDescription(
	[
	    declare_map_yaml_cmd,
	    declare_params_file_cmd,
	    declare_use_sim_time_cmd,
            nav2_bringup_launch,
	]
    )
