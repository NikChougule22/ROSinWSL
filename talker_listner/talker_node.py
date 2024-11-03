import rclpy
from rclpy.node import Node  #this is needed becuase any node that you create as class needs to inherit from node from rclpy library
from std_msgs.msg import String #this is needed to select the data type for publisher when it publishes data which is of string type

class TalkerNode(Node):  #Class talker node created which inherits from Node in rclpy
    def __init__(self): #create constructor
        super().__init__("talker_node")   #initialize base class
        self.publisher_=self.create_publisher(String,'topic',10)  # create publisher node of sring type, string "topic" and que size 10
        timer_period=0.5 #frequency/timer speed declaration
        self.timer = self.create_timer(timer_period, self.timer_callback) #creating timer with a method inherted from node and calling a timer callback function
        self.count = 0 # creating counter which will be used in timer_callback function
        
    def timer_callback(self):  # Timer call back function that runs when self.timer runs and calls this function
        msg = String() # defining message type in function
        msg.data=f"Hello everyone {self.count}" # printing message and pritning count value
        self.publisher_.publish(msg)
        self.count +=1 #increasing counter everytime the fucntion is run
        self.get_logger().info(f"Publishing {msg.data}")  #display what we are pubishing on pubishing node terminal

  
def main(args=None):
    rclpy.init(args=args)  #anyytime you want to create node you need to initialize the node through rclpy.init
    
    #create node
    talkerNode = TalkerNode()
    
    #use node
    rclpy.spin(talkerNode)
    
    #destroy node
    talkerNode.destroy_node() 
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()