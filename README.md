# Hand Gesture Based AC Light Dimmer

Control AC Light with Hand Gesture (Python - OpenCV - MediaPipe and Arduino)

### Youtube Video

[![IMAGE_ALT](https://img.youtube.com/vi/tuxtHrDm3WQ/0.jpg)](https://www.youtube.com/watch?v=tuxtHrDm3WQ)

### Installation

### Step 1
Upload Dimmer.ino to Arduino

### Step 2
Install Dependencies

pip3 install opencv-python\
pip3 install mediapipe\
pip3 install pyserial

### Step 3
Run and Enjoy

python3 dimmer.py

### Circuit Diagram

![CircuitDiagram](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/schematic.png)

### PCB Design

![PCBBack](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/pcb_back.jpg)
![PCBFront](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/pcb_front.jpg)
![PCBSolderedBack](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/pcb_soldered_back.jpg)
![PCBSolderedFront](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/pcb_soldered_front.jpg)

### Dimmer Module Schematic and PCB

![Schematic](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/ac_dimmer_schematic.png)
![PCB](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/ac_dimmer_pcb.png)

### 50 Hz Sine Wave and Zero Cross Detection Input

In alternating current, the zero-crossing is the instantaneous point at which there is no voltage present. In a sine wave or other simple waveform, this normally occurs twice during each cycle. It is a device for detecting the point where the voltage crosses zero in either direction.

The zero-crossing is important for systems that send digital data over AC circuits, such as modems, X10 home automation control systems, and Digital Command Control type systems for Lionel and other AC model trains.

https://en.wikipedia.org/wiki/Zero_crossing

Signal frequency > 50hz

![SineWave](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/sine_wave.png)

Fully rectified signal frequency > 100hz

![ZeroCrossDetectionInput](https://github.com/bilkeonur/HandGestureAcDimmer/blob/main/Images/rectified_sine_wave.png)

T=1/F -> T=1/100 -> T=0.01 Second -> T=10ms

With the code below, we add a function that is triggered every 10ms

```c++
attachInterrupt(digitalPinToInterrupt(ZERO_CROSS_PIN), zeroCrossInterrupt, RISING);
```

```c++
void zeroCrossInterrupt()
{ 
  delayMicroseconds(dimLevel*75);
  digitalWrite(DIM_PIN, LOW); //Turn On Triac
  delayMicroseconds(10);
  digitalWrite(DIM_PIN, HIGH); //Turn Off Triac
}
```

# About The Author

### Onur BiLKE

#### Computer Engineer
#### Android & IOS & Backend Developer && Embedded System Designer

<a href="https://www.linkedin.com/in/onur-bilke-55b04275/"><img src="https://github.com/aritraroy/social-icons/blob/master/linkedin-icon.png?raw=true" width="60"></a>

# License

```
Copyright 2022 bilkeonur

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
