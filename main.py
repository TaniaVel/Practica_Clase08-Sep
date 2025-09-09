import datetime;
import decimal;

"""
    int (int-long)
    float, decimal, complex
    str
    datetime (datetime.datetime.now())
    bool (True, False)
"""

class Estados:
    id: int = 0;

    def GetId(self) -> int:
        return self.id;
    def SetId(self, value: int) -> None:
        self.id = value;

    nombre: str = None;

    def GetNombre(self) -> str:
        return self.nombre;
    def SetNombre(self, value: str) -> None:
        self.nombre = value;

class Conexion:
    cadena_conexion: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=db_universidad;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";

estado = Estados();
print("Hola mundo!");