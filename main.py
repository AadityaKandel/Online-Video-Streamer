from tkinter import *
import os as o
import tkinter.messagebox as tmsg

root = Tk()

root.title('Online YouTube Video Streamer By Aaditya Kandel')


def entrychanger(this_is_nothing):
    if (url.get())=="Eg: https://www.youtube.com/watch?v=2Vv-BfVoq4g":
        en1.config(state=NORMAL)
        url.set('')
    else:
        url.set((url.get()))
        en1.config(state=NORMAL)

def entryexiter(this_is_nothing):
    en1.config(state=DISABLED)
    if (url.get())=="":
        url.set('Eg: https://www.youtube.com/watch?v=2Vv-BfVoq4g')
    else:
        url.set((url.get()))

def starter():

    try:
        o.system('start vlc ' + (final.get()))
        o.system('cls')
    except:
        o.system('C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe ' + (final.get()))
        o.system('cls')

def first():
    b = (url.get())[0:13]
    c = (url.get())[17:9999]

    final.set(b+'be.com'+'/embed/'+c)

def second():
    bb = (url.get())[0:24]
    cc = (url.get())[32:999]

    final.set(bb+'embed/'+cc)


def vlcwatch():
    final.set((url.get())[4:9999])

    try:

        if 'youtu.be' in (url.get()):
            first()
            starter()
        elif 'channel' in (url.get()):
            warner()
        elif 'Eg' in (url.get()):
            starter()
        else:
            second()
            starter()
    except:

        tmsg.showwarning('Warning','VLC Is Not Found In This System')

def htmlwatch():

    if 'youtu.be' in (url.get()):
        first()
    elif 'channel' in (url.get()):
        warner()
    elif 'Eg' in (url.get()):
        final.set('https://www.youtube.com/embed/2Vv-BfVoq4g')
    else:
        second()
    fornoerror = "background-color: "

    f = open('watch-Video.html','w+')
    a = '''
<!DOCTYPE html>
<html>
<head>
	<title>
		AK's Yt Video Watch
	</title>
</head>

<style type="text/css">
	
	body{
		background-color: #3997c1;
		text-align: center;
	}

</style>

<body>

	<br><br><br><br><br>

'''
    b = f'''
<iframe src="{(final.get())}" allowfullscreen width="711" height="400" frameborder="0">
	
</iframe>

</body>
</html>'''

    f.write(a+b)
    f.close()

    o.startfile('watch-Video.html')

def warner():
    tmsg._show('HELP', 'Hey, Youtube Has Many Different Links And This One Is Not Supported\n\
                \nSo If Your Link Is Like: \nhttps://www.youtube.com/watch?v=2Vv-BfVoq4g&ab_channel=EdSheeran\n\
                \nThen Just Remove &ab_channel="CHANNEL NAME" And Provide Here This Link\n\
                    https://www.youtube.com/watch?v=2Vv-BfVoq4g')

url = StringVar()
url.set('Eg: https://www.youtube.com/watch?v=2Vv-BfVoq4g')

final = StringVar()

f1 = Frame(borderwidth=10,bg="black")
f2 = Frame(borderwidth=10,bg="black")

Label(f1,text="YouTube Url: ",bg="black",fg="white",font="comicsansms 15 italic").pack(side=LEFT)
en1 = Entry(f1,textvariable=url,bg="white",fg="black",font="comicsansms 14 bold",width=47,state=DISABLED)

en1.bind('<Enter>',entrychanger)
en1.bind('<Leave>',entryexiter)

en1.pack(side=LEFT)

b1 = Button(f2,text="Watch On Vlc",bg="black",fg="white",font="comicsansms 15 italic",borderwidth=2,relief=SUNKEN,padx=10,pady=10,command=vlcwatch)
b1.pack(side=LEFT)

Label(f2,text="       ",bg="black").pack(side=LEFT)

b2 = Button(f2,text="Watch On HTML",bg="black",fg="white",font="comicsansms 15 italic",borderwidth=2,relief=SUNKEN,padx=10,pady=10,command=htmlwatch)
b2.pack(side=LEFT)

f1.pack(anchor=W)
f2.pack(anchor=W)

root.config(bg="black")
root.mainloop()