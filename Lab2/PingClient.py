#coding: utf-8
from socket import *
import sys
import time
import random
import numpy

#Define connection (socket) parameters
#Address + Port no
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(0.6)
sseq = random.randint(10000, 20000)
rtts = []

starttime = int(time.time()*1000)
for i in range(15):
    message = 'PING'
    seq = str(sseq + i)
    message += ('-' + seq)
    sendtime = time.time()
    message += ('-' + str(sendtime))
    # print(message)
    try:
        clientSocket.sendto(message.encode('utf-8'),(serverName, serverPort))
        reply, serverAddress = clientSocket.recvfrom(1024)
        recvtime = time.time()
        rtt = recvtime - sendtime
        print('PING to ' + serverName + ', seq=' + seq + ', rtt=' + str(int(rtt*1000)) + ' ms')
        rtts.append(int(rtt*1000))
        # print(reply.decode('utf-8'))

    except:  
        print('PING to ' + serverName + ', seq=' + seq + ', rtt=timeout')

    # time.sleep(0.1)

clientSocket.close()
# Close the socket
stoptime = int(time.time()*1000)
nprtts = numpy.array(rtts)
rtt_diff = numpy.diff(nprtts)
jitter = sum(abs(rtt_diff))/len(rtt_diff)


# print(rtts)
print('')
print('Total packets sent: 15')
print('Packets acknowledged: ' + str(len(rtts)))
print('Packet loss: ' + f"{((15 - len(rtts))/15):.0%}")


print('Minimum RTT: ' + str(min(rtts)) + ' ms, Maximum RTT: ' + str(max(rtts)) + ' ms, Average RTT: ' + str(int(sum(rtts)/len(rtts))) + ' ms')
print('Total transmission time: ' + str(stoptime - starttime) + ' ms')

print('Jitter: ' + str(int(jitter)) + ' ms')



