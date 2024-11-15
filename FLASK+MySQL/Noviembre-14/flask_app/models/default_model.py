

from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
from mysqlconnection import connectToMySQL

# Clase que define el modelo por defecto de las tablas de la base de datos


@dataclass(init=False)
class default_model:
    # Nombre de la tabla como atributo de la clase
    table_name: ClassVar[str] = None

    # Atributos de la clase
    id: int
    created_at: datetime
    updated_at: datetime

    # Constructor
    def __init__(self, data):
        # Asignar los valores de los atributos a partir de los datos recibidos en el constructor de la clase
        for field in fields(self):
            setattr(self, field.name, data.get(field.name))

    # Métodos CRUD

    # Método para obtener todos los registros de la tabla

    @classmethod
    def all(cls):
        # Crear el query
        query = f'SELECT * FROM {cls.table_name}'
        # Obtener los resultados
        results = connectToMySQL('red_social').query_db(query)
        # Crear una lista de objetos de la clase
        instances = []
        # Crear una instancia de la clase por cada resultado
        for result in results:
            instances.append(cls(result))
        # Retornar la lista de instanciasF
        return instances

    # Método para obtener un registro de la tabla por su id
    @classmethod
    def find_by_id(cls, id):
        try:
            # Crea el query
            query = f'SELECT * FROM {cls.table_name} WHERE id = {id}'
            # Obtiene el resultado
            result = connectToMySQL('red_social').query_db(query)
            # Retorna una instancia de la clase con el resultado obtenido en la posición 0
            return cls(result[0])
        except:
            return None

    @classmethod
    # Método para guardar un registro en la tabla
    def save(cls, data):
        # Crea los campos de la tabla como string separados por comas
        string_fields = ', '.join(cls.data_fields())
        # Crea los valores de los campos como string separados por comas y con el formato %s
        string_values = ', '.join([f'%({field})s' for field in cls.data_fields()])
        # Crea el query
        query = f'INSERT INTO {cls.table_name} ({string_fields}) VALUES ({string_values})'
        # Retorna el id del nuevo registro
        return connectToMySQL('red_social').query_db(query, data)
        

    # Método para actualizar un registro de la tabla
    def update(self):
        pass

    # Método para eliminar un registro de la tabla
    def delete_by_id(self, id):
        pass

    @classmethod
    # Método para ver todos los campos
    def data_fields(cls):
        class_data_fields = []
        for field in fields(cls):
            if (field.name != 'id' and field.name != 'created_at' and field.name != 'updated_at'):
                class_data_fields.append(field.name)
        return class_data_fields

# PRUEBAS


if __name__ == '__main__':
    # Crear un objeto de la clase DefaultModel
    default = {
        'id': 1,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }

    default_model = default_model(default)

    # Imprimir el objeto
    print(default_model)

    print(default_model.data_fields())
