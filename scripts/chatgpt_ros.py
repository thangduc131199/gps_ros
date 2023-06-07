import rospy
from std_msgs.msg import String
import  chatgpt

import os


class ChatGPTNode:
    def __init__(self):
        """
        constructer
        """
        rospy.init_node("chatgpt_node_ahiih")
        rospy.Subscriber("/input_text", String,self.listener_callback,queue_size=10)
        self.pub = rospy.Publisher("/output_text", String,queue_size = 10)
        self.chatgpt = chatgpt.ChatGPT("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")
        rospy.spin()

    def listener_callback(self, msg):
        """
        Subscribe callback function

        Parameters
        ----------
        msg : std_msgs.msg.String
            subscribe message
        """
        rospy.loginfo(f"Subscribed Text: {msg.data}")
        prompt = msg.data
        response = self.chatgpt.generate_text(prompt)
        rospy.loginfo(response)
        output_msg = String()
        if response != None:
            output_msg.data = response
            self.pub.publish(output_msg)


def main(args=None):
    """
    main function
    """
    node = ChatGPTNode()


if __name__ == "__main__":
    main()
