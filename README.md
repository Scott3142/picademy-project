
                          picademy Workshop Motion Sensing Live Camera Stream - Scott Morgan 2017

  What is it?
  -----------

  This is a project completed during picademy, which uses a PIR sensor to detect motion and start and stop a http stream via a picamera. 

  What will you need?
  -------------

  Essential hardware:
    Raspberry Pi + peripherals (tested on model 3B)
    Picamera
    PIR sensor
    Jumper cables

  Essential software:
    VLC player running on both the RPi and the client device
    tmux

  The file motionsense.pdf shows the wiring required to connect the PIR sensor. 
  
  Installation
  ------------

  Before you start:
    Ensure that your Raspberry Pi is loaded with the latest version of Raspbian from https://www.raspberrypi.org/downloads/
    Ensure that your Picamera is connected and working using instructions from https://www.raspberrypi.org/learning/getting-started-with-picamera/
    Follow the documentation in motionsense.pdf to connect the PIR sensor to you Pi. 

  On the Pi:
    
    ```
    #update
    sudo apt-get update

    #install tmux and vlc
    sudo apt-get install tmux vlc
    ```
  
  On the client device:
    Install vlc - instructions available at https://vlc-media-player.en.softonic.com/
    

  Viewing the stream
  ------------

  On the Pi:
    Open VLC
    Go to Media -> Open Network Stream
    Enter http://localhost:12345 and press Play

  On a client device:
    On the Pi:
    Find your local network IP address by running 
      ```
      ifconfig
      ```
    in a Terminal. (More instructions available at https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/finding-your-pis-ip-address)

    On the client device:
    Make sure your device is attached to the same network as the Pi
    Open VLC
    Open Network/MRL Stream (procedure may differ depending on the device) 
    Enter http://***.***.*.**:12345 (where ***.***.*.** is the ip address of your pi)

  Contacts
  --------

  Any questions or comments about this code can be directed to @ScottM3142
