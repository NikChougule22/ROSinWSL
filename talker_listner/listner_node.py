import rclpy
from rclpy.node import Node  #this is needed becuase any node that you create as class needs to inherit from node from rclpy library
from std_msgs.msg import String #this is needed to select the data type for publisher when it publishes data which is of string type


class ListnerNode(Node):
    def __init__(self):
        super().__init__("listner_node")
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listner_callback,
            10
        )
    def listner_callback(self,msg):
        self.get_logger().info(f"Received {msg.data}")

def main(args=None):
    rclpy.init(args=args)  #anyytime you want to create node you need to initialize the node through rclpy.init
    
    #create node
    listnerNode = ListnerNode()
    
    #use node
    rclpy.spin(listnerNode)
    
    #destroy node
    listnerNode.destroy_node() 
    rclpy.shutdown()
    

if __name__== "__main__":
    main()