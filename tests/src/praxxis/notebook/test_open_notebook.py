def test_open_notebook_ads(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook(viewer="ads")
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
    except error.ADSNotFoundError:
        assert 1

def test_open_notebook_ads_not_found(setup, add_test_library, current_scene_db, library_db):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook(viewer="ads")
    ads_location = "fake_path"
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
        assert 0 # previous command should fail
    except error.ADSNotFoundError:
        assert 1

def test_open_notebook_html(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object

    notebook1 = dummy_object.make_dummy_notebook(viewer="html")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, True) == 0

def test_open_notebook_bad_editor(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook()
    editor = "not real"
    try:
        open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, editor, test=True) == 0
        assert 0
    except error.EditorNotFoundError:
        assert 1

def test_open_notebook_editor(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook()
    editor = "vim"
    try:
        assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, editor, test=True) == 0
    except error.EditorNotFoundError:
        # if vim not installed (e.g. windows)
        assert 1

def test_open_notebook_jupyter(setup, add_test_library, current_scene_db, library_db, ads_location):
    from src.praxxis.notebook import open_notebook
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import error

    notebook1 = dummy_object.make_dummy_notebook(viewer="jupyter")
    assert open_notebook.open_notebook(notebook1, current_scene_db, library_db, ads_location, test=True) == 0
    