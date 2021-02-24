#####################################
##   11 bit Operation at ADC       ##
#####################################

# import Libraries
import csv
import cmath
import numpy as np
import matplotlib.pyplot as plt

# Temperature & Resistance from PT-100 Datasheet
temp=[]
res=[]
count=0
for row in csv.reader(open('pt100-datasheet.csv'), delimiter=','):
	if count == 0:
		count+=1
	else:
		temp.append(float(row[0]))
		res.append(float(row[1]))

# Interpolated Resistance & Temperature
interpolated_res=[]
interpolated_temp=[]
for t in np.arange(-40,160.125,0.125):
	x=np.interp(t,temp,res)
	interpolated_res.append(x)
	interpolated_temp.append(t)


#################################### 
###       AFE Operation          ###
####################################
opamp_output=[]
gain=659.67
for value_r in interpolated_res:
	opamp_input= (100*(10**(-6)))*(value_r-82)
	opamp_output.append(gain*opamp_input)


##################################### 
###      11 bit ADC Operation     ###
#####################################

# Storing Output voltages as after 11 bit operation in ADC
lsb = 6.25/(2**11)
eleven_bit=[]
for value in opamp_output:
	x = value//lsb
	eleven_bit.append(x)


code_voltage=[]
for code in eleven_bit:
	code_voltage.append(lsb*code)


###################################################
###   Program for calculation of temperature    ###
###################################################

# a,b,c from opamp_output values
a = -3.84022*(10**(-6))
b = 0.0257823
c = 1.18718

calculated_temp=[]
for volt in code_voltage:
	dis = (b**2) - (4*a*(c-volt))
	temp_list = (-b + cmath.sqrt(dis))/(2 * a)
	calculated_temp.append(round((temp_list.real),3))

# Error between the Ideal & Calculated Temperature Value
error=[]
for i in range(len(code_voltage)):
	error.append(interpolated_temp[i]-calculated_temp[i])

# Plotting Figure

#Plotting Resistance vs Temperature from Datasheet
plt.plot(interpolated_temp,interpolated_res,'-b')
plt.xlabel('Temperature (°C)')
plt.ylabel('Resistance (Ω) ')
plt.title('Resistance vs Temperature')
plt.show()

#Plotting  INA output voltage vs Temperature
plt.plot(interpolated_temp,opamp_output,'-b')
plt.xlabel('Temperature (°C)')
plt.ylabel('AFE Output (Volt)')
plt.title('AFE Output Voltage vs Temperature')
plt.show()

#Plotting code vs Temperature 
plt.plot(interpolated_temp,eleven_bit,'-b')
plt.xlabel('Temperature (°C)')
plt.ylabel('11 bit code')
plt.title('Code vs Temperature')
plt.show()

#Plotting Error b/w Calculated & Datasheet Temperature
plt.plot(interpolated_temp,error,'-b')
plt.xlabel('Temperature (°C)')
plt.ylabel('Error (°C) ')
plt.title('Error vs Temperature')
plt.show()
