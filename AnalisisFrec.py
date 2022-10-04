from collections import Counter
alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"	
frecuencia="EAOLSNDRUITCPMYQBHGFVJÑZXKW"
listaCaracteresOrdenada=""
print("Escribe el mensaje que quieres descifrar:")
mensaje="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXVITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIVCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCVI ET DKIRXNI KXVITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXVITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
#Contar letras mensaje
counter=Counter(mensaje)
listaLetras={}
for caracter in alfabeto:
	listaLetras[caracter]=counter[caracter]
listaOrdenada = sorted(listaLetras.items(), key=lambda x: x[1], reverse=True)
print(listaOrdenada)
for i in range(len(listaOrdenada)):
	listaCaracteresOrdenada= listaCaracteresOrdenada + listaOrdenada[i][0]
	
mensajeDescifrado= mensaje.maketrans(listaCaracteresOrdenada, frecuencia)
print("### MENSAJE CIFRADO ###")
print(mensaje)
print("### FRECUENCIAS ###")
print(frecuencia)
print("### CARACTERES ORDENADOS DE MAYOR A MENOR FRECUENCIA ###")
print(listaCaracteresOrdenada)
print("### MENSAJE DESCIFRADO ###")	
mensajeDescifrado=mensaje.translate(mensajeDescifrado)
print(mensajeDescifrado)
print("### AJUSTAR MENSAJE ###")
print("¿Quieres ajustar el mensaje? --> SÍ(Y) O NO (N)")
eleccion=input()
while(eleccion == "Y"):
	print("Introduce una cadena a cambiar")
	cadena=input()
	print("Introduce otra cadena a cambiar de la misma longitud")
	cadena2=input()
	mensajeDescifradoII= mensajeDescifrado.maketrans(cadena, cadena2)
	mensajeDescifradoII=mensajeDescifrado.translate(mensajeDescifradoII)
	print(mensajeDescifradoII)
	print("¿Quieres seguir ajustando el mensaje? --> SÍ(Y) O NO(N)")
	eleccion= input()
	mensajeDescifrado=mensajeDescifradoII
else:
	print("¡Perfecto!")
