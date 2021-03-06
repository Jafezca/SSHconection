import os

class Tabla():
    ESQUINA = '+'
    LATERAL = '|'
    INTERMEDIO = '-'

    def __init__(self, titulos, contenido):
        dict_espacios = dict()
        self.titulos_tabla = []
        self.contenido_tabla = []
        for i in titulos:
            posicion = titulos.index(i)
            lista_temp = []
            lista_temp.append(i)
            for a in contenido:
                lista_temp.append(a[posicion])

            dict_espacios[titulos.index(i)]=self.len_check(lista_temp)

        for i in titulos:
            spaces = dict_espacios.get(titulos.index(i)) - len(i)
            temp_spaces = ' ' * spaces
            frase = ' ' + i + temp_spaces + ' '
            self.titulos_tabla.append(frase)

        for i in contenido:
            linea = []
            for e in i:
                espacios = dict_espacios.get(i.index(e)) - len(e)
                espacios_temp = ' ' * espacios
                frase = ' ' + e + espacios_temp + ' '
                linea.append(frase)

            self.contenido_tabla.append(linea)

        self.interline = self.line_spicing()
        self.titulos_tabla, self.contenido_tabla = self.lateral_bars()


    def len_check(self, texto):
        max_len = 0
        for i in texto:
            if len(i) > max_len:
                max_len = len(i)
        return max_len

    def line_spicing(self):
        respuesta = self.ESQUINA
        for i in self.titulos_tabla:
            lineas = self.INTERMEDIO * len(i)
            respuesta += lineas + self.ESQUINA
        return respuesta

    def lateral_bars(self):
        respuesta_titulos = self.LATERAL.join(self.titulos_tabla)
        respuesta_titulos = self.LATERAL + respuesta_titulos + self.LATERAL
        respuesta_contenido = []
        for i in self.contenido_tabla:
            temp_string = self.LATERAL.join(i)
            temp_string = self.LATERAL + temp_string + self.LATERAL
            respuesta_contenido.append(temp_string)

        return respuesta_titulos, respuesta_contenido

    def print_table(self):
        print(self.interline)
        print(self.titulos_tabla)
        print(self.interline)
        for i in self.contenido_tabla:
            print(i)
        print(self.interline)


os.system('clear')
titulos = ['Mes', 'Dia', 'Hora', 'Usuario', 'IP', 'Aceptada/Rechazada']

doc = open('/var/log/auth.log', 'r')
doc_b = open ('/var/log/auth.log.1', 'r')
read_doc = doc.read() + doc_b.read()
lista = read_doc.splitlines()
lista_conexiones = []

for i in lista:
	test_one = False
	test_two = False
	if i.find('Accepted') != -1:
		test_one = True
	if i.find('Failed') != -1:
		test_two = True
		
	if i.find('message repeated') == -1:
		if i.find('ssh') != -1:	
			if test_one == True or test_two == True:
				lista_conexiones.append(i)
		
contenido = []
for i in lista_conexiones:
	temp_list = i.split()
	in_list_for = temp_list.index('for')
	in_list_from = temp_list.index('from')
	
	
	mes = temp_list[0]
	dia = temp_list[1]
	hora = temp_list[2]
	usuario = temp_list[in_list_for + 1]
	ip = temp_list[in_list_from + 1]
	
	if 'Accepted' in temp_list:
		estado = 'Conexion aceptada'
	if 'Failed' in temp_list:
		estado = 'Conexion rechazada'
	
	linea = [mes, dia, hora, usuario, ip, estado]
	contenido.append(linea)
	
tabla = Tabla(titulos, contenido)
tabla.print_table()
