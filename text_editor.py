from guizero import TextBox,App,Box,PushButton,Slider,Combo,MenuBar,warn
app=App(title="Text editor",width=850,height=700)
def open_file():
    with open(file_name.value,"r") as f:
        editor.value=f.read()
def save_file():
    with open(file_name.value,"w") as f:
        f.write(editor.value)
    save_button.disable()
    save_button.hide()
def save_enable():
    save_button.enable()
    save_button.show()
def change_size():
    editor.text_size=size.value
    editor.resize(1, 1)
    editor.resize("fill", "fill")
def change_font():
    editor.font=font.value
def exit():
    if save_button.enabled==True:
        warn("Warning","Your document is not saved")
    else:
        app.destroy()
menubar=MenuBar(app,
                toplevel=["File"],
                options=[[["open",open_file],["save",save_file],["exit",exit]]])
file_box=Box(app,align="top",width="fill")
file_name=TextBox(file_box,text="text_file.txt",width=50,align="left")
save_button=PushButton(file_box,text="SAVE",align="right",command=save_file)
save_button.hide()
save_button.disable()
open_button=PushButton(file_box,text="OPEN",align="right",command=open_file)
editor=TextBox(app,height="fill",width="fill",multiline=True,command=save_enable)
func_box=Box(app,align="bottom",width="fill",border=True)
font = Combo(func_box, options=["courier", "times new roman", "verdana"], align="left", command=change_font)
size=Slider(func_box,command=change_size)

app.display()