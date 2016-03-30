# Install
    sudo apt-get install mplayer2 festival python3 amixer
    git clone --recursive https://github.com/terokorp/raspberrypi-nfc-mp3.git
    cd raspberrypi-nfc-mp3
    ./nfc-mp3.py

# Troubleshooting

## If no sound
try following commands:

    amixer cset numid=3 0 # output auto
    amixer cset numid=3 1 # output jack
    amixer cset numid=3 2 # output hdmi

    amixer cset numid=1 400 # Full volume
    amixer cset numid=1 0 # Loud
    
## If no /dev/i2c-1
insert following lines to /etc/modules and restart

    bcm2708-rng
    i2c-bcm2708
    i2c-dev

