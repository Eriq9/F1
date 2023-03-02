import ergast_py



############### Algorytm ########################


class FormulaAlgorithm:
    def __init__(self,year,race_round):
        self.year = year
        self.race_round = race_round

    def RunAlgorithm(self):

        e = ergast_py.Ergast()
        race_results = e.season(self.year).round(self.race_round).get_result()

        race_results_constructors = e.season(self.year).round(self.race_round).get_constructor_standings()

        race_results_drivers = e.season(self.year).round(self.race_round).get_driver_standings()

        lista_wystąpien = []
        lista_kierowcow = []
        lista_pkt = []
        lista_zespolow = []
        lista_pozycji = []
        lista_pkt_GUI = []
        tabela_zespolow = {"FERRARI": 0,
                   "REDBULL": 0,
                   "MERC": 0,
                   "HAAS": 0,
                   "ROMEO": 0,
                   "ALPINE": 0,
                   "TAURI": 0,
                   "ASTON": 0,
                   "WILLIAMS": 0,
                   "MCLAREN": 0
                   }

        tabela_zespolow_last = {"FERRARI": 0,
                   "REDBULL": 0,
                   "MERC": 0,
                   "HAAS": 0,
                   "ROMEO": 0,
                   "ALPINE": 0,
                   "TAURI": 0,
                   "ASTON": 0,
                   "WILLIAMS": 0,
                   "MCLAREN": 0
                   }

        klasKonstr_pkt = []
        klasKonstr_teams = []
        klasKier_pkt = []
        klasKier_kier = []


        for i in range (len(race_results.results)):
            lista_kierowcow.append(race_results.results[i].driver.driver_id)
            lista_pkt.append(race_results.results[i].points)
            lista_pkt_GUI.append(race_results.results[i].points)
            lista_zespolow.append(race_results.results[i].constructor.constructor_id)
            lista_pozycji.append(race_results.results[i].position)

        for j in range (0,10):
            klasKonstr_pkt.append(race_results_constructors[0].constructor_standings[j].points)
            klasKonstr_teams.append(race_results_constructors[0].constructor_standings[j].constructor.name)

        for y in range (0,20):
            klasKier_pkt.append(race_results_drivers[0].driver_standings[y].points)
            klasKier_kier.append(race_results_drivers[0].driver_standings[y].driver.family_name)


################ Tabela na podstawie tylko punktów #################################


        iterator = 0


        for x in lista_zespolow:
            if x == "red_bull":
                tabela_zespolow["REDBULL"] += lista_pkt[iterator]
                iterator += 1
            elif x == "ferrari":
                tabela_zespolow["FERRARI"] += lista_pkt[iterator]
                iterator += 1
            elif x == "mercedes":
                tabela_zespolow["MERC"] += lista_pkt[iterator]
                iterator += 1
            elif x == "alfa":
                tabela_zespolow["ROMEO"] += lista_pkt[iterator]
                iterator += 1
            elif x == "alpine":
                tabela_zespolow["ALPINE"] += lista_pkt[iterator]
                iterator += 1
            elif x == "williams":
                tabela_zespolow["WILLIAMS"] += lista_pkt[iterator]
                iterator += 1
            elif x == "aston_martin":
                tabela_zespolow["ASTON"] += lista_pkt[iterator]
                iterator += 1
            elif x == "alphatauri":
                tabela_zespolow["TAURI"] += lista_pkt[iterator]
                iterator += 1
            elif x == "mclaren":
                tabela_zespolow["MCLAREN"] += lista_pkt[iterator]
                iterator += 1
            elif x == "haas":
                tabela_zespolow["HAAS"] += lista_pkt[iterator]
                iterator += 1

        order_by_points = dict(sorted(tabela_zespolow.items(), key=lambda item: item[1],reverse=True))


################ Ostateczna tabela #################################



        iterator_pkt = 0

        for pkt in lista_pkt:
            if pkt > 0:
                lista_pkt[iterator_pkt] = lista_pkt[iterator_pkt] * -1
                lista_wystąpien.append(lista_zespolow[iterator_pkt])
                iterator_pkt +=1
            else:
                if lista_zespolow[iterator_pkt] in lista_wystąpien:
                    iterator_pkt += 1
                else:

                    lista_pkt[iterator_pkt] = lista_pozycji[iterator_pkt]
                    lista_wystąpien.append(lista_zespolow[iterator_pkt])
                    iterator_pkt += 1



        iterator_last = 0


        for x in lista_zespolow:
            if x == "red_bull":
                tabela_zespolow_last["REDBULL"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "ferrari":
                tabela_zespolow_last["FERRARI"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "mercedes":
                tabela_zespolow_last["MERC"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "alfa":
                tabela_zespolow_last["ROMEO"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "alpine":
                tabela_zespolow_last["ALPINE"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "williams":
                tabela_zespolow_last["WILLIAMS"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "aston_martin":
                tabela_zespolow_last["ASTON"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "alphatauri":
                tabela_zespolow_last["TAURI"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "mclaren":
                tabela_zespolow_last["MCLAREN"] += lista_pkt[iterator_last]
                iterator_last += 1
            elif x == "haas":
                tabela_zespolow_last["HAAS"] += lista_pkt[iterator_last]
                iterator_last += 1


        order_last = dict(sorted(tabela_zespolow_last.items(), key=lambda item: item[1]))

        lista_teams_GUI = list(order_last.keys())


        return lista_teams_GUI, lista_kierowcow, lista_zespolow, lista_pkt_GUI,klasKonstr_teams,klasKonstr_pkt, klasKier_kier, klasKier_pkt
