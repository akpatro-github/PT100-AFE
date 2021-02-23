# PT100-AFE
Analog Front-End for the PT100 temperature sensor inside the HIMA temperature chamber.

# PT-100 Temperature vs. Resistance Data

# Analog Front-End (AFE) Architecture

## 1. Design Summary
The Design requirements are as follows:
- Supply voltage: 5V
- RTD Temperature range: -40℃ to 151℃
- RTD Resistance range: 84.27Ω to 157.69Ω
- Output Range: 0V to 5V

## 2. Theory of operation

Figure 1 and Figure 2 show the schematic of the RTD amplifier for minimum and maximum output conditions. Note that this circuit was designed for a -40℃ to 151℃ RTD temperature range. At -40℃ the RTD resistance is 84.27Ω and the voltage across it is 8.427mV (VRTD = (100μA)(84.27Ω), see Figure 1). Notice that Rtrim develops a voltage drop that opposes the RTD drop. The drop across Rtrim is used to shift amplifiers input differential voltage to a minimum level. The output is the differential input multiplied by the gain (Vout = 659.67 x 227μV = 0.1497V). At 151℃ the RTD resistance is 157.69Ω and the voltage across it is 15.769mV (VRTD = (100μA)(157.69Ω)). This produces a differential input of 7.569mV and an output voltage of 4.9930V (Vout = 659.67 x 7.569mV = 4.9930V, see Figure 2).

![@-40 C Figure](https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/-40C.png)

![@151 C Figure](https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/151C.png)

### 2.1. **Lead Resistance cancelation (3 wire RTD)**
	
Figure 3 below shows the three wire RTD configuration can be used to cancel lead resistance. Note that the resistance in each lead must be equal to cancel the error. Also, the two current sources in the REF200 need to be equal. Notice that the voltage developed on the two top leads of the RTD are equal and opposite polarity so that the amplifiers input is only from the RTD voltage. In this example, the RTD drop is 15.679mV and the leads each have 0.02mV. Notice that the 0.02mV drops cancel. Finally, notice that the voltage on the 3rd lead (0.04mV) creates a small shift in the common mode voltage. In some applications, a larger resistor is intentionally added to shift the common mode voltage. However, the INA826 has a rail to rail common mode range, so it can accept common mode voltages near ground.

![schematic Figure](https://github.com/akpatro-github/PT100-AFE/blob/main/Block%20Diagram/schematic.png)

### 2.2 Noise Calculation

### 2.3 Selecting Gain and Offset Resistor

- Calculate the require Gain (ΔVout/ΔVin)

G =  $\frac{(Voutmax - Voutmin) }{(RRTDmax-RRTDmin).Iref}$ = $\frac{(4.993-0.15) }{(157.69-84.27).100u}$ = 659.63
	
- Choose standard resistors to assure that the actual gain is equal to or less than the calculated gain. From INA826 data sheet we get the gain equation as:
	
G =  1+$\frac{49.4K }{RG}$
RG = $\frac{G-1 }{49.4K}$ = 75Ω (standard value)
	
- Calculate a value of R3 based on the minimum output voltage and the gain
R3 = 82Ω (standard value)
	
## 3. PCB Design
###3.1. PCB Layout

![PCB Top ](https://github.com/akpatro-github/PT100-AFE/blob/main/PCB/PCB_Top.png)

![PCB Bottom](https://github.com/akpatro-github/PT100-AFE/blob/main/PCB/PCB_Bottom.png)

# Analog Discovery 2
