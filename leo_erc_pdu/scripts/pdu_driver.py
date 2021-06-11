#!/usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerResponse
from std_msgs.msg import Empty, UInt8
from dynamixel_workbench_msgs.srv import DynamixelCommand 

def pdu_reset(req):
    global probe_cnt 

    dynamixel_client(
        id=0,
        addr_name='Goal_Position',
        value=0
    )
    probe_cnt=0

    return TriggerResponse(True, "")


def pdu_callback(msg):
    global probe_cnt

    if (probe_cnt >= probe_number):
        return

    probe_cnt += 1

    dynamixel_client(
        id=0,
        addr_name='Goal_Position',
        value=probe_cnt*204
    )

    # if log.success:
    #     rospy.loginfo(log.status_message)
    # else:
    #     rospy.logerr(log.status_message)

    pdu_dropped_pub.publish(probe_cnt)


rospy.init_node("pdu_node")

probe_number = 5
probe_cnt = 0

pdu_dropped_pub = rospy.Publisher(
    "probe_deployment_unit/probes_dropped",
    UInt8, queue_size=1, latch=True)

pdu_dropped_pub.publish(probe_cnt)

dynamixel_client = rospy.ServiceProxy('dynamixel_driver/dynamixel_command', DynamixelCommand )

pdu_reset_srv = rospy.Service("probe_deployment_unit/home", Trigger, pdu_reset)

pdu_drop_sub = rospy.Subscriber(
    "probe_deployment_unit/drop",
    Empty,
    pdu_callback)

# pdu_reset(Trigger)
rospy.spin()