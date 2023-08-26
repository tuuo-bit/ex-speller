#imports
import tkinter as tk
import ttkbootstrap as tb
import itertools

#functions
def script():
      with open( "word_list.txt", "r") as file:
            store=[]
            letters=[ entry0.get(), entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get()]
            central_letter=letters[ 0].upper()
            other_letters="".join( letters[ 1:]).upper()
            subject=central_letter+other_letters
            if len( subject)+sum( map( lambda x: int( x.isalpha()), letters))==14:
                  word_list=set( file.readlines())
                  for word_length in range( 4, 8):
                              for permutation in set( itertools.permutations( subject , word_length)):
                                    word_maybe="".join( permutation)
                                    if central_letter in word_maybe and word_maybe+"\n" in word_list:
                                          store.append( word_maybe)
                  output.set( "\t".join( store))

def is_valid_entry( data):
      if ( data.isalpha() and len( data)==1) or data=="":
            return True
      else:
            return False

#window
win=tb.Window()
win.title( "ex-speller")
win.geometry( "900x900+450+25")
win.configure( bg="#AEC1AE")
validator=win.register( is_valid_entry)
#input frame
border=tb.Frame( master=win, height=412.5, width=850, bootstyle="dark")
border.place( x=25, y=25)
#input frame 2
input_frame=tb.Frame( master=border, height=382.5, width=820, bootstyle="light")
input_frame.place( x=15, y=15)
#input entry
entry0=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry0.place( x=395, y=176.25, height=60, width=60)
entry1=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry1.place( x=395, y=96.25, height=60, width=60)
entry2=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry2.place( x=395, y=256.25, height=60, width=60)
entry3=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry3.place( x=315, y=136.25, height=60, width=60)
entry4=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry4.place( x=315, y=216.25, height=60, width=60)
entry5=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry5.place( x=475, y=136.25, height=60, width=60)
entry6=tb.Entry( master=border, textvariable=tk.StringVar(), font="Bahnschrift 18", validate="focus", validatecommand=( validator, "%P"), bootstyle="dark")
entry6.place( x=475, y=216.25, height=60, width=60)
#input heading
tb.Label( master=border, text="INPUT ", font="Bahnschrift 18 bold", bootstyle="inverse-dark").place( x=5, y=365)
#button
button=tb.Button( master=input_frame, text="ex-spell !?", command=script, bootstyle="secondary-outline")
button.place( x=805, y=368.5, height=50, width=125, anchor="se")
#output frame
output_frame=tb.Frame( master=win, height=412.5, width=850, bootstyle="dark")
output_frame.place( x=25, y=462.5)
#output 
output=tk.StringVar()
output_label=tb.Label( master=output_frame, font="Bahnschrift 18", textvariable=output, wraplength=800, justify="left", padding=10, bootstyle="inverse-light")
output_label.place( x=15, y=15, height=382.5, width=820)
#output heading
tb.Label( master=output_frame, text="OUTPUT ", font="Bahnschrift 18 bold", bootstyle="inverse-dark").place( x=5, y=365)
#window loop
win.mainloop()
