import customtkinter as kc
from time import strftime
import qrcode as qrs

App = kc.CTk()
App.after(0, lambda: App.state("zoomed"))
App.grid_columnconfigure(0, weight=1)
App.grid_rowconfigure(0, weight=1)

opciones_conversion = ["C -> F",
                       "C -> K",
                       "F -> C",
                       "F -> K",
                       "K -> C",
                       "K -> F"
                       
                       ]
opciones_tiempo = [
    "Seg -> Min",
    "Min -> Seg",
    "Min -> Horas",
    "Horas -> Min",
    "Horas -> Días",
    "Días -> Horas",
]

def limpiar_pantalla():
    
    for widget in Aplicacion_prueba.winfo_children():
        
        if widget != Label_Resultado and widget != Label_Image:
            widget.destroy()
            
   
    Label_Image.configure(image="")
    Label_Image.image = None
    
    
    Label_Resultado.configure(text="")
def Matriz():
    limpiar_pantalla()
    Columnas = int(columnas_entry.get())
    Filas = int(Filas_entry.get())
    frame_entries_matriz = kc.CTkFrame(
        Aplicacion_prueba, width=200, height=200, fg_color="transparent"
    )
    frame_entries_matriz.grid(row=0, column=0)
    
    for c in range(Columnas):
        for f in range(Filas):
            Matriz = kc.CTkEntry(frame_entries_matriz
                ,
                width=10,
                height=10,
                placeholder_text="",
                font=("comic sans",20,"bold"),
                border_width=1,
                corner_radius=2,
                fg_color="#04A404",
                border_color="#008F11",
                text_color="#00FF41",
                justify="center",
            )
            Matriz.grid(row=f, column=c, padx=1, pady=1)
            
def crearQR(event=None):
    limpiar_pantalla()
    Qr_DATA = str(Entry_QR.get())
    qr = qrs.QRCode(
        version=1, error_correction=qrs.constants.ERROR_CORRECT_M, border=4, box_size=4
    )

    qr.add_data(Qr_DATA)
    qr.make(fit=True)
    qr_img_forPil = qr.make_image(fill_color="#aaaaaa", back_color="#ffffff").convert(
        "RGB"
    )

    Imagen_QR = kc.CTkImage(
        light_image=qr_img_forPil, dark_image=qr_img_forPil, size=(200, 200)
    )
    Label_Image.configure(image=Imagen_QR)
    Label_Image.image = Imagen_QR
    Entry_QR.delete(0, "end")


def tiempo(valor):
    try:
        Tiempo = float(Entry_Tiempo.get())

    except ValueError:

        return
    if valor == "Seg -> Min":
        resultado = Tiempo / 60
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Min")
    if valor == "Min -> Seg":
        resultado = Tiempo * 60
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Seg")
    if valor == "Min -> Horas":
        resultado = Tiempo / 60
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Hrs")
    if valor == "Horas -> Min":
        resultado = Tiempo * 60
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Min")
    if valor == "Horas -> Días":
        resultado = Tiempo / 24
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Días")
    if valor == "Días -> Horas":
        resultado = Tiempo * 24
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} Hrs")

    Entry_Tiempo.delete(0, "end")


def Temperaturas(valor):
    try:
        Temperatura = float(Entry_Temperatura.get())
    except ValueError:

        return

    if valor == "C -> F":
        resultado = (Temperatura * 9 / 5) + 32
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} F°")
    if valor == "C -> K":
        resultado = Temperatura + 273.15
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} K°")
    if valor == "F -> C":
        resultado = (Temperatura - 32) * 5 / 9
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} C°")
    if valor == "F -> K":
        resultado = (Temperatura - 32) * 5 / 9 + 273.15
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} K°")
    if valor == "K -> C":
        resultado = Temperatura - 273.15
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} C°")
    if valor == "K -> F":
        resultado = (Temperatura - 273.15) * 9 / 5 + 32
        resultado_r = round(resultado, 2)
        Label_Resultado.configure(text=f"{resultado_r} F°")

    Entry_Temperatura.delete(0, "end")


def actualizar_hora():
    hora_actual = strftime("%H:%M:%S%p")
    label_hora.configure(text=hora_actual)
    label_hora.after(1000, actualizar_hora)


def escape():
    App.destroy()


Frame_Tablet = kc.CTkFrame(
    App,
    width=400,
    height=700,
    corner_radius=20,
    border_width=5,
    border_color="#000000",
)
Frame_Tablet.grid(row=0, column=0)
Frame_Tablet.grid_propagate(False)
Frame_Tablet.grid_columnconfigure(0, weight=1)
Frame_Tablet.grid_rowconfigure(0, weight=1)

Frame_camera = kc.CTkFrame(
    Frame_Tablet,
    width=380,
    height=30,
)
Frame_camera.grid(row=0, column=0, sticky="n", pady=7, padx=2)
Frame_camera.grid_propagate(False)

Camara_Object = kc.CTkFrame(
    Frame_camera,
    width=50,
    height=20,
    border_width=2,
    border_color="#000000",
)
Camara_Object.place(relx=0.5, rely=0.5, anchor="center")

circulo_camara = kc.CTkFrame(
    Camara_Object,
    width=20,
    height=10,
    corner_radius=20,
    fg_color="#000000",
)
circulo_camara.place(relx=0.5, rely=0.5, anchor="center")

label_hora = kc.CTkLabel(
    Frame_camera,
    text="",
    font=("Arial", 15, "bold"),
    text_color="#FFFFFF",
)
label_hora.grid(row=0, column=0, sticky="w")

Frame_Aplicaciones = kc.CTkFrame(
    Frame_Tablet,
    width=380,
    height=400,
)
Frame_Aplicaciones.grid(row=0, column=0, pady=(0, 100))
Frame_Aplicaciones.grid_propagate(False)
Frame_Aplicaciones.grid_columnconfigure(0, weight=1)
Frame_Aplicaciones.grid_rowconfigure(0, weight=1)

Aplicacion_prueba = kc.CTkFrame(
    Frame_Aplicaciones,
    width=340,
    height=340,
    corner_radius=25,
    fg_color="#252525",
    border_width=2,
    border_color="#333333",
)
Aplicacion_prueba.grid(row=0, column=0, pady=20, padx=20)
Aplicacion_prueba.grid_propagate(False)
Aplicacion_prueba.grid_columnconfigure(0, weight=1)
Aplicacion_prueba.grid_rowconfigure(0, weight=1)


Label_Resultado = kc.CTkLabel(
    Aplicacion_prueba,
    text="",
    font=("comic sans", 40, "bold"),
)
Label_Resultado.place(relx=0.5, rely=0.5, anchor="center")

frame_botons_down = kc.CTkFrame(
    Frame_Tablet,
    width=385,
    height=30,
)
frame_botons_down.grid(row=2, column=0, sticky="s", pady=(0, 7))
frame_botons_down.grid_propagate(False)

Boton_salir_app = kc.CTkButton(
    frame_botons_down,
    width=100,
    height=20,
    corner_radius=10,
    text="",
    fg_color="#000000",
    hover_color="#272525",
    command=escape,
)
Boton_salir_app.place(relx=0.5, rely=0.5, anchor="center")

Opciones_Tab = kc.CTkTabview(
    Frame_Tablet,
    width=380,
    height=130,
    segmented_button_fg_color="#1E1E1E",
    segmented_button_selected_color="#3A3A3C",
    segmented_button_selected_hover_color="#48484A",
    segmented_button_unselected_color="#1E1E1E",
    segmented_button_unselected_hover_color="#2C2C2E",
    text_color="#FFFFFF",
    text_color_disabled="#8E8E93",command=limpiar_pantalla
)
Opciones_Tab.grid(row=0, column=0, sticky="s", pady=(0, 45))
Opciones_Tab.add("Temperaturas").grid_columnconfigure(0, weight=1)
Opciones_Tab.add("Tiempo").grid_columnconfigure(0, weight=1)
Opciones_Tab.add("QR").grid_columnconfigure(0, weight=1)
Opciones_Tab.add("Matriz").grid_columnconfigure(0, weight=1)

Filas_entry = kc.CTkEntry(Opciones_Tab.tab("Matriz"), placeholder_text="Filas")
Filas_entry.grid(row=0, column=0)

columnas_entry = kc.CTkEntry(Opciones_Tab.tab("Matriz"), placeholder_text="Columnas")
columnas_entry.grid(row=1, column=0, pady=(10, 0))

Boton_Matriz = kc.CTkButton(
    Opciones_Tab.tab("Matriz"),
    text="Generar",
    fg_color="#aaaaaa",
    hover_color="#6f6a6a",
    command=Matriz,
)
Boton_Matriz.grid(row=0, column=1, padx=(0, 10))
Lista_temperaturas = kc.CTkOptionMenu(
    Opciones_Tab.tab("Temperaturas"),
    values=opciones_conversion,
    width=100,
    height=20,
    corner_radius=15,
    fg_color="#2B2B2B",
    button_color="#1F1F1F",
    button_hover_color="#333333",
    dropdown_fg_color="#1F1F1F",
    dropdown_hover_color="#3A3A3A",
    dropdown_text_color="#FFFFFF",
    font=("Helvetica", 14, "bold"),
    dropdown_font=("Helvetica", 12),
    command=Temperaturas,
)
Lista_temperaturas.set("Seleccionar conversión")
Lista_temperaturas.grid(row=0, column=0)

frame_entry = kc.CTkFrame(
    Opciones_Tab.tab("Temperaturas"),
    width=200,
    height=120,
    fg_color="transparent",
)
frame_entry.grid(row=0, column=1)

Entry_Temperatura = kc.CTkEntry(
    frame_entry,
    placeholder_text="Temperatura: ",
)
Entry_Temperatura.grid(row=0, column=0, padx=(20, 0))
Entry_Temperatura.bind("<Return>", lambda e: Temperaturas(Lista_temperaturas.get()))

actualizar_hora()
Lista_Tiempos = kc.CTkOptionMenu(
    Opciones_Tab.tab("Tiempo"),
    values=opciones_tiempo,
    width=100,
    height=20,
    corner_radius=15,
    fg_color="#2B2B2B",
    button_color="#1F1F1F",
    button_hover_color="#333333",
    dropdown_fg_color="#1F1F1F",
    dropdown_hover_color="#3A3A3A",
    dropdown_text_color="#FFFFFF",
    font=("Helvetica", 14, "bold"),
    dropdown_font=("Helvetica", 12),
    
)
Lista_Tiempos.set("Seleccionar conversión")
Lista_Tiempos.grid(row=0, column=0)

frame_entry_2 = kc.CTkFrame(
    Opciones_Tab.tab("Tiempo"),
    width=200,
    height=120,
    fg_color="transparent",
)
frame_entry_2.grid(row=0, column=1)

Entry_Tiempo = kc.CTkEntry(
    frame_entry_2,
    placeholder_text="Tiempo: ",
)
Entry_Tiempo.grid(row=0, column=0, padx=(20, 0))
Entry_Tiempo.bind("<Return>", lambda e: tiempo(Lista_Tiempos.get()))

Entry_QR = kc.CTkEntry(Opciones_Tab.tab("QR"), placeholder_text="Ingresa:" " ")
Entry_QR.grid(row=0, column=0)
Boton_crear_qr = kc.CTkButton(
    Opciones_Tab.tab("QR"),
    text="Generar",
    fg_color="#aaaaaa",
    hover_color="#6f6a6a",
    command=crearQR,
)
Boton_crear_qr.grid(row=1, column=0, pady=(10, 0))
Label_Image = kc.CTkLabel(
    Aplicacion_prueba,
    text="",
)
Label_Image.grid(row=0, column=0)

App.mainloop()
