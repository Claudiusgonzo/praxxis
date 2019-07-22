
import pytest

def test_activate_ruleset(setup, create_deactivated_ruleset, rulesengine_db):
    """
    tests activate_ruleset functionality. Requires that setup is run and there is a ruleset inactive.
    """
    from src.mtool.rulesengine import activate_ruleset
    from tests.src.mtool.util import dummy_object
    import os

    name1 = dummy_object.make_dummy_ruleset("generated_deactivated_ruleset")

    result = activate_ruleset.activate_ruleset(name1, rulesengine_db)
    
    assert result == name1.name

def test_activate_ruleset_nonexistent(setup, rulesengine_db):
    from src.mtool.rulesengine import activate_ruleset
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error
    name1 = dummy_object.make_dummy_ruleset("nonexistent_ruleset")

    try:
        activate_ruleset.activate_ruleset(name1, rulesengine_db)
    except error.RulesetNotFoundError:
        assert 1
        
def test_activate_ruleset_already_active(setup, create_one_ruleset, rulesengine_db):
    from src.mtool.rulesengine import activate_ruleset
    from tests.src.mtool.util import dummy_object
    from src.mtool.util import error
    import os

    name1 = dummy_object.make_dummy_ruleset("generated_one_ruleset")

    try:
        activate_ruleset.activate_ruleset(name1, rulesengine_db)
    except error.RulesetActiveError:
        assert 1
    
    

def test_resume_scene(setup, create_ended_scene, scene_root, history_db, current_scene_db):
    from src.mtool.scene import resume_scene
    from src.mtool.util.sqlite import sqlite_scene
    
    ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    assert len(ended_scenes) == 1
    resume_scene.resume_scene("generated_ended_scene", scene_root, history_db)
    ended_scenes = sqlite_scene.get_ended_scenes(history_db)
    assert len(ended_scenes) == 0