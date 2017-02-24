
                          picademy Workshop Motion Sensing Live Camera Stream - Scott Morgan 2017

  What is it?
  -----------


  This is a project completed during picademy, which uses a PIR sensor to detect motion and start and stop a http stream via a picamera. 


  What will you need?
  -------------


  - Essential hardware:

    - Raspberry Pi + peripherals (tested on model 3B)
    - Picamera

  - Optional hardware:

    - PIR sensor
    - Jumper cables

  - Essential software:

    - VLC player running on both the RPi and the client device
    - tmux

  - The file motionsense.pdf shows the wiring required to connect the PIR sensor. 

  
  Installation
  ------------


  - Before you start:

     - Ensure that your Raspberry Pi is loaded with the latest version of Raspbian from [here](https://www.raspberrypi.org/downloads/).
     - Ensure that your Picamera is connected and working using instructions [here](https://www.raspberrypi.org/learning/getting-started-with-picamera/).     
     - Follow the documentation in motionsense.pdf to connect the PIR sensor to you Pi. 

  - In a terminal on the Pi:

    ```sudo apt-get update```


    ```sudo apt-get install tmux vlc git```


    ```git clone git@github.com:Scott3142/picademy-project.git```  


  - On the client device:

    - Install vlc - instructions available [here](https://vlc-media-player.en.softonic.com/).
    

  Running the script
  ------------

  - You can start and stop the stream without the motion detection by running:    

    ```cd picademy-project```

    ```./startstream```
    

  - To activate the motion detection, run

    ```cd picademy-project```


    ```python3 motionsense.py```


  Viewing the stream
  ------------

  - On the Pi:

    1. Open VLC
    2. Go to Media -> Open Network Stream
    3. Enter http://localhost:12345 and press Play

  - On a client device:

      1. On the Pi:

        1. Find your local network IP address by running 
           ```
           ifconfig
           ```
           in a terminal. (More instructions available [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/finding-your-pis-ip-address).)

      2. On the client device:

          1. Make sure your device is attached to the same network as the Pi
          2. Open VLC
          3. Open Network/MRL Stream (procedure may differ depending on the device) 
          4. Enter http://\*\*\*.\*\*\*.\*.\*\*:12345 (where \*\*\*.\*\*\*.\*.\*\* is the ip address of your pi)

  Contacts
  --------

  Any questions or comments about this code can be directed to @ScottM3142


  Acknowledgements
  --------

  Adapted from a tutorial [here](http://www.raspberry-projects.com/pi/pi-hardware/raspberry-pi-camera/streaming-video-using-vlc-player).

