"""
tests listing notebooks
"""
import pytest 


from tests.src.mtool.fixtures.setup_library import add_test_library

def test_list_notebooks_empty(setup, scene_root, library_root, library_db, current_scene_db, start, stop):
    """ tests listing notebooks when no libraries exist """
    import os
    from src.mtool.notebook import list_notebook
    from src.mtool.scene import current_scene
    notebooks = list_notebook.list_notebook(scene_root, library_root, library_db, current_scene_db, start, stop)
    assert notebooks == []


def test_list_notebooks_populated(setup, add_test_library, scene_root, library_root, library_db, current_scene_db, start, stop, notebooks_list):
    from src.mtool.notebook import list_notebook
    
    notebooks = list_notebook.list_notebook(scene_root, library_root, library_db, current_scene_db, start, stop)
    assert len(notebooks) == len(notebooks_list)