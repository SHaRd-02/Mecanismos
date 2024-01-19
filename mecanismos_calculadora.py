from tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox
import math
#from pitagoras import TrianguloRectanguloCalculator

# importando librerias necesarias


# creando clase
class Mecanismos:
    # creando constructor para inicializar la clase
    def __init__(self):
        # definiendo la ventana principal y sus parametros
        self.root = ttk.Window(themename="darkly")
        self.root.title("Calculadora de Mecanismos de 4 barras")
        self.root.geometry("500x400")

        # Creando variables de los resultados

        # Variables de los resultados del mecanismo de 4 barras simple
        self.k1 = None
        self.k2 = None
        self.k3 = None
        self.k4 = None
        self.k5 = 0

        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.F = 0

        self.teta4_1 = 0
        self.teta4_2 = 0
        self.teta3_1 = 0
        self.teta3_2 = 0

        self.omega_3 = 0
        self.omega_4 = 0
        self.va = 0
        self.vab = 0
        self.vb = 0

        self.A2 = 0
        self.B2 = 0
        self.C2 = 0
        self.D2 = 0
        self.E2 = 0
        self.F2 = 0
        self.alfa_3 = 0
        self.alfa_4 = 0
        self.aA = 0
        self.aAB = 0
        self.aB = 0

        # Variables de los resultados del mecanismo MBC

        # Creando labels de la ventana principal
        label_titulo = ttk.Label(
            master=self.root,
            text="Calculadora de mecanismos \n                   de 4 barras",
            font="Calibri 24 bold",
        )
        label_titulo.pack(padx=10, pady=10)

        ttk.Label(
            master=self.root,
            text="Seleccione qué tipo de mecanismo desea calcular",
            font="Calibri 12",
        ).pack(padx=10, pady=10)

        # Creando botones para elegir el tipo de mecanismo
        boton_simple = ttk.Button(
            master=self.root, text="Mecanismo simple", command=self.simple_window
        )
        boton_simple.pack(padx=10, pady=10)

        boton_descentrado = ttk.Button(
            master=self.root,
            text="Mecanismo descentrado",
            command=self.descentrado_window,
        )
        boton_descentrado.pack(padx=10, pady=10)

        boton_desface = ttk.Button(
            master=self.root, text="Mecanismo en desface", command=self.desface_window
        )
        boton_desface.pack(padx=10, pady=10)

        # Inicializando el programa
        self.root.mainloop()

    def calculo_simple(self):
        self.convertir_1()
        self.teta_2_rad = math.radians(self.teta_2)
        self.k1 = self.d / self.a
        self.k2 = self.d / self.c
        self.k3 = (
            self.a * self.a - self.b * self.b + self.c * self.c + self.d * self.d
        ) / (2.0 * self.a * self.c)
        self.k4 = self.d / self.b
        self.k5 = (
            self.c * self.c - self.d * self.d - self.a * self.a - self.b * self.b
        ) / (2.0 * self.a * self.b)

        self.A = (
            math.cos(self.teta_2_rad)
            - self.k1
            - self.k2 * math.cos(self.teta_2_rad)
            + self.k3
        )
        self.B = -2.0 * math.sin(self.teta_2_rad)
        self.C = self.k1 - (self.k2 + 1.0) * math.cos(self.teta_2_rad) + self.k3
        self.D = (
            math.cos(self.teta_2_rad)
            - self.k1
            + self.k4 * math.cos(self.teta_2_rad)
            + self.k5
        )
        self.E = -2.0 * math.sin(self.teta_2_rad)
        self.F = self.k1 + (self.k4 - 1.0) * math.cos(self.teta_2_rad) + self.k5

        self.teta4_1 = math.degrees(
            2.0
            * math.atan(
                (-self.B - math.sqrt(self.B * self.B - 4.0 * self.A * self.C))
                / (2.0 * self.A)
            )
        )
        self.teta4_2 = math.degrees(
            2.0
            * math.atan(
                (-self.B + math.sqrt(self.B * self.B - 4.0 * self.A * self.C))
                / (2.0 * self.A)
            )
        )

        self.teta3_1 = math.degrees(
            2.0
            * math.atan(
                (-1.0 * self.E - math.sqrt(self.E * self.E - 4.0 * self.D * self.F))
                / (2.0 * self.D)
            )
        )
        self.teta3_2 = math.degrees(
            2.0
            * math.atan(
                (-1.0 * self.E + math.sqrt(self.E * self.E - 4.0 * self.D * self.F))
                / (2.0 * self.D)
            )
        )

        self.teta3_1_rad = math.radians(self.teta3_1)
        self.teta3_2_rad = math.radians(self.teta3_2)
        self.teta4_1_rad = math.radians(self.teta4_1)
        self.teta4_2_rad = math.radians(self.teta4_2)

        self.omega_3 = ((self.a * self.omega2) / (self.b)) * (
            (math.sin(self.teta4_1_rad - self.teta_2_rad))
            / (math.sin(self.teta3_1_rad - self.teta4_1_rad))
        )
        self.omega_4 = ((self.a * self.omega2) / (self.c)) * (
            (math.sin(self.teta_2_rad - self.teta3_1_rad))
            / (math.sin(self.teta4_1_rad - self.teta3_1_rad))
        )

        self.vai = (self.a * self.omega2) * (-math.sin(self.teta_2_rad))
        self.vaj = (self.a * self.omega2) * (math.cos(self.teta_2_rad))

        self.tauva = math.degrees(math.atan(self.vaj / self.vai))

        if self.vai > 0 and self.vaj > 0:
            self.gradosva = self.tauva
        elif self.vai < 0 and self.vaj > 0:
            self.gradosva = self.tauva + 180
        elif self.vai < 0 and self.vaj < 0:
            self.gradosva = self.tauva + 180
        elif self.vai > 0 and self.vaj < 0:
            self.gradosva = self.tauva + 360

        self.va = math.sqrt((self.vai) ** 2 + (self.vaj) ** 2)

        self.vabi = (self.b * self.omega_3) * (-math.sin(self.teta3_1_rad))
        self.vabj = (self.b * self.omega_3) * (math.cos(self.teta3_1_rad))
        self.vab = math.sqrt((self.vabi) ** 2 + (self.vabj) ** 2)

        self.vbi = (self.c * self.omega_4) * (-math.sin(self.teta4_1_rad))
        self.vbj = (self.c * self.omega_4) * (math.cos(self.teta4_1_rad))

        self.tauvb = math.degrees(math.atan(self.vbj / self.vbi))
        if self.vbi > 0 and self.vbj > 0:
            self.gradosvb = self.tauvb
        elif self.vbi < 0 and self.vbj > 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi < 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi > 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 360

        self.vb = math.sqrt((self.vbi) ** 2 + (self.vbj) ** 2)

        self.A2 = self.c * math.sin(self.teta4_1_rad)

        self.B2 = self.b * math.sin(self.teta3_1_rad)

        self.C2 = (
            (self.a * self.alfa2 * math.sin(self.teta_2_rad))
            + (self.a * ((self.omega2) ** 2) * math.cos(self.teta_2_rad))
            + (self.b * (self.omega_3) ** 2 * math.cos(self.teta3_1_rad))
            - (self.c * (self.omega_4) ** 2 * math.cos(self.teta4_1_rad))
        )

        self.D2 = self.c * math.cos(self.teta4_1_rad)

        self.E2 = self.b * math.cos(self.teta3_1_rad)

        self.F2 = (
            (self.a * self.alfa2 * math.cos(self.teta_2_rad))
            - (self.a * (self.omega2) ** 2 * math.sin(self.teta_2_rad))
            - (self.b * (self.omega_3) ** 2 * math.sin(self.teta3_1_rad))
            + (self.c * (self.omega_4) ** 2 * math.sin(self.teta4_1_rad))
        )

        self.alfa_3 = ((self.C2) * (self.D2) - (self.A2) * (self.F2)) / (
            (self.A2) * (self.E2) - (self.B2) * (self.D2)
        )

        self.alfa_4 = ((self.C2) * (self.E2) - (self.B2) * (self.F2)) / (
            (self.A2) * (self.E2) - (self.B2) * (self.D2)
        )

        self.aAi = (self.a * self.alfa2 * -math.sin(self.teta_2_rad)) - (
            self.a * (self.omega2) ** 2 * math.cos(self.teta_2_rad)
        )
        self.aAj = (self.a * self.alfa2 * math.cos(self.teta_2_rad)) - (
            self.a * (self.omega2) ** 2 * math.sin(self.teta_2_rad)
        )
        self.tauaA = math.degrees(math.atan(self.aAj / self.aAi))
        if self.aAi > 0 and self.aAj > 0:
            self.gradosaA = self.tauaA
        elif self.aAi < 0 and self.aAj > 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi < 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi > 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 360

        self.aA = math.sqrt((self.aAi) ** 2 + (self.aAj) ** 2)

        self.aABi = (self.b * self.alfa_3 * -math.sin(self.teta3_1_rad)) - (
            self.b * (self.omega_3) ** 2 * math.cos(self.teta3_1_rad)
        )
        self.aABj = (self.b * self.alfa_3 * math.cos(self.teta3_1_rad)) - (
            self.b * (self.omega_3) ** 2 * math.sin(self.teta3_1_rad)
        )
        self.aAB = math.sqrt((self.aABi) ** 2 + (self.aABj) ** 2)

        self.aBi = (self.c * self.alfa_4 * -math.sin(self.teta4_1_rad)) - (
            self.c * (self.omega_4) ** 2 * math.cos(self.teta4_1_rad)
        )
        self.aBj = (self.c * self.alfa_4 * math.cos(self.teta4_1_rad)) - (
            self.c * (self.omega_4) ** 2 * math.sin(self.teta4_1_rad)
        )
        self.tauaB = math.degrees(math.atan(self.aBj / self.aBi))
        if self.aBi > 0 and self.aBj > 0:
            self.gradosaB = self.tauaB
        elif self.aBi < 0 and self.aBj > 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi < 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi > 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 360

        self.aB = math.sqrt((self.aBi) ** 2 + (self.aBj) ** 2)

        print(
            f" k1 = { self.k1} k2 = {self.k2} k3 = {self.k3} k4 = {self.k4} k5 = {self.k5}"
        )

        self.k1_entry.insert(0, str(self.k1))
        self.k1_entry["state"] = "readonly"

        self.k2_entry.insert(0, str(self.k2))
        self.k2_entry["state"] = "readonly"

        self.k3_entry.insert(0, str(self.k3))
        self.k3_entry["state"] = "readonly"

        self.k4_entry.insert(0, str(self.k4))
        self.k4_entry["state"] = "readonly"

        self.k5_entry.insert(0, str(self.k5))
        self.k5_entry["state"] = "readonly"

        self.A_entry.insert(0, str(self.A))
        self.A_entry["state"] = "readonly"

        self.B_entry.insert(0, str(self.B))
        self.B_entry["state"] = "readonly"

        self.C_entry.insert(0, str(self.C))
        self.C_entry["state"] = "readonly"

        self.D_entry.insert(0, str(self.D))
        self.D_entry["state"] = "readonly"

        self.E_entry.insert(0, str(self.E))
        self.E_entry["state"] = "readonly"

        self.F_entry.insert(0, str(self.F))
        self.F_entry["state"] = "readonly"

        self.teta3_1_entry.insert(0, str(self.teta3_2 + 180))
        self.teta3_1_entry["state"] = "readonly"

        self.teta3_2_entry.insert(0, str(self.teta3_1))
        self.teta3_2_entry["state"] = "readonly"

        self.teta4_1_entry.insert(0, str(self.teta4_1))
        self.teta4_1_entry["state"] = "readonly"

        self.teta4_2_entry.insert(0, str(self.teta4_2))
        self.teta4_2_entry["state"] = "readonly"

        self.omega3_entry.insert(0, str(self.omega_3))
        self.omega3_entry["state"] = "readonly"

        self.omega4_entry.insert(0, str(self.omega_4))
        self.omega4_entry["state"] = "readonly"

        self.va_entry.insert(0, str(self.va))
        self.va_entry["state"] = "readonly"

        self.vab_entry.insert(0, str(self.vab))
        self.vab_entry["state"] = "readonly"

        self.vb_entry.insert(0, str(self.vb))
        self.vb_entry["state"] = "readonly"

        self.alfa_3_entry.insert(0, str(self.alfa_3))
        self.alfa_3_entry["state"] = "readonly"

        self.alfa_4_entry.insert(0, str(self.alfa_4))
        self.alfa_4_entry["state"] = "readonly"

        self.aA_entry.insert(0, str(self.aA))
        self.aA_entry["state"] = "readonly"

        self.aAB_entry.insert(0, str(self.aAB))
        self.aAB_entry["state"] = "readonly"

        self.aB_entry.insert(0, str(self.aB))
        self.aB_entry["state"] = "readonly"

        self.A2_entry.insert(0, str(self.A2))
        self.A2_entry["state"] = "readonly"

        self.B2_entry.insert(0, str(self.B2))
        self.B2_entry["state"] = "readonly"

        self.C2_entry.insert(0, str(self.C2))
        self.C2_entry["state"] = "readonly"

        self.D2_entry.insert(0, str(self.D2))
        self.D2_entry["state"] = "readonly"

        self.E2_entry.insert(0, str(self.E2))
        self.E2_entry["state"] = "readonly"

        self.F2_entry.insert(0, str(self.F2))
        self.F2_entry["state"] = "readonly"

        self.alfa_3_entry.insert(0, str(self.alfa_3))
        self.alfa_3_entry["state"] = "readonly"

        self.alfa_4_entry.insert(0, str(self.alfa_4))
        self.alfa_4_entry["state"] = "readonly"

        self.aA_entry.insert(0, str(self.aA))
        self.aA_entry["state"] = "readonly"

        self.aAB_entry.insert(0, str(self.aAB))
        self.aAB_entry["state"] = "readonly"

        self.aB_entry.insert(0, str(self.aB))
        self.aB_entry["state"] = "readonly"

        self.gradosva_entry.insert(0, str(self.gradosva))
        self.gradosva_entry["state"] = "readonly"

        self.gradosvb_entry.insert(0, str(self.gradosvb))
        self.gradosvb_entry["state"] = "readonly"

        self.gradosaA_entry.insert(0, str(self.gradosaA))
        self.gradosaA_entry["state"] = "readonly"

        self.gradosaB_entry.insert(0, str(self.gradosaB))
        self.gradosaB_entry["state"] = "readonly"

    def calculo_simple_lc(self):
        self.convertir_1_2()
        self.teta_2_rad = math.radians(self.teta_2)
        self.k1 = self.d / self.a
        self.k2 = self.d / self.c
        self.k3 = (
            self.a * self.a - self.b * self.b + self.c * self.c + self.d * self.d
        ) / (2.0 * self.a * self.c)
        self.k4 = self.d / self.b
        self.k5 = (
            self.c * self.c - self.d * self.d - self.a * self.a - self.b * self.b
        ) / (2.0 * self.a * self.b)

        self.A = (
            math.cos(self.teta_2_rad)
            - self.k1
            - self.k2 * math.cos(self.teta_2_rad)
            + self.k3
        )
        self.B = -2.0 * math.sin(self.teta_2_rad)
        self.C = self.k1 - (self.k2 + 1.0) * math.cos(self.teta_2_rad) + self.k3
        self.D = (
            math.cos(self.teta_2_rad)
            - self.k1
            + self.k4 * math.cos(self.teta_2_rad)
            + self.k5
        )
        self.E = -2.0 * math.sin(self.teta_2_rad)
        self.F = self.k1 + (self.k4 - 1.0) * math.cos(self.teta_2_rad) + self.k5

        self.teta4_1 = math.degrees(
            2.0
            * math.atan(
                (-self.B - math.sqrt(self.B * self.B - 4.0 * self.A * self.C))
                / (2.0 * self.A)
            )
        )
        self.teta4_2 = math.degrees(
            2.0
            * math.atan(
                (-self.B + math.sqrt(self.B * self.B - 4.0 * self.A * self.C))
                / (2.0 * self.A)
            )
        )

        self.teta3_1 = math.degrees(
            2.0
            * math.atan(
                (-1.0 * self.E - math.sqrt(self.E * self.E - 4.0 * self.D * self.F))
                / (2.0 * self.D)
            )
        )
        self.teta3_2 = math.degrees(
            2.0
            * math.atan(
                (-1.0 * self.E + math.sqrt(self.E * self.E - 4.0 * self.D * self.F))
                / (2.0 * self.D)
            )
        )

        self.teta3_1_rad = math.radians(self.teta3_1)
        self.teta3_2_rad = math.radians(self.teta3_2)
        self.teta4_1_rad = math.radians(self.teta4_1)
        self.teta4_2_rad = math.radians(self.teta4_2)

        self.omega_3 = ((self.a * self.omega2) / (self.b)) * (
            (math.sin(self.teta4_2_rad - self.teta_2_rad))
            / (math.sin(self.teta3_2_rad - self.teta4_2_rad))
        )
        self.omega_4 = ((self.a * self.omega2) / (self.c)) * (
            (math.sin(self.teta_2_rad - self.teta3_2_rad))
            / (math.sin(self.teta4_2_rad - self.teta3_2_rad))
        )

        self.vai = (self.a * self.omega2) * (-math.sin(self.teta_2_rad))
        self.vaj = (self.a * self.omega2) * (math.cos(self.teta_2_rad))

        self.tauva = math.degrees(math.atan(self.vaj / self.vai))

        if self.vai > 0 and self.vaj > 0:
            self.gradosva = self.tauva
        elif self.vai < 0 and self.vaj > 0:
            self.gradosva = self.tauva + 180
        elif self.vai < 0 and self.vaj < 0:
            self.gradosva = self.tauva + 180
        elif self.vai > 0 and self.vaj < 0:
            self.gradosva = self.tauva + 360

        self.va = math.sqrt((self.vai) ** 2 + (self.vaj) ** 2)

        self.vabi = (self.b * self.omega_3) * (-math.sin(self.teta3_2_rad))
        self.vabj = (self.b * self.omega_3) * (math.cos(self.teta3_2_rad))
        self.vab = math.sqrt((self.vabi) ** 2 + (self.vabj) ** 2)

        self.vbi = (self.c * self.omega_4) * (-math.sin(self.teta4_2_rad))
        self.vbj = (self.c * self.omega_4) * (math.cos(self.teta4_2_rad))

        self.tauvb = math.degrees(math.atan(self.vbj / self.vbi))
        if self.vbi > 0 and self.vbj > 0:
            self.gradosvb = self.tauvb
        elif self.vbi < 0 and self.vbj > 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi < 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi > 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 360

        self.vb = math.sqrt((self.vbi) ** 2 + (self.vbj) ** 2)

        self.A2 = self.c * math.sin(self.teta4_2_rad)

        self.B2 = self.b * math.sin(self.teta3_2_rad)

        self.C2 = (
            (self.a * self.alfa2 * math.sin(self.teta_2_rad))
            + (self.a * ((self.omega2) ** 2) * math.cos(self.teta_2_rad))
            + (self.b * (self.omega_3) ** 2 * math.cos(self.teta3_2_rad))
            - (self.c * (self.omega_4) ** 2 * math.cos(self.teta4_2_rad))
        )

        self.D2 = self.c * math.cos(self.teta4_2_rad)

        self.E2 = self.b * math.cos(self.teta3_2_rad)

        self.F2 = (
            (self.a * self.alfa2 * math.cos(self.teta_2_rad))
            - (self.a * (self.omega2) ** 2 * math.sin(self.teta_2_rad))
            - (self.b * (self.omega_3) ** 2 * math.sin(self.teta3_2_rad))
            + (self.c * (self.omega_4) ** 2 * math.sin(self.teta4_2_rad))
        )

        self.alfa_3 = ((self.C2) * (self.D2) - (self.A2) * (self.F2)) / (
            (self.A2) * (self.E2) - (self.B2) * (self.D2)
        )

        self.alfa_4 = ((self.C2) * (self.E2) - (self.B2) * (self.F2)) / (
            (self.A2) * (self.E2) - (self.B2) * (self.D2)
        )

        self.aAi = (self.a * self.alfa2 * -math.sin(self.teta_2_rad)) - (
            self.a * (self.omega2) ** 2 * math.cos(self.teta_2_rad)
        )
        self.aAj = (self.a * self.alfa2 * math.cos(self.teta_2_rad)) - (
            self.a * (self.omega2) ** 2 * math.sin(self.teta_2_rad)
        )
        self.tauaA = math.degrees(math.atan(self.aAj / self.aAi))
        if self.aAi > 0 and self.aAj > 0:
            self.gradosaA = self.tauaA
        elif self.aAi < 0 and self.aAj > 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi < 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi > 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 360

        self.aA = math.sqrt((self.aAi) ** 2 + (self.aAj) ** 2)

        self.aABi = (self.b * self.alfa_3 * -math.sin(self.teta3_2_rad)) - (
            self.b * (self.omega_3) ** 2 * math.cos(self.teta3_2_rad)
        )
        self.aABj = (self.b * self.alfa_3 * math.cos(self.teta3_2_rad)) - (
            self.b * (self.omega_3) ** 2 * math.sin(self.teta3_2_rad)
        )
        self.aAB = math.sqrt((self.aABi) ** 2 + (self.aABj) ** 2)

        self.aBi = (self.c * self.alfa_4 * -math.sin(self.teta4_2_rad)) - (
            self.c * (self.omega_4) ** 2 * math.cos(self.teta4_2_rad)
        )
        self.aBj = (self.c * self.alfa_4 * math.cos(self.teta4_2_rad)) - (
            self.c * (self.omega_4) ** 2 * math.sin(self.teta4_2_rad)
        )
        self.tauaB = math.degrees(math.atan(self.aBj / self.aBi))
        if self.aBi > 0 and self.aBj > 0:
            self.gradosaB = self.tauaB
        elif self.aBi < 0 and self.aBj > 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi < 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi > 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 360

        self.aB = math.sqrt((self.aBi) ** 2 + (self.aBj) ** 2)

        print(
            f" k1 = { self.k1} k2 = {self.k2} k3 = {self.k3} k4 = {self.k4} k5 = {self.k5}"
        )

        self.k1_entry.insert(0, str(self.k1))
        self.k1_entry["state"] = "readonly"

        self.k2_entry.insert(0, str(self.k2))
        self.k2_entry["state"] = "readonly"

        self.k3_entry.insert(0, str(self.k3))
        self.k3_entry["state"] = "readonly"

        self.k4_entry.insert(0, str(self.k4))
        self.k4_entry["state"] = "readonly"

        self.k5_entry.insert(0, str(self.k5))
        self.k5_entry["state"] = "readonly"

        self.A_entry.insert(0, str(self.A))
        self.A_entry["state"] = "readonly"

        self.B_entry.insert(0, str(self.B))
        self.B_entry["state"] = "readonly"

        self.C_entry.insert(0, str(self.C))
        self.C_entry["state"] = "readonly"

        self.D_entry.insert(0, str(self.D))
        self.D_entry["state"] = "readonly"

        self.E_entry.insert(0, str(self.E))
        self.E_entry["state"] = "readonly"

        self.F_entry.insert(0, str(self.F))
        self.F_entry["state"] = "readonly"

        self.teta3_1_entry.insert(0, str(self.teta3_2 + 180))
        self.teta3_1_entry["state"] = "readonly"

        self.teta3_2_entry.insert(0, str(self.teta3_1))
        self.teta3_2_entry["state"] = "readonly"

        self.teta4_1_entry.insert(0, str(self.teta4_1))
        self.teta4_1_entry["state"] = "readonly"

        self.teta4_2_entry.insert(0, str(self.teta4_2))
        self.teta4_2_entry["state"] = "readonly"

        self.omega3_entry.insert(0, str(self.omega_3))
        self.omega3_entry["state"] = "readonly"

        self.omega4_entry.insert(0, str(self.omega_4))
        self.omega4_entry["state"] = "readonly"

        self.va_entry.insert(0, str(self.va))
        self.va_entry["state"] = "readonly"

        self.vab_entry.insert(0, str(self.vab))
        self.vab_entry["state"] = "readonly"

        self.vb_entry.insert(0, str(self.vb))
        self.vb_entry["state"] = "readonly"

        self.alfa_3_entry.insert(0, str(self.alfa_3))
        self.alfa_3_entry["state"] = "readonly"

        self.alfa_4_entry.insert(0, str(self.alfa_4))
        self.alfa_4_entry["state"] = "readonly"

        self.aA_entry.insert(0, str(self.aA))
        self.aA_entry["state"] = "readonly"

        self.aAB_entry.insert(0, str(self.aAB))
        self.aAB_entry["state"] = "readonly"

        self.aB_entry.insert(0, str(self.aB))
        self.aB_entry["state"] = "readonly"

        self.A2_entry.insert(0, str(self.A2))
        self.A2_entry["state"] = "readonly"

        self.B2_entry.insert(0, str(self.B2))
        self.B2_entry["state"] = "readonly"

        self.C2_entry.insert(0, str(self.C2))
        self.C2_entry["state"] = "readonly"

        self.D2_entry.insert(0, str(self.D2))
        self.D2_entry["state"] = "readonly"

        self.E2_entry.insert(0, str(self.E2))
        self.E2_entry["state"] = "readonly"

        self.F2_entry.insert(0, str(self.F2))
        self.F2_entry["state"] = "readonly"

        self.alfa_3_entry.insert(0, str(self.alfa_3))
        self.alfa_3_entry["state"] = "readonly"

        self.alfa_4_entry.insert(0, str(self.alfa_4))
        self.alfa_4_entry["state"] = "readonly"

        self.aA_entry.insert(0, str(self.aA))
        self.aA_entry["state"] = "readonly"

        self.aAB_entry.insert(0, str(self.aAB))
        self.aAB_entry["state"] = "readonly"

        self.aB_entry.insert(0, str(self.aB))
        self.aB_entry["state"] = "readonly"

        self.gradosva_entry.insert(0, str(self.gradosva))
        self.gradosva_entry["state"] = "readonly"

        self.gradosvb_entry.insert(0, str(self.gradosvb))
        self.gradosvb_entry["state"] = "readonly"

        self.gradosaA_entry.insert(0, str(self.gradosaA))
        self.gradosaA_entry["state"] = "readonly"

        self.gradosaB_entry.insert(0, str(self.gradosaB))
        self.gradosaB_entry["state"] = "readonly"

    # Funcion para calcular mecanismo en desface
    def calculo_desface(self):
        self.convertir_2()

        self.teta2_rad = math.radians(self.teta2)
        self.teta1_rad = math.radians(self.teta1)

        self.A = (
            2
            * self.d
            * (
                (self.a * math.cos(self.teta1_rad))
                - ((self.b * math.cos(self.teta2_rad)))
            )
        )
        self.B = (
            2
            * self.d
            * (
                (self.a * math.sin(self.teta1_rad))
                - ((self.b * math.sin(self.teta2_rad)))
            )
        )
        self.C = (
            (self.a) ** 2
            + (self.b) ** 2
            - (self.c) ** 2
            + (self.d) ** 2
            - (2 * self.a * self.b * math.cos(self.teta1_rad - self.teta2_rad))
        )
        self.D = (
            2
            * self.c
            * (
                (self.b * math.cos(self.teta2_rad))
                - ((self.a * math.cos(self.teta1_rad)))
            )
        )
        self.E = (
            2
            * self.c
            * (
                (self.b * math.sin(self.teta2_rad))
                - ((self.a * math.sin(self.teta1_rad)))
            )
        )
        self.F = (
            (self.a) ** 2
            + (self.b) ** 2
            + (self.c) ** 2
            - (self.d) ** 2
            - (2 * self.a * self.b * math.cos(self.teta2_rad - self.teta1_rad))
        )

        self.teta4_1 = math.degrees(
            2
            * math.atan(
                (-self.B + math.sqrt((self.A) ** 2 + (self.B) ** 2 - (self.C) ** 2))
                / (self.C - self.A)
            )
        )
        self.teta4_2 = math.degrees(
            2
            * math.atan(
                (-self.B - math.sqrt((self.A) ** 2 + (self.B) ** 2 - (self.C) ** 2))
                / (self.C - self.A)
            )
        )
        self.teta3_1 = math.degrees(
            2
            * math.atan(
                (-self.E + math.sqrt((self.D) ** 2 + (self.E) ** 2 - (self.F) ** 2))
                / (self.F - self.D)
            )
        )
        self.teta3_2 = math.degrees(
            2
            * math.atan(
                (-self.E - math.sqrt((self.D) ** 2 + (self.E) ** 2 - (self.F) ** 2))
                / (self.F - self.D)
            )
        )

        self.teta3_1_rad = math.radians(self.teta3_1)
        self.teta4_2_rad = math.radians(self.teta4_2)
        self.teta3_2_rad = math.radians(self.teta3_2)
        self.teta4_1_rad = math.radians(self.teta4_1)

        self.omega3 = (
            self.omega2 * self.b * math.sin(self.teta4_2_rad - self.teta2_rad)
        ) / (self.c * math.sin(self.teta3_1_rad - self.teta4_2_rad))
        self.omega4 = (
            self.omega2 * self.b * math.sin(self.teta2_rad - self.teta3_1_rad)
        ) / (self.d * math.sin(self.teta4_2_rad - self.teta3_1_rad))

        self.vai = (self.b * self.omega2) * (-math.sin(self.teta2_rad))
        self.vaj = (self.b * self.omega2) * (math.cos(self.teta2_rad))
        self.va = math.sqrt((self.vai) ** 2 + (self.vaj) ** 2)

        self.tauva = math.degrees(math.atan(self.vaj / self.vai))
        if self.vai > 0 and self.vaj > 0:
            self.gradosva = self.tauva
        elif self.vai < 0 and self.vaj > 0:
            self.gradosva = self.tauva + 180
        elif self.vai < 0 and self.vaj < 0:
            self.gradosva = self.tauva + 180
        elif self.vai > 0 and self.vaj < 0:
            self.gradosva = self.tauva + 360

        self.vabi = (self.c * self.omega3) * (-math.sin(self.teta3_1_rad))
        self.vabj = (self.c * self.omega3) * (math.cos(self.teta3_1_rad))
        self.vab = math.sqrt((self.vabi) ** 2 + (self.vabj) ** 2)

        self.vbi = (self.d * self.omega4) * (-math.sin(self.teta4_2_rad))
        self.vbj = (self.d * self.omega4) * (math.cos(self.teta4_2_rad))
        self.vb = math.sqrt((self.vbi) ** 2 + (self.vbj) ** 2)
        print(self.vbj, self.vbi)
        self.tauvb = math.degrees(math.atan(self.vbj / self.vbi))
        if self.vbi > 0 and self.vbj > 0:
            self.gradosvb = self.tauvb
        elif self.vbi < 0 and self.vbj > 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi < 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 180
        elif self.vbi > 0 and self.vbj < 0:
            self.gradosvb = self.tauvb + 360

        self.alfa_3 = (
            ((self.omega4) ** 2 * self.d)
            - (
                (self.omega2) ** 2
                * self.b
                * math.cos(self.teta2_rad - self.teta4_2_rad)
            )
            - (self.alfa2 * self.b * math.sin(self.teta2_rad - self.teta4_2_rad))
            - (
                (self.omega3) ** 2
                * (self.c)
                * math.cos(self.teta3_1_rad - self.teta4_2_rad)
            )
        ) / (self.c * math.sin(self.teta3_1_rad - self.teta4_2_rad))
        self.alfa_4 = (
            ((self.omega3) ** 2 * self.c)
            + (
                (self.omega2) ** 2
                * self.b
                * math.cos(self.teta2_rad - self.teta3_1_rad)
            )
            + (self.alfa2 * self.b * math.sin(self.teta2_rad - self.teta3_1_rad))
            - (
                (self.omega4) ** 2
                * (self.d)
                * math.cos(self.teta4_2_rad - self.teta3_1_rad)
            )
        ) / (self.d * math.sin(self.teta4_2_rad - self.teta3_1_rad))

        self.aAi = (self.b * self.alfa2 * -math.sin(self.teta2_rad)) - (
            self.b * (self.omega2) ** 2 * math.cos(self.teta2_rad)
        )
        self.aAj = (self.b * self.alfa2 * math.cos(self.teta2_rad)) - (
            self.b * (self.omega2) ** 2 * math.sin(self.teta2_rad)
        )
        self.tauaA = math.degrees(math.atan(self.aAj / self.aAi))
        if self.aAi > 0 and self.aAj > 0:
            self.gradosaA = self.tauaA
        elif self.aAi < 0 and self.aAj > 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi < 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 180
        elif self.aAi > 0 and self.aAj < 0:
            self.gradosaA = self.tauaA + 360

        self.aA = math.sqrt((self.aAi) ** 2 + (self.aAj) ** 2)

        self.aABi = (self.c * self.alfa_3 * -math.sin(self.teta3_1_rad)) - (
            self.c * (self.omega_3) ** 2 * math.cos(self.teta3_1_rad)
        )
        self.aABj = (self.c * self.alfa_3 * math.cos(self.teta3_1_rad)) - (
            self.c * (self.omega_3) ** 2 * math.sin(self.teta3_1_rad)
        )
        self.aAB = math.sqrt((self.aABi) ** 2 + (self.aABj) ** 2)

        self.aBi = (self.d * self.alfa_4 * -math.sin(self.teta4_2_rad)) - (
            self.d * (self.omega_4) ** 2 * math.cos(self.teta4_2_rad)
        )
        self.aBj = (self.d * self.alfa_4 * math.cos(self.teta4_2_rad)) - (
            self.d * (self.omega_4) ** 2 * math.sin(self.teta4_2_rad)
        )
        self.tauaB = math.degrees(math.atan(self.aBj / self.aBi))
        if self.aBi > 0 and self.aBj > 0:
            self.gradosaB = self.tauaB
        elif self.aBi < 0 and self.aBj > 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi < 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 180
        elif self.aBi > 0 and self.aBj < 0:
            self.gradosaB = self.tauaB + 360

        self.aB = math.sqrt((self.aBi) ** 2 + (self.aBj) ** 2)

        self.A_entry.insert(0, str(self.A))
        self.A_entry["state"] = "readonly"

        self.B_entry.insert(0, str(self.B))
        self.B_entry["state"] = "readonly"

        self.C_entry.insert(0, str(self.C))
        self.C_entry["state"] = "readonly"

        self.D_entry.insert(0, str(self.D))
        self.D_entry["state"] = "readonly"

        self.E_entry.insert(0, str(self.E))
        self.E_entry["state"] = "readonly"

        self.F_entry.insert(0, str(self.F))
        self.F_entry["state"] = "readonly"

        self.teta4_1_entry.insert(0, str(self.teta4_1))
        self.teta4_1_entry["state"] = "readonly"

        self.teta4_2_entry.insert(0, str(self.teta4_2))
        self.teta4_2_entry["state"] = "readonly"

        self.teta3_1_entry.insert(0, str(self.teta3_1))
        self.teta3_1_entry["state"] = "readonly"

        self.teta3_2_entry.insert(0, str(self.teta3_2))
        self.teta3_2_entry["state"] = "readonly"

        self.omega3_entry.insert(0, str(self.omega3))
        self.omega3_entry["state"] = "readonly"

        self.omega4_entry.insert(0, str(self.omega4))
        self.omega4_entry["state"] = "readonly"

        self.alfa_3_entry.insert(0, str(self.alfa_3))
        self.alfa_3_entry["state"] = "readonly"

        self.alfa_4_entry.insert(0, str(self.alfa_4))
        self.alfa_4_entry["state"] = "readonly"

        self.va_entry.insert(0, str(self.va))
        self.va_entry["state"] = "readonly"

        self.vab_entry.insert(0, str(self.vab))
        self.vab_entry["state"] = "readonly"

        self.vb_entry.insert(0, str(self.vb))
        self.vb_entry["state"] = "readonly"

        self.aA_entry.insert(0, str(self.aA))
        self.aA_entry["state"] = "readonly"

        self.aAB_entry.insert(0, str(self.aAB))
        self.aAB_entry["state"] = "readonly"

        self.aB_entry.insert(0, str(self.aB))
        self.aB_entry["state"] = "readonly"

        self.gradosva_entry.insert(0, str(self.gradosva))
        self.gradosva_entry["state"] = "readonly"

        self.gradosvb_entry.insert(0, str(self.gradosvb))
        self.gradosvb_entry["state"] = "readonly"

        self.gradosaA_entry.insert(0, str(self.gradosaA))
        self.gradosaA_entry["state"] = "readonly"

        self.gradosaB_entry.insert(0, str(self.gradosaB))
        self.gradosaB_entry["state"] = "readonly"

    # Funcion para calcular mecanismo descentrado
    def calculo_descentrado(self):
        self.convertir_3()

        self.teta1 = self.teta4 - 90

        self.teta4_rad = math.radians(self.teta4)
        self.teta2_rad = math.radians(self.teta2)
        self.G = self.r3 * math.sin(self.teta4_rad)
        self.H = -self.r3 * math.cos(self.teta4_rad)
        self.I = -self.r1 - self.r2 * math.sin(self.teta2_rad - self.teta4_rad)
        self.J = 1
        self.K = -2 * self.r2 * math.cos(self.teta2_rad - self.teta4_rad)
        self.L = (
            (2 * self.r1 * self.r2 * math.sin(self.teta2_rad - self.teta4_rad))
            + (self.r1) ** 2
            + (self.r2) ** 2
            - (self.r3) ** 2
        )

        self.teta3 = math.degrees(
            2
            * math.atan(
                (-self.H - math.sqrt((self.G) ** 2 + (self.H) ** 2 - (self.I) ** 2))
                / (self.I - self.G)
            )
        )

        self.r4 = 0.5 * (-self.K + math.sqrt((self.K) ** 2 - 4 * (self.L)))

        self.teta3_rad = math.radians(self.teta3)

        self.v4 = (
            self.omega2 * self.r2 * self.sin(self.teta3_rad - self.teta2_rad)
        ) / (math.cos(self.teta4_rad - self.teta3_rad))

        self.omega3 = (
            -self.omega2 * self.r2 * math.cos(self.teta2_rad - self.teta4_rad)
        ) / (self.r3 * math.cos(self.teta3_rad - self.teta4_rad))

        self.alfa_3 = (
            ((self.omega3) ** 2 * self.r3 * math.sin(self.teta3_rad - self.teta4_rad))
            + ((self.omega2) ** 2 * self.r2 * math.sin(self.teta2_rad - self.teta4_rad))
            - (self.alfa2 * self.r2 * math.cos(self.teta2_rad - self.teta4_rad))
        ) / (self.r3 * math.cos(self.teta3_rad - self.teta4_rad))

        self.alfa_4 = (
            (self.alfa2 * self.r2 * math.sin(self.teta3_rad - self.teta2_rad))
            - ((self.omega2) ** 2 * self.r2 * math.cos(self.teta2_rad - self.teta3_rad))
            - ((self.omega3) ** 2 * self.r3)
        ) / (math.cos(self.teta4_rad - self.teta3_rad))

        self.teta3_1_entry.insert(0, str(self.teta3_2))
        self.teta3_1_entry["state"] = "readonly"

        self.teta3_2_entry.insert(0, str(self.teta3_1 + 180))
        self.teta3_2_entry["state"] = "readonly"

        self.teta4_1_entry.insert(0, str(self.teta4_1))
        self.teta4_1_entry["state"] = "readonly"

        self.teta4_2_entry.insert(0, str(self.teta4_2))
        self.teta4_2_entry["state"] = "readonly"

        print(f"A = {self.A} B = {self.B} C = {self.C}")

    # Funcion que obtiene los valores de todos los entrys mecanismo simple
    def obtener_valores(self):
        self.a_text = self.a_entry.get()
        self.b_text = self.b_entry.get()
        self.c_text = self.c_entry.get()
        self.d_text = self.d_entry.get()
        self.teta2_text = self.teta2_entry.get()
        self.omega2_text = self.omega2_entry.get()
        self.alfa2_text = self.alfa2_entry.get()

    # Funcion que obtiene los valores de todos los entrys mecanismo desface
    def obtener_valores_desface(self):
        self.a_text = self.a_entry.get()
        self.b_text = self.b_entry.get()
        self.c_text = self.c_entry.get()
        self.d_text = self.d_entry.get()
        self.teta2_text = self.teta2_entry.get()
        self.teta1_text = self.teta1_entry.get()
        self.omega2_text = self.omega2_entry.get()
        self.alfa2_text = self.alfa2_entry.get()

    # Funcion que obtiene los valores de todos los entrys mecanismo biela-corredera en descentrado
    def obtener_valores_descentrado(self):
        self.r1_text = self.r1_entry.get()
        self.r2_text = self.r2_entry.get()
        self.r3_text = self.r3_entry.get()
        self.teta2_text = self.teta2_entry.get()
        self.teta4_text = self.teta4_entry.get()
        self.omega2_text = self.omega2_entry.get()
        self.alfa2_text = self.alfa2_entry.get()

    # Funcion para mostrar los resultados
    def convertir_1(self):
        self.obtener_valores()
        # validacion para que no haya valores faltantes
        if (
            self.a_text
            and self.b_text
            and self.c_text
            and self.d_text
            and self.teta2_text
            and self.omega2_text
            and self.alfa2_text != ""
        ):
            self.a = float(self.a_text)
            self.b = float(self.b_text)
            self.c = float(self.c_text)
            self.d = float(self.d_text)
            self.teta_2 = float(self.teta2_text)
            self.omega2 = float(self.omega2_text)
            self.alfa2 = float(self.alfa2_text)

            # manda a llamar al a funcion que despliega el resultado
            # antes de eso tambien agregar funcion para hacer el calculo
            self.resultados_simple()
        else:
            #
            messagebox.showerror("Error", "Ningun campo puede quedar vacio!!!")

        # print(f"[{self.a} {self.b} {self.c} {self.d} {self.teta} {self.omega} {self.alfa}]")

    def convertir_1_2(self):
        self.obtener_valores()
        # validacion para que no haya valores faltantes
        if (
            self.a_text
            and self.b_text
            and self.c_text
            and self.d_text
            and self.teta2_text
            and self.omega2_text
            and self.alfa2_text != ""
        ):
            self.a = float(self.a_text)
            self.b = float(self.b_text)
            self.c = float(self.c_text)
            self.d = float(self.d_text)
            self.teta_2 = float(self.teta2_text)
            self.omega2 = float(self.omega2_text)
            self.alfa2 = float(self.alfa2_text)

            # manda a llamar al a funcion que despliega el resultado
            # antes de eso tambien agregar funcion para hacer el calculo
            self.resultados_simple_lc()
        else:
            #
            messagebox.showerror("Error", "Ningun campo puede quedar vacio!!!")

        # print(f"[{self.a} {self.b} {self.c} {self.d} {self.teta} {self.omega} {self.alfa}]")

    # Funcion para convertir los valores de entrada de mecanismo en desface a flotantes
    def convertir_2(self):
        self.obtener_valores_desface()
        if (
            self.a_text
            and self.b_text
            and self.c_text
            and self.d_text
            and self.teta1_text
            and self.teta2_text
            and self.omega2_text
            and self.alfa2_text != ""
        ):
            self.a = float(self.a_text)
            self.b = float(self.b_text)
            self.c = float(self.c_text)
            self.d = float(self.d_text)
            self.teta1 = float(self.teta1_text)
            self.teta2 = float(self.teta2_text)
            self.omega2 = float(self.omega2_text)
            self.alfa2 = float(self.alfa2_text)

            # manda a llamar al a funcion que despliega el resultado
            # antes de eso tambien agregar funcion para hacer el calculo
            self.resultados_desface()
        else:
            #
            messagebox.showerror("Error", "Ningun campo puede quedar vacio!!!")

        # Funcion para convertir los valores de entrada de mecanismo en desface a flotantes

    def convertir_3(self):
        self.obtener_valores_descentrado()
        if (
            self.r1_text
            and self.r2_text
            and self.r3_text
            and self.teta2_text
            and self.teta4_text
            and self.omega2_text
            and self.alfa2_text != ""
        ):
            self.r1 = float(self.r1_text)
            self.r2 = float(self.r2_text)
            self.r3 = float(self.r3_text)
            self.teta_4 = float(self.teta4_text)
            self.teta_2 = float(self.teta2_text)
            self.omega2 = float(self.omega2_text)
            self.alfa2 = float(self.alfa2_text)

            # manda a llamar al a funcion que despliega el resultado
            # antes de eso tambien agregar funcion para hacer el calculo
            self.resultados_descentrado()
        else:
            #
            messagebox.showerror("Error", "Ningun campo puede quedar vacio!!!")

    # funcion para ingresar los valores para el mecanismo simple
    def simple_window(self):
        # Creando ventana del mecanismo simple
        ventana_1 = ttk.Toplevel()
        ventana_1.title("Mecanismo simple")
        ventana_1.geometry("400x600")
        # Creando y desplegando labels y entrys para ingresar los datos
        a_label = ttk.Label(master=ventana_1, text="Ingrese el valor de a")
        a_label.pack(padx=5, pady=5)

        self.a_entry = ttk.Entry(master=ventana_1)
        self.a_entry.pack(padx=5, pady=5)
        self.a_entry.focus()

        b_label = ttk.Label(master=ventana_1, text="Ingrese el valor de b")
        b_label.pack(padx=5, pady=5)

        self.b_entry = ttk.Entry(master=ventana_1)
        self.b_entry.pack(padx=5, pady=5)

        c_label = ttk.Label(master=ventana_1, text="Ingrese el valor de c")
        c_label.pack(padx=5, pady=5)

        self.c_entry = ttk.Entry(master=ventana_1)
        self.c_entry.pack(padx=5, pady=5)

        d_label = ttk.Label(master=ventana_1, text="Ingrese el valor de d")
        d_label.pack(padx=5, pady=5)

        self.d_entry = ttk.Entry(master=ventana_1)
        self.d_entry.pack(padx=5, pady=5)

        teta2_label = ttk.Label(master=ventana_1, text="Ingrese el valor de θ 2")
        teta2_label.pack(padx=5, pady=5)

        self.teta2_entry = ttk.Entry(master=ventana_1)
        self.teta2_entry.pack(padx=5, pady=5)

        omega2_label = ttk.Label(master=ventana_1, text="Ingrese el valor de ω 2")
        omega2_label.pack(padx=5, pady=5)

        self.omega2_entry = ttk.Entry(master=ventana_1)
        self.omega2_entry.pack(padx=5, pady=5)

        alfa2_label = ttk.Label(master=ventana_1, text="Ingrese el valor de α 2")
        alfa2_label.pack(padx=5, pady=5)

        self.alfa2_entry = ttk.Entry(master=ventana_1)
        self.alfa2_entry.pack(padx=5, pady=5)

        # Creando boton que obtiene los valores de los entry para lazo abierto
        self.calcular_simple = ttk.Button(
            master=ventana_1, text="Calcular Lazo Abierto", command=self.calculo_simple
        )
        self.calcular_simple.pack(padx=10, pady=10)

        # Creando boton que obtiene los valores de los entry para lazo abierto
        self.calcular_simple_lc = ttk.Button(
            master=ventana_1,
            text="Calcular Lazo Cerrado",
            command=self.calculo_simple_lc,
        )
        self.calcular_simple_lc.pack(padx=10, pady=10)

    # Creando ventana para desplegar los resultados del mecanismo simple
    def resultados_simple(self):
        self.obtener_valores()
        resultados_2 = ttk.Toplevel()
        resultados_2.title("Resultados Mecanismo Simples (Lazo Abierto)")
        resultados_2.geometry("1200x900")

        self.obtener_valores()
        print(f"[{self.a} {self.b} {self.c} {self.d} {self.teta_2} ]")

        ttk.Label(master=resultados_2, text="Posicion:", font="Calibri 20 bold").place(
            x=340, y=20
        )
        # k-----------------------------------------------------------------------------------
        self.k1_label = ttk.Label(master=resultados_2, text="k1: ")
        self.k1_label.place(x=30, y=70)
        self.k1_entry = ttk.Entry(master=resultados_2)
        self.k1_entry.place(x=70, y=70)
        # usar el metodo insert() para insertar el resultado en el entry
        # recordar modificar todos los entry despues para que despliegue el resultado correcto
        # self.k1_entry.insert(0, str(self.k1))
        # self.k1_entry["state"] = "readonly"

        self.k2_label = ttk.Label(master=resultados_2, text="k2: ")
        self.k2_label.place(x=30, y=110)
        self.k2_entry = ttk.Entry(master=resultados_2)
        self.k2_entry.place(x=70, y=110)
        # self.k2_entry.insert(0, str(self.k2))
        # self.k2_entry["state"] = "readonly"

        self.k3_label = ttk.Label(master=resultados_2, text="k3: ")
        self.k3_label.place(x=30, y=150)
        self.k3_entry = ttk.Entry(master=resultados_2)
        self.k3_entry.place(x=70, y=150)
        # self.k3_entry.insert(0, str(self.k3))
        # self.k3_entry["state"] = "readonly"

        self.k4_label = ttk.Label(master=resultados_2, text="k4: ")
        self.k4_label.place(x=30, y=190)
        self.k4_entry = ttk.Entry(master=resultados_2)
        self.k4_entry.place(x=70, y=190)
        # self.k4_entry.insert(0, str(self.k4))
        # self.k4_entry["state"] = "readonly"

        self.k5_label = ttk.Label(master=resultados_2, text="k5: ")
        self.k5_label.place(x=30, y=230)
        self.k5_entry = ttk.Entry(master=resultados_2)
        self.k5_entry.place(x=70, y=230)
        # self.k5_entry.insert(0, str(self.k5))
        # self.k5_entry["state"] = "readonly"

        # ----------------------------------------------------

        self.A_label = ttk.Label(master=resultados_2, text="A: ")
        self.A_label.place(x=400, y=70)
        self.A_entry = ttk.Entry(master=resultados_2)
        self.A_entry.place(x=440, y=70)

        self.B_label = ttk.Label(master=resultados_2, text="B: ")
        self.B_label.place(x=400, y=110)
        self.B_entry = ttk.Entry(master=resultados_2)
        self.B_entry.place(x=440, y=110)

        self.C_label = ttk.Label(master=resultados_2, text="C: ")
        self.C_label.place(x=400, y=150)
        self.C_entry = ttk.Entry(master=resultados_2)
        self.C_entry.place(x=440, y=150)

        self.D_label = ttk.Label(master=resultados_2, text="D: ")
        self.D_label.place(x=400, y=190)
        self.D_entry = ttk.Entry(master=resultados_2)
        self.D_entry.place(x=440, y=190)

        self.E_label = ttk.Label(master=resultados_2, text="E: ")
        self.E_label.place(x=400, y=230)
        self.E_entry = ttk.Entry(master=resultados_2)
        self.E_entry.place(x=440, y=230)

        self.F_label = ttk.Label(master=resultados_2, text="F: ")
        self.F_label.place(x=400, y=270)
        self.F_entry = ttk.Entry(master=resultados_2)
        self.F_entry.place(x=440, y=270)

        # ----------------------------------------------------------------------------

        self.teta4_1_label = ttk.Label(master=resultados_2, text="θ4(1): ")
        self.teta4_1_label.place(x=30, y=350)
        self.teta4_1_entry = ttk.Entry(master=resultados_2)
        self.teta4_1_entry.place(x=90, y=350)

        self.teta4_2_label = ttk.Label(master=resultados_2, text="θ4(2): ")
        self.teta4_2_label.place(x=30, y=390)
        self.teta4_2_entry = ttk.Entry(master=resultados_2)
        self.teta4_2_entry.place(x=90, y=390)

        self.teta3_1_label = ttk.Label(master=resultados_2, text="θ3(1): ")
        self.teta3_1_label.place(x=400, y=350)
        self.teta3_1_entry = ttk.Entry(master=resultados_2)
        self.teta3_1_entry.place(x=460, y=350)

        self.teta3_2_label = ttk.Label(master=resultados_2, text="θ3(2): ")
        self.teta3_2_label.place(x=400, y=390)
        self.teta3_2_entry = ttk.Entry(master=resultados_2)
        self.teta3_2_entry.place(x=460, y=390)

        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        ttk.Label(master=resultados_2, text="Velocidad:", font="Calibri 20 bold").place(
            x=340, y=435
        )
        self.omega3_label = ttk.Label(master=resultados_2, text="ω3: ")
        self.omega3_label.place(x=30, y=490)
        self.omega3_entry = ttk.Entry(master=resultados_2)
        self.omega3_entry.place(x=70, y=490)

        self.omega4_label = ttk.Label(master=resultados_2, text="ω4: ")
        self.omega4_label.place(x=30, y=530)
        self.omega4_entry = ttk.Entry(master=resultados_2)
        self.omega4_entry.place(x=70, y=530)

        self.va_label = ttk.Label(master=resultados_2, text="VA: ")
        self.va_label.place(x=400, y=490)
        self.va_entry = ttk.Entry(master=resultados_2)
        self.va_entry.place(x=460, y=490)

        self.gradosva_label = ttk.Label(master=resultados_2, text="∡vA: ")
        self.gradosva_label.place(x=400, y=530)
        self.gradosva_entry = ttk.Entry(master=resultados_2)
        self.gradosva_entry.place(x=460, y=530)

        self.vb_label = ttk.Label(master=resultados_2, text="VB: ")
        self.vb_label.place(x=400, y=570)
        self.vb_entry = ttk.Entry(master=resultados_2)
        self.vb_entry.place(x=460, y=570)

        self.gradosvb_label = ttk.Label(master=resultados_2, text="∡vB: ")
        self.gradosvb_label.place(x=400, y=610)
        self.gradosvb_entry = ttk.Entry(master=resultados_2)
        self.gradosvb_entry.place(x=460, y=610)

        self.vab_label = ttk.Label(master=resultados_2, text="VA/B: ")
        self.vab_label.place(x=400, y=650)
        self.vab_entry = ttk.Entry(master=resultados_2)
        self.vab_entry.place(x=460, y=650)

        ttk.Label(
            master=resultados_2, text="Aceleracion:", font="Calibri 20 bold"
        ).place(x=800, y=10)

        self.A2_label = ttk.Label(master=resultados_2, text="A: ")
        self.A2_label.place(x=800, y=70)
        self.A2_entry = ttk.Entry(master=resultados_2)
        self.A2_entry.place(x=840, y=70)

        self.B2_label = ttk.Label(master=resultados_2, text="B: ")
        self.B2_label.place(x=800, y=110)
        self.B2_entry = ttk.Entry(master=resultados_2)
        self.B2_entry.place(x=840, y=110)

        self.C2_label = ttk.Label(master=resultados_2, text="C: ")
        self.C2_label.place(x=800, y=150)
        self.C2_entry = ttk.Entry(master=resultados_2)
        self.C2_entry.place(x=840, y=150)

        self.D2_label = ttk.Label(master=resultados_2, text="D: ")
        self.D2_label.place(x=800, y=190)
        self.D2_entry = ttk.Entry(master=resultados_2)
        self.D2_entry.place(x=840, y=190)

        self.E2_label = ttk.Label(master=resultados_2, text="E: ")
        self.E2_label.place(x=800, y=230)
        self.E2_entry = ttk.Entry(master=resultados_2)
        self.E2_entry.place(x=840, y=230)

        self.F2_label = ttk.Label(master=resultados_2, text="F: ")
        self.F2_label.place(x=800, y=270)
        self.F2_entry = ttk.Entry(master=resultados_2)
        self.F2_entry.place(x=840, y=270)

        # ----------------------------------------------------------------

        self.alfa_3_label = ttk.Label(master=resultados_2, text="α3: ")
        self.alfa_3_label.place(x=800, y=310)
        self.alfa_3_entry = ttk.Entry(master=resultados_2)
        self.alfa_3_entry.place(x=840, y=310)

        self.alfa_4_label = ttk.Label(master=resultados_2, text="α4: ")
        self.alfa_4_label.place(x=800, y=350)
        self.alfa_4_entry = ttk.Entry(master=resultados_2)
        self.alfa_4_entry.place(x=840, y=350)

        self.aA_label = ttk.Label(master=resultados_2, text="aA: ")
        self.aA_label.place(x=800, y=390)
        self.aA_entry = ttk.Entry(master=resultados_2)
        self.aA_entry.place(x=840, y=390)

        self.gradosaA_label = ttk.Label(master=resultados_2, text="∡aA: ")
        self.gradosaA_label.place(x=800, y=430)
        self.gradosaA_entry = ttk.Entry(master=resultados_2)
        self.gradosaA_entry.place(x=840, y=430)

        self.aAB_label = ttk.Label(master=resultados_2, text="aAB: ")
        self.aAB_label.place(x=800, y=470)
        self.aAB_entry = ttk.Entry(master=resultados_2)
        self.aAB_entry.place(x=840, y=470)

        self.aB_label = ttk.Label(master=resultados_2, text="aB: ")
        self.aB_label.place(x=800, y=510)
        self.aB_entry = ttk.Entry(master=resultados_2)
        self.aB_entry.place(x=840, y=510)

        self.gradosaB_label = ttk.Label(master=resultados_2, text="∡aB: ")
        self.gradosaB_label.place(x=800, y=550)
        self.gradosaB_entry = ttk.Entry(master=resultados_2)
        self.gradosaB_entry.place(x=840, y=550)

    # Creando ventana para desplegar los resultados del mecanismo simple con lazo cerrado
    def resultados_simple_lc(self):
        self.obtener_valores()
        resultados_2lc = ttk.Toplevel()
        resultados_2lc.title("Resultados Mecanismo Simples (Lazo Cerrado)")
        resultados_2lc.geometry("1200x900")

        self.obtener_valores()
        print(f"[{self.a} {self.b} {self.c} {self.d} {self.teta_2} ]")

        ttk.Label(
            master=resultados_2lc, text="Posicion:", font="Calibri 20 bold"
        ).place(x=340, y=20)
        # k-----------------------------------------------------------------------------------
        self.k1_label = ttk.Label(master=resultados_2lc, text="k1: ")
        self.k1_label.place(x=30, y=70)
        self.k1_entry = ttk.Entry(master=resultados_2lc)
        self.k1_entry.place(x=70, y=70)
        # usar el metodo insert() para insertar el resultado en el entry
        # recordar modificar todos los entry despues para que despliegue el resultado correcto
        # self.k1_entry.insert(0, str(self.k1))
        # self.k1_entry["state"] = "readonly"

        self.k2_label = ttk.Label(master=resultados_2lc, text="k2: ")
        self.k2_label.place(x=30, y=110)
        self.k2_entry = ttk.Entry(master=resultados_2lc)
        self.k2_entry.place(x=70, y=110)
        # self.k2_entry.insert(0, str(self.k2))
        # self.k2_entry["state"] = "readonly"

        self.k3_label = ttk.Label(master=resultados_2lc, text="k3: ")
        self.k3_label.place(x=30, y=150)
        self.k3_entry = ttk.Entry(master=resultados_2lc)
        self.k3_entry.place(x=70, y=150)
        # self.k3_entry.insert(0, str(self.k3))
        # self.k3_entry["state"] = "readonly"

        self.k4_label = ttk.Label(master=resultados_2lc, text="k4: ")
        self.k4_label.place(x=30, y=190)
        self.k4_entry = ttk.Entry(master=resultados_2lc)
        self.k4_entry.place(x=70, y=190)
        # self.k4_entry.insert(0, str(self.k4))
        # self.k4_entry["state"] = "readonly"

        self.k5_label = ttk.Label(master=resultados_2lc, text="k5: ")
        self.k5_label.place(x=30, y=230)
        self.k5_entry = ttk.Entry(master=resultados_2lc)
        self.k5_entry.place(x=70, y=230)
        # self.k5_entry.insert(0, str(self.k5))
        # self.k5_entry["state"] = "readonly"

        # ----------------------------------------------------

        self.A_label = ttk.Label(master=resultados_2lc, text="A: ")
        self.A_label.place(x=400, y=70)
        self.A_entry = ttk.Entry(master=resultados_2lc)
        self.A_entry.place(x=440, y=70)

        self.B_label = ttk.Label(master=resultados_2lc, text="B: ")
        self.B_label.place(x=400, y=110)
        self.B_entry = ttk.Entry(master=resultados_2lc)
        self.B_entry.place(x=440, y=110)

        self.C_label = ttk.Label(master=resultados_2lc, text="C: ")
        self.C_label.place(x=400, y=150)
        self.C_entry = ttk.Entry(master=resultados_2lc)
        self.C_entry.place(x=440, y=150)

        self.D_label = ttk.Label(master=resultados_2lc, text="D: ")
        self.D_label.place(x=400, y=190)
        self.D_entry = ttk.Entry(master=resultados_2lc)
        self.D_entry.place(x=440, y=190)

        self.E_label = ttk.Label(master=resultados_2lc, text="E: ")
        self.E_label.place(x=400, y=230)
        self.E_entry = ttk.Entry(master=resultados_2lc)
        self.E_entry.place(x=440, y=230)

        self.F_label = ttk.Label(master=resultados_2lc, text="F: ")
        self.F_label.place(x=400, y=270)
        self.F_entry = ttk.Entry(master=resultados_2lc)
        self.F_entry.place(x=440, y=270)

        # ----------------------------------------------------------------------------

        self.teta4_1_label = ttk.Label(master=resultados_2lc, text="θ4(1): ")
        self.teta4_1_label.place(x=30, y=350)
        self.teta4_1_entry = ttk.Entry(master=resultados_2lc)
        self.teta4_1_entry.place(x=90, y=350)

        self.teta4_2_label = ttk.Label(master=resultados_2lc, text="θ4(2): ")
        self.teta4_2_label.place(x=30, y=390)
        self.teta4_2_entry = ttk.Entry(master=resultados_2lc)
        self.teta4_2_entry.place(x=90, y=390)

        self.teta3_1_label = ttk.Label(master=resultados_2lc, text="θ3(1): ")
        self.teta3_1_label.place(x=400, y=350)
        self.teta3_1_entry = ttk.Entry(master=resultados_2lc)
        self.teta3_1_entry.place(x=460, y=350)

        self.teta3_2_label = ttk.Label(master=resultados_2lc, text="θ3(2): ")
        self.teta3_2_label.place(x=400, y=390)
        self.teta3_2_entry = ttk.Entry(master=resultados_2lc)
        self.teta3_2_entry.place(x=460, y=390)

        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        ttk.Label(
            master=resultados_2lc, text="Velocidad:", font="Calibri 20 bold"
        ).place(x=340, y=435)
        self.omega3_label = ttk.Label(master=resultados_2lc, text="ω3: ")
        self.omega3_label.place(x=30, y=490)
        self.omega3_entry = ttk.Entry(master=resultados_2lc)
        self.omega3_entry.place(x=70, y=490)

        self.omega4_label = ttk.Label(master=resultados_2lc, text="ω4: ")
        self.omega4_label.place(x=30, y=530)
        self.omega4_entry = ttk.Entry(master=resultados_2lc)
        self.omega4_entry.place(x=70, y=530)

        self.va_label = ttk.Label(master=resultados_2lc, text="VA: ")
        self.va_label.place(x=400, y=490)
        self.va_entry = ttk.Entry(master=resultados_2lc)
        self.va_entry.place(x=460, y=490)

        self.gradosva_label = ttk.Label(master=resultados_2lc, text="∡vA: ")
        self.gradosva_label.place(x=400, y=530)
        self.gradosva_entry = ttk.Entry(master=resultados_2lc)
        self.gradosva_entry.place(x=460, y=530)

        self.vb_label = ttk.Label(master=resultados_2lc, text="VB: ")
        self.vb_label.place(x=400, y=570)
        self.vb_entry = ttk.Entry(master=resultados_2lc)
        self.vb_entry.place(x=460, y=570)

        self.gradosvb_label = ttk.Label(master=resultados_2lc, text="∡vB: ")
        self.gradosvb_label.place(x=400, y=610)
        self.gradosvb_entry = ttk.Entry(master=resultados_2lc)
        self.gradosvb_entry.place(x=460, y=610)

        self.vab_label = ttk.Label(master=resultados_2lc, text="VA/B: ")
        self.vab_label.place(x=400, y=650)
        self.vab_entry = ttk.Entry(master=resultados_2lc)
        self.vab_entry.place(x=460, y=650)

        ttk.Label(
            master=resultados_2lc, text="Aceleracion:", font="Calibri 20 bold"
        ).place(x=800, y=10)

        self.A2_label = ttk.Label(master=resultados_2lc, text="A: ")
        self.A2_label.place(x=800, y=70)
        self.A2_entry = ttk.Entry(master=resultados_2lc)
        self.A2_entry.place(x=840, y=70)

        self.B2_label = ttk.Label(master=resultados_2lc, text="B: ")
        self.B2_label.place(x=800, y=110)
        self.B2_entry = ttk.Entry(master=resultados_2lc)
        self.B2_entry.place(x=840, y=110)

        self.C2_label = ttk.Label(master=resultados_2lc, text="C: ")
        self.C2_label.place(x=800, y=150)
        self.C2_entry = ttk.Entry(master=resultados_2lc)
        self.C2_entry.place(x=840, y=150)

        self.D2_label = ttk.Label(master=resultados_2lc, text="D: ")
        self.D2_label.place(x=800, y=190)
        self.D2_entry = ttk.Entry(master=resultados_2lc)
        self.D2_entry.place(x=840, y=190)

        self.E2_label = ttk.Label(master=resultados_2lc, text="E: ")
        self.E2_label.place(x=800, y=230)
        self.E2_entry = ttk.Entry(master=resultados_2lc)
        self.E2_entry.place(x=840, y=230)

        self.F2_label = ttk.Label(master=resultados_2lc, text="F: ")
        self.F2_label.place(x=800, y=270)
        self.F2_entry = ttk.Entry(master=resultados_2lc)
        self.F2_entry.place(x=840, y=270)

        # ----------------------------------------------------------------

        self.alfa_3_label = ttk.Label(master=resultados_2lc, text="α3: ")
        self.alfa_3_label.place(x=800, y=310)
        self.alfa_3_entry = ttk.Entry(master=resultados_2lc)
        self.alfa_3_entry.place(x=840, y=310)

        self.alfa_4_label = ttk.Label(master=resultados_2lc, text="α4: ")
        self.alfa_4_label.place(x=800, y=350)
        self.alfa_4_entry = ttk.Entry(master=resultados_2lc)
        self.alfa_4_entry.place(x=840, y=350)

        self.aA_label = ttk.Label(master=resultados_2lc, text="aA: ")
        self.aA_label.place(x=800, y=390)
        self.aA_entry = ttk.Entry(master=resultados_2lc)
        self.aA_entry.place(x=840, y=390)

        self.gradosaA_label = ttk.Label(master=resultados_2lc, text="∡aA: ")
        self.gradosaA_label.place(x=800, y=430)
        self.gradosaA_entry = ttk.Entry(master=resultados_2lc)
        self.gradosaA_entry.place(x=840, y=430)

        self.aAB_label = ttk.Label(master=resultados_2lc, text="aAB: ")
        self.aAB_label.place(x=800, y=470)
        self.aAB_entry = ttk.Entry(master=resultados_2lc)
        self.aAB_entry.place(x=840, y=470)

        self.aB_label = ttk.Label(master=resultados_2lc, text="aB: ")
        self.aB_label.place(x=800, y=510)
        self.aB_entry = ttk.Entry(master=resultados_2lc)
        self.aB_entry.place(x=840, y=510)

        self.gradosaB_label = ttk.Label(master=resultados_2lc, text="∡aB: ")
        self.gradosaB_label.place(x=800, y=550)
        self.gradosaB_entry = ttk.Entry(master=resultados_2lc)
        self.gradosaB_entry.place(x=840, y=550)

    # funcion para ingresar los valores para el mecanismo descentrado
    def descentrado_window(self):
        ventana_2 = ttk.Toplevel()
        ventana_2.title("Mecanismo descentrado")
        ventana_2.geometry("400x700")

        # Creando y desplegando labels y entrys para ingresar los datos
        r1_label = ttk.Label(master=ventana_2, text="Ingrese el valor de r1")
        r1_label.pack(padx=5, pady=5)

        self.r1_entry = ttk.Entry(master=ventana_2)
        self.r1_entry.pack(padx=5, pady=5)
        self.r1_entry.focus()

        r2_label = ttk.Label(master=ventana_2, text="Ingrese el valor de r2")
        r2_label.pack(padx=5, pady=5)

        self.r2_entry = ttk.Entry(master=ventana_2)
        self.r2_entry.pack(padx=5, pady=5)

        r3_label = ttk.Label(master=ventana_2, text="Ingrese el valor de r3")
        r3_label.pack(padx=5, pady=5)

        self.r3_entry = ttk.Entry(master=ventana_2)
        self.r3_entry.pack(padx=5, pady=5)

        teta2_label = ttk.Label(master=ventana_2, text="Ingrese el valor de θ 2")
        teta2_label.pack(padx=5, pady=5)

        self.teta2_entry = ttk.Entry(master=ventana_2)
        self.teta2_entry.pack(padx=5, pady=5)

        teta4_label = ttk.Label(master=ventana_2, text="Ingrese el valor de θ 4")
        teta4_label.pack(padx=5, pady=5)

        self.teta4_entry = ttk.Entry(master=ventana_2)
        self.teta4_entry.pack(padx=5, pady=5)

        omega2_label = ttk.Label(master=ventana_2, text="Ingrese el valor de ω 2")
        omega2_label.pack(padx=5, pady=5)

        self.omega2_entry = ttk.Entry(master=ventana_2)
        self.omega2_entry.pack(padx=5, pady=5)

        alfa2_label = ttk.Label(master=ventana_2, text="Ingrese el valor de α 2")
        alfa2_label.pack(padx=5, pady=5)

        self.alfa2_entry = ttk.Entry(master=ventana_2)
        self.alfa2_entry.pack(padx=5, pady=5)

        # Creando boton que obtiene los valores de los entry
        self.calcular_simple = ttk.Button(
            master=ventana_2, text="Calcular", command=self.calculo_descentrado
        )

        self.calcular_simple.pack(padx=10, pady=10)

    def resultados_descentrado(self):
        self.obtener_valores_descentrado()
        resultados_3 = ttk.Toplevel()
        resultados_3.title("Resultados Mecanismo descentrado")
        resultados_3.geometry("800x9000")

        self.obtener_valores_descentrado()
        # print(f"[{self.a} {self.b} {self.c}  {self.teta_2} ]")

        ttk.Label(master=resultados_3, text="Posicion:", font="Calibri 20 bold").place(
            x=340, y=10
        )
        # ----------------------------------------------------

        self.G_label = ttk.Label(master=resultados_3, text="G: ")
        self.G_label.place(x=400, y=70)
        self.G_entry = ttk.Entry(master=resultados_3)
        self.G_entry.place(x=440, y=70)

        self.H_label = ttk.Label(master=resultados_3, text="H: ")
        self.H_label.place(x=400, y=110)
        self.H_entry = ttk.Entry(master=resultados_3)
        self.H_entry.place(x=440, y=110)

        self.I_label = ttk.Label(master=resultados_3, text="I: ")
        self.I_label.place(x=400, y=150)
        self.I_entry = ttk.Entry(master=resultados_3)
        self.I_entry.place(x=440, y=150)

        self.J_label = ttk.Label(master=resultados_3, text="J: ")
        self.J_label.place(x=400, y=190)
        self.J_entry = ttk.Entry(master=resultados_3)
        self.J_entry.place(x=440, y=190)

        self.K_label = ttk.Label(master=resultados_3, text="K: ")
        self.K_label.place(x=400, y=230)
        self.K_entry = ttk.Entry(master=resultados_3)
        self.K_entry.place(x=440, y=230)

        self.L_label = ttk.Label(master=resultados_3, text="L: ")
        self.L_label.place(x=400, y=270)
        self.L_entry = ttk.Entry(master=resultados_3)
        self.L_entry.place(x=440, y=270)

        # ----------------------------------------------------------------------------

        self.teta3_label = ttk.Label(master=resultados_3, text="θ3: ")
        self.teta3_label.place(x=400, y=390)
        self.teta3_entry = ttk.Entry(master=resultados_3)
        self.teta3_entry.place(x=460, y=390)

        self.r4_label = ttk.Label(master=resultados_3, text="r4: ")
        self.r4_label.place(x=400, y=350)
        self.r4_entry = ttk.Entry(master=resultados_3)
        self.r4_entry.place(x=460, y=350)

        # -----------------------------------------------------------------------
        ttk.Label(master=resultados_3, text="Velocidad:", font="Calibri 20 bold").place(
            x=340, y=435
        )
        self.omega3_label = ttk.Label(master=resultados_3, text="ω3: ")
        self.omega3_label.place(x=30, y=490)
        self.omega3_entry = ttk.Entry(master=resultados_3)
        self.omega3_entry.place(x=70, y=490)

        self.v3_label = ttk.Label(master=resultados_3, text="V3: ")
        self.v3_label.place(x=400, y=490)
        self.v3_entry = ttk.Entry(master=resultados_3)
        self.v3_entry.place(x=460, y=490)

        self.gradosv3_label = ttk.Label(master=resultados_3, text="∡v3: ")
        self.gradosv3_label.place(x=400, y=530)
        self.gradosv3_entry = ttk.Entry(master=resultados_3)
        self.gradosv3_entry.place(x=460, y=530)

        self.v4_label = ttk.Label(master=resultados_3, text="V4: ")
        self.v4_label.place(x=400, y=570)
        self.v4_entry = ttk.Entry(master=resultados_3)
        self.v4_entry.place(x=460, y=570)

        self.gradosv4_label = ttk.Label(master=resultados_3, text="∡v4: ")
        self.gradosv4_label.place(x=400, y=610)
        self.gradosv4_entry = ttk.Entry(master=resultados_3)
        self.gradosv4_entry.place(x=460, y=610)

        self.v34_label = ttk.Label(master=resultados_3, text="V3/4: ")
        self.v34_label.place(x=400, y=650)
        self.v34_entry = ttk.Entry(master=resultados_3)
        self.v34_entry.place(x=460, y=650)

        ttk.Label(
            master=resultados_3, text="Aceleracion:", font="Calibri 20 bold"
        ).place(x=800, y=10)
        # ----------------------------------------------------------------

        self.alfa_3_label = ttk.Label(master=resultados_3, text="α3: ")
        self.alfa_3_label.place(x=800, y=310)
        self.alfa_3_entry = ttk.Entry(master=resultados_3)
        self.alfa_3_entry.place(x=840, y=310)

        self.a3_label = ttk.Label(master=resultados_3, text="a3: ")
        self.a3_label.place(x=800, y=390)
        self.a3_entry = ttk.Entry(master=resultados_3)
        self.a3_entry.place(x=840, y=390)

        self.gradosa3_label = ttk.Label(master=resultados_3, text="∡a3: ")
        self.gradosa3_label.place(x=800, y=430)
        self.gradosa3_entry = ttk.Entry(master=resultados_3)
        self.gradosa3_entry.place(x=840, y=430)

        self.a34_label = ttk.Label(master=resultados_3, text="a3/4: ")
        self.a34_label.place(x=800, y=470)
        self.a34_entry = ttk.Entry(master=resultados_3)
        self.a34_entry.place(x=840, y=470)

        self.a4_label = ttk.Label(master=resultados_3, text="a4: ")
        self.a4_label.place(x=800, y=510)
        self.a4_entry = ttk.Entry(master=resultados_3)
        self.a4_entry.place(x=840, y=510)

        self.gradosa4_label = ttk.Label(master=resultados_3, text="∡aB: ")
        self.gradosa4_label.place(x=800, y=550)
        self.gradosa4_entry = ttk.Entry(master=resultados_3)
        self.gradosa4_entry.place(x=840, y=550)

        # usar el metodo config() para cambiar el master de los labels

    # funcion para ingresar los valores para el mecanismo en desface
    def desface_window(self):
        ventana_3 = ttk.Toplevel()
        ventana_3.title("Mecanismo en desface")
        ventana_3.geometry("400x700")

        # Creando y desplegando labels y entrys para ingresar los datos
        a_label = ttk.Label(master=ventana_3, text="Ingrese el valor de a")
        a_label.pack(padx=5, pady=5)

        self.a_entry = ttk.Entry(master=ventana_3)
        self.a_entry.pack(padx=5, pady=5)
        self.a_entry.focus()

        b_label = ttk.Label(master=ventana_3, text="Ingrese el valor de b")
        b_label.pack(padx=5, pady=5)

        self.b_entry = ttk.Entry(master=ventana_3)
        self.b_entry.pack(padx=5, pady=5)

        c_label = ttk.Label(master=ventana_3, text="Ingrese el valor de c")
        c_label.pack(padx=5, pady=5)

        self.c_entry = ttk.Entry(master=ventana_3)
        self.c_entry.pack(padx=5, pady=5)

        d_label = ttk.Label(master=ventana_3, text="Ingrese el valor de d")
        d_label.pack(padx=5, pady=5)

        self.d_entry = ttk.Entry(master=ventana_3)
        self.d_entry.pack(padx=5, pady=5)

        teta1_label = ttk.Label(master=ventana_3, text="Ingrese el valor de θ1")
        teta1_label.pack(padx=5, pady=5)

        self.teta1_entry = ttk.Entry(master=ventana_3)
        self.teta1_entry.pack(padx=5, pady=5)

        teta2_label = ttk.Label(master=ventana_3, text="Ingrese el valor de θ 2")
        teta2_label.pack(padx=5, pady=5)

        self.teta2_entry = ttk.Entry(master=ventana_3)
        self.teta2_entry.pack(padx=5, pady=5)

        omega2_label = ttk.Label(master=ventana_3, text="Ingrese el valor de ω 2")
        omega2_label.pack(padx=5, pady=5)

        self.omega2_entry = ttk.Entry(master=ventana_3)
        self.omega2_entry.pack(padx=5, pady=5)

        alfa2_label = ttk.Label(master=ventana_3, text="Ingrese el valor de α 2")
        alfa2_label.pack(padx=5, pady=5)

        self.alfa2_entry = ttk.Entry(master=ventana_3)
        self.alfa2_entry.pack(padx=5, pady=5)

        # Creando boton que obtiene los valores de los entry
        self.calcular_simple = ttk.Button(
            master=ventana_3, text="Calcular", command=self.calculo_desface
        )
        self.calcular_simple.pack(padx=10, pady=10)

    def resultados_desface(self):
        self.obtener_valores_desface()
        resultados_1 = ttk.Toplevel()
        resultados_1.title("Resultados Mecanismo en desface")
        resultados_1.geometry("800x9000")

        self.obtener_valores_desface()

        # --------------------------------------------------------
        def pitagoras(self):
            objeto = TrianguloRectanguloCalculator()
            objeto.run()
            
        # Creando el menu
        

        # --------------------------------------------------------

        ttk.Label(master=resultados_1, text="Posicion:", font="Calibri 20 bold").place(
            x=340, y=10
        )
        # usar el metodo insert() para insertar el resultado en el entry
        # recordar modificar todos los entry despues para que despliegue el resultado correcto

        # ----------------------------------------------------

        self.A_label = ttk.Label(master=resultados_1, text="A: ")
        self.A_label.place(x=400, y=70)
        self.A_entry = ttk.Entry(master=resultados_1)
        self.A_entry.place(x=440, y=70)

        self.B_label = ttk.Label(master=resultados_1, text="B: ")
        self.B_label.place(x=400, y=110)
        self.B_entry = ttk.Entry(master=resultados_1)
        self.B_entry.place(x=440, y=110)

        self.C_label = ttk.Label(master=resultados_1, text="C: ")
        self.C_label.place(x=400, y=150)
        self.C_entry = ttk.Entry(master=resultados_1)
        self.C_entry.place(x=440, y=150)

        self.D_label = ttk.Label(master=resultados_1, text="D: ")
        self.D_label.place(x=400, y=190)
        self.D_entry = ttk.Entry(master=resultados_1)
        self.D_entry.place(x=440, y=190)

        self.E_label = ttk.Label(master=resultados_1, text="E: ")
        self.E_label.place(x=400, y=230)
        self.E_entry = ttk.Entry(master=resultados_1)
        self.E_entry.place(x=440, y=230)

        self.F_label = ttk.Label(master=resultados_1, text="F: ")
        self.F_label.place(x=400, y=270)
        self.F_entry = ttk.Entry(master=resultados_1)
        self.F_entry.place(x=440, y=270)

        # ----------------------------------------------------------------------------

        self.teta4_1_label = ttk.Label(master=resultados_1, text="θ4(1): ")
        self.teta4_1_label.place(x=30, y=350)
        self.teta4_1_entry = ttk.Entry(master=resultados_1)
        self.teta4_1_entry.place(x=90, y=350)

        self.teta4_2_label = ttk.Label(master=resultados_1, text="θ4(2): ")
        self.teta4_2_label.place(x=30, y=390)
        self.teta4_2_entry = ttk.Entry(master=resultados_1)
        self.teta4_2_entry.place(x=90, y=390)

        self.teta3_1_label = ttk.Label(master=resultados_1, text="θ3(1): ")
        self.teta3_1_label.place(x=400, y=350)
        self.teta3_1_entry = ttk.Entry(master=resultados_1)
        self.teta3_1_entry.place(x=460, y=350)

        self.teta3_2_label = ttk.Label(master=resultados_1, text="θ3(2): ")
        self.teta3_2_label.place(x=400, y=390)
        self.teta3_2_entry = ttk.Entry(master=resultados_1)
        self.teta3_2_entry.place(x=460, y=390)

        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        ttk.Label(master=resultados_1, text="Velocidad:", font="Calibri 20 bold").place(
            x=340, y=435
        )
        self.omega3_label = ttk.Label(master=resultados_1, text="ω3: ")
        self.omega3_label.place(x=30, y=490)
        self.omega3_entry = ttk.Entry(master=resultados_1)
        self.omega3_entry.place(x=70, y=490)

        self.omega4_label = ttk.Label(master=resultados_1, text="ω4: ")
        self.omega4_label.place(x=30, y=530)
        self.omega4_entry = ttk.Entry(master=resultados_1)
        self.omega4_entry.place(x=70, y=530)

        self.va_label = ttk.Label(master=resultados_1, text="VA: ")
        self.va_label.place(x=400, y=490)
        self.va_entry = ttk.Entry(master=resultados_1)
        self.va_entry.place(x=460, y=490)

        self.gradosva_label = ttk.Label(master=resultados_1, text="∡vA: ")
        self.gradosva_label.place(x=400, y=530)
        self.gradosva_entry = ttk.Entry(master=resultados_1)
        self.gradosva_entry.place(x=460, y=530)

        self.vb_label = ttk.Label(master=resultados_1, text="VB: ")
        self.vb_label.place(x=400, y=570)
        self.vb_entry = ttk.Entry(master=resultados_1)
        self.vb_entry.place(x=460, y=570)

        self.gradosvb_label = ttk.Label(master=resultados_1, text="∡vB: ")
        self.gradosvb_label.place(x=400, y=610)
        self.gradosvb_entry = ttk.Entry(master=resultados_1)
        self.gradosvb_entry.place(x=460, y=610)

        self.vab_label = ttk.Label(master=resultados_1, text="VA/B: ")
        self.vab_label.place(x=400, y=650)
        self.vab_entry = ttk.Entry(master=resultados_1)
        self.vab_entry.place(x=460, y=650)

        ttk.Label(
            master=resultados_1, text="Aceleracion:", font="Calibri 20 bold"
        ).place(x=800, y=10)

        # ----------------------------------------------------------------

        self.alfa_3_label = ttk.Label(master=resultados_1, text="α3: ")
        self.alfa_3_label.place(x=800, y=310)
        self.alfa_3_entry = ttk.Entry(master=resultados_1)
        self.alfa_3_entry.place(x=840, y=310)

        self.alfa_4_label = ttk.Label(master=resultados_1, text="α4: ")
        self.alfa_4_label.place(x=800, y=350)
        self.alfa_4_entry = ttk.Entry(master=resultados_1)
        self.alfa_4_entry.place(x=840, y=350)

        self.aA_label = ttk.Label(master=resultados_1, text="aA: ")
        self.aA_label.place(x=800, y=390)
        self.aA_entry = ttk.Entry(master=resultados_1)
        self.aA_entry.place(x=840, y=390)

        self.gradosaA_label = ttk.Label(master=resultados_1, text="∡aA: ")
        self.gradosaA_label.place(x=800, y=430)
        self.gradosaA_entry = ttk.Entry(master=resultados_1)
        self.gradosaA_entry.place(x=840, y=430)

        self.aAB_label = ttk.Label(master=resultados_1, text="aAB: ")
        self.aAB_label.place(x=800, y=470)
        self.aAB_entry = ttk.Entry(master=resultados_1)
        self.aAB_entry.place(x=840, y=470)

        self.aB_label = ttk.Label(master=resultados_1, text="aB: ")
        self.aB_label.place(x=800, y=510)
        self.aB_entry = ttk.Entry(master=resultados_1)
        self.aB_entry.place(x=840, y=510)

        self.gradosaB_label = ttk.Label(master=resultados_1, text="∡aB: ")
        self.gradosaB_label.place(x=800, y=550)
        self.gradosaB_entry = ttk.Entry(master=resultados_1)
        self.gradosaB_entry.place(x=840, y=550)


# creando instancia de la clase
mecanismos = Mecanismos()
