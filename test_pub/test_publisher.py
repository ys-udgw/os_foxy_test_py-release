import rclpy
import random
from rclpy.node import Node

from std_msgs.msg import String


class Test_Publisher(Node):

    def __init__(self):
        super().__init__('test_publisher')
        self.pub = self.create_publisher(String, 'test_topic', 10)
        time_p = 1.0

        self.timer = self.create_timer(time_p, self.callback)
        self.data = random.randint(1,100)


    def callback(self):
        msg = String()
        msg.data = 'Test Data: %d' % self.data 
        self.pub.publish(msg)
        self.get_logger().info('Test Publisher send: "%s"' % msg.data)
        self.data = random.randint(1,100)
         


def main(args=None):
    rclpy.init(args=args)

    test_pub = Test_Publisher()

    rclpy.spin(test_pub)

    test_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
