import pymysql, csv

# Open database connection
password = "mysql"
db = pymysql.connect("localhost", "root", password, "mit")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# open the file and import the data into mysql
with open("../data/incidenti-per-tipo-di-veicoli-coinvolti-e-regione---anni-2001-2013.csv", "r") as input:
    input_csv = csv.reader(input, delimiter=',', quotechar='"')
    header = False
    for line in input_csv:
        # skip header
        if not header:
            header = True
            continue
        # skip useless lines
        if line[0] in ["Italia_Settentrionale", "Italia_Centrale", "Italia_Meridionale_e_Insulare"] \
            or line[0][:9] == "Totale_20":
            continue
        # Prepare SQL query to INSERT a record into the database.
        sql = "insert into incidenti(regione, anno, totale_incidenti, autovettura_privata, \
              autovettura_privata_con_rimorchio, \
              autovettura_pubblica, autovettura_soccorso_o_polizia, autobus_o_filobus_servizio_urbano, \
              autobus_servizio_extraurbano, tram, autocarro, autotreno_con_rimorchio, autosnodato_autoarticolato, \
              veicoli_speciali, trattore_stradale_o_motrice, trattore_agricolo, velocipede, ciclomotore, \
              motociclo_a_solo, \
              motociclo_con_passeggero, motocarro_o_motofurgone, veicolo_trazione_animale_o_braccia, \
              veicolo_ignoto_datosi_alla_fuga, quadriciclo_leggero, altri_veicoli, totale_veicoli_coinvolti)\
              values ('%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d'\
              , '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % \
              (line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]), int(line[5]), int(line[6]),
               int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), int(line[12]), int(line[13]),
               int(line[14]), int(line[15]), int(line[16]), int(line[17]), int(line[18]), int(line[19]),
               int(line[20]), int(line[21]), int(line[22]), int(line[23]), int(line[24]), int(line[25]))
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()

        except:
            # Rollback in case there is any error
            db.rollback()

# disconnect from server
db.close()
