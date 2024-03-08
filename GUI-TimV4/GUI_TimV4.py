# Tim Do 
# Oregon State University 
# College of EECS
# March 7th, 2024

import customtkinter                                                                                                # Python GUI library
import serial																										# Python Serial Library

customtkinter.set_appearance_mode("dark")                                                                           # Dark Background
customtkinter.set_default_color_theme("dark-blue")                                                                  # Dark Blue Theme
root = customtkinter.CTk()                                                                                          # Root Element
root.geometry("470x430")                                                                                            # Window Size
root.title("EJ16 GUI")                                                                                              # Name of Window
root.resizable(width=False, height=False)                                                                           # Unchangeable Window Size to prevent user error
frame1 = customtkinter.CTkFrame(master=root, width=500, height=500)                                                 # Contain Elements Inside Frame 
frame1.pack(pady=15, padx=15)																						# Spacing for Frame Around Voltage Slider
frame2 = customtkinter.CTkFrame(master=root, width=500, height=1900)                                                # Contain Elements Inside Frame
frame2.pack(pady=15, padx=15)																						# Spacing for Frame Around Current Slider
label1 = customtkinter.CTkLabel(master=frame1, text="Select Voltage:", font=("Arial", 20))							# Label for Upper Frame
label1.place(x=160, y=5)																							# Spacing for Label 1
label2 = customtkinter.CTkLabel(master=frame2, text="Select Current:", font=("Arial", 20))							# Label for Bottom Frame
label2.place(x=160, y=5)																							# Spacing for Label 2

ser = serial.Serial('COM5', 9600)																					# Open Serial Port, Match Baud Rate

def send_command(command):																							# Serial Send Function 
    ser.write((command + '\n').encode())																			# Encode Data Sent Over Serial
    response = ser.readline().decode().strip()																		# Waiting for Response, Decode Data Being 
    return response																									# Return Response

def slidingV(valueV):																								# Voltage Slider Function
	my_labelV.configure(text=(valueV))																				# Numerical Label for Voltage Slider

def applyV():																										# Apply Button Function (Upper Frame)
	spg=my_sliderV.get()																							# Get Value from Slider, Convert to String
	print(spg, "volts has been applied!")																			# Print Voltage Statement on Console
	response = send_command("VOLT " + str(spg))																		# Data sent to Arduino, Await Response
	print("Response: ", response)																					# Print Response from Arduino

my_sliderV = customtkinter.CTkSlider(frame1,																		# Voltage Slider
	from_=2,																										# Starting Value of Slider: 2
	to=14,																											# Ending Value of Slider: 14
	command=slidingV,																								# Call function; Voltage Slider
	number_of_steps=24,																								# Increment by 0.5, from 2 to 14
	width=450,																										# Width of Slider
	height=32,																										# Height of Slider
	border_width=15,																								# Border Width of Slider
	fg_color="white",																								# Slider Bar Default Color is White					
	progress_color="yellow")																						# Slider Bar Turns Yellow to Show Selected Value
	
my_sliderV.pack(pady=50, padx=35)																					# Sizing and Positioning of Voltage Slider
my_sliderV.set(2)																									# Without Any User Input, Start at a Value of 2
	
my_labelV = customtkinter.CTkLabel(frame1, text=my_sliderV.get(), font=("Arial", 20))								# Numerical Label Sizing Beneath Voltage Slider 
my_labelV.place(x=205, y=95)																						# Exact Positioning for that Numerical Label
	
buttonV = customtkinter.CTkButton(master=frame1, text="Apply", command=applyV)										# Button for Applying Voltage Settings           
buttonV.pack(pady=12, padx=10)																						# Button Spacing from Other Components

def slidingI(valueI):																								# Current Sliding Function
	my_labelI.configure(text=(valueI))																				# Numerical Label for Current Slider
	
def applyI():																										# Apply Button Function (Upper Frame)
	fpg=my_sliderI.get()																							# Get Value from Slider, Convert to String
	rounded_number = "{:.1f}".format(fpg)																			# Convert String to 2 Significant Figures
	print(rounded_number, "amps has been applied!")																	# Print Current statement on console
	response = send_command("CURR " + str(rounded_number))															# Data sent to Arduino, Await Response
	print("Response: ", response)																					# Print Response from Arduino
	
my_sliderI = customtkinter.CTkSlider(frame2,																		# Current Slider
	from_=0,																										# Starting Value of Slider: 0
	to=1.5,																											# Ending Value of Slider: 1.5
	command=slidingI,																								# Call function; Current Slider
	number_of_steps=15,																								# Increment by 0.1, from 0 to 1.5
	width=450,																										# Width of Slider
	height=32,																										# Height of Slider
	border_width=15,																								# Border Width of Slider
	fg_color="white",																								# Slider Bar Default Color is White	
	progress_color="blue")																							# Slider Bar Turns Blue to Show Selected Value

my_sliderI.pack(pady=50, padx=35)																					# Sizing and Positioning of Current Slider 
my_sliderI.set(0)																									# Without Any User Input, Start at a Value of 0

my_labelI = customtkinter.CTkLabel(frame2, text=my_sliderI.get(), font=("Arial", 20))								# Numerical Label Sizing Beneath Current Slider 
my_labelI.place(x=205, y=95)																						# Exact Positioning for that Numerical Label

buttonI = customtkinter.CTkButton(frame2, text="Apply", command=applyI)												# Button for Applying Current Settings    
buttonI.pack(pady=12, padx=10)																						# Button Spacing from Other Components

root.mainloop()																										# Loop