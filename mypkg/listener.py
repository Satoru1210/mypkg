import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def main():
    rclpy.init()
    node = Node("listener")

    def cb(msg):
        node.get_logger().info(f"listen: {msg.data}")

    # "zodiac_topic" というトピック名で購読
    node.create_subscription(String, "zodiac_topic", cb, 10)

    rclpy.spin(node)

if __name__ == "__main__":
    main()

