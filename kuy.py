import customtkinter

app = customtkinter.CTk()
app.title('บวกเลขโง่ๆ')
app.geometry('500*500')

#ข้อความเเสดงผล
label = customtkinter.CTkLabel(app, text='Plus Stuff', font=('Nawabiat',40))
label.pack(pady=(20,0))

#ข้อความเเสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text ,font=('Nawabiat', 40))
answer_label.pack(pady=(20, 0))

#กล่องค่ารับinput
entry = customtkinter.CTkEntry(app, placeholder_text='ใส่ input ของคุณตรงนี้')
entry.pack(pady=(15, 0))

#ปุ่มโง่ๆ
def button_event():
    user_input=entry.get()
    answer = eval(user_input)
    answer_text.set(answer)
    print(user_input, answer)

button = customtkinter.CTkButton(app, text='กดซะไอ้โง่', command=button_event)
button.pack(pady=(20,0))

app.mainloop()