from tkinter import *
from datetime import date
import time

GLOBAL_SEATRGB = 0
GLOBAL_SEATRGB_R = 0
GLOBAL_SEATRGB_G = 0
GLOBAL_SEATRGB_B = 0
GLOBAL_SEATRGB_Y = 0
GLOBAL_SEATRGB_M = 0

GLOBAL_BEDRGB = 0
GLOBAL_BEDRGB_R = 0
GLOBAL_BEDRGB_G = 0
GLOBAL_BEDRGB_B = 0
GLOBAL_BEDRGB_Y = 0
GLOBAL_BEDRGB_M = 0

GLOBAL_RGB1 = 0
GLOBAL_RGB2 = 0
GLOBAL_PC = 0
GLOBAL_AUDIO = 0
GLOBAL_MAIN = 0

def update_ui():
	global GLOBAL_SEATRGB
	global GLOBAL_BEDRGB
	global GLOBAL_RGB1
	global GLOBAL_RGB2
	global GLOBAL_PC
	global GLOBAL_AUDIO
	global GLOBAL_MAIN

	if GLOBAL_SEATRGB == 1:
		f5Label6.configure(bg='green', text='ON')
	else:
		f5Label6.configure(bg='red', text='OFF')

	if GLOBAL_BEDRGB == 1:
		f5Label7.configure(bg='green', text='ON')
	else:
		f5Label7.configure(bg='red', text='OFF')
		
	if GLOBAL_MAIN == 1:
		f5Label5.configure(bg='green', text='ON')
	else:
		f5Label5.configure(bg='red', text='OFF')
		
	if GLOBAL_PC == 1:
		f5Label1.configure(bg='green', text='ON')
	else:
		f5Label1.configure(bg='red', text='OFF')
		
	if GLOBAL_AUDIO == 1:
		f5Label2.configure(bg='green', text='ON')
	else:
		f5Label2.configure(bg='red', text='OFF')
		
	if GLOBAL_RGB1 == 1:
		f5Label3.configure(bg='green', text='ON')
	else:
		f5Label3.configure(bg='red', text='OFF')
		
	if GLOBAL_RGB2 == 1:
		f5Label4.configure(bg='green', text='ON')
	else:
		f5Label4.configure(bg='red', text='OFF')
	

def update_ui_sec():
	update_ui()
	curr_timer = time.strftime("%H:%M:%S")
	f3TimeLabel.configure(text=curr_timer)
	f3.after(1000, update_ui_sec)
	
def update_ui_hrs():
	curr_date = date.today()
	f3DateLabel.configure(text=curr_date)
	curr_temp = 0.0
	f3TempLabel.configure(text='%f °C' % (curr_temp))
	f3.after(60000, update_ui_hrs)
	
def toggle_main_light():
	global GLOBAL_MAIN
	if GLOBAL_MAIN == 1:
		GLOBAL_MAIN = 0
	else:
		GLOBAL_MAIN = 1
	update_ui()
	
def toggle_seat_rgb():
	global GLOBAL_SEATRGB
	if GLOBAL_SEATRGB == 1:
		GLOBAL_SEATRGB = 0
	else:
		GLOBAL_SEATRGB = 1
	update_ui()

def toggle_bed_rgb():
	global GLOBAL_BEDRGB
	if GLOBAL_BEDRGB == 1:
		GLOBAL_BEDRGB = 0
	else:
		GLOBAL_BEDRGB = 1
	update_ui()

def toggle_rgb1():
	global GLOBAL_RGB1
	if GLOBAL_RGB1 == 1:
		GLOBAL_RGB1 = 0
	else:
		GLOBAL_RGB1 = 1
	update_ui()

def toggle_rgb2():
	global GLOBAL_RGB2
	if GLOBAL_RGB2 == 1:
		GLOBAL_RGB2 = 0
	else:
		GLOBAL_RGB2 = 1
	update_ui()

def toggle_pc():
	global GLOBAL_PC
	if GLOBAL_PC == 1:
		GLOBAL_PC = 0
	else:
		GLOBAL_PC = 1
	update_ui()

def toggle_audio():
	global GLOBAL_AUDIO
	if GLOBAL_AUDIO == 1:
		GLOBAL_AUDIO = 0
	else:
		GLOBAL_AUDIO = 1
	update_ui()
	
def pick_rgb_seat_color():
	global GLOBAL_SEATRGB
	global GLOBAL_SEATRGB_R
	global GLOBAL_SEATRGB_G
	global GLOBAL_SEATRGB_B
	global GLOBAL_SEATRGB_Y
	global GLOBAL_SEATRGB_M
	
	def _0_close():
		global GLOBAL_SEATRGB_R
		global GLOBAL_SEATRGB_G
		global GLOBAL_SEATRGB_B
		global GLOBAL_SEATRGB_Y
		global GLOBAL_SEATRGB_M
		GLOBAL_SEATRGB_R = f0_1Slider1.get()
		GLOBAL_SEATRGB_G = f0_1Slider2.get()
		GLOBAL_SEATRGB_B = f0_1Slider3.get()
		GLOBAL_SEATRGB_Y = f0_1Slider4.get()
		root2.destroy()
		update_ui()
		
	def _0_update_display():
		_0_curr_color = '#%02x%02x%02x' % (f0_1Slider1.get(), f0_1Slider2.get(), f0_1Slider3.get())
		f0_1Button1.configure(bg=_0_curr_color)
		if root2.winfo_exists() == 1:
			f0_1.after(100, _0_update_display)
			
	def _0_change_mode():
		global GLOBAL_SEATRGB_M
		if GLOBAL_SEATRGB_M == 0:
			GLOBAL_SEATRGB_M = 1
			f0_1Button3.configure(text='Fade')
		elif GLOBAL_SEATRGB_M == 1:
			GLOBAL_SEATRGB_M = 2
			f0_1Button3.configure(text='Flash')
		else:
			GLOBAL_SEATRGB_M = 0
			f0_1Button3.configure(text='None')
	
	def _0_trigger():
		global GLOBAL_SEATRGB
		if GLOBAL_SEATRGB == 1:
			GLOBAL_SEATRGB = 0
			f0_1Button1.configure(text='OFF')
		else:
			GLOBAL_SEATRGB = 1
			f0_1Button1.configure(text='ON')
		
	root2 = Toplevel(root)
	root2.geometry('480x320')
	root2.resizable(0,0)
	#root2.wait_visibility(root2)
	root2.attributes('-topmost', True)
	root2.attributes('-fullscreen', True)
	root2.grid_propagate(False)
	
	f0_1 = Frame(root2, width=480, height=320)
	f0_1.grid_propagate(False)
	f0_1.columnconfigure(0, weight=1)
	f0_1.columnconfigure(1, weight=4)
	f0_1.rowconfigure(0, weight=10)
	f0_1.rowconfigure(1, weight=1)
	f0_1.rowconfigure(2, weight=1)
	f0_1.rowconfigure(3, weight=1)
	f0_1.rowconfigure(4, weight=1)
	f0_1.rowconfigure(5, weight=1)
	f0_1.rowconfigure(6, weight=1)
	
	f0_1Button1 = Button(f0_1, bg='white', relief='flat', command=_0_trigger)
	if GLOBAL_SEATRGB == 1:
		f0_1Button1.configure(text='ON')
	else:
		f0_1Button1.configure(text='OFF')
	f0_1Button2 = Button(f0_1, text='Apply', command=_0_close)
	f0_1Button3 = Button(f0_1, text='None', relief='flat', command=_0_change_mode)
	if GLOBAL_SEATRGB_M == 0:
		f0_1Button3.configure(text='None')
	elif GLOBAL_SEATRGB_M == 1:
		f0_1Button3.configure(text='Fade')
	else:
		f0_1Button3.configure(text='Flash')
	f0_1Label2 = Label(f0_1, text='Mode:', anchor=CENTER)
	f0_1Label3 = Label(f0_1, text='Red:', anchor=CENTER)
	f0_1Label4 = Label(f0_1, text='Green:', anchor=CENTER)
	f0_1Label5 = Label(f0_1, text='Blue:', anchor=CENTER)
	f0_1Label6 = Label(f0_1, text='Intensity:', anchor=CENTER)
	f0_1Slider1 = Scale(f0_1, from_=0, to=255, orient=HORIZONTAL)
	f0_1Slider1.set(GLOBAL_SEATRGB_R)
	f0_1Slider2 = Scale(f0_1, from_=0, to=255, orient=HORIZONTAL)
	f0_1Slider2.set(GLOBAL_SEATRGB_G)
	f0_1Slider3 = Scale(f0_1, from_=0, to=255, orient=HORIZONTAL)
	f0_1Slider3.set(GLOBAL_SEATRGB_B)
	f0_1Slider4 = Scale(f0_1, from_=0, to=100, orient=HORIZONTAL)
	f0_1Slider4.set(GLOBAL_SEATRGB_Y)
	f0_1.grid(row=0, column=0, sticky='nsew')
	f0_1Button1.grid(row=0, column=0, columnspan=2, sticky='nsew')
	f0_1Label3.grid(row=1, column=0, sticky='nsew')
	f0_1Slider1.grid(row=1, column=1, sticky='nsew')
	f0_1Label4.grid(row=2, column=0, sticky='nsew')
	f0_1Slider2.grid(row=2, column=1, sticky='nsew')
	f0_1Label5.grid(row=3, column=0, sticky='nsew')
	f0_1Slider3.grid(row=3, column=1, sticky='nsew')
	f0_1Label6.grid(row=4, column=0, sticky='nsew')
	f0_1Slider4.grid(row=4, column=1, sticky='nsew')
	f0_1Label2.grid(row=5, column=0, sticky='nsew')
	f0_1Button3.grid(row=5, column=1, sticky='nsew')
	f0_1Button2.grid(row=6, column=0, columnspan=2, sticky='nsew')
	
	_0_update_display()
	root2.mainloop()
	
def pick_rgb_bed_color():
	global GLOBAL_BEDRGB
	global GLOBAL_BEDRGB_R
	global GLOBAL_BEDRGB_G
	global GLOBAL_BEDRGB_B
	global GLOBAL_BEDRGB_Y
	global GLOBAL_BEDRGB_M
	
	def _1_close():
		global GLOBAL_BEDRGB_R
		global GLOBAL_BEDRGB_G
		global GLOBAL_BEDRGB_B
		global GLOBAL_BEDRGB_Y
		global GLOBAL_BEDRGB_M
		GLOBAL_BEDRGB_R = f1_1Slider1.get()
		GLOBAL_BEDRGB_G = f1_1Slider2.get()
		GLOBAL_BEDRGB_B = f1_1Slider3.get()
		GLOBAL_BEDRGB_Y = f1_1Slider4.get()
		root3.destroy()
		update_ui()
		
	def _1_update_display():
		_1_curr_color = '#%02x%02x%02x' % (f1_1Slider1.get(), f1_1Slider2.get(), f1_1Slider3.get())
		f1_1Button1.configure(bg=_1_curr_color)
		if root3.winfo_exists() == 1:
			f1_1.after(100, _1_update_display)
			
	def _1_change_mode():
		global GLOBAL_BEDRGB_M
		if GLOBAL_BEDRGB_M == 0:
			GLOBAL_BEDRGB_M = 1
			f1_1Button3.configure(text='Fade')
		elif GLOBAL_BEDRGB_M == 1:
			GLOBAL_BEDRGB_M = 2
			f1_1Button3.configure(text='Flash')
		else:
			GLOBAL_BEDRGB_M = 0
			f1_1Button3.configure(text='None')
	
	def _1_trigger():
		global GLOBAL_BEDRGB
		if GLOBAL_BEDRGB == 1:
			GLOBAL_BEDRGB = 0
			f1_1Button1.configure(text='OFF')
		else:
			GLOBAL_BEDRGB = 1
			f1_1Button1.configure(text='ON')
		
	root3 = Toplevel(root)
	root3.geometry('480x320')
	root3.resizable(0,0)
	#root3.wait_visibility(root3)
	root3.attributes('-topmost', True)
	root3.attributes('-fullscreen', True)
	root3.grid_propagate(False)
	
	f1_1 = Frame(root3, width=480, height=320)
	f1_1.grid_propagate(False)
	f1_1.columnconfigure(0, weight=1)
	f1_1.columnconfigure(1, weight=4)
	f1_1.rowconfigure(0, weight=10)
	f1_1.rowconfigure(1, weight=1)
	f1_1.rowconfigure(2, weight=1)
	f1_1.rowconfigure(3, weight=1)
	f1_1.rowconfigure(4, weight=1)
	f1_1.rowconfigure(5, weight=1)
	f1_1.rowconfigure(6, weight=1)
	
	f1_1Button1 = Button(f1_1, bg='white', relief='flat', command=_1_trigger)
	if GLOBAL_BEDRGB == 1:
		f1_1Button1.configure(text='ON')
	else:
		f1_1Button1.configure(text='OFF')
	f1_1Button2 = Button(f1_1, text='Apply', command=_1_close)
	f1_1Button3 = Button(f1_1, text='None', relief='flat', command=_1_change_mode)
	if GLOBAL_BEDRGB_M == 0:
		f1_1Button3.configure(text='None')
	elif GLOBAL_BEDRGB_M == 1:
		f1_1Button3.configure(text='Fade')
	else:
		f1_1Button3.configure(text='Flash')
	f1_1Label2 = Label(f1_1, text='Mode:', anchor=CENTER)
	f1_1Label3 = Label(f1_1, text='Red:', anchor=CENTER)
	f1_1Label4 = Label(f1_1, text='Green:', anchor=CENTER)
	f1_1Label5 = Label(f1_1, text='Blue:', anchor=CENTER)
	f1_1Label6 = Label(f1_1, text='Intensity:', anchor=CENTER)
	f1_1Slider1 = Scale(f1_1, from_=0, to=255, orient=HORIZONTAL)
	f1_1Slider1.set(GLOBAL_BEDRGB_R)
	f1_1Slider2 = Scale(f1_1, from_=0, to=255, orient=HORIZONTAL)
	f1_1Slider2.set(GLOBAL_BEDRGB_G)
	f1_1Slider3 = Scale(f1_1, from_=0, to=255, orient=HORIZONTAL)
	f1_1Slider3.set(GLOBAL_BEDRGB_B)
	f1_1Slider4 = Scale(f1_1, from_=0, to=100, orient=HORIZONTAL)
	f1_1Slider4.set(GLOBAL_BEDRGB_Y)
	f1_1.grid(row=0, column=0, sticky='nsew')
	f1_1Button1.grid(row=0, column=0, columnspan=2, sticky='nsew')
	f1_1Label3.grid(row=1, column=0, sticky='nsew')
	f1_1Slider1.grid(row=1, column=1, sticky='nsew')
	f1_1Label4.grid(row=2, column=0, sticky='nsew')
	f1_1Slider2.grid(row=2, column=1, sticky='nsew')
	f1_1Label5.grid(row=3, column=0, sticky='nsew')
	f1_1Slider3.grid(row=3, column=1, sticky='nsew')
	f1_1Label6.grid(row=4, column=0, sticky='nsew')
	f1_1Slider4.grid(row=4, column=1, sticky='nsew')
	f1_1Label2.grid(row=5, column=0, sticky='nsew')
	f1_1Button3.grid(row=5, column=1, sticky='nsew')
	f1_1Button2.grid(row=6, column=0, columnspan=2, sticky='nsew')
	
	_1_update_display()
	root3.mainloop()
	
root = Tk()
root.geometry('480x320')
root.resizable(0,0)
root.attributes("-fullscreen",True)
root.grid_propagate(False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

window = Frame(root, width=480, height=320)
window.grid_propagate(False)

f1 = Button(window, text='Main light', command=toggle_main_light)
f1.grid_propagate(False)

f2 = Frame(window, width=320, height=30, borderwidth=1, relief=GROOVE)
f2.grid_propagate(False)
f2.columnconfigure(0, weight=1)
f2.columnconfigure(1, weight=1)
f2.rowconfigure(1, weight=1)
f2Label = Label(f2, text='RGB LED Strips')
f2Button1 = Button(f2, text='Seat', command=pick_rgb_seat_color)
f2Button2 = Button(f2, text='Bed', command=pick_rgb_bed_color)
f2Label.grid(row=0, column=0, columnspan=2)
f2Button1.grid(row=1, column=0, sticky='nsew')
f2Button2.grid(row=1, column=1, sticky='nsew')

f3 = Frame(window, width=160, height=120, borderwidth=1, relief=GROOVE)
f3.grid_propagate(False)
f3.columnconfigure(0, weight=1)
f3.rowconfigure(0, weight=1)
f3.rowconfigure(1, weight=1)
f3.rowconfigure(2, weight=1)
f3TimeLabel = Label(f3, text='', anchor=CENTER)
f3DateLabel = Label(f3, text='', anchor=CENTER)
f3TempLabel = Label(f3, text='', anchor=CENTER)
f3TimeLabel.grid(row=0, column=0, sticky='nsew')
f3DateLabel.grid(row=1, column=0, sticky='nsew')
f3TempLabel.grid(row=2, column=0, sticky='nsew')

f4 = Frame(window, width=320, height=200, borderwidth=1, relief=GROOVE)
f4.grid_propagate(False)
f4.columnconfigure(0, weight=1)
f4.columnconfigure(1, weight=1)
f4.rowconfigure(1, weight=1)
f4.rowconfigure(2, weight=1)
f4Label = Label(f4, text='Electric')
f4Button1 = Button(f4, text='PC', padx=40, command=toggle_pc)
f4Button2 = Button(f4, text='Audio', command=toggle_audio)
f4Button3 = Button(f4, text='RGB LED I', command=toggle_rgb1)
f4Button4 = Button(f4, text='RGB LED II', command=toggle_rgb2)
f4Label.grid(row=0, column=0, columnspan=2)
f4Button1.grid(row=1, column=0, sticky='nsew')
f4Button2.grid(row=1, column=1, sticky='nsew')
f4Button3.grid(row=2, column=0, sticky='nsew')
f4Button4.grid(row=2, column=1, sticky='nsew')

f5 = Frame(window, width=160, height=200, borderwidth=1, relief=GROOVE)
f5.grid_propagate(False)
f5.columnconfigure(0, weight=1)
f5.columnconfigure(1, weight=1)
f5.rowconfigure(0, weight=1)
f5.rowconfigure(1, weight=1)
f5.rowconfigure(2, weight=1)
f5.rowconfigure(3, weight=1)
f5.rowconfigure(4, weight=2)
f5.rowconfigure(5, weight=2)
f5.rowconfigure(6, weight=1)
f5.rowconfigure(7, weight=1)
f5.rowconfigure(8, weight=0)
f5Label1 = Label(f5, text='OFF', anchor=CENTER, bg='red', width=3)
f5Label2 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Label3 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Label4 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Label5 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Label6 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Label7 = Label(f5, text='OFF', anchor=CENTER, bg='red')
f5Button1 = Button(f5, text='PC', relief='flat', command=toggle_pc)
f5Button2 = Button(f5, text='Audio', relief='flat', command=toggle_audio)
f5Button3 = Button(f5, text='RGB LED I', relief='flat', command=toggle_rgb1)
f5Button4 = Button(f5, text='RGB LED II', relief='flat', command=toggle_rgb2)
f5Button5 = Button(f5, text='Main light', relief='flat', command=toggle_main_light)
f5Button6 = Button(f5, text='RGB Seat', relief='flat', command=toggle_seat_rgb)
f5Button7 = Button(f5, text='RGB Bed', relief='flat', command=toggle_bed_rgb)
f5Button8 = Button(f5, text='Minimize', relief='flat', font=('Arial', 6), command=root.iconify)
f5Label1.grid(row=0, column=1, sticky='nsew')
f5Label2.grid(row=1, column=1, sticky='nsew')
f5Label3.grid(row=2, column=1, sticky='nsew')
f5Label4.grid(row=3, column=1, sticky='nsew')
f5Label5.grid(row=4, column=1, rowspan=2, sticky='nsew')
f5Label6.grid(row=6, column=1, sticky='nsew')
f5Label7.grid(row=7, column=1, sticky='nsew')
f5Button1.grid(row=0, column=0, sticky='nsew')
f5Button2.grid(row=1, column=0, sticky='nsew')
f5Button3.grid(row=2, column=0, sticky='nsew')
f5Button4.grid(row=3, column=0, sticky='nsew')
f5Button5.grid(row=4, column=0, rowspan=2, sticky='nsew')
f5Button6.grid(row=6, column=0, sticky='nsew')
f5Button7.grid(row=7, column=0, sticky='nsew')
f5Button8.grid(row=8, column=0, columnspan=2, sticky='nsew')

window.grid(row=0, column=0, sticky='nsew')
f1.grid(row=0, column=0, sticky='nsew')
f2.grid(row=1, column=0, sticky='nsew')
f3.grid(row=0, column=1, rowspan=2, sticky='nsew')
f4.grid(row=2, column=0, sticky='nsew')
f5.grid(row=2, column=1, sticky='nsew')

update_ui_sec()
update_ui_hrs()
root.mainloop()