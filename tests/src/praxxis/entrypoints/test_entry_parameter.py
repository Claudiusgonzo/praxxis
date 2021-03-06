from src.praxxis.entrypoints import entry_parameter
from tests.src.praxxis.util import dummy_object

def test_view_library_param(setup, add_test_library, scene_root, history_db, library_db, current_scene_db, query_start, query_end):
    from src.praxxis.parameter import list_param

    library_params = list_param.list_library_param("test_notebooks", library_db, current_scene_db, query_start, query_end)
    params = dummy_object.make_dummy_params()

    entry_parameter.view_library_param("test_notebooks", scene_root, history_db, library_db, current_scene_db)
    assert params.parameter == library_params


def test_list_param(setup, set_one_param, scene_root, history_db, query_start, query_end, current_scene_db):
    from src.praxxis.parameter import list_param
    entry_parameter.list_param("", scene_root, history_db, query_start, query_end, current_scene_db)
    
    assert len(list_param.list_param(current_scene_db, query_start, query_end)) == 1


def test_delete_param(setup, set_one_param, scene_root, history_db, current_scene_db, query_start, query_end):
    from src.praxxis.parameter import list_param

    entry_parameter.delete_param("generated_single_param", scene_root, history_db, current_scene_db)
    assert len(list_param.list_param(current_scene_db, query_start, query_end)) == 0

def test_set_param(setup, scene_root, history_db, current_scene_db):
    from src.praxxis.parameter import delete_param
    from src.praxxis.util import error

    param = dummy_object.make_dummy_parameter("test_set_param", "test")

    entry_parameter.set_param(param, scene_root, history_db)
    try:
        delete_param.delete_parameter(param, scene_root, history_db, current_scene_db)
    except error.ParamNotFoundError:
        assert 0
    else:
        assert 1


def test_view_notebook_param(setup, add_test_library, scene_root, library_db, history_db, current_scene_db, query_start, query_end):
    import os
    from src.praxxis.parameter import list_param

    notebook = dummy_object.make_dummy_notebook_with_params()
    dummy_params = dummy_object.make_dummy_params()
    
    entry_parameter.view_notebook_param(notebook, scene_root, library_db, history_db, current_scene_db)

    params = list_param.list_notebook_param(notebook, library_db, current_scene_db)

    assert dummy_params.parameter ==  params
