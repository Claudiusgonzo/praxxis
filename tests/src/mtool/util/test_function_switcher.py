from src.mtool.util import function_switcher
from tests.src.mtool.util import dummy_object

def test_get_current_scene_db(setup, scene_root, history_db):
    import os

    current_scene_db = function_switcher.get_current_scene_db(scene_root, history_db)
    assert os.path.basename(current_scene_db) == "scene.db"


def test_run_notebook(setup, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert function_switcher.run_notebook(notebook, telemetry_db, outfile_root, library_root, library_db, scene_root, history_db, current_scene_db) == 0


def test_view_notebook_env(setup, add_test_library, library_db):
    import os

    notebook = dummy_object.make_dummy_notebook_params()
    envs = function_switcher.view_notebook_env(notebook, library_db)
    
    assert len(envs) == 2


def test_open_notebook(setup, add_test_library, scene_root, history_db, library_db, ads_location, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    assert function_switcher.open_notebook(notebook, scene_root, history_db, library_db, ads_location, current_scene_db) == 0


def test_search_notebook(setup, add_test_library, scene_root, history_db, library_db, start, stop, current_scene_db):
    search = dummy_object.make_dummy_search()

    notebooks = function_switcher.search_notebook(search, scene_root, history_db, library_db, start, stop, current_scene_db)
    assert len(notebooks) == 2


def test_list_notebook(setup, add_test_library, scene_root, history_db, library_root, library_db, start, stop, current_scene_db):
    notebook = dummy_object.make_dummy_notebook()

    notebook_list = function_switcher.list_notebook(notebook, scene_root, history_db, library_root, library_db, start, stop, current_scene_db)
    assert len(notebook_list) == 3


def test_next_notebook():    
    notebook = dummy_object.make_dummy_notebook()
    assert function_switcher.next_notebook(notebook) == "coming soon"


def test_history(setup, generate_short_history, scene_root, history_db, library_db, current_scene_db):
    assert len(function_switcher.history("", scene_root, history_db, library_db, current_scene_db)) == 1


def test_new_scene(setup, scene_root, history_db):
    from src.mtool.scene import delete_scene

    scene = dummy_object.make_dummy_scene("generated_new_scene")

    new_scene = function_switcher.new_scene(scene, scene_root, history_db)
    assert new_scene[1] == "generated_new_scene"

    delete_scene.delete_scene("generated_new_scene", scene_root, history_db)


def test_end_scene(setup, create_one_scene, scene_root, history_db, current_scene_db):
    ended = function_switcher.end_scene("generated_one_scene", scene_root, history_db, current_scene_db)

    assert ended == "generated_one_scene"


def test_change_scene(setup, create_one_scene, scene_root, history_db):
    scene = dummy_object.make_dummy_scene("scene")

    change_scene = function_switcher.change_scene(scene, scene_root, history_db)
    assert change_scene == "scene"


def test_resume_scene(setup, create_ended_scene, scene_root, history_db):
    resume_scene = function_switcher.resume_scene("generated_ended_scene", scene_root, history_db)

    assert resume_scene == "generated_ended_scene"


def test_delete_scene(setup, create_one_scene, scene_root, history_db):
    delete_scene = function_switcher.delete_scene("generated_one_scene", scene_root, history_db)

    assert delete_scene == "generated_one_scene"


def test_set_env():
    pass