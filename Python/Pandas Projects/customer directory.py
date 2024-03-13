client_data = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

client_list = client_data.split('\n')

directory = {}

fields_list = client_list[0].split(';')

for i in client_list[1:]:
    client = {}
    
    list_info = i.split(';')
    
    for j in range(1, len(fields_list)):
        if fields_list[j] == 'descuento':
            list_info[j] = float(list_info[j])
        client[fields_list[j]] = list_info[j]
        
    directory[list_info[0]] = client
    
for i in directory:
    print(directory[i])