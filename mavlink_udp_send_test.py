from pymavlink import mavutil
import time

current_time = int(time.time())

sender = mavutil.mavlink_connection('127.0.0.1:14550',input=False)


while True:
    sender.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_GCS,mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)
    
    sender.mav.attitude_send(current_time,1.2, 1.7, 3.10, 0.01, 0.02, 0.03)




