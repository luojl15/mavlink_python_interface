from pymavlink import  mavutil

master = mavutil.mavlink_connection('127.0.0.1:14550')
master.wait_heartbeat()

print("heartbeat from system (system %u componet %u)" %(
            master.target_system,master.target_system))

while True:
    try:
        msg = master.recv_msg()
        #print(msg._type)
        if msg:
            if msg._type =='ATTITUDE':
                print("pitch: ",msg.pitch)
                print("roll: ",msg.roll)
                print("raw: ",msg.yaw)
                print("----")
            elif msg._type =='HEARTBEAT':
                print("heartbeat from system (system %u componet %u)" %(master.target_system,master.target_system))
    except KeyboardInterrupt:
        print('Key boardInterrupt!exit')
        break
      


