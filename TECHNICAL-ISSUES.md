# Technical Issues

PyBricks
- [EV3 Color Sensor Mode Switch Latency](https://github.com/pybricks/support/issues/14)
- [Delay between different Infrared Sensor modes](https://github.com/pybricks/support/issues/62)
- [OSError when using MultiProcessing in PyBricks](https://github.com/pybricks/support/issues/80)
- [NXT viability](https://github.com/pybricks/support/issues/169)

EV3Dev
- [LEGO EV3 UART sensors return stale values after mode switch](https://github.com/ev3dev/ev3dev/issues/1401)
- [`ValueError: invalid literal for int() with base 10: ''` when using InfraredSensor in Threading](https://github.com/ev3dev/ev3dev-lang-python/issues/746)
  - similar: [GyroSensor angle for GYRO-ANG sometimes returns empty string instead of integer](https://github.com/ev3dev/ev3dev/issues/1269)
  - related: [Device objects not thread safe](https://github.com/ev3dev/ev3dev-lang-python/issues/704)
  - possibly related: [sensors stop working](https://github.com/ev3dev/ev3dev/issues/1083)
- [Threading error when 2 Threads may control the same Motor. Errors encountered in EV3Dev2 with different error messages on MicroPython vs Python3. No such errors encountered in EV3Dev(1) and PyBricks.](https://github.com/ev3dev/ev3dev-lang-python/issues/750)
  - related: [OSError exception [Errno 4] EINTR when running motors in EV3](https://github.com/ev3dev/ev3dev-lang-python/issues/727)
    - related: [MicroPython: implement PEP 475](https://github.com/micropython/micropython/pull/5723)

MicroPython
- [Multiple-Inheritance Issues](https://github.com/micropython/micropython/search?q=%22multiple+inheritance%22&state=open&type=Issues)
  - [Differences vs. CPython](https://docs.micropython.org/en/latest/genrst/core_language.html#classes)

Other
- Broken EV3 Motors:
  - [Lego EV3 Motor Issue](https://www.youtube.com/watch?v=bsA2N7a34cY)

  - Mr. Hino:
    - [Solving the Broken LEGO Mindstorms EV3 Motor Issue](https://www.youtube.com/watch?v=vU3SU9yoXnA)
    - [The Continued Mystery of the Broken Motor Port](https://www.youtube.com/watch?v=jwBy7mDSYEo)
      - Elias Malak: Thank you for the video Mr. Hino. This cleared a lot of things up. If you change the brick, the same problem will occur. If you change the motor that was slow, the same problem will occur. If you switch the ports between b and c, the problem will still occur. However, if you change the motor that is fast, the problem will be fixed. What's happening is that your motor that is going fast has a broken encoder which is why in port view, it does not read anything. When the makers of the ev3 programming programmed the software, they made it so that the brick keeps adding power to the motor that does not show any rotations or degrees so that it can try to "move", because in the brick, it thinks the motor isn't moving at all since the encoder(tracker) is broken, therefore if you change the motor that is going fast, your problem will be resolved. Let me know if this fixes your problem? Thanks, Eli.
  
  - SOLUTION: use the Device Browser in EV3Dev to manually set the mode/status of the motor from "No Motor" to "Tacho Motor"


## Resolved

EV3Dev
- [Difference between stopping the program with EV3 Brick's physical Back/Stop button vs. stopping by VSCode stop button](https://github.com/ev3dev/vscode-ev3dev-browser/issues/103)
  - related: [Sometimes not all child processes are ended by `conrun-kill`](https://github.com/ev3dev/ev3dev/issues/1422)
