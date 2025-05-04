# DeliveryDrone
Software written for drone delivery network. 
Credits: Malcolm Gilmore, Juston Armstrong


This is open source software written for drones operating on raspberry pi + pixhawk flight controllers. The network is fully autonomous and uses a VPN tunnel to establish a secure connection between the drones and the desired webserver. 
The system uses a hub and spoke model topology to achieve dynamic endpoint allocation, so that both the drones and users will maintain a stable connection to one another regardless of the geographic location. 

For now the current software we've written is only compatible with a pixhawk flight controller. The preferred RTOS (Real Time Operating System) for the flight controller is ChibiOS, and the raspberry Pi is using native PiOS. 
The hardware and software support will be expanded on over time. 















Instructions on adding a device to the  internal drone virtual private network (ID-VPN) for Windows devices: 


Part One: 



![Screenshot 2024-10-31 171423](https://github.com/user-attachments/assets/78969d80-d1bd-4fc5-beb2-f8cad7befaf0)



Part Two: 

Run the add_to_drone_network.ps1 script included in the files. 


Part Three: 

Contact Github owners to add your IP and public key to the wireguard conf file to become a user.
