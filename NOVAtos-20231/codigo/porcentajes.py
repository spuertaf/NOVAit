#objeto para obtner porcentajes
import pandas as pd

class Porcentajes:
    def __init__(self, dataframe:pd.DataFrame, columna:str, sort:str = None) -> None:
        self.__dataframe = dataframe
        self.__columna = columna
        self.__sort = sort


    def obtener_porcentajes(self) -> pd.DataFrame:
        assert self.__columna in self.__dataframe.columns, f"{self.__columna} no es una columna del dataframe"
        porcentajes = self.__dataframe[self.__columna].value_counts().sort_index().to_frame()
        porcentajes = porcentajes.reset_index()
        porcentajes.columns = ["Semestre", "Numero Personas"]
        if self.__sort is not None:
            porcentajes = porcentajes.sort_values(by=self.__sort, ascending=False)
        porcentajes["Porcentajes"] = round((porcentajes["Numero Personas"] / sum(porcentajes["Numero Personas"])),3)*100
        porcentajes["Acumulado Porcentajes"] = porcentajes["Porcentajes"].cumsum()
        return porcentajes
