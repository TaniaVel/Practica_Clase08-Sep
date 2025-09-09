import datetime;
import decimal;
import pyodbc;

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

    def CargarEstados(self) -> None:
        conexion = pyodbc.connect(self.cadena_conexion);

        consulta: str = """ SELECT * FROM estados; """;
        cursor = conexion.cursor();
        cursor.execute(consulta);

        for elemento in cursor:
            print(elemento);

        cursor.close();
        conexion.close();

conexion = Conexion();
conexion.CargarEstados();
print("Hola mundo!");