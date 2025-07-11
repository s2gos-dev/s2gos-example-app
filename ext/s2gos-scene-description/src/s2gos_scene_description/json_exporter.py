import json
from pathlib import Path

from .scene import Scene


def to_json(path: Path, scene: Scene):
    scene_json = scene.model_dump_json()
    with open(path, "w") as f:
        json.dump(scene_json, f, ensure_ascii=False, indent=4)
