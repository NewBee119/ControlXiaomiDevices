import socket
import time

ip = "192.168.9.150"
port = 54321

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

openbull = '6045cba1f18b7811dc65b66b08004500008c6a100000ff11ef48c0a809961b6d7c5cd4311f750078a70f21310070000000000453f4385af6b006f719146b112f8302eda4ec50e411ad8e89a75eb0846288e2afa9474d5329aca7b1216f1708128f4291a3e1a77b9133fb1b04b85ee042f473e2367a8c124a0faf4f330b194cea0c3764671d1deef77bb865e4b154513c486fb3518cdead3ca633'.decode('hex')
openack = '6045cba1f18b7811dc65b66b08004500009c6a160000ff11ef32c0a809961b6d7c5cd4311f750088a5d221310080000000000453f4385af6b00db69bc191182bdc77e038994a2da6726989a75eb0846288e2afa9474d5329aca7d9e00b1b1c53a315197598fe9450b51a8b83cdd01be8929d10db625c58fff42c68bfa189d4100d05ecbdfd76ce2beb5d937376ffd044f7efeb301e8f777b6b0689d7f3e84665985e043f4a31c21d47b8'.decode('hex')
closebull = '6045cba1f18b7811dc65b66b08004500008c6a1d0000ff11ef3bc0a809961b6d7c5cd4311f750078392a21310070000000000453f4385af6b013897414502e2a662f9b9eb430de38f37889a75eb0846288e2afa9474d5329aca7d9e00b1b1c53a315197598fe9450b51ad4321c5d7c632be7003131784581a884cd5d4f50825761512be286d2565cb532beea7dfb54c3c81e629c82f4d429dffe'.decode('hex')
closeack = '6045cba1f18b88259319faec08004500005c000040003311e5891b6d7c5cc0a809961f75d43100487e2721310040000000000453f4385af6b028d3a6f163b51d4bd6d05142ce99c251d6bca002336145cf24a0a2f18c78eadac39d93c69b3873f41f247c5066a23bc4b7'.decode('hex')

opencmd =''
closecmd =''
openrev =''
closerev =''

for data1 in openbull:
    opencmd += chr(int('{:08b}'.format(ord(data1)),2))

for data2 in openbull:
    closecmd += chr(int('{:08b}'.format(ord(data2)),2))

for data3 in openack:
    openrev += chr(int('{:08b}'.format(ord(data3)),2))

for data4 in closeack:
    closerev += chr(int('{:08b}'.format(ord(data4)),2))

for i in range(1,5):
    sock.sendto(opencmd,(ip,port))  #open mi air
    time.sleep(1)
    sock.sendto(openrev,(ip,port)) 
    time.sleep(1)
    sock.sendto(closecmd,(ip,port))  #close mi air
    time.sleep(1)
    sock.sendto(closerev,(ip,port)) 
    time.sleep(1)
sock.close()
