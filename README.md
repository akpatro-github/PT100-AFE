# PT100-AFE
Analog Front-End for the PT100 temperature sensor inside the HIMA temperature chamber.

|<img title="Block Diagram" src="https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/Temp_sensor_block%20_dia.png">|
|:--:|
|*Figure 1: Block Diagram of PT-100*|

# PT-100 Temperature vs. Resistance Data

[Click Here](https://github.com/akpatro-github/PT100-AFE/blob/main/pt100-datasheet.csv) to get the PT-100 Temperature vs. Resistance Data.

# Analog Front-End (AFE) Architecture

## 1. Design Summary
The Design requirements are as follows:
- Supply voltage: 5V
- RTD Temperature range: -40℃ to 151℃
- RTD Resistance range: 84.27Ω to 157.69Ω
- Output Range: 0V to 5V

## 2. Theory of operation

Figure 2 and Figure 3 show the schematic of the RTD amplifier for minimum and maximum output conditions. Note that this circuit was designed for a -40℃ to 151℃ RTD temperature range. At -40℃ the RTD resistance is 84.27Ω and the voltage across it is 8.427mV (VRTD = (100μA)(84.27Ω), see Figure 2). Notice that Rtrim develops a voltage drop that opposes the RTD drop. The drop across Rtrim is used to shift amplifiers input differential voltage to a minimum level. The output is the differential input multiplied by the gain (Vout = 659.67 x 227μV = 0.1497V). At 151℃ the RTD resistance is 157.69Ω and the voltage across it is 15.769mV (VRTD = (100μA)(157.69Ω)). This produces a differential input of 7.569mV and an output voltage of 4.9930V (Vout = 659.67 x 7.569mV = 4.9930V, see Figure 3).

|<img title="@-40C" src="https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/-40C.png">|
|:--:|
|*Fig 2:RTD Amplifier wit minimum output condition*|

|<img title="@151C" src="https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/151C.png">|
|:--:|
|*Fig 3:RTD Amplifier wit maximum output condition*|



Fig 2:RTD Amplifier wit maximum output condition

### 2.1. **Lead Resistance cancelation (3 wire RTD)**
	
Figure 3 below shows the three wire RTD configuration can be used to cancel lead resistance. Note that the resistance in each lead must be equal to cancel the error. Also, the two current sources in the REF200 need to be equal. Notice that the voltage developed on the two top leads of the RTD are equal and opposite polarity so that the amplifiers input is only from the RTD voltage. In this example, the RTD drop is 15.679mV and the leads each have 0.02mV. Notice that the 0.02mV drops cancel. Finally, notice that the voltage on the 3rd lead (0.04mV) creates a small shift in the common mode voltage. In some applications, a larger resistor is intentionally added to shift the common mode voltage. However, the INA826 has a rail to rail common mode range, so it can accept common mode voltages near ground.

|<img title="Schematic" src="https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/schematic.png">|
|:--:|
|*Figure 4: Schematic of AFE*|


### 2.2 Noise Calculation
#### Resistror Noise
For Analysis purpose, Rwire = 20Ω,
		     Temperature = 45℃(318k), 
		     B.W. = 30KHz

Thermal noise of resistor = <a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_n_r^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;R" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_n_r^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;R" title="\bar{V}_n_r^2 = 4 * K * T * R" /></a>


i)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nr1}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{wire}&space;&plus;&space;R_{trim})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nr1}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{wire}&space;&plus;&space;R_{trim})" title="\small \bar{V}_{nr1}^2 = 4 * K * T * (R_{wire} + R_{trim})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr1}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;318&space;*&space;(82&plus;20)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr1}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;318&space;*&space;(82&plus;20)" title="\bar{V}_{nr1}^2 = 4 * 1.38 * 10^{-23} * 318 * (82+20)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr1}^2&space;=&space;1.79&space;*&space;10^{-18}&space;\frac{V^{2}}{HZ}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr1}^2&space;=&space;1.79&space;*&space;10^{-18}&space;\frac{V^{2}}{HZ}" title="\bar{V}_{nr1}^2 = 1.79 * 10^{-18} \frac{V^{2}}{HZ}" /></a>

ii)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nr2}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{PT100}&space;&plus;&space;R_{wire})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nr2}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{PT100}&space;&plus;&space;R_{wire})" title="\small \bar{V}_{nr2}^2 = 4 * K * T * (R_{PT100} + R_{wire})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr2}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;433&space;*&space;(161.04&plus;20)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr2}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;433&space;*&space;(161.04&plus;20)" title="\bar{V}_{nr2}^2 = 4 * 1.38 * 10^{-23} * 433 * (161.04+20)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr2}^2&space;=&space;4.33&space;*&space;10^{-18}\frac{V^{2}}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr2}^2&space;=&space;4.33&space;*&space;10^{-18}\frac{V^{2}}{{Hz}}" title="\bar{V}_{nr2}^2 = 4.33 * 10^{-18}\frac{V^{2}}{{Hz}}" /></a>

iii)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nr3}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{wire})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nr3}^2&space;=&space;4&space;*&space;K&space;*&space;T&space;*&space;(R_{wire})" title="\small \bar{V}_{nr3}^2 = 4 * K * T * (R_{wire})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr2}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;318&space;*&space;20" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr3}^2&space;=&space;4&space;*&space;1.38&space;*&space;10^{-23}&space;*&space;318&space;*&space;20" title="\bar{V}_{nr3}^2 = 4 * 1.38 * 10^{-23} * 318 * 20" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nr2}^2&space;=&space;3.51&space;*&space;10^{-19}\frac{V^{2}}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nr3}^2&space;=&space;3.51&space;*&space;10^{-19}\frac{V^{2}}{{Hz}}" title="\bar{V}_{nr3}^2 = 3.51 * 10^{-19}\frac{V^{2}}{{Hz}}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;Total&space;Resistance&space;Noise&space;=&space;V_{nr}&space;=&space;\sqrt{(1.34)^{2}&space;&plus;&space;(2.1)^2}&space;&plus;&space;0.6&space;=&space;3.1\frac{nV}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;Total&space;Resistance&space;Noise&space;=&space;V_{nr}&space;=&space;\sqrt{(1.34)^{2}&space;&plus;&space;(2.1)^2}&space;&plus;&space;0.6&space;=&space;3.1\frac{nV}{\sqrt{Hz}}" title="\small Total Resistance Noise = V_{nr} = \sqrt{(1.34)^{2} + (2.1)^2} + 0.6 = 3.1\frac{nV}{\sqrt{Hz}}" /></a>

#### Current Noise

From the datasheet of INA826 current noise = <a href="https://www.codecogs.com/eqnedit.php?latex=10fA/\sqrt{Hz}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?10fA/\sqrt{Hz}" title="10fA/\sqrt{Hz}" /></a>

i)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nc1}^2&space;=&space;0.00001&space;*&space;\frac{nA}{\sqrt{Hz}}&space;*&space;(20&plus;161.04)ohm" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nc1}^2&space;=&space;0.00001&space;&space;\frac{nA}{\sqrt{Hz}}&space;*&space;(20&plus;161.04)ohm" title="\small \bar{V}_{nc1}^2 = 0.00001 * \frac{nA}{\sqrt{Hz}} * (20+161.04)ohm" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nc1}^2&space;=&space;0.0018\frac{nV}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nc1}&space;=&space;0.0018\frac{nV}{\sqrt{Hz}}" title="\bar{V}_{nc1}^2 = 0.0018\frac{nV}{\sqrt{Hz}}" /></a>

ii)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nc2}^2&space;=&space;0.00001&space;*&space;\frac{nA}{\sqrt{Hz}}&space;*&space;(20&plus;82)ohm" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nc2}^2&space;=&space;0.00001&space;&space;\frac{nA}{\sqrt{Hz}}&space;*&space;(20&plus;82)ohm" title="\small \bar{V}_{nc2}^2 = 0.00001 * \frac{nA}{\sqrt{Hz}} * (20+82)ohm" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nc2}^2&space;=&space;0.00102\frac{nV}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nc2}&space;=&space;0.00102\frac{nV}{\sqrt{Hz}}" title="\bar{V}_{nc2}^2 = 0.00102\frac{nV}{\sqrt{Hz}}" /></a>

iii)

<a href="https://www.codecogs.com/eqnedit.php?latex=\small&space;\bar{V}_{nc3}^2&space;=&space;0.00002&space;*&space;\frac{nA}{\sqrt{Hz}}&space;*&space;20&space;ohm" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\small&space;\bar{V}_{nc3}^2&space;=&space;0.00002&space;*&space;\frac{nA}{\sqrt{Hz}}&space;*&space;20&space;ohm" title="\small \bar{V}_{nc3}^2 = 0.00002 * \frac{nA}{\sqrt{Hz}} * 20 ohm" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{nc2}^2&space;=&space;0.0004\frac{nV}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{nc3}&space;=&space;0.0004\frac{nV}{\sqrt{Hz}}" title="\bar{V}_{nc2}^2 = 0.0004\frac{nV}{\sqrt{Hz}}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=Total&space;Noise&space;=&space;\bar{V}_{nc}&space;=&space;\sqrt{\bar{V}_{nc1}^{2}&space;&plus;&space;\bar{V}_{nc2}^{2}&space;}&space;&plus;&space;\bar{V}_{nc3}&space;=&space;\bar{V}_{nc}&space;=&space;0.0025&space;\frac{nV}{HZ}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Total&space;Noise&space;=&space;\bar{V}_{nc}&space;=&space;\sqrt{\bar{V}_{nc1}^{2}&space;&plus;&space;\bar{V}_{nc2}^{2}&space;}&space;&plus;&space;\bar{V}_{nc3}&space;=&space;\bar{V}_{nc}&space;=&space;0.0025&space;\frac{nV}{HZ}" title="Total Noise =  \sqrt{\bar{V}_{nc1}^{2} + \bar{V}_{nc2}^{2} } + \bar{V}_{nc3} = \bar{V}_{nc} = 0.0025 \frac{nV}{HZ}" /></a>

#### Voltage Noise

<a href="https://www.codecogs.com/eqnedit.php?latex=e_{ni}&space;=&space;20&space;\frac{nV}{\sqrt{Hz}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e_{ni}&space;=&space;20&space;\frac{nV}{\sqrt{Hz}}" title="e_{ni} = 20 \frac{nV}{\sqrt{Hz}}" /></a>

#### Total Noise for a Bandwidth of 30KHz
 
<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{n}&space;=&space;\sqrt{(\bar{V}_{nr}^{2}&space;&plus;&space;\bar{V}_{nc}^{2}&space;&plus;&space;\bar{V}_{nv}^{2})&space;*&space;B.W.&space;}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{n}&space;=&space;\sqrt{(\bar{V}_{nr}^{2}&space;&plus;&space;\bar{V}_{nc}^{2}&space;&plus;&space;\bar{V}_{nv}^{2})&space;*&space;B.W.&space;}" title="\bar{V}_{n} = \sqrt{(\bar{V}_{nr}^{2} + \bar{V}_{nc}^{2} + \bar{V}_{nv}^{2}) * B.W. }" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{n}&space;=&space;\sqrt{(3.1^{2}&space;&plus;&space;0.0025^{2}&space;&plus;&space;20^{2})&space;*&space;30KHz&space;}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{n}&space;=&space;\sqrt{(3.1^{2}&space;&plus;&space;0.0025^{2}&space;&plus;&space;20^{2})&space;*&space;30KHz&space;}" title="\bar{V}_{n} = \sqrt{(3.1^{2} + 0.0025^{2} + 20^{2}) * 30KHz }" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bar{V}_{n}&space;=&space;3.5uV" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bar{V}_{n}&space;=&space;3.5uV" title="\bar{V}_{n} = 3.5uV" /></a>


 ### 2.3 Selecting Gain and Offset Resistor

- Calculate the require Gain (ΔVout/ΔVin)

<a href="https://www.codecogs.com/eqnedit.php?latex=G&space;=&space;\frac{(Voutmax&space;-&space;Voutmin)}{(Rmax-Rmin).Iref}&space;=&space;\frac{(4.993-0.15)}{(157.69-84.27).100u}&space;=&space;659.63" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;=&space;\frac{(Voutmax&space;-&space;Voutmin)}{(Rmax-Rmin).Iref}&space;=&space;\frac{(4.993-0.15)}{(157.69-84.27).100u}&space;=&space;659.63" title="G = \frac{(Voutmax - Voutmin)}{(Rmax-Rmin).Iref} = \frac{(4.993-0.15)}{(157.69-84.27).100u} = 659.63" /></a>
	
- Choose standard resistors to assure that the actual gain is equal to or less than the calculated gain. From INA826 data sheet we get the gain equation as:
	
<a href="https://www.codecogs.com/eqnedit.php?latex=G&space;=&space;1&plus;\frac{49.4K&space;}{RG}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?G&space;=&space;1&plus;\frac{49.4K&space;}{RG}" title="G = 1+\frac{49.4K }{RG}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=RG&space;=&space;\frac{G-1&space;}{49.4K}&space;=75ohm&space;(standard&space;value)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?RG&space;=&space;\frac{G-1&space;}{49.4K}&space;=75ohm&space;(standard&space;value)" title="RG = \frac{G-1 }{49.4K} =75ohm (standard   value)" /></a>
	
- Calculate a value of R3 based on the minimum output voltage and the gain
R3 = 82Ω (standard value)

### 2.4 External Low Pass Filter
- Given that when G = 1000, BandWidth = 6KHz (From Data sheet of INA826)
- In this operation G = 659.67, So B.W. = 9.1KHz
- calculating the value of Rf and Cf
 
<a href="https://www.codecogs.com/eqnedit.php?latex=f_{c}=\frac{1}{2\cdot&space;\prod&space;\cdot&space;R_{f}\cdot&space;C_{f}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{c}=\frac{1}{2\cdot&space;\prod&space;\cdot&space;R_{f}\cdot&space;C_{f}}" title="f_{c}=\frac{1}{2\cdot \prod \cdot R_{f}\cdot C_{f}}" /></a>

From this equation
Rf = 75Ω &
Cf = 0.22uF


## 3. PCB Design
### 3.1. PCB Layout

|<img title="PCB Top" src="https://github.com/akpatro-github/PT100-AFE/blob/main/PCB/PCB_Top.png">|
|:--:|
|*Figure 4: PCB Top - Red*|


|<img title="PCB Bottom" src="https://github.com/akpatro-github/PT100-AFE/blob/main/PCB/PCB_Bottom.png">|
|:--:|
|*Figure 5: PCB Bottom - Blue*|

### 3.2. Component Selection

[Click Here](https://github.com/akpatro-github/PT100-AFE/blob/main/PCB/bill%20of%20components.docx) to get the bill of components.


# Analog Discovery 2
