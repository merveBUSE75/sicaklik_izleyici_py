import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SicaklikSensoru(Node):
    def __init__(self):
        super().__init__('sicaklik_sensoru')

        self.publisher = self.create_publisher(
            Float32, '/sicaklik', 10
        )

        self.timer = self.create_timer(1.0, self.publish_temperature)

    def publish_temperature(self):
        msg = Float32()
        msg.data = float(random.randint(20, 40))

        self.publisher.publish(msg)
        self.get_logger().info(f'Sıcaklık: {msg.data:.1f} °C')


def main(args=None):
    rclpy.init(args=args)
    node = SicaklikSensoru()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()

