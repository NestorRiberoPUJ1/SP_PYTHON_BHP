from dataclasses import dataclass
from typing import ClassVar

from flask import render_template
from flask_app.controllers import default_controller as DC
from flask_app.models import species
from flask_app import app

#POLIMORFISMO CON DATA CLASSES

@dataclass(init=False)
class SpecieDetail(DC.ModelDetail):

    def get(self, id):
        item = self.model.find_by_id(id)
        item = item.get_breeds()
        return render_template(f"{self.template_folder}/detail.html", item=item)



# RUTAS PARA ESPECIES

# RUTA PARA VER TODAS LAS ESPECIES
app.add_url_rule('/species', view_func=DC.ModelList.as_view('species', model=species.species, template_folder='species'))
# RUTA PARA VER LOS DETALLES DE UNA ESPECIE
app.add_url_rule('/species/<int:id>', view_func=SpecieDetail.as_view('species_detail', model=species.species, template_folder='species'))
# RUTA PARA CREAR UNA ESPECIE
app.add_url_rule('/species/create', view_func=DC.ModelCreate.as_view('species_create', model=species.species, template_folder='species', on_create_redirect='species'))
# RUTA PARA EDITAR UNA ESPECIE
app.add_url_rule('/species/<int:id>/edit', view_func=DC.ModelEdit.as_view('species_edit', model=species.species, template_folder='species', on_update_redirect='species'))
# RUTA PARA ELIMINAR UNA ESPECIE
app.add_url_rule('/species/<int:id>/delete', view_func=DC.ModelDelete.as_view('species_delete', model=species.species, on_delete_redirect='species'))


