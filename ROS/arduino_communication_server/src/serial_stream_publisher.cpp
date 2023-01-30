#include <ros/ros.h>
#include <std_msgs/Int8.h>


int main(int argc, char **argv){
	
	ros::init(argc, argv, "serial_stream_publisher");
	ros::NodeHandle n;
	ros::Publisher publisher = n.advertise<std_msgs::Int8>("serial_stream",1);
	
	ros::Rate naptime(1.0);
	
	std_msgs::Int8 serial_one;
	std_msgs::Int8 serial_zero;
	
	serial_one.data = 1;
	serial_zero.data = 0;
	
	while (ros::ok())
	{		
		publisher.publish(serial_one);
		ROS_INFO("%d",serial_one.data);
		naptime.sleep();
		publisher.publish(serial_zero);
		ROS_INFO("%d",serial_zero.data);
		naptime.sleep();	
	}		
}
